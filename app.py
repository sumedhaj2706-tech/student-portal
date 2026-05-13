from flask import Flask, render_template, request

app = Flask(__name__)

# Temporary storage (list)
submissions = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    usn = request.form['usn']
    title = request.form['title']
    link = request.form['link']

    # Store data
    submissions.append({
        "name": name,
        "usn": usn,
        "title": title,
        "link": link
    })

    return f"""
    <h3>Submitted Successfully!</h3>
    <a href="/">Go Back</a>
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)

print("Test for deployment")