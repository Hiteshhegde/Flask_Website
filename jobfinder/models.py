from flask_sqlalchemy import SQLAlchemy
from jobfinder import db, login_manager
from flask_login import UserMixin


# Create data models here

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# creating db model for storing scraped jobs

class Job(db.Model):
    __tablename__ = 'job'

    id = db.Column(db.Integer, primary_key=True)
    jobid = db.Column(db.String, unique=True)
    position = db.Column(db.String)
    location = db.Column(db.String)
    company = db.Column(db.String)
    remote = db.Column(db.String)
    status = db.Column(db.String)
    description = db.Column(db.String)
    joburl = db.Column(db.String)
    categor = db.Column(db.String)
    subcategor = db.Column(db.String)
    tags  = db.Column(db.String)




    # Repesents the unique id when queried for data

    def __repr__(self):
        return f'<Job:{self.position}, Job url: {self.joburl}>'

    # serializing the data
    def serialize(self):
        return {
            'id' 			: self.id,
            'jobid'			: self.jobid,
            'position'		: self.position,
            'location'      : self.location,
            'company'       : self.company,
            'remote'        : self.remote,
            'status'        : self.status,
            'description'   : self.description,
            'joburl' 		: self.joburl,
            'categor'		: self.categor,
            'subcategor' 	: self.subcategor,
            'tags'          : self.tags
        }


# creating Db model for User

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    userprofiles = db.relationship('UserProfile')

        

    def __repr__(self):
        return f"<User:'{self.username}','{self.email}>"

    def __str__(self):
        return f"<User: {self.username}>"



#Creating DB model for User profiles/ Job seeker 
class UserProfile(db.Model, UserMixin):
    __tablename__ = 'userProfile'

    id = db.Column(db.Integer, primary_key=True)
    user_profilename = db.Column(db.String(50), nullable=False)
    user_int_position = db.Column(db.String(25), nullable=False)
    user_jobtype = db.Column(db.String(20), nullable=False)
    user_city = db.Column(db.String(20), nullable=False)
    user_state = db.Column(db.String(20), nullable=False)
    user_skills = db.Column(db.String(120), nullable=False)
    user_work_status = db.Column(db.String(), nullable=False)
    user_work_auth = db.Column(db.String(20), nullable=False)
    user_remote_status = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    

    def __repr__(self):
        return f"<User Profile : {self.user_profilename} ',' {self.user_int_position}>"


    # serializing the data
    def serialize(self):
        return {
            'id'                : self.id,
            'user_profilename'  : self.user_profilename,
            'user_int_position' : self.user_int_position,
            'user_jobtype'      : self.user_jobtype,
            'user_city'         : self.user_city,
            'user_state'        : self.user_state,
            'user_skills'       : self.user_skills,
            'user_work_status'  : self.user_work_status,
            'user_work_auth'    : self.user_work_auth,
        }