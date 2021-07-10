## Flask_Website
### Basic website with full functionality  written in Flask

### *Setting up Postgres*
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
***alter user devopsuser with password 'yourpassword';***  

Run following to exit from psql:  
***\q***  

Enable remote access to postgresql,by editing:  
***sudo vi /etc/postgresql/10/main/postgresql.conf***  

Change the line :  
***"listen_addresses = 'localhost' "*** to ***"listen_addresses = '\*' "***  
Save and exit the file

Restart postgresql:  
***sudo /etc/init.d/postgresql restart***  

### *Activate existing python3 virtual environment which includes all packages.*

Go into the cloned directory:  
***cd Flask_Website***  

Type the follwing command and you are in virtual env:  
***source env/bin/activate***

### *Create Virtual environment and installing packages using requirements.txt*  

Make a folder and create virutal env as so:  
***mkdir new_folder***    
***cd new_folder***  
***python3 -m venv env***  
***source env/bin/activate***  

Install requirements.txt using pip:  
***pip install requirements.txt***  

### *Database Migration*  

Run the following commands in terminal:  
These commands creates a schema in the database  
***python3 manage.py db init***  
***python3 manage.py db migrate***  
***python3 manage.py db upgrade***  

### *Running the app*  

Run the following command from the root of project directory  
***python3 manage.py runserver***  

Now Open the browser and hit the url:  
***- localhost:5000***  

or the one in your terminal.  

