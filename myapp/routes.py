from flask import render_template, request, redirect, url_for, flash, make_response
from flask import current_app as app
from .models import db, Post
from flask_classy import FlaskView, route

#This is the index route where we are going to
#query on all our employee data
@app.route('/')
def Index():
    post_data = Post.query.all()
    return render_template("index.html", posts = post_data)


#this route is for inserting data to mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        author = request.form['author']

        post_obj = Post(title, description, author)
        db.session.add(post_obj)
        db.session.commit()

        flash("Employee Inserted Successfully")
        return redirect(url_for('Index'))


#this is our update route where we are going to update our employee
@app.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        post_obj = Post.query.get(request.form.get('id'))
        
        if post_obj:
            post_obj.title = request.form['title']
            post_obj.description = request.form['description']
            post_obj.author = request.form['author']
            db.session.commit()
            flash("Employee Updated Successfully")
            return redirect(url_for('Index'))
        
        flash("Object Does Not Exist!")
        return redirect(url_for('Index'))


#This route is for deleting our employee
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    post_obj = Post.query.get(id)
    
    if post_obj:
        db.session.delete(post_obj)
        db.session.commit()
        flash("Employee Deleted Successfully")
        return redirect(url_for('Index'))
    
    flash("Object Does Not Exist!")
    return redirect(url_for('Index'))


##################### class based views ##############################

#created home view
class HomeView(FlaskView):
 
    def index(self):
        return "<h1>Codeloop.org - Flask Classy Tutorial<h1>"
 
    def get(self, id):
        return "<h1>codeloop.org, ID is {} </h1>".format(id)
 
 
    @route('/contact/')
    def contact(self):
        return "<h1>codeloop.org, this is contact route</h1>"
 
 
HomeView.register(app)