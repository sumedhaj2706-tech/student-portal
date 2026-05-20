from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# Connect to local MongoDB
client = MongoClient("mongodb+srv://devsync:devsync123@cluster0.mchqn3s.mongodb.net/?appName=Cluster0")

# Create database
db = client["student_portal"]

# Create collection
collection = db["submissions"]


# Home Route
@app.route('/')
def index():
    return render_template('index.html')


# Form Submission Route
@app.route('/submit', methods=['POST'])
def submit():

    # Receive form data
    name = request.form['name']
    usn = request.form['usn']
    title = request.form['title']
    link = request.form['link']

    # Insert into MongoDB
    collection.insert_one({
        "name": name,
        "usn": usn,
        "title": title,
        "link": link
    })

    # Redirect to submissions page
    return redirect('/submissions')


# Show all submissions
@app.route('/submissions')
def submissions_page():

    submissions = list(collection.find())

    return render_template(
        'submissions.html',
        submissions=submissions
    )


# Run Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)