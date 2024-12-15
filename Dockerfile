# Step 1 - Use Python version 3.13.1 on Alpine Linux
FROM python:3.13.1-alpine

# Step 2 - Initialize project
LABEL maintainer="Created by @weegex"
WORKDIR /appdir
ENTRYPOINT [ "python", "app" ]

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY .env .

# Step 3 - Install python libraries
COPY requirements.txt .
RUN pip install -r requirements.txt

# Step 4 - Copy all files and directories
COPY . .
