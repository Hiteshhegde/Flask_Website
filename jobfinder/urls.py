from flask import request, jsonify, render_template, flash, redirect, url_for
from jobfinder import app, db, bcrypt
from jobfinder.models import Job, User, UserProfile
from jobfinder.forms import RegistrationForm, LoginForm, ProfileForm
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
def main():
    return render_template('main.html', title='Main')

@app.route("/home")
def home():
    return render_template('home.html', title='Home')


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/dashboard", methods=['GET','POST'])
def dashboard():
    form = ProfileForm()
    if form.validate_on_submit():
        user_profile = UserProfile(
                    user_profilename=form.full_name.data,
                    user_int_position=form.position_int.data,
                    user_jobtype= form.job_type.data,
                    user_city = form.city.data,
                    user_state = form.state.data,
                    user_skills = form.skills.data,
                    user_work_status = form.work_status.data,
                    user_work_auth = form.work_auth.data
            )
        db.session.add(user_profile)
        db.session.commit()
        flash('Your profile has been saved', 'success')
        return redirect(url_for('home'))
    return render_template('dashboard.html', title='Dashboard', form=form)


# Rendering scraped Jobs at /jobs endpoint 
@app.route("/jobs", methods=['GET'])
def jobs():
    try:
        jobs = Job.query.all()
        return render_template('jobs.html', title='Jobs', jobs=jobs)
    except Exception as e:
        return(str(e))

@app.route("/profiles", methods=['GET'])
def profiles():
    try:
        profiles = UserProfile.query.all()
        return render_template('profiles.html', title='Profiles', profiles= profiles)
    except Exception as e:
        return(str(e))



# Rendering register forms at /register endpoint
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email= form.email.data, password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You can now login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


# Rendering login form at /login endpoint

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main'))

    """
job2= Job(jobid='2',position='Front-end Developer', 
joburl='https://www.google.com/', 
categor='Science', subcategor='Technology', 
company='Snap Inc.', remote = 'Yes', status='U.S Citizens only',
 description='Front-end developement using Reactjs')
    """
