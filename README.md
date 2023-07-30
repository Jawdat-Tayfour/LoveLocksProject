# LoveLocksProject
A Django Open Source Project To Simulate The Love Locks That Were Removed Of Pont Des Arts Bridge In Paris

# LoveLocksProject
A Django Open Source Project To Simulate The Love Locks That Were Removed Of Pont Des Arts Bridge In Paris




" The bridge couldn't survive and the Town Hall was forced to remove them in 2015 after part of the bridge collapsed."

That is where this project started.

I read an article which I will link down below that the love padlocks were removed off “Pont Des Arts” bridge.

I was in the middle of reading “Django For Beginners”  by William S. Vincent, which I mentioned in previous posts of mine.

I had this Idea to transfer the whole Love Padlock concept into something virtual that anyone from any place can take part in. Since, I missed my chance to place my own padlock on Pont Des Arts.

I started the project with the same blog concept that I learned from the book. I wanted to do more than just a blog but my skill set wasn’t totally ready for such a huge thing as what I ended up wanting this project to be, which is a form of a social network.

I have already built the skeleton of the website.
I replaced the old signing up mechanism with one that uses email verification to ensure that all of my users are real users. And got to learn more about tokens generation, temporarily links and how verifying by email works

I also implemented the password reset and password change the same way the book taught me to. So that wasn’t so new to me except the fact that writing the code for it without copying and pasting is pretty challenging.
![Log in](https://github.com/Jawdat-Tayfour/LoveLocksProject/assets/40719001/6296238d-a4da-4564-b7f4-fb2af3bdb335)
![Forgot Your Password](https://github.com/Jawdat-Tayfour/LoveLocksProject/assets/40719001/54755e31-a02d-489a-aee5-024b0069afed)
![Profile Settings](https://github.com/Jawdat-Tayfour/LoveLocksProject/assets/40719001/0211b49d-a4e2-4876-a2e0-7b80bd458c16)
![Change Password](https://github.com/Jawdat-Tayfour/LoveLocksProject/assets/40719001/d9580ad0-b064-4edc-a8a4-2b8f81bff05c)
![Email For Password Reset](https://github.com/Jawdat-Tayfour/LoveLocksProject/assets/40719001/6fa6eca5-1519-41d4-84e2-a2e31f5568a6)

I also learned how to fetch certain data from the database through reading many blogs and watching many tutorials about the subject, I created my own very simple User-Search functionality in this website.

I have also learned how friend/follow requests work on huge websites (or at least just the concept behind it ) by creating my own type of requests which I called “Lock Requests”. 
A Lock Request is just the trigger for creating what I called a Padlock.
And a padlock in this scenario is a mutual Post that has a title of choice “You and the other person’s motto as I assumed”, the date when your story started, your story but this one is optional because not all of us are writers or have the skill to write a good story.

Ok, so the whole thing until this point work this way to put it simply: 
- Create an account and verify from the link in you email
Sign Up : 
![Sign up](https://github.com/Jawdat-Tayfour/LoveLocksProject/assets/40719001/2f35b9ac-2be3-4c14-aab1-d21fa2bc89ab)

- Login to your account 
![Log in](https://github.com/Jawdat-Tayfour/LoveLocksProject/assets/40719001/df48f485-f1fb-4d7f-91e1-3c280028b71f)

- Search for the account of the person that you want to create the padlock
![Search for users](https://github.com/Jawdat-Tayfour/LoveLocksProject/assets/40719001/7672bf57-1e5e-4c95-b63d-a8ce46d9d32b)

- Request to create a lock with them (send a Lock Request)
![Search for users](https://github.com/Jawdat-Tayfour/LoveLocksProject/assets/40719001/00dd380c-bea9-4c1f-b319-df7decc0ca3f)

- Wait until they accept the request
![Accept Request or Decline it](https://github.com/Jawdat-Tayfour/LoveLocksProject/assets/40719001/92acd511-57cf-46c7-9d87-a0d351c81bb3)
![Post-Accept](https://github.com/Jawdat-Tayfour/LoveLocksProject/assets/40719001/51a754a3-9b38-497e-b808-e258f7a51102)


- Once they accept it, you can add the details to the padlock
![Post Accept for the first user](https://github.com/Jawdat-Tayfour/LoveLocksProject/assets/40719001/a6b21544-39c6-4e71-9185-8f13171bd68e)

- Then, the padlock will be sent for them to read, add, delete and fix anything - about the details that you have added
- When they finish up with the padlock the padlock gets published 
![Edit Padlock](https://github.com/Jawdat-Tayfour/LoveLocksProject/assets/40719001/74ad0366-d671-4597-845f-345b692992d4)

- Once it’s published it cannot be removed nor viewed until the anniversary - - of your story, which, you have entered previously while creating the padlock. You also cannot create another one, just like a real Love Padlock.
![Profile waiting for Lock Day](https://github.com/Jawdat-Tayfour/LoveLocksProject/assets/40719001/09be4729-6938-450e-b0ab-77ff518e6575)


What can you do with the website after you create the padlock, or, if you didn’t have the ability to create a padlock (You had no one that you would like to share such an experience with)?
 
You can scroll through other’s stories and mottos and add comments of your own which will show up on your profile for you to revisit whenever you want.

![Padlock View to others](https://github.com/Jawdat-Tayfour/LoveLocksProject/assets/40719001/579567ba-411e-41cc-9e60-50bc99336372)
![Padlock Details](https://github.com/Jawdat-Tayfour/LoveLocksProject/assets/40719001/9a299889-f61b-4c42-ab30-a92df907d1b1)
![Create Comment](https://github.com/Jawdat-Tayfour/LoveLocksProject/assets/40719001/f7921a88-d1f8-446e-961e-b6f470684761)


What happens on your Lock’s anniversary ?

You can view and modify your padlock.

![Profile at Lock Day](https://github.com/Jawdat-Tayfour/LoveLocksProject/assets/40719001/e4d284c4-3263-4160-94a6-bfbaccae4045)

Can you search for certain padlocks that you have not commented on?

Yes, just search their motto/title in your padlock search bar which only appears if you have created a padlock with someone.
![Profile at Lock Day](https://github.com/Jawdat-Tayfour/LoveLocksProject/assets/40719001/31ceb26f-a876-4eda-8665-68deb3ce3772)

What’s next ?

For the next week I will be writing tests and fixing some minor issues with the project, 
Such as which user can visit which page and under which circumstances.
I’ll go back to practise some more problem solving, just to keep my knowledge about Algorithms and Data Structures fresh in my memory

Once I make sure the whole project is sound and ready to push it into a github repo, I’ll make it an open source project which everyone can contribute to and take part in. Hopefully, that will happen in the next one or two weeks.

I’m gonna start working on two small projects right after I put this project up on my github, and continue with my Django journey with William S. Vincent’s next book, Django for Professionals: Production Websites with Python & Django.

Link for the article I mentioned :

https://lnkd.in/dpKdFNMV

Link for my GitHub:

https://lnkd.in/dpY__47J

Thanks for reading.

#Django #Python #webdevelopment #project #bootstrap
