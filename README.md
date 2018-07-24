# Pax

## Overview

Pax (_"peace" in Latin_) is a Python-based web application that provides an interface that allows joint users to plan and evaluate courses of action within a mission. As such, it allows users to prepare for missions that combine cyber and physical components.

## Technology stack

The Python web application uses [Django](https://www.djangoproject.com/) as the backend framework and [Angular](https://angular.io/) as the frontend framework. Documentation of the RESTful API service is handled by [Swagger](https://swagger.io/). Development is done within a [Docker](https://www.docker.com/) environment. We use [MongoDB](https://www.mongodb.com/) as the main database and [MongoDB Compass](https://www.mongodb.com/products/compass) as the database GUI.

## Building the application

We use Docker in the development of Pax to make it easy to build, run and share. The application is built across two Docker containers. Assuming a Linux terminal, execute the following command from the root directory of the Pax application:
```
docker build -t pax:latest .
```
This should kick off the composition of the Docker containers and the installation of the relevant Python and Node packages. To manually install Node packages please ensure you have Node (NPM) and install the essential frontend packages by executing the following commands:
```
cd gui/app
npm install
```
The Typescript (`.ts`) files can be compiled, as normal, with the `tsc` command.

## Running the application

Running the application is different from building the application. The application is run with the following command:
```
docker-compose run --service-ports pax
```
By default, the main Pax application is accessible on port `8200` and the MongoDB database is run on port `8210`. The `docker-compose.yml` can be altered to allow these services to run on different ports. Swagger API documentation can be found at `localhost:8200/swagger/`.

Six environmental variables are assiociated with the project, these can be modified in the `docker-compose.yml` file:
```
environment:
  - RISK_DB_PORT=8210
  - RISK_UI_PORT=8200
  - RISK_DB_HOSTNAME=pax-db
  - RISK_UI_HOSTNAME=pax-ui
  - RISK_DB_NAME=PaxDB
```

## Contact

The best way to troubleshoot or ask for a new feature or enhancement is to create a Github [issue](https://github.com/O1sims/Pax/issues). However, if you have any further questions you can contact [me](mailto:sims.owen@gmail.com) directly.
