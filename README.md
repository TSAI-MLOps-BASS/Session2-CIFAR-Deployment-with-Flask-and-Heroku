# TSAI EMLO - Session 2

## Learning Objective ##
This week we learned about REST APIs and Flask framework for application building. We also explored HTML, CSS and Bootstrap to create a simple application that we deployed on Heroku. We trained a Resnet18 based model in Pytorch on CIFAR10 dataset and used that in the application to classify newly uploaded images.

### API ###
API stands for application Programming Interface. It is a set of definitions and protocols that let multiple applications or devices communicate with each other. APIs make the applications loosely coupled and flexible. It makes the design simple and easy to maintain, and paves the way for more innovation.

### REST API ###
There are some architectural principles and protocols to establish API communication such as REST (Representational State Transfer), SOAP (Simple Object Access Protocol), GraphQL etc. REST is simple, lightweight with smaller learning curve that made it the most popular web service protocol.

#### Structure of RESTful API URL ####
Under **REST** principles a URL identifies a resource that returns data when it is called. The data is sent in one of the formats such as JSON, HTML, Python, XML, Text with JSON being the more popular one. The structure of a URL follows the following principles.  
  
**Endpoint**  
It is the URL that we invoke to send and receive the data. It is basically the concatenation of root endpoint, path and query parameters. E.g.  
https://api.github.com/users/theschoolofai/repos?sort=pushed
  
**Method**
Method denotes the type of action the URL is supposed to take such as GET, POST, PUT, PATCH and DELETE. PUT makes the request replace a specific data entity such as a person's email ID whereas PATCH allows to change a part of the email ID.  
  
**Header**
Header in an API provides information to both Client and Server. It carries additional data required for the successful execution of request such authentication, output type, SSL certification enabling etc.
  
**Body**
It is the payload that we send as input while making API call.

### Flask ###
Flask is an easy to use web framework written in Python. It provides a set of modules and libraries that enables web development seamlessly. 

### Quick Tutorial ###
(To be added here)

## Project ##
This week's project is to train a Resnet18 Pytorch model trained on CIFAR10 dataset, build a Flask application to serve incoming image classification request and deploy it on Heroku.  
**Stet up**  
* Create a project directory and clone the repository
* Create a virtual environment and run dependencies ```pip install -r requirements_env.txt```
* Run CIFAR10_Resnet18_Pytorch.ipynb notebook on COLAB to train and save the model
* Follow the steps in the link https://www.python-engineer.com/posts/pytorch-model-deployment-with-flask/ for environment set up and detailed understanding
* In the app path on the terminal execute ```flask run``` to start the application and followed by ```python test.py``` in another terminal to test the application locally
* Follow the steps from the above mentioned tutorial to deploy the application on heroku and test the URL endpoint generated
  

**Hosted Application**  
https://cifar10-resnet18-pytorch.herokuapp.com/
  
## Future Work ##
At present, the uploaded image is not rendering on the website hosted on heroku although the application is working fine on local machine. The next effort will be fix the issue and publish an enriched UI.