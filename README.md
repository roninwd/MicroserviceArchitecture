Otus course - [Microservice Architecture](https://otus.ru/learning/133124/)

### Разворачивание проекта на minicube
0. прописать ip поднятого кластера в /etc/hosts.(Посмотреть выданный ip можно командой minikube ip)
1. minikube addons enable ingress
2. kubectl create namespace samurenko
3. helm install db-chart ./db-chart/
4. kubectl apply -f initdb.yaml
5. kubectl apply -f app-config.yaml -f ingress.yaml -f service.yaml -f client.yaml -f swagger.yaml
