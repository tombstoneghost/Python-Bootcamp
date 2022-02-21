# Imports
from flask import Flask, render_template, request
from posts import Post


# Flask Configurations
app = Flask(__name__)

# Post Objects
post_obj = Post()

# Home Route
@app.route('/')
def index():
    blogs = post_obj.get_all_blogs()
    return render_template("index.html", blogs=blogs)

# About Route
@app.route('/about')
def about():
    return render_template("about.html")

# Contact Route
@app.route('/contact')
def contact():
    return render_template("contact.html")

# View Blog
@app.route('/blog')
def view_blog():
    params = request.args.get("id")

    blog = post_obj.get_blog(id=params)

    return render_template("post.html", blog=blog)


# Main
if __name__ == "__main__":
    app.run(debug=True)
