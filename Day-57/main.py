# Imports
from flask import Flask, render_template, request
from post import Post

# Flask Configurations
app = Flask(__name__)

# Post Object
post_obj = Post()

@app.route('/')
def home():
    blogs = post_obj.get_all_blogs()
    return render_template("index.html", blogs=blogs)

@app.route('/blog', methods=['GET'])
def show_post():
    params = request.args.get("index")
    
    blog = post_obj.get_blog(id=params)

    return render_template("post.html", blog=blog)


if __name__ == "__main__":
    app.run(debug=True)
