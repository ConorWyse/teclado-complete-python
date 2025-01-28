from flask import Flask, render_template


app = Flask(__name__)
posts = {
    0: {
        'title': 'Hellow, world',
        'content': 'This is my first blog post!'
    }
}


@app.route('/')
def home():
    return 'Hello, world!'


@app.route('/post/<int:post_id>')
def get_post(post_id):
    post = posts.get(post_id)
    if not post:
        return render_template('404.jinja2', message=f'A post with id {post_id} was not found.')
    #return f"Post {post['title']}, content:\n\n{post['content']}"
    return render_template('post.jinja2', post=post)


if __name__ == '__main__':
    app.run(debug=True)
