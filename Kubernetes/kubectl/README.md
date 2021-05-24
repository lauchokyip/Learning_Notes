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
  1) Master (the brain of Kubernetes)
  * API server (All communication between every components must go through API server)
  * Storage (usually persistent storage (etcd) is used, consistency over availability)
  * The controller manager (implements all of the background control loops that monitor the cluster and respond to events. It's ***controller of controllers***. It constantly watching the API Server for changes. It first Obtain the desired state, Observe the current state, Determine differences and Reconcile differences)
  * The scheduler (watches the API server for new work tasks and assigns them to appropriate healthy nodes)
  * The cloud controller manager (manage integrations with underlying cloud technologies and services such as, instances, load-balancers, and storage)
  2) Nodes (workers of Kubernetes cluster, it watches API server for new work assignments, execute new work assignments and report back to the control plane)
  * Kubelet (It will be installed in every node. It will then responsible for resgitering the node with the cluster. It will also watch the API server for new work assignments. )
  * Container runtime
  * Kube-proxy (responsible for local cluster networking. For example, it makes sure each node gets its own unique IP address, and implements local IPTABLES or IPVS rules to handle routing and load-balancing of traffic on the Pod network.)



### References
[The Kubernetes Book](https://www.amazon.com/Kubernetes-Book-Version-November-2018-ebook/dp/B072TS9ZQZ/ref=sr_1_5?dchild=1&keywords=kubernetes&qid=1621828785&sr=8-5)
