from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr
import bcrypt
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
import secrets
from uuid import uuid4

#Configuration for JWT
SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256" 
ACCESS_TOKEN_EXPIRE_MINUTES = 30

active_access_tokens = []

def create_access_token(data: dict):
	token_id = str(uuid4())
	to_encode = data.copy()
	expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
	to_encode.update(
		{
			"exp" : expire,
			"token_id" : token_id,
		}
	)
	active_access_tokens.append(token_id)
	return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def verify_access_token(token: str):
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		if payload['token_id'] in active_access_tokens:
			return payload
		else: raise HTTPException(status_code=401, detail="Invalid or expired token")
	except jwt.JWTError:
		raise HTTPException(status_code=401, detail="Invalid or expired token")


active_refresh_tokens = []

REFRESH_TOKEN_EXPIRE_DAYS = 7

def create_refresh_token(data: dict):
	token_id = str(uuid4())
	to_encode = data.copy()
	expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
	to_encode.update(
		{
			"exp" : expire, 
			"id" : token_id,
			}
		)
	active_refresh_tokens.append(token_id)
	return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_refresh_token(token: str):
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		return payload
	except jwt.JWTError:
		raise HTTPException(status_code=401, detail="Invalid or expired token")

class User(BaseModel):
	id: int
	email: EmailStr
	password: str
	role: str | None = "user"

class UserCreate(BaseModel):
	email: EmailStr
	password: str

class UserProfile(BaseModel):
	id: int
	firstName: str
	lastName: str
	age: int | None = None
	bio: str | None = None

class UserProfileCreate(BaseModel):
	firstName: str
	lastName: str
	age: int
	bio: str | None = None

users = [
	User(id=1, email="adil@gmail.com", password="adil", role="user"),
]

users_profile = [
	UserProfile(id=1, firstName="Adilkhan", lastName="Tubulbayev", age=19, bio="NIS Student.")
]

app = FastAPI()

@app.get("/health")
async def health():
	return {"message" : "fastapi is working"}


#FOR ADMIN (EDITING USERS DATA)
@app.get("/users")
async def get_users():
	return users

@app.get("/users/profile")
async def get_users_profile():
	return users_profile

@app.get("/user/profile")
async def get_user_profile(token: str):
	user_data = verify_access_token(token)
	for u in users_profile:
		if u.id == user_data['id']:
			return u


@app.get("/user/{user_id}")
async def get_user_by_id(user_id: int):
	for u in users:
		if u.id == user_id:
				return u
	else: return {"message" : "user doesn't exist"}

@app.post("/user")
async def create_user(user: User):
	for u in users:
		if u.email == user.email:
			raise HTTPException(status_code=409, detail="user already exists.")
	
	hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
	new_user = User(
		id= len(users) + 1,
		email= user.email,
		password= hashed_password,
	)
	users.append(new_user)
	return users

@app.put("/user/profile")
async def update_user_profile(token: str, user_profile: UserProfileCreate):
	user_data = verify_access_token(token)
	for u in users_profile:
		if u.id == user_data['id']:
			u.firstName = user_profile.firstName
			u.lastName = user_profile.lastName
			u.age = user_profile.age
			u.bio = user_profile.bio
			return u

@app.put("/user/{user_id}")
async def update_user(user_id: int, user: User):
	for u in users:
		if u.id == user_id:
			u.email = user.email
			u.password = user.password
			u.role = user.role
	return users
	return {"message" : "user doesn't exist"}


@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
	for u in users:
		if u.id == user_id:
			users.remove(u)
			return users
	return {"message" : "user doesn't exist"}


#FOR USERS (EDITING OWN DATA)
@app.post("/auth/register")
async def user_register(user: UserCreate):
	for u in users:
		if u.email == user.email:
			raise HTTPException(status_code=409, detail="user already exists")
		
	hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
	new_user = User(
		id=len(users) + 1,
		email=user.email,
		password=hashed_password,
		role="user",
	)
	users.append(new_user)

	new_user_profile = UserProfile(
		id=len(users_profile) + 1,
		firstName="",
		lastName="",
		age=None,
		bio="",
	)
	users_profile.append(new_user_profile)

	return users

@app.post("/auth/login")
async def user_login(user: UserCreate):
	for u in users:
		if u.email == user.email:
			if bcrypt.checkpw(user.password.encode('utf-8'), u.password.encode('utf-8')):
				user_dict = u.model_dump()
				active_refresh_tokens.clear()
				active_access_tokens.clear()
				access_token = create_access_token(user_dict)
				refresh_token = create_refresh_token(user_dict)
				return {
					"acccess token: " : access_token,
					"refresh token: " : refresh_token,
					}
	return {"message" : "Invalid email or password"}


@app.get("/auth/refresh")
async def refresh_access_token(refresh_token: str):
	try:
		user_data = verify_refresh_token(refresh_token)
		token_id = user_data.get('id')

		if token_id not in active_refresh_tokens:
			raise HTTPException(status_code=401, detail="Refresh token is not active.")
		
		active_refresh_tokens.remove(token_id)

		new_access_token = create_access_token(user_data)
		new_refresh_token = create_refresh_token(user_data)

		return {
			"access token: " : new_access_token,
			"refresh token: " : new_refresh_token,
			}
	except jwt.ExpiredSignatureError:
		raise HTTPException(status_code=401, detail="Refresh token expired")
	except jwt.JWTError:
		raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/protected")
async def protected_route(token: str):
	user_data = verify_access_token(token)
	return {"message" : f"Welcome man! I know ur role: {user_data['role']}"}

@app.get("/me")
async def get_current_user(token: str):
	user_data = verify_access_token(token)
	return {
		"email" : user_data['email'],
		"role" : user_data['role']
	}

def check_user_role(user_data, required_role):
	if user_data['role'] != required_role:
		raise HTTPException(status_code=403, detail="You can't access to this endpoint.")
	else: return True

@app.get("/admin")
async def admin_route(token: str):
	user_data = verify_access_token(token)
	if check_user_role(user_data, "admin"):
		return {"message" : f"Welcome, admin! You have full access."}

@app.get("/user-route")
async def user_route(token: str):
	user_data = verify_access_token(token)
	if check_user_role(user_data, "user"):
		return {"message" : f"Welcome, user! This resource for users only."}
	
@app.get("/auth/logout")
async def logout_user(token: str):
	user_data = verify_access_token(token)
	active_refresh_tokens.clear()
	active_access_tokens.clear()
	return {"message" : "successfully logged out."}

# @app.post("/user/profile")
# async def create_user_profile(token: str, user_profile: UserProfileCreate):
# 	user_data = verify_access_token(token)
# 	user = UserProfile(
# 		id = len(users_profile) + 1,
# 		firstName = user_profile.firstName,
# 		lastName = user_profile.lastName,
# 		age = user_profile.age,
# 		bio = user_profile.bio,
# 	)
# 	users_profile.append(user)
# 	return user



#FOR ME
#for /auth/refresh I'm keeping access token