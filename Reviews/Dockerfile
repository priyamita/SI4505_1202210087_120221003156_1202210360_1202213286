# base image
FROM python:3.9-slim

# set working dir
WORKDIR /app

# copy all files
COPY . /app

# install dependencies
RUN pip install -r requirements.txt


# expose port
EXPOSE 5003

# run app
CMD ["python", "reviews.py"]