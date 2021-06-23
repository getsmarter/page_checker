# Page Checker - Basic web page checking using Selenium

[![Python](https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white)](https://python.org)
[![GitHub tag](https://img.shields.io/github/tag/pjdvmalan/page_checker?include_prereleases=&sort=semver)](https://github.com/pjdvmalan/page_checker/releases/)
[![License - MIT](https://img.shields.io/badge/License-MIT-blue)](#license)

## Raison d'être

We require a tool that can automate post production deployment checks.

## Usage

### Clone the repository

```sh
git clone git@github.com:getsmarter/page_checker.git
cd page_checker
```

### Configure

Create a local configuration file:

```sh
cp etc/config_local_template.py etc/config_local.py
```

Set parameters in the new, un-versioned, file. In most cases, you will only need
to define the following variables to config_local.py:

* PC_USERNAME
* PC_PASSWORD

### Run using Docker

Run docker compose up or down to run/stop the container. I.e. to start container:

```sh
docker-compose up
```

## Manual Installation

### Install system dependencies

Install Firefox - see the [download](https://www.mozilla.org/en-US/firefox/new/) page.

Install Firefox's webdriver:

```sh
# macOS
brew install geckodriver

# Debian/Ubuntu
sudo apt-get update
sudo apt-get install firefox-geckodriver
```

Install Python 3:

```sh
# macOS
brew install python@3

# Debian/Ubuntu
sudo apt-get update
sudo apt-get install python3
```

### Install project packages

Create a virtual environment in the repo. Activate it whenever install packages into it or running this project.

```sh
python3 -m venv venv
source venv/bin/activate
```

Install production dependencies:

```sh
pip install -r requirements.txt
```

Or, install prod and dev dependencies at once:

```sh
pip install -r requirements-dev.txt
```

### Configure Manual Installation

Create a local configuration file:

```sh
cp etc/config_local_template.py etc/config_local.py
```

Set parameters in the new, un-versioned, file. In most cases, you will only need
to define the following variables to config_local.py:

* PC_USERNAME
* PC_PASSWORD

Run commands inside the virtual environment.

The project entrypoint is [page_checker.py](/page_checker.py).

### Contributing

Run `pylint` before submitting a PR.
