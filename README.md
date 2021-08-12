# Practical-Project
## Ojective
To create a service-orientated architecture for your application, this application must be composed of at least 4 services that work together.

The following constraints were also set:

* Kanban Board: Jira
* Version Control: Git - using the feature-branch model
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Reverse Proxy: NGINX
* Database Layer: MySQL

## Idea - Gun Skin Opener
The app will output the skin rarity and the gun. From these two random inputs a price will be outputted. Service 1 or my front end will display these outputs and the last five rolls.
## Service 1
### Front End
* Show current roll
* Show last 5 rolls
## Service 2 
### Skin Rarity
Gnerate a random rarity from a text file in the service
## Service 3 
### Guns
Gnerate a random gun from a text file in the service
### Price
* Blue = £1
* Purple = £2
* Pink = £5
* Red = £20
* AK-47 = £5
* M4A4 = £3
* AWP = £4
* Glock-18 = £1
* USP-S = £2
## Service 4
* Skin Rarity Price + Gun Price

# Planning 

## User Stories
![User Stories](https://raw.githubusercontent.com/PranayWara/Practical-Project/main/Images/user%20stories.jpg)

Above is my kanban user stories which gave me a visual and easy way to set out my user requirements

## Project Requirements
![Project Requirements](https://raw.githubusercontent.com/PranayWara/Practical-Project/main/Images/project%20requiements.jpg)

From all the objective I put them in a seperate epic in Jira

## Database Design
![ERD](https://raw.githubusercontent.com/PranayWara/Practical-Project/main/Images/ERD.jpg)

The design for my stand alone database which inclued the previous rolls of rarity, gun and price

## Risk Assessment 
### Initial Risk Assessment
![Risk Assessment](https://raw.githubusercontent.com/PranayWara/Practical-Project/main/Images/risk_assessment_2.jpg)
05/08/2021

### Updated Risk Assessment
![Updated Risk Assessment](https://raw.githubusercontent.com/PranayWara/Practical-Project/main/Images/risk_assessment_3.jpg)
12/08/2021

Above is my details risk assessment which will outline the impacts and the level of risk.

## Test Plans
![Test Plan](https://raw.githubusercontent.com/PranayWara/Practical-Project/main/Images/test%20case.jpg)

These are the tests which will show the app is fully functioning and the design of the app is test driven.
# Continous Deployment and Intergration

## Jenkins Pipline
![Jenkins Pipline](https://raw.githubusercontent.com/PranayWara/Practical-Project/main/Images/jenkins%20pipeline.jpg)

Above is my jenkins pipeline which was used for this project. 

### The 5 stages are:

#### Test
Testing the app using the test plan above, when all have passed it will move to the next stage.

#### Build
This will login to docker, then build the images from the test passed app and lastly push the images up to my dockerhub account

#### Ansible
This will configure Nginx on the load-balancer so it can talk to the swarm. On the swarm, it will install docker and if it's a manager it will initialize the swarm and the worker will be added to it.

#### Configure 
This will install any requirements onto the swarm and make sure all is up to date.

#### Deploy
This will copy the docker-compose.yaml file to the manager and then stack deploy the swarm to fully deploy the application.

### CICD Pipeline Diagram
The diagram below shows the full the pipeline of the project.
![CICD Pipeline](https://raw.githubusercontent.com/PranayWara/Practical-Project/main/Images/CICD%20.jpg)

# Components in Detail

### Docker
Docker is a software platform for building applications based on containers and lightweight execution environments that make shared use of the operating system kernel but otherwise run in isolation from one another.

### Docker-Compose
Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application's services. Then, with a single command, you create and start all the services from your configuration.

### Docker-Swarm
Swarm is a container orchestration tool built into Docker that allows us to run a network of containers across multiple host machines, also known as nodes.

### Ansible 
Ansible is an open-source software provisioning, configuration management, and application-deployment tool.

### Nginx
Nginx is a web server which can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache.
#### Nginx Diagram
I will be using nginx as a load balancer which will tend the user onto a node which has the least load.
![Nginx Diagram](https://raw.githubusercontent.com/PranayWara/Practical-Project/main/Images/nginx.jpg)

## Services

### Service 1

### Service 2

### Service 3

### Service 4

## Testing

## Front End

## Jenkins Deploy

## Improvement
