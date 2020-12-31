# Dev_Connect

### TrelloBoard

### Description

This social/work app allows developers to connect and collaborate with other developers on projects. Each developer has a brief profile with a photo, their project description/link and what they are looking for example a back-end developer might be looking for a front-end developer to finish their project to be ready to launch. Developers can then message other developers to organise collaboration. 

This app is an extension of LinkedIn, a career app designed to connect those seeking work with employers, fellow work colleagues and industry professionals. Dev-Connect as an extension will allow a connection of developers to start working on projects together through LinkedIn networks.

### Instructions
**Install python 3.9**
$ apt-get install python3.9

**Clone repository**
$ git clone https://github.com/Karen-Stewart80/Dev_Connect.git

**Change directory into app**
$ cd Dev_Connect

**Install venv**
$ pip install venv

**Create virtual environment**
$ python3.9 -m venv venv

**Activate virtual environment**
$source venv/bin/activate

**Install dependencies**
$ pip install -r requirements.txt

**Run app**
$ python src/main.py

**Set Flask variables**
$ export FLASK_APP=main.py
$ export FLASK_ENV=development
$ flask run

**Testing end points**

email: test0@test.com
password: 123456

Copy the JWT token generated and perform actions. This is the admin user able to perform admin rights in the database dump end points. Faker and random generated data is used in the database.


### CICD pipeline
Code will be pushed to Github repository. Unittest will run tests.





 
