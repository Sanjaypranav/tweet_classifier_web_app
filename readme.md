# Flask app to classify tweets

Before we jump in lets study over view of docker and how to use it to build a flask app.
## Docker and it's components 
Docker is a containerization technology that allows you to run applications on a virtual machine. In simple words if you are training a model on a training environment you want to deploy it to a production environment. You can use docker to do that. 
<!--image to explain -->
![alt text](https://www.pngfind.com/pngs/m/385-3851598_as-you-can-see-docker-client-and-docker.png)

### 1 Docker Client:
Docker client is a command line interface that allows you to interact with docker. It is a terminal application. Docker CLI is the gateway to interact with Docker on any system.

### 2 Docker Compose:
Docker compose is a tool that allows you to create a docker environment. It is a json file that contains all the configurations for your docker environment.
### 3 Docker Image:
Before Docker images, which essentially act as a blueprint for
Docker containers, it makes sense to cover Dockerfiles. A Dockerfile is the
initialization point of the Docker container lifecycle. We first need to have
a Dockerfile to build a Docker image and subsequently run a container
based on that image.

#### 4.1 Dockerfile:
Dockerfile is a text file that contains all the instructions to build a Docker image.
for example:
```Dockerfile
FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install -r requirements.txt
WORKDIR /app
COPY . .
RUN python3 app.py
```

### 5 Docker Container:
Docker container is a container that contains collections of docker images.

### 6 Docker Registry:
Docker registry is a service that allows you to store and manage Docker images.

[Docker Hub](https://hub.docker.com/) is for images what GitHub is
for code repositories. It’s a collection of public and private images. It
contains official images as well as customized public images for different applications. It’s a central repository for Docker images. It allows you to push and pull images to and from the registry.

### 7 Docker Server:
Docker server is a container that runs docker. Docker servers otherwise called as daemon.

### Some more about docker:
read [Docker Documentation](https://www.docker.com/) for  more information.

## To Run this  Project

from [makefile](https://www.makeuseof.com/tag/makefile-for-linux-ubuntu/)

```make
make install
```
or to just run app (if you have virtual environment already)
```make
make app
```
## Flask app

importing libraries and initialising  

```python
from flask import Flask, render_template, request
app = Flask(__name__)
```
routing function to render html template

```python
@app.route('/')
def index():
    return render_template('index.html')
```

you can also use `@app.route('/<name>')` to route to a specific page.

you can change hostname and port number in the `app.run()` function

```python
if __name__ == '__main__':
    app.run(debug=True, host='localhost',port=5500)
```