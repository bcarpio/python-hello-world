############################################################
# Dockerfile to build Python WSGI Application Containers
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM ubuntu

# File Author / Maintainer
MAINTAINER Brian Carpio

# Update the sources list
RUN apt-get update

# Install basic applications

# Install Python and Basic Python Tools
RUN apt-get install -y python python-dev python-distribute curl
RUN curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
RUN python ./get-pip.py

ADD /hello_world/ /hello_world

# Get pip to download and install requirements:
RUN pip install -r /hello_world/requirements.txt

# Expose ports
EXPOSE 8080

# Set the default directory where CMD will execute
WORKDIR /hello_world

# Set the default command to execute
# when creating a new container
# i.e. using CherryPy to serve the application
CMD python server.py
