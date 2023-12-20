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

Then we run in the current workspace:

```bash
kubectl apply -f deployment-backend.yml
```

And check if the container is running:

```bash
kubectl get pods
```

This launches a test container running in the cluster for now. You can find the container here: [Docker](https://hub.docker.com/repository/docker/johanneshoelker/scratch/general)

In order to add your own containers, store the source code in this repo in a seperate folder and push them to docker hub. Afterwards add them in the deployment.yml.