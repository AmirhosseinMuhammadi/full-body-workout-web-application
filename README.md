# full-body-workout-web-application

# Goals
After learning concepts of panel framework, it’s time to create real world projects.
The Idea is to make a sport related web application that helps people in their workout. If focuses on full body and has all the fundamentals of web app development. In this project I wish to work on options like creating user accounts and manipulating data.

# Objectives
I developed 3 main pages using panel. Home page with some basic information about the app, register page for sign in or sign up and main page which is the user panel and is accessible when the user logs into the site. There is almost no HTML and CSS and I used only panel to create frontend and backend(despite the limitations of the framework in the server side development.).

# Challenges & Solutions
Here I should mention that using HTML and CSS can be extremely challenging in panel. I had problems using CSS animations in the home page and after searching a lot I could find some solutions with the help of ChatGPT.
Also to animate some features and elements css is not enough and javascript is needed. Since using javascript wasn’t possible I made some gif files and used them instead of JS and CSS animations.
One of the biggest problems of panel is serving multiple pages. In order to transfer from one page to another the serve() function can be used, however it makes problems and bugs for serving some widgets specially input type widgets. I couldn’t find any way to fix this problem and I believe it can be a bug and it should be solved in the future updates. Therefore I served multiple pages when I hosted the pages from the terminal.
The most challenging part was making login/sign up actions and create user dashboards. Since I’ve not used any RDMS or databases in this project, I replaced all the related features by using text files and CSV files, so every data of registered user saves into either a text file or a CSV file.

# CONCLUSION
When users are registered and logged into the app, they can use its features. They can see their profile name in the Profile tab, change their profile photo, change their password, log out or even delete their account.
In the Report Tab users can enter their height and weight and observe their BMI and the healthy weight range.
The Chat tab provides a way for all the users to communicate to each other and share their fitness experiences. This tab is not actually completed but it’s not much difficult to complete the development of this part. I’m not in the mood anyway. The Training tab’s purpose is obvious. Since it’s not a commercial project, there’s only low content for arm workout and there is nothing for the others. Some screen shots from the app are available in this repository.
