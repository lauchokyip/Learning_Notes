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
  * The scheduler (watches the API server for new work tasks and assigns them to appropriate healthy nodes. The scheduler isn't responsible for running tasks, just picking the nodes a task will run on)
  * The controller manager (implements all of the background control loops that monitor the cluster and respond to events. It's ***controller of controllers***. It constantly watching the API Server for changes. It first Obtain the desired state, Observe the current state, Determine differences and Reconcile differences)
  * The cloud controller manager (manage integrations with underlying cloud technologies and services such as, instances, load-balancers, and storage)
  2) Nodes (workers of Kubernetes cluster, it watches API server for new work assignments, execute new work assignments and report back to the control plane)
  * Kubelet (It will be installed in every node. It will then responsible for resgitering the node with the cluster. It will also watch the API server for new work assignments. )
  * Container runtime
  * Kube-proxy (responsible for local cluster networking. For example, it makes sure each node gets its own unique IP address, and implements local IPTABLES or IPVS rules to handle routing and load-balancing of traffic on the Pod network.)
* every Kubernetes cluster has an internal **DNS service**. The DNS service has a static IP address that is hard-coded into every Pod on the cluster, meaning all containers and Pods know ohw to find it.
* Every new service is automatically reigstered with the cluster's DNS so that all components in the cluster can find every Service by name.
* A **Pod** is a sandbox for hosting containers. Containers in a pod share the same ***namespace, memory, volumes, network stack and more***. That also means containers in the same Pod will share the same IP address.
* Every time a **Pod** is restarted , it will be assigned with new ID and IP address.
* **Deployments** is a higher level controller that has features such as ***scaling, zero-downtime updates m and versioned rollbacks***. Behind the scene, it implements a controller and a watch loop that is contanstly observing the cluster making sure that current state matches desired state.
* **Service** provides reliable networking for a set of Pods. It has stable DNS name, IP address, and port. It's a stable network abstraction point thta provdies TCP and UDP load-balancing across a dynamic set of Pods.
* **Service** uses label selector to know which set of Pods to load-balance traffic to. 

### References
[The Kubernetes Book](https://www.amazon.com/Kubernetes-Book-Version-November-2018-ebook/dp/B072TS9ZQZ/ref=sr_1_5?dchild=1&keywords=kubernetes&qid=1621828785&sr=8-5)
