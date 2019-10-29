#run this file after installing kubernetes

kubectl delete deployment front-deployment
kubectl delete deployment back-deployment
kubectl delete service front-expose-service
kubectl delete service back-expose-service
