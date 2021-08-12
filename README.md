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

## Components in Detail

### Docker

### Docker-Compose

### Docker-Swarm

### Ansible 

### Nginx

## Services

### Service 1

### Service 2

### Service 3

### Service 4

## Testing

## Front End

## Jenkins Deploy

## Improvement
