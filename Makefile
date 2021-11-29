init:
	minikube delete
	minikube start
	minikube addons enable ingress
	kubectl create namespace samurenko
	skaffold dev

start:
	minikube start
	skaffold dev
