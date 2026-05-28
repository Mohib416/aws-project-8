# 🚀 AWS Project 8 – ECS Fargate CI/CD Infrastructure

## Project Overview

In this project, I built a production-style AWS cloud infrastructure using **Terraform, ECS Fargate, Docker, CI/CD, Route53, HTTPS, CloudWatch, and Auto Scaling**.

The goal of this project was not only to study AWS theory, but to gain real hands-on experience by building, troubleshooting, and understanding how cloud services work together in a real environment.

This project includes:

- Infrastructure as Code (Terraform)
- Docker containerized application
- ECS Fargate deployment
- Application Load Balancer (ALB)
- HTTPS / SSL with ACM
- Custom domain using Route53
- GitHub Actions CI/CD pipeline
- CloudWatch Logs & Monitoring
- ECS Auto Scaling
- Real troubleshooting and debugging

---

## 🏗️ Architecture Diagram

![Architecture Diagram](Diagram/Project%208%20Diagram.png)

---

## ☁️ AWS Services Used

This project includes the following AWS services:

- **Amazon ECS Fargate** → Serverless container hosting
- **Amazon ECR** → Container image registry
- **Application Load Balancer (ALB)** → Traffic distribution and HTTPS routing
- **Route53** → DNS and domain management
- **AWS Certificate Manager (ACM)** → SSL/HTTPS certificates
- **CloudWatch Logs & Metrics** → Monitoring and troubleshooting
- **Auto Scaling** → Dynamic container scaling
- **IAM Roles & Policies** → ECS permissions
- **VPC / Subnets / Security Groups** → Networking and security

---

## 🔄 Infrastructure Flow

The application request flow works like this:

```text
User Browser
↓
mohibcloud.com
↓
Amazon Route53 (DNS)
↓
HTTPS / SSL (ACM)
↓
Application Load Balancer (ALB)
↓
Target Group
↓
ECS Cluster
↓
ECS Fargate Service
↓
Docker Container
↓
Flask Web App
```

The ALB manages incoming traffic, HTTPS, and health checks before forwarding requests to healthy ECS tasks.

---

## 🐳 Docker & ECS Deployment

I created a Flask application and containerized it using Docker.

The process included:

- Creating a Dockerfile
- Building a Docker image locally
- Testing the application on localhost
- Pushing the image to Amazon ECR
- Updating ECS Task Definition to use the custom image

After deployment, the application was successfully accessible through the ALB DNS.

---

## ⚙️ CI/CD Pipeline (GitHub Actions)

I implemented a **CI/CD pipeline using GitHub Actions** to automate deployments.

Workflow:

```text
Code Change
↓
git push
↓
GitHub Actions
↓
Docker Build
↓
Push Image to Amazon ECR
↓
ECS Service Update
↓
New Container Deployment
```

This means every time I update the application and push code to GitHub, deployment happens automatically.

No manual Docker push or ECS restart is needed.

---

## 🔐 HTTPS & Custom Domain

I secured the application using:

- **AWS Certificate Manager (ACM)**
- **HTTPS Listener (443)**
- **HTTP → HTTPS Redirect**
- **Custom Domain**

Domain used:

- `mohibcloud.com`
- `www.mohibcloud.com`

Initially, I used **Namecheap DNS**, but later migrated DNS management to **AWS Route53** for better reliability and easier management.

---

## 📊 Monitoring & Logging

I configured **CloudWatch Logs and Metrics** for monitoring.

### CloudWatch Logs

Used for:

- Container logs
- Flask application logs
- HTTP requests
- Health checks
- Troubleshooting issues

Example:

```text
GET / HTTP/1.1 200
```

Meaning:

- `200` = Success
- `404` = Not Found
- `500` = Server Error

---

### CloudWatch Metrics

I monitored:

- CPU utilization
- Memory usage
- Network traffic
- ALB response time
- Request count
- Error metrics

This helped me understand if the infrastructure was healthy and performing correctly.

---

## 📈 Auto Scaling

I implemented ECS Auto Scaling based on CPU utilization.

Configuration:

- **Minimum Tasks:** 1
- **Maximum Tasks:** 3
- **CPU Target:** 70%

Scaling logic:

```text
Low Traffic
↓
1 Task

High CPU Usage
↓
2 Tasks
↓
3 Tasks

Traffic Low Again
↓
Scale Back Down
```

To test scaling, I created a `/stress` route that increases CPU usage and generated traffic to trigger automatic scaling.

---

## 🛠️ Real Troubleshooting Experience

This project gave me real troubleshooting experience.

Some issues I solved:

- ECS task deployment issues
- IAM role permission problems
- ALB listener configuration
- HTTPS certificate setup
- DNS propagation problems
- `DNS_PROBE_FINISHED_NXDOMAIN`
- Namecheap DNS limitations
- Route53 migration
- Terraform destroy/apply issues
- ECS monitoring setup

This helped me better understand how AWS services work together in real-world environments.

---

## 📷 Project Screenshots

### Architecture Diagram

![Architecture](screenshots/project8_aws_ecs_architecture_diagram.png)

### ECS Service Running

![ECS Service](screenshots/ecs_service_running.png)

### CI/CD Success

![CI/CD](screenshots/cicd_success.png)

### HTTPS Working Domain

![HTTPS](screenshots/https_working.png)

### CloudWatch Metrics

![CloudWatch](screenshots/cloudwatch_metrics.png)

### Auto Scaling

![Autoscaling](screenshots/autoscaling.png)

---

## 🎯 Lessons Learned

This project helped me understand the difference between learning AWS theory and building real cloud infrastructure.

I learned how multiple AWS services work together in a real environment, including networking, containers, CI/CD, HTTPS, monitoring, scaling, and troubleshooting.

One of the biggest lessons was understanding how to debug real problems and not just follow tutorials.

---

## 💡 Skills Gained

- AWS ECS Fargate
- Terraform
- Docker
- GitHub Actions CI/CD
- Route53
- Application Load Balancer (ALB)
- HTTPS / SSL / ACM
- CloudWatch Logs & Metrics
- ECS Auto Scaling
- Amazon ECR
- DNS Management
- Infrastructure as Code (IaC)
- Troubleshooting & Debugging

---

## 👨‍💻 Author

**Mohib Rizwan**  
AWS Certified Solutions Architect | Cloud | DevOps | Cybersecurity
