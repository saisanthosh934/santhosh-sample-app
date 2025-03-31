                                                                        How to Use This Application
Clone this repository

Build the Docker image: docker build -t python-app .

Run the container: docker run -p 5000:5000 python-app

Access the application at http://localhost:5000

Metrics are available at http://localhost:5000/metrics

For Kubernetes deployment:

Apply the manifests: kubectl apply -f kubernetes/

The application will be available through the LoadBalancer service

Prometheus will automatically scrape metrics if properly configured

This application provides:

A clear frontend displaying your assignment information

Built-in Prometheus metrics endpoint

Health check endpoint

Proper logging

Kubernetes-ready deployment

Jenkins pipeline for CI/CD

Monitoring integration via ServiceMonitor


                                                                            Important Notes for Implementation:
AWS ALB Ingress Controller:

You need to have the AWS ALB Ingress Controller installed in your cluster

Replace your-acm-certificate-arn with your actual ACM certificate ARN for HTTPS

Storage Configuration:

The StorageClass uses AWS EBS (gp2)

Adjust the storage parameters based on your cloud provider if not using AWS

HPA Configuration:

The HPA is configured to scale based on CPU (50%) and memory (70%) utilization

Adjust these values based on your application's requirements

Persistent Storage:

The application now tracks visit counts in a file on persistent storage

Each pod will have its own PVC (ReadWriteOnce)

Prerequisites:

AWS EBS CSI driver installed for dynamic provisioning

Proper IAM permissions for the ALB Ingress Controller

Metrics server installed in your cluster for HPA to work

This enhanced setup provides:

Automatic scaling based on resource usage

Persistent storage for your application data

Highly available application with multiple replicas

Secure HTTPS access via ALB

Monitoring of both application and infrastructure metrics