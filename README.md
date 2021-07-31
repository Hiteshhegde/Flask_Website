# JobFinder
## Basic website with full functionality  written in Flask
##### Built using Flask Python and Postgres.
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
<img alt="Postgres" src ="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white"/>  
<img alt="Flask" src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"/>
<img alt="HTML5" src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"/>  
  
  
## *Setting up Postgres*
Install postgres using the below command:  
***sudo apt-get install postgresql postgresql-contrib***  

To verify installation, run the command:  
***sudo -u postgres psql -c "SELECT version();"***  

Create User and DataBase:  
***sudo su - postgres -c "createuser yourusername"***  
***sudo su - postgres -c "createdb yourdbname"***  

Grant privileges on the database to the user which you created in the previous commands:  
***sudo -u postgres psql***  
***grant all privileges on yourdbname  to yourusername;***  
***alter user yourusername with password 'yourpassword';***  

Run following to exit from psql:  
***\q***  

To Enable remote access to postgresql,by editing:  
***sudo vi /etc/postgresql/10/main/postgresql.conf***  

Change the line :  
***"listen_addresses = 'localhost' "*** to ***"listen_addresses = '\*' "***  
Save and exit the file

Restart postgresql:  
***sudo /etc/init.d/postgresql restart***  

## *Create Virtual environment and installing packages using requirements.txt*  

Execute these commands in your terminal creates a new folder:  
***mkdir new_folder***    
***cd new_folder***  

Execute these commands to create virtual environment:  
***python3 -m venv env***  
***source env/bin/activate***  

Install requirements.txt using pip:  
***pip install -r requirements.txt***  

## *Database Migration*  

Run the following commands in terminal:  
These commands creates a schema in the database  
***python3 manage.py db init***  
***python3 manage.py db migrate***  
***python3 manage.py db upgrade***  

## *Running the app*  

Before running the app we have to connect the db to flask app. We can do so by changing the DATABASE URL in the **\__init\__.py** file inside the jobfinder folder:  
***DATABASE_URL = "postgresql://yourusername:password@yourIP:yourport/yourdbname"***   


Run the following command from the root of project directory  
***python3 manage.py runserver***  

Now Open the browser and hit the url:  
***- localhost:5000***  

or the one in your terminal.  

