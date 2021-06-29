#run this file after installing kubernetes

kubectl create -f namespace.yaml
kubectl create -f frontend-deployment.yaml
kubectl create -f backend-deployment.yaml
kubectl create -f frontend-expose-service.yaml
kubectl create -f backend-expose-service.yaml
