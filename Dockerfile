FROM python:3.7-slim


# Set the working directory in the container
WORKDIR / firstapp

RUN pip install --PycharmProjects\Practice-Django\firstapp -r requirements.txt