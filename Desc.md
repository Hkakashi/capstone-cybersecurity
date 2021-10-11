# Welcome to the Cybersecurity Capstone Project!

Your task for the next few weeks is to build a simple, secure messaging system. Users should be able to post messages to other user, and read messages sent to them. The system must be secure so no unauthorized people should be able to read a message.

# **Web Server Details**

Your messaging system must be web-based. You can either run your code on your own server OR provide a package that will run a local server on the user’s machine. In either case, you must also provide your source code.

## **Requirements**

All the functionality outlined in the interface details must be accessible over an http connection with HTML-based web pages. You cannot embed an applet, servlet, flash, or other application in a web page to serve as this project.

## **Access**

If you implement this on your own server, you should provide the URL of the home page.

If you provide a local repository, it must meet the following requirements.

- An evaluator can download an archive that contains all the necessary libraries and code.

- An automated system will invoke make in the build directory of your submission.

- make must function without internet connectivity and it must return within ten minutes.

- Evaluators should not require any libraries or installation on their own machines. All necessary libraries must be included in your archive.

- Your software must be actually built, through initiation of make, from source (not including libraries you might use). Submitting binaries (only) is not acceptable.

make should produce an executable file that can be launched to run the server. Your server must be accessible through any web browser on the machine where the server is running at http://localhost:5813

## **Functionality**

### Interface

The user interface is the way users and evaluators will interact with your messaging system. You should think carefully about the usability of the interface, particularly with respect to the security elements.

It must include the following pages:

- index.html, the default home page, which should have links to “Register” or “Log in”

- Registration page where users register for the system. You can design your own process. For example, you may have users provide all their information, including a username and password, up front or you can create a multi-step registration process with email verification, etc. You can use whatever type of password / authentication system you like. After successfully registering, users should be taken to the login page.

- Login page, where users authenticate. If a user does not remember their login information, there should be some way to reset it (use whatever you like – email, text, security questions, etc.) After successfully authenticating, they should be taken to their inbox.

- Inbox, where users can see messages sent to them. You can display this however you like – clickable with previews like email, a long running list of messages similar to the Twitter newsfeed, or anything else you like. The requirements are simply that the user can see new messages sent to them. You can decide how you want to manage message storage after they have been read the first time.

- Send message page allows users to send messages to other users. One user should be able to address a message to another by username.

You are free to create other pages as you see fit.

### Message Storage

You may store your message data anyway you like. Use flat files, databases, etc. However, you must encrypt the data before you store it. You can use whatever encryption mechanism you like.

Evaluators should be able to dump your database and view the contents. This should be accessible at http://example.com/YOUR HOME DIRECTORY/dbdump if you are running on your own server or http://localhost:5813/dbdump if you are providing a local server. Dump the data as plain text files using whatever formatting you like. If the data is encrypted, you can dump it as encrypted. If there are binaries, use whatever plain-text export functionality your database has. The goal here is for people to see how your data is stored, not to review every entry in the database.

## **Rules**

- Do not obfuscate your code

- Teams must do their own work and not share solutions with others.

## **Scoring**

See the evaluation rubric for scoring awarded for each element of the core functionality and for usability analysis.

A bug is defined as incorrect behavior by a program. In this case, a bug must be a behavior that violates one of the functionality or access requirements described above. A vulnerability is defined as a security exploit in a program. Again, these should be security exploits related to the functionality outlined above; it could be allowing inappropriate access to messages or accounts. A vulnerability in, say, a javascript library you use would not count against you in this capstone. A crash is defined as unexpected program termination. We are adopting a strict definition of a crash for the purposes of the capstone. It must be one that causes the app to abort or otherwise completely stop working (requiring either a manual or automatic restart).

For every unique bug found against your submission during the Break-it phase, you will lose 5 points. For every unique bug found against your submission that leads to a crash, you will lose 10 points. For every unique vulnerability found during the Break-it phase, you will lose 15 points.

Usability will be scored as the sum of the ratings your evaluators provide on their analysis of your authentication system. See the rubric for the exact elements they will look for. Each team will rate the usability (not the security) of your user-facing authentication system on the following scales:



| difficult   | 1 2 3 4 5 6 7 8 9 | easy       |
| ----------- | ----------------- | ---------- |
| frustrating | 1 2 3 4 5 6 7 8 9 | satisfying |
| terrible    | 1 2 3 4 5 6 7 8 9 | wonderful  |
| confusing   | 1 2 3 4 5 6 7 8 9 | very clear |
| slow        | 1 2 3 4 5 6 7 8 9 | fast       |

# **Evaluation**

You will evaluate three other teams’ projects. For each project, you will be provided with:

\1. The source code, accessible at a repository

\2. Either a live, running web-based system or a locally compilable server that you can run on your system according to the instructions above.

\3. Access to dump the database

You will evaluate the usability and security of each project as described in the rubric.

Your evaluations will all be reviewed by the other teams that analyzed the same project. For example, if you are team A, your analysis of Team B will be reviewed by Teams C and D. Your analysis of Team C will be reviewed by Teams B and D. Your analysis of Team D will be reviewed by teams B and C.

## **Evaluation Groupings**

Each team will be connected to three other teams. Your team will evaluate the projects of all three other teams. They will all evaluate your project. You will also give feedback on the other teams’ evaluations.

For example, if we have Teams A, B, C, and D:

- Team A will evaluate the projects of Teams B, C, and D.

- Team B will evaluate the projects of Teams A, C, and D

- Team C will evaluate the projects of Teams A, B, and D

- Team D will evaluate the projects of Teams A, B, and C.

Then, each team will provide feedback on the evaluations of the projects they have seen. For example, Team A will give feedback on:

- Team B and Team C’s evaluation of Team D

- Team B and Team D’s evaluation of Team C

- Team C and Team D’s evaluation of Team B

In all, each team will evaluate 3 projects and give feedback on 6 evaluations. In turn, the team will receive three evaluations of their own project with two evaluations of each project evaluation.

## **Primary Evaluation**

First, you will evaluate the projects of assigned teams. This will have three major components:

\1. Requirements Met – does the project have all the required pages and functionality? If you try it, does it work for you?

\2. Usable Security Analysis - Is the password easy to remember? Is the login easy? Are the most secure behaviors the easiest to do? What elements could be confusing to users and which are easy? How does the usability impact the security? For example, if a long password is required, are there steps taken to make it easier to remember? If not, could it lead to frequent password resets that could be exploited?

\3. Break it – Try to break the security of the project you are evaluating. Access data you are not supposed to. Decrypt data in the data base. Log in as someone else. Find whatever security holes you can and document both your process of discovering them and how the weakness can be exploited. Provide as much documentation as you can of the steps you take to access the system illicitly and what you were able to do once you broke it.

Below is a checklist of items to evaluate for the Requirements and Usable Security Analysis with room for you to add in your own discussion of additional elements.

Assemble all of this into a clear, easy-to-read report for the project creators and other evaluators to look at.

## **Evaluation Feedback**

After completing your three evaluations, you will provide feedback on others’ reports about the projects you have evaluated. You will offer both feedback and reflection on the other teams’ reports according to the rubric.

## Scoring

Your evaluation will be scored based on the feedback from other teams and on how many problems you find in the other team’s projects. For an evaluation report you receive:

- 5 points for each A / DO answer in the Basic Functionality section (75 points total)

- 5 points for each “Yes” answer in the Usability Analysis section (25 points total)

- The following points for the Break It section:

- For each bug you find that is verified by the teams providing you feedback, you earn 5 points.

- For each bug that leads to a crash that you find and that is verified by the teams providing you feedback, you earn 10 points.

- For each security vulnerability you find that is verified by the teams providing you feedback, you earn 15 points.

- Bugs and vulnerabilities that neither feedback team can replicate and validate will receive 0 points.