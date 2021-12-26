import sqlite3

from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdf'


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        people = request.form['content']
        matching_ingredients = get_matching_ingredients(people)
        return render_template('post.html', ingredients=matching_ingredients)
        #return render_template('post.html', ingredients=matching_ingredients)
        
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM person').fetchall()
    conn.close()
    return render_template('index.html', people=posts)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    # so you can have name-based access to columns
    conn.row_factory = sqlite3.Row
    return conn
    
def get_post(post_id=None):
    post = None
    if post_id is not None:
        conn = get_db_connection()
        post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
        conn.close()
    if post is None or post_id is None:
        abort(404)
    return post

def get_matching_ingredients(people):
    names = people.split('\n')
    names = [name.strip() for name in names]
    conn = get_db_connection()
    matching_ingredients = []
    first_pass = True
    # start with assumption all ingredients are good
    good_ingredients = {ing[0] for ing in conn.execute('SELECT name FROM ingredient_types').fetchall()}
    for name in names:
        print(name)
        name_id = conn.execute('SELECT person_id FROM person WHERE name=?',
                               (name,)).fetchall()
        if len(name_id) > 0:
            name_id = name_id[0][0]
            good_ingredients_results = conn.execute('SELECT it.name FROM preference p JOIN ingredient_types it ON it.ingredient_id = p.ingredient_type_id WHERE person_id = ? AND preference_type_id = ?', (name_id, 1)).fetchall()
            # extract as set 
            good_ingredients = good_ingredients.intersection({name[0] for name in good_ingredients_results})
        #breakpoint()
    return good_ingredients

"""a variable rule <int:post_id> to specify that the part 
after the slash (/) is a positive integer (marked with the
int converter) that you need to access in your view function.
Flask recognizes this and passes its value to the post_id
keyword argument of your post() view function"""
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', 
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')
    
@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)
    
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
            
    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))


if __name__ == "__main__":
    print('running as script')
    app.run(host='0.0.0.0')
