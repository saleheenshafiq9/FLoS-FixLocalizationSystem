# FLoS-FixLocalizationSystem
 The “Fix Localisation System” (FLoS) is a web application that automates the testing process for localization in a mobile application. It will handle localization for text, media contents (audio, video & image) and user interfaces.
 
 ## 2.1 Overview of FLoS
The “Fix Localisation System” (FLoS) is a web application that automates the testing process for detecting
localization in a mobile application and provides fixes for the issues. It handles localization for both text
and media content (audio, video & image). It has three modules which are registration & login for
creating an account, project handling module for creating projects & controlling access to it and finally
test & fix localization module. The modules are described below:
### 2.1.1 Registration & Login
A user needs to sign up for creating an account and to do that, he needs to enter his username(unique),
email, password and additional information (e.g company name). To verify the email address, an OTP is
generated and sent to the mail. The user needs to enter that OTP to confirm his email address.
If the user forgets his password and wants to recover his account, an OTP is generated and sent to the
email address for that account. The user needs to enter that OTP to authenticate his identity and now, he
can create a new password for his account. Note that, the users can change their user information
anytime after logging in.
### 2.1.2 Project Handling
After logging in, the user can create a new project and become the project owner. He may search and
add other users in the project and the added users are called testers. The project owner can edit project
information and view results of all localization tests run. He can set the project to be private or
community. For community projects, the tester can see the test results of other testers associated with
the project. For private projects, they can only view their own results.
A user can also view the list of existing projects he has access to. After selecting a project, the user can
view the list of localization tests and their results for that project. The list includes the following
information - the apk file that was submitted for testing, time of when the test was conducted, number
of localization issues detected and fixed, fixed apk file and any additional comments.
### 2.1.3 Test & Fix Localization
The user can choose to run a new test for a project and for that, he uploads the apk file. Then the user
needs to select languages(e.g. French, English etc) for which he wishes to run the localization tests.
After selecting languages, the user confirms his submission and then, the system initiates testing of
localization that respects the value of universalism.
The system checks for localization in text and media content. It detects the language for text-content and
subtitles, voice speech & captions for media-content.
After that, the user can view the Localization Test Report. The localization test report includes - list of
localization issues & their content type (text or media content), status (whether issues are found or not),
line of code where the localization issue has occurred, link to the content (image, audio, video) with
localization issues and tester who has run the test.
After viewing the report, the user is asked to select the localization issues he wants to resolve from the
localization issues’ list. The system then tries to generate fixes for those localization issues in 3 steps:
#### 1. Translation: System translates & saves the texts, subtitles and captions in a translation file. The
user may check the translation file and see whether the translation is correct or not. If he does
not like any translation, he may download, edit and upload the translation file.
#### 2. Fixing Graphical User Interface(GUI): If translated text requires more space than the size of the
GUI element the text is in, then the GUI element is resized by the system in a manner that the
fixed GUI remains consistent with the original GUI.
#### 3. Media Content Fix: System adds translated subtitles to video and audio in the selected language.
It also translates extracted texts from images as captions to fix that issue.
After patching the fixes in the source code, the system presents the results as a Localisation Fix Report.
The report includes - report version and type, issue status (total number of fixed localization issues & unfixed localization issues), list of localization issues, their content type, line of code & whether they
were fixed or not, link to the original & fixed content so that the user may view them. Tester who has run
the test can download the fixed apk file or add comments once the fix generation is completed.
A notification is sent to the project owner after the localization fix report is generated. Note that the
report & fixed apk file are stored in the system as a log. After a year, the project owner will be asked
whether he wants to archive the log data or not.
## 2.2 Assumption
1. An APK file for the mobile application will be available.
2. System will generate the translation but ultimately, uploading the correct translation is the duty
of the tester.
3. API for all phases of coding will be available and the API query limit will not be exceeded.
## 2.3 Scope
1. We only cover text & media content based localization that respects the value of universalism.
2. When generating a fix, we only consider height, width & spacing.
