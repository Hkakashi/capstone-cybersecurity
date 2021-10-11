# Evaluation Rubric

Your project will be evaluated by other teams. This rubric describes the criteria they will use for the evaluation and the points awarded.

## Basic Functionality

Scoring awards the project’s team 10 points for every Yes and 0 points for every No. 150 points total

- [ ] Code repository is downloadable	?

- [ ] Database dump from /dbdump is successful	?

- [ ] Are messages in the database encrypted?

- [ ] Can you access the website	?

## Interface elements

To test this, please create two accounts and send a message from each account to the other. Answer Yes/No to each prompt.

- [ ] Is there an index.html page that includes options (or links to pages) to register and to login

- [ ] Registration page present

- [ ] Registration page functional

- [ ] Login page present

- [ ] Login works after registration

- [ ] Page to see messages sent to the user is present

- [ ] Messages to the user are actually shown on the messages page

- [ ] Page to send messages is present

- [ ] Messages are successfully sent to the recipient

## Security Usability Analysis

Score for the project team is 2 X the sum of ratings on the final question’s scale. 50 points total. Also answer the following descriptive questions.

- What are the password requirements?

- Could a user who just wants to access the system as quickly / easily as possible circumvent the security measures with insecure behavior (e.g. a “12345” password, etc.)?

If there is password-based authentication…

- How easy is it for a person to memorize this password? Is it easier or harder than a standard 8-character password that requires upper case, lower case, numbers, and punctuation? Justify your answer with principles of memory such as the 7+/-2 rule, chunking, etc.

- Please indicate More Usable, Equally Usable, Less Usable and provide a reason.

If there is no username-password authentication, but something else in its place…

- How usable is this alternative to a standard 8-character password? Justify with principles of usability: speed, efficiency, memorability, learnability, user preference. Please indicate More Usable, Equally Usable, Less Usable and provide a reason.

If there are authentication measures beyond the initial authentication step…

- What are the additional steps?

- How long to the additional steps take to complete (time it)?

- How usable are the additional steps? Justify with principles of usability: speed, efficiency, memorability, learnability, user preference.

Rate the user experience with the authentication mechanism on this site on the following scale. Note that you are not rating how secure it is, only the experience for the user:

| very difficult   | 1 2 3 4 5 | very easy        |
| ---------------- | --------- | ---------------- |
| very frustrating | 1 2 3 4 5 | very satisfying  |
| really terrible  | 1 2 3 4 5 | really wonderful |
| very confusing   | 1 2 3 4 5 | very clear       |
| very slow        | 1 2 3 4 5 | very fast        |



## Break It

Scoring for the project’s team: 

- For every unique bug found against your submission during the Break-it phase, you will lose 5 points. 
- For every unique bug found against your submission that leads to a crash, you will lose 10 points. 
- For every unique vulnerability found during the Break-it phase, you will lose 15 points.

Recall the following definitions:

> A bug is defined as incorrect behavior by a program, while a vulnerability is defined as a security exploit in a program. 
>
> A crash is defined as unexpected program termination due to violations of memory safety.

- For each bug you find that other teams can verify, you earn 5 points.

- For each bug that leads to a crash that you find that other teams can verify, you earn 10 points.

- For each security vulnerability you find that other teams can verify, you earn 15 points.

Document each unique way you break the system. Provide clear step-by-step instructions on how to detect the bug, cause the crash, or exploit the vulnerability. You will not receive any points if other teams cannot replicate your results.

A bug or vulnerability is unique if it uses a different problem in the system. For example, if an SQL injection attack can let you change a message and also read a message or delete a message, that counts only as one vulnerability: the system is not robust against SQL injection attacks. It would not count as three vulnerabilities (one for changing, one for deleting, one for reading).

Number each problem, beginning with 1. Label each as “bug”, “crash”, or “vulnerability”. Thoroughly document how another team could replicate your finding.