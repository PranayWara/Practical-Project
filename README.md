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
Test script can be found [here.](https://github.com/PranayWara/Practical-Project/blob/main/scripts/test.sh)

#### Build
This will login to docker, then build the images from the test passed app and lastly push the images up to my dockerhub account.
Build script can be found [here.](https://github.com/PranayWara/Practical-Project/blob/main/scripts/build.sh)


#### Ansible
This will configure Nginx on the load-balancer so it can talk to the swarm. On the swarm, it will install docker and if it's a manager it will initialize the swarm and the worker will be added to it.

#### Configure 
This will install any requirements onto the swarm and make sure all is up to date.
Configure script can be found [here.](https://github.com/PranayWara/Practical-Project/blob/main/scripts/configure.sh)

#### Deploy
This will copy the docker-compose.yaml file to the manager and then stack deploy the swarm to fully deploy the application.
Deploy script can be found [here.](https://github.com/PranayWara/Practical-Project/blob/main/scripts/deploy.sh)


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
![Nginx Diagram](https://raw.githubusercontent.com/PranayWara/Practical-Project/main/Images/nginx2.jpg)

## Services
### Service Diagram 
![Service Diagram](https://raw.githubusercontent.com/PranayWara/Practical-Project/main/Images/service_diagram.jpg)
Below is how my application would commincate with the backend services.
### Service 1
#### Front-End 
This is what the user sees when they go onto the page. They will see the rarity, gun and price diplayed clearly.
### Service 2
#### Generate Rarity
Randomly picks a rarity from the list in a text file within the service.
### Service 3
#### Generate Gun
Randomly picks a gun from the list in a text file within the service.
### Service 4
#### Price
Using a post request, the gun and rarity is inputted and service 4 will find the price of both and add them together.
## Testing
Testing the app was dne through the pipeline. Service 1 was tested by requests_mock to mock the service 2 and 3 output. From that service 4 is outputted using the mock input. Using this test it allows me to test the app as if its live meaning it can be implamented into the pipeline. 
### Service 1
![Service 1 - app.py](https://raw.githubusercontent.com/PranayWara/Practical-Project/main/Images/unit_1_app.jpg)

![Service 1 - application](https://raw.githubusercontent.com/PranayWara/Practical-Project/main/Images/unit_1_application.jpg)

### Service 2
![Service 2 - application](https://raw.githubusercontent.com/PranayWara/Practical-Project/main/Images/unit_2_app.jpg)

### Service 3
![Service 3 - application](https://raw.githubusercontent.com/PranayWara/Practical-Project/main/Images/unit_3_app.jpg)

### Service 4
![Service 4 - application](https://raw.githubusercontent.com/PranayWara/Practical-Project/main/Images/unit_4_app.jpg)

As its clear the coverage of the entire tests came to 100%.

For extra clarity I installed Junit and Cobertura plugin on Jenkins which gave me a helpful graph to show the progress.

![Junit](https://raw.githubusercontent.com/PranayWara/Practical-Project/main/Images/JUNIT.jpg)

![Cobertura](https://raw.githubusercontent.com/PranayWara/Practical-Project/main/Images/cobertura%20report.jpg)

These reports where added in the test scripts.

## Front End
![Frontend 1](https://raw.githubusercontent.com/PranayWara/Practical-Project/main/Images/frontend-1.jpg)

Above is how the front end (service 1) looks, it will generate the roll and then show the user the previous rolls.

![Frontend 2](https://raw.githubusercontent.com/PranayWara/Practical-Project/main/Images/frontend-2.jpg)

This screenshot is to show after 1 refresh of the page the roll is stored in the 'Last few rolls'

## Jenkins Deploy
Using the deploy script below I am able to deploy the application through Jenkins which means I am able to do rolling updates.

## Improvement
* The configure process could've been quicker in jenkins as it had to go through all the installation which took much longer then everything else.
* Implemented intergration testing using selenium.
* More intricate testing plan

### Author
#### Pranay Wara 

### Acknowledgements
* Ruan Wright
* Oliver Nichols