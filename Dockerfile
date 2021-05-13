# set base image (host OS)
FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt

# Update package manager and add FF repo
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y software-properties-common

# Install Firefox
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A6DCF7707EBC211F
RUN apt-add-repository "deb http://ppa.launchpad.net/ubuntu-mozilla-security/ppa/ubuntu bionic main"
RUN apt-get update -y
RUN apt-get install firefox -y

# Install requirements
RUN pip3 install -r requirements.txt

# Install geckodriver driver
RUN wget "https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz"
RUN tar -xvzf geckodriver* --directory /usr/local/bin
RUN chmod +x /usr/local/bin/geckodriver

RUN type geckodriver
RUN type python3
RUN type firefox

COPY . .

# command to run on container start
CMD [ "python", "./page_checker.py" ]
