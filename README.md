# Welcome to the Plant Game Project.

This Program is going to be created as an Assessment for the Technical Project at the ISEN Yncrea University.
The App should give a notification to all users (once a day/week) to find a specific plant. 
The user tries to find it then and makes pictures of plants he thinks are the right one. 
If the picture is of the wrong one he is told to continue searching. 
If the user finds the requested plant, he/she can post it on Instagram and gets one level up.

In this Repo the Kubernetes setup is stored. To run the setup for development, the following commands do the job. We need kubectl and minikube installed for that.

First we have to have a running Kubernetes Cluster. We can use minikube for that (see [minikube start](https://minikube.sigs.k8s.io/docs/start/)):

```bash
start minikube
```

Then we type in the current workspace the following command:

```bash
kubectl apply -f deployment/plantgame-deployment-http-server.yml -f deployment/plantgame-deployment-rabbitmq.yml 
```

This runs the respective containers all at once. To check if the containers are running type:

```bash
kubectl get pods
```

This launches a test http server container running in the cluster for now. You can find the container here: [Docker](https://hub.docker.com/repository/docker/johanneshoelker/scratch/general)

Testing the http-server is possible with this command:

```bash
url -X POST http://plantgame-backend/guess -d '{"key": "value"}' -H "Content-Type: application/json"
```

This posts a message from outside the cluster to the http server. The hostname must resolve to the minikube ip adress. In Linux this is done by adding a line to /etc/hosts like this:

```   
192.168.49.2 plantgame-backend
```



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

In order to add your own containers, store the source code in this repo in a seperate folder and push them to docker hub. Afterwards add them in the deployment.yml.
