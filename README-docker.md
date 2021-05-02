
# Page Checker - Basic web page checking using Selenium using docker compose

[![Python](https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white)](https://python.org)
[![GitHub tag](https://img.shields.io/github/tag/pjdvmalan/page_checker?include_prereleases=&sort=semver)](https://github.com/pjdvmalan/page_checker/releases/)
[![License - MIT](https://img.shields.io/badge/License-MIT-blue)](#license)

## Installation

### Clone the repository

```sh
git clone git@github.com:pjdvmalan/page_checker.git
cd page_checker
```

### Configure

- Create local config.

    ```sh
    cp etc/config_local_template.py etc/config_local.py
    ```

- Set parameters in the new, un-versioned, file.

### Usage

- Run docker compose up or down to run/stop the container. I.e. to start container:
    ```sh
    docker-compose up
    ```

The project entrypoint is [page_checker.py](/page_checker.py).
