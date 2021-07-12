# todo-list
fully functioning python web app which can store task list in database, you can add and delete tasks. Flask is used to handle requests, jinja2 template is used for beautiful, interactive interface.
Topics covered in this project:
- python3 flask, jinja template, using template html
- mongodb, collections, find(), insertOne(),
- pymongo in python3 to connect to mongodb
- using environment variables in python3


# How to Run

### On Docker
To run the app -
  1. Install docker, docker-compose
  2. In the todo-list directory run : \
       &nbsp;&nbsp;  $ sudo docker-compose up
  3. Open your browser and open the url "0.0.0.0:9000"  or "localhost:9000"
  
### On Kubernetes
To run the app -
  1. Install kubernetes, make sure, kubectl is running
  2. In the todo-list directory run : \
       &nbsp;&nbsp;  $ ./k8s-deployment/one-click-deploy.sh
  3. Open your browser and open the url "\<ip-of-frontend-node\>:31900" \
  &nbsp; if you're using minikube, just run  \
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$ &nbsp;minikube service front-expose-service

To remove the app -
  1. In the todo-list directory run : \
       &nbsp;&nbsp;  $ &nbsp;./k8s-deployment/one-click-remove.sh
