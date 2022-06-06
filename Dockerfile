## The image you are going to inherit your Dockerfile from
#FROM python:latest
## Necessary, so Docker doesn't buffer the output and that you can see the output
## of your application (e.g., Django logs) in real-time.
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
## Make a directory in your Docker image, which you can use to store your source code
## RUN mkdir /django_recipe_api
## Set the /app/backend directory as the working directory
#RUN mkdir /taskmanager
#WORKDIR /taskmanager
#
## Copy the requirements.txt file adjacent to the Dockerfile to your Docker image
#COPY ./requirements.txt /app/taskmanager/requirements.txt
#
#RUN pip3 install --upgrade pip
#RUN pip3 install mysqlclient
#RUN pip3 install -r /app/taskmanager/requirements.txt
## Copies from your local machine's current directory to the /app/backend folder in the Docker image
#COPY ./entrypoint.sh /entrypoint.sh
#
#COPY . .
#
#RUN ["chmod", "+x", "/entrypoint.sh"]
## RUN ["chmod", "+x", "./manage.py"]
#ENTRYPOINT ["/entrypoint.sh"]


# The image you are going to inherit your Dockerfile from
FROM python:latest
# Necessary, so Docker doesn't buffer the output and that you can see the output
# of your application (e.g., Django logs) in real-time.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Make a directory in your Docker image, which you can use to store your source code
# RUN mkdir /django_recipe_api
# Set the /app/backend directory as the working directory
RUN mkdir /taskmanager
WORKDIR /taskmanager

# Copy the requirements.txt file adjacent to the Dockerfile to your Docker image
COPY ./requirements.txt /taskmanager/

RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /taskmanager/
# Copies from your local machine's current directory to the /app/backend folder in the Docker image
ADD . /lab_3-4/
