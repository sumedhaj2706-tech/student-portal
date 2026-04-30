🎓 Student Project Submission Portal (DevOps Project)

📌 Overview
This project is a Flask-based web application that allows students to submit their project details through a simple form.

It demonstrates a complete DevOps pipeline including:

- Application development
- Containerization using Docker
- Continuous Integration (CI)
- Continuous Deployment (CD)
- Cloud deployment on AWS EC2

---

🛠️ Tech Stack

- Backend: Flask (Python)
- Frontend: HTML, CSS
- Containerization: Docker
- CI/CD: GitHub Actions
- Cloud Platform: AWS EC2

---

🚀 Features

- Submit student details:
  - Name
  - USN
  - Project Title
  - GitHub Link
- Simple and clean UI
- Fully containerized application
- Automated deployment pipeline

---

📂 Project Structure

student-portal/ │ ├── app.py ├── requirements.txt ├── Dockerfile ├── .dockerignore ├── templates/ ├── static/ └── .github/workflows/ ├── python-ci.yml └── deploy.yml

---

⚙️ How to Run Locally

🔹 1. Clone the repository

bash git clone https://github.com/sumedhaj2706-tech/student-portal.git cd student-portal

🔹 2. Build Docker Image

bash docker build -t student-portal .

🔹 3. Run Container

bash docker run -p 5000:5000 student-portal

🔹 4. Open in Browser

http://localhost:5000

🔄 CI/CD Pipeline

🔹 Continuous Integration (CI)

On every push:

- Install Python
- Install dependencies
- Run checks/tests
- Build Docker image

---

🔹 Continuous Deployment (CD)

On every push:

- GitHub Actions connects to EC2 via SSH
- Pulls latest code
- Builds Docker image
- Runs container on port 5000

---

☁️ Live Deployment

Application is deployed on AWS EC2:

http://16.170.241.110:5000

---

🧪 Testing

Basic Flask test example:

python def test_home(): from app import app client = app.test_client() response = client.get('/') assert response.status_code == 200

---

👥 Team Contributions

- Member 1(Sumedha P): Flask Application Development
- Member 2(Trisha J): CI/CD Pipeline (GitHub Actions)
- Member 3(Tushitha B R): AWS EC2 Setup & Deployment

---

📊 DevOps Workflow

Code → GitHub → CI → Docker Build → CD → AWS EC2 → Live App

---

🎯 Conclusion

This project demonstrates how a simple application can be transformed into a production-ready system using DevOps practices like automation, containerization, and cloud deployment.

---

## 🙌 Acknowledgement

This project was developed as part of a DevOps learning initiative to understand real-world deployment pipeline
