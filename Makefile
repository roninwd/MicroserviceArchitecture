init:
	minikube delete
	minikube start
	minikube addons enable ingress
	kubectl create namespace samurenko
	kubectl apply -f postgres.yaml
	skaffold dev

start:
	minikube start
	skaffold dev
