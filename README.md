# CI/CD Pipeline to AWS EKS

This project demonstrates a complete automated Continuous Integration and Continuous Deployment (CI/CD) pipeline for a Python application. The pipeline is triggered by a Git push and handles the entire process from code commit to deployment on a Kubernetes cluster.

## Features

- **Automated Workflow:** A single Git push triggers the entire pipeline.
- **Dockerization:** The Python application is packaged into a Docker container.
- **Container Registry:** The Docker image is stored in Amazon Elastic Container Registry (ECR).
- **Orchestration:** The application is deployed and managed by Amazon Elastic Kubernetes Service (EKS).
- **Publicly Accessible:** The application is exposed to the internet via a Kubernetes Load Balancer Service.

## Technologies Used

* **GitHub Actions:** The CI/CD automation tool.
* **Git:** For version control.
* **Python (Flask):** The web application framework.
* **Docker:** For containerization.
* **Amazon Web Services (AWS):**
    * **EKS:** Elastic Kubernetes Service.
    * **ECR:** Elastic Container Registry.
* **Kubernetes:** For container orchestration.
* **kubectl:** Kubernetes command-line tool.
* **eksctl:** A command-line tool for creating and managing EKS clusters.

## CI/CD Pipeline Workflow

The pipeline is defined in `.github/workflows/ci-cd.yml`. When a developer pushes code to the `master` branch, the following steps are executed:

1.  **Checkout Code:** The workflow checks out the latest code from the repository.
2.  **AWS Authentication:** Authenticates with AWS using secrets stored in GitHub.
3.  **Docker Build & Push:** Builds the Docker image from the `Dockerfile` and pushes it to ECR.
4.  **Kubernetes Deployment:** Updates the Kubernetes deployment to use the new image and deploys it to the EKS cluster.
5.  **Service Exposure:** Ensures the application is publicly accessible via the LoadBalancer service.



## How to Run the Project (Local Testing)

If you wanted to test this project locally, you would:

1.  Clone this repository.
2.  Build the Docker image: `docker build -t my-devops-app .`
3.  Run the container: `docker run -p 5000:5000 my-devops-app`
