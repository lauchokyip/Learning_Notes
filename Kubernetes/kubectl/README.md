# Kubernetes Notes 
* Kubernetes as an orchestrator. **Orchestrator is just an fancy work for a system that takes care of deploying and managing applications** 
* Similar to OS which creates an abstraction between CPU, memory, storage and networking, Kubernetes creates an abstraction between cloud and center resources. 
* Simple steps to run applications on Kubernetes cluster </br>
  1) Write application as small independent microservices
  2) Package them in a container
  3) Wrap each container in a Pod
  4) Deploy Pods to the cluster via controllers such as **Deployments, DaemonSets, StatefulSets and Cronjobs**
* ***Deployments*** offer scalability and rolling updates, ***DaemonSets*** run one instance of a service on every nod ein the cluster, ***StatefulSets*** are for 
stateful applicatoin components, ***CronJobs*** are for short-lived tasks that need t orun at set times
* Kubernetes **cluster** is made of ***control plane/master*** and ***nodes***.
* Basic Kubernetes Componenents:
  1) Master
  * API server (All communication between every components must go through API server)
  * Storage (usually persistent storage (etcd) is used, consistency over availability)
  * The controller manager (implements all of the background control loops that monitor the cluster and respond to events. It's ***controller of controllers***. It constantly watching the API Server for changes. It first Obtain the desired state, Observe the current state, Determine differences and Reconcile differences)
  * The scheduler
  * The cloud controller manager
  2) Nodes
  * Kubelet
  * Container runtime
  * Kube-proxu
