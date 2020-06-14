# OctupusTest
Author: Akshay Sapra
Library Required: 
* django
* Selenium 

## Platform used: Windows

Steps to make the web app:
*	Create project:  ```django-admin startproject octopusTest ```
*	Create app: ```python manage.py startapp octTest```
*	Made the changes in settings.py to allow octTest app
*	Made the changes in models.py to specify the data fields
*	Initial migration to generate migration files: ```python manage.py makemigrations```
*	Runs all the migration in project: ```python manage.py migrate```
*	Run management command: ```python manage.py load_data```
*	Create superuser: ```python manage.py createsuperuser```
*	Verifying the changes through admin credentials.

## Testing the app:
* Download the code to your local machine, open the terminam/command prompt and go the path.
* Run the application by using the following command ``` python manage.py runserver```
* Open the url: http://localhost:8000/admin
*Use the credentials: 
>- Username: asapra
>- password: Octopus$5

 

## Instruction for creating Testing Suite:
*	Install virtual environment: ```pip3 install venv```
*	Making Virtual environment: ```virtualenv venv_main```
*	Starting virtual environment (slight change in command for windows): ```call venv_main/Scripts/activate``` 
*	Installing selenium in virtualenv: ```pip install selenium```
*	Download Geckodriver according to the machine (I used the one for windows) from https://github.com/mozilla/geckodriver/releases
*	After downloading the driver, unzip the downloaded file and copy the geckodriver.exe file to the venv_main/Scripts folder (for windows)
*	Installing Django in virtual environment: ```pip install Django```
*	Make the changes in test.py to add the unit test and functional tests

## Testing the Test Suite
*	After creating the test cases, we will start the app by ```python manage.py runserver``` in a terminal window or command prompt
* Open another command prompt/terminal window and start the virtual enviroment by running the following command ```call venv_main/Scripts/activate``` 
* in the virtual environment window go to the path where app is located.
* Run the test cases by using ```python manage.py test```
*	If permission is required, grant the permission to the machine.

Note: I have created some sample unit tests and functional tests with a dummy html. More tests can be added according to the functionality.
