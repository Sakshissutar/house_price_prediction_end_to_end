# House Price Prediction - End-to-End ML Project with CI/CD

## This project is an end-to-end machine learning application that predicts house prices based on various features. The project demonstrates the complete ML lifecycle including data processing, model training, deployment, and CI/CD automation using Docker and AWS EC2.

### deployment
- Dockerized application
- Deployed on AWS EC2
- Exposed via port 8501

### used technologies
- Python
- Streamlit
- Scikit-learn
- Docker
- GitHub Actions (CI/CD)
- AWS EC2
  
## CI/CD Pipeline

The project uses GitHub Actions for continuous integration and deployment:

1. Code pushed to GitHub
2. Docker image is built
3. Image pushed to Docker Hub
4. EC2 instance pulls latest image
5. Container restarts automatically

### the app is live:
[http://13.51.150.222:8501/](http://13.49.238.196:8501/)
 
### the app is live on streamlit:
https://housepricepredictionendtoend-xqp6dppcevpqpsooueknml.streamlit.app/
