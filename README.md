# VDT-HW8-DevSecOps-CI-CD

## Description 
Welcome to my repository for the implementation of a web application developed as part of the HW8 assignment for the DevSecOps/CI-CD course at Viettel Digital Talent. This web application is intentionally designed to include two web vulnerabilities from the OWASP Top 10 list. 

## Usage
To build and run the web application, follow these steps:

- Clone the repository:
```
git clone https://github.com/Thanh-WuTan/VDT-HW8-VulnWebApp.git
```

- Navigate to the project directory:
```
cd VDT-HW8-VulnWebApp
```

- Build the Docker image:
```
docker build -t vulnwebapp .
```

- Start the application using Docker Compose:
```
docker-compose up --build -d
```

Access the web application at localhost:5000 in your web browser.


