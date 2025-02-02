from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ContactForm(BaseModel):
		name: str
		email: str
		message: str

@app.post("/contact")
async def submit_contact_form(form_data: ContactForm):
		print(f"Name: {form_data.name}")
		print(f"Email: {form_data.email}")
		print(f"Message: {form_data.message}")

		return {"message": "Form submitted successfully!"}
