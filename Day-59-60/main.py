# Imports
import smtplib
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

# Send-Email
def send_email(body):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="YOUR_USERNAME", password="YOUR_PASSWORD")
        connection.send_message(msg=body, to_addrs="TO_ADDR", from_addr="FROM_ADDR")

# Contact Route
@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", msg="Contact Me")
    elif request.method == "POST":
        form_data = request.form

        name = form_data.get("name")
        email = form_data.get("email")
        phone = form_data.get("phone")
        message = form_data.get("message")

        body = f"Name: {name}\nE-Mail: {email}\nPhone: {phone}\nMessage: {message}"



        return render_template("contact.html", msg="Successfully Sent your message")

# View Blog
@app.route('/blog')
def view_blog():
    params = request.args.get("id")

    blog = post_obj.get_blog(id=params)

    return render_template("post.html", blog=blog)

# Main
if __name__ == "__main__":
    app.run(debug=True)
