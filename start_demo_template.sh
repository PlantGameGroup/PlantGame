#!/usr/bin/env bash
echo "The Plant Game Demo is booting..."
rm -rf log
mkdir -p log

# Configuration for Backend
systemctl start docker
minikube start > log/minikube.txt 2> log/minikube_err.txt
kubectl apply -f PlantGame/deployment/plantgame-deployment-backend.yml > log/kubectl.txt 2> log/kubectl_err.txt
kubectl apply -f PlantGame/deployment/plantgame-deployment-game-board-service.yml > log/kubectl.txt 2> log/kubectl_err.txt
kubectl apply -f PlantGame/deployment/plantgame-deployment-http-server.yml > log/kubectl.txt 2> log/kubectl_err.txt
kubectl apply -f PlantGame/deployment/plantgame-deployment-rabbitmq.yml > log/kubectl.txt 2> log/kubectl_err.txt
kubectl apply -f PlantGame/deployment/postgres-deployment.yaml > log/kubectl.txt 2> log/kubectl_err.txt

# Configuration for Frontend
~/Android/Sdk/tools/emulator -avd pixel_xl -camera-back webcam0 > log/emulator.txt 2> log/emulator_err.txt &
echo "Pixel Emulator started!"
sleep 10
cd PlantGameFlutterFE
flutter run > ../log/flutter.txt 2> ../log/flutter_err.txt &
echo "Flutter App started.."
cd ..
