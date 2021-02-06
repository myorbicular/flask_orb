from flask import request, jsonify, abort, make_response
from flask import current_app as app
from .models import db, Post
from .schemas import *

"""
@app.route('/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
"""

#adding a post
@app.route('/api/v1/post', methods = ['POST'])
def add_post():
    title = request.json['title']
    description = request.json['description']
    author = request.json['author']
 
    my_posts = Post(title, description, author)
    db.session.add(my_posts)
    db.session.commit()
    return post_schema.jsonify(my_posts)

#getting posts
@app.route('/api/v1/get', methods = ['GET'])
def get_post():
    all_posts = Post.query.all()
    result = posts_schema.dump(all_posts)
    return jsonify(result)
 
 
#getting particular post
@app.route('/api/v1/post_details/<id>/', methods = ['GET'])
def post_details(id):
    post = Post.query.get(id)
    return post_schema.jsonify(post)
 
 
#updating post
@app.route('/api/v1/post_update/<id>/', methods = ['PUT'])
def post_update(id):
    post = Post.query.get(id)
    title = request.json['title']
    description = request.json['description']
    author = request.json['author']
 
    post.title = title
    post.description = description
    post.author = author
    db.session.commit()
    return post_schema.jsonify(post)
 
 
#deleting post
@app.route('/api/v1/post_delete/<id>/', methods = ['DELETE'])
def post_delete(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return post_schema.jsonify(post)


