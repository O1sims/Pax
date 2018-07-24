# Pax

## Overview

Pax (*"peace"* in Latin) is a Python-based web application that provides a set of interfaces to facilitate joint users in planning and evaluating courses of action within a mission environment. As such, it allows users to oversee and prepare for missions that combine cyber and physical components. Courses of action are evaluated based on the time taken to achieve the mission, the probability of success, what the enemy is preparing to do and the risk inherent within the course of action.

**Research.** We use [game theory](https://en.wikipedia.org/wiki/Game_theory) as our main set of tools for evaluating the risk inherent within a course of action. Research was conducted in constructing the theory and algorithms around the Pax project. This research can be found in the [`NetworkDefence`](https://github.com/O1sims/NetworkDefence) repository. This article develops an attack-defence game within a topological structure.

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
docker-compose up
```
By default, the main Pax application is accessible on port `8200` and the MongoDB database is run on port `8210`. The `docker-compose.yml` can be altered to allow these services to run on different ports. Swagger API documentation can be found at `localhost:8200/swagger/`.

Five environmental variables are associated with the project:
```
environment:
  - DB_PORT=8210
  - UI_PORT=8200
  - DB_HOSTNAME=pax-db
  - UI_HOSTNAME=pax-ui
  - DB_NAME=PaxDB
```
These can be found and modified in the `docker-compose.yml` file.

## Contact

The best way to troubleshoot or ask for a new feature or enhancement is to create a Github [issue](https://github.com/O1sims/Pax/issues). However, if you have any further questions you can contact [me](mailto:sims.owen@gmail.com) directly.
