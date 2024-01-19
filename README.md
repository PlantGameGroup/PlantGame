# Welcome to the Plant Game Project.

This Program is going to be created as an Assessment for the Technical Project at the ISEN Yncrea University.
The App gives the user a quest to find a list of plants inside a chosen park. 
The user tries to find it one by one and makes pictures of plants he thinks are the right one. 
If the picture is of the wrong one he is told to continue searching. 
If the user finds the requested plant, he/she can post it on Instagram and gets one level up.

In this Repo the Kubernetes setup is stored. To run the setup for development, the following commands do the job. We need kubectl and minikube installed for that. 

First we have to have a running Kubernetes Cluster. We can use minikube for that (see [minikube start](https://minikube.sigs.k8s.io/docs/start/)):

```bash
start minikube
```

Then to start all necessary containers we type in the current workspace :

```bash
kubectl apply -f deployment/plantgame-deployment-backend.yml
kubectl apply -f deployment/plantgame-deployment-game-board-service.yml
kubectl apply -f deployment/plantgame-deployment-http-server.yml 
kubectl apply -f deployment/plantgame-deployment-rabbitmq.yml 
kubectl apply -f deployment/postgres-deployment.yaml 
```

To check if all ods are running type:

```bash
kubectl get all
```

## HTTP Server with Flask

This launches a test http server container running in the cluster for now. You can find the container here: [HTTP-Server-Docker](https://hub.docker.com/repository/docker/johanneshoelker/http-server/) and the code for it in the container_http folder in this repo.

Testing the http-server is possible with Postman like this:

![](/home/jo/.var/app/com.github.marktext.marktext/config/marktext/images/2024-01-19-17-56-38-image.png)

You need the three headers:

- gameID

- imageURI (for example: https://www.plantura.garden/wp-content/uploads/2018/05/Orchidee-Bl%C3%BCte.jpg )

- guessedSpecies

This posts a message from outside the cluster to the http server. The hostname must resolve to the minikube ip adress. In Linux this is done by adding a line to /etc/hosts like this:

```
192.168.49.2 plantgame-backend
```

It's also possible to call the minikube ip directly on Port 5000.

## Message Queue with RabbitMQ

You can see the rabbitmq management interface by port forwarding the 

```bash
kubectl port-forward <pod_name> 5672:5672 15672:15672
```

And then open http://localhost:1567 Here you can see all queues and messages in the rabbitmq pipe.

The following command can be used for testing to post a message to the pipe:

```bash
curl -i -u guest:guest -H "content-type:application/json" -X POST \                         ✔  base  
-d'{"properties":{},"routing_key":"test","payload":"Hello, RabbitMQ!","payload_encoding":"string"}' \
http://localhost:15672/api/exchanges/%2f/amq.default/publish
```

## Backend with Ubuntu Container

Accessing the backend container by command line iis done like this:

```bash
kubectl exec -it <plantgame-backend-pod-name> -- /bin/bash 
```

Inside the container console you can start the functionalities with this:

```bash
python3 main.py
```

Using nano for testing the script is the easiest way for manipulation. The script is going to be started later automatically.

## Deployment

In order to add your own containers, store the source code in this repo in a seperate folder and push them to docker hub. Afterwards add a deployment file for them in the deployment folder.
