import React from 'react';
import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
} from '@/components/ui/navigation-menu';
import { SignedIn, UserButton } from '@clerk/clerk-react';
import { Link } from 'react-router-dom';

export default function Home() {
  return (
    <>
      <SignedIn>
        <div className="flex justify-between items-center mr-4 mt-2 border-b-4">
          <h1 className="ml-60 text-2xl">KazMentor</h1>
          <div className="flex">
            <NavigationMenu className="">
              <NavigationMenuList className="w-42">
                <NavigationMenuItem>
                  <NavigationMenuTrigger>
                    <Link to="/learn">
                      <h1 className="text-2xl">Learn</h1>
                    </Link>
                  </NavigationMenuTrigger>
                  <NavigationMenuContent className="">
                    <div className="w-96">
                      <NavigationMenuLink>
                        <h1 className="text-2xl">Physics</h1>
                      </NavigationMenuLink>
                      <NavigationMenuLink>
                        <h1 className="text-2xl">Biology</h1>
                      </NavigationMenuLink>
                      <NavigationMenuLink>
                        <h1 className="text-2xl">Computer Science</h1>
                      </NavigationMenuLink>
                      <NavigationMenuLink>
                        <h1 className="text-2xl">Chemistry</h1>
                      </NavigationMenuLink>
                    </div>
                  </NavigationMenuContent>
                </NavigationMenuItem>
              </NavigationMenuList>
            </NavigationMenu>

            <NavigationMenu>
              <NavigationMenuList>
                <NavigationMenuItem>
                  <NavigationMenuTrigger>
                    <h1 className="text-2xl">Ask the Legends</h1>
                  </NavigationMenuTrigger>
                  <NavigationMenuContent>
                    <div className="w-42">
                      <NavigationMenuLink>
                        <h1 className="text-2xl">Tesla</h1>
                      </NavigationMenuLink>
                      <NavigationMenuLink>
                        <h1 className="text-2xl">Enstein</h1>
                      </NavigationMenuLink>
                    </div>
                  </NavigationMenuContent>
                </NavigationMenuItem>
              </NavigationMenuList>
            </NavigationMenu>
          </div>
          <UserButton
            appearance={{
              elements: {
                avatarBox: {
                  width: '45px',
                  height: '45px',
                },
              },
            }}
          />
        </div>
      </SignedIn>
    </>
  );
}
