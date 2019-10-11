# Currency Converter - Inter-currency conversions

A Simple Flask Web Application to convert one currency into another according to the instantaneous rates.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need the following: 
- Python 3
- `virtualenv`


### Installing

- Set up a separate Virtual Environment for the repository.

    ```
    virtualenv env
    ```

- Activate the Virtual Environment

    ```
    source env/bin/activate
    ```
    on Linux or
    ```
    env\Scripts\activate
    ```
    on Windows

- Now navigate to the project folder and run

    ```
    pip install -r requirements.txt
    ```
- Make sure the Environment Varibale `FLASK_APP` is set to `application.py`. 
    In Linux, you can do this using:
    ```
    export FLASK_APP=application.py
    ```
    In Windows, you can do this from Advanced System Settings

-   now run the application using: 
    ```
    flask run
    ```
    or
    ```
    python -m flask run
    ```
    


## Deployment

Deployment needs to be done on a WSGI Server such as Gunicorn or Nginx

## Contributing

Contributions are Welcomed. You can fork/clone this repository and PR any suitable changes. Any small improvement would be highly appreciated.
