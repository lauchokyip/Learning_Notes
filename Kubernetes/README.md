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
* `kudeadm` is used to create a node and connect different node together
* `kubectl config` contains definitions for:
  * Clusters (a list of clusters that `kubectl` knows about)
  * Users (define different users that might have different levels of permissions on each cluster)
  * Contexts (bring together clusters and users under a friendly name. For example **Context** = deploy-prod, **User** = deploy, **Cluster** = prod)
* **Pod** is a special type of container called a **pause container**. It's a collection of system resources that containers running inside of it will inherit and share
* 1)**Port** exposes the Kubernetes service on the specified port within the cluster. Other pods within the cluster can communicate with this server on the specified port.
  2) **Target Port** is the port on which the service will send requests to, that your pod will be listening on. Your application in the container will need to be listening on this port also.
  3) **Node Port** exposes a service externally to the cluster by means of the target nodes IP address and the NodePort. NodePort is the default setting if the port field is not specified.
* Assume Pod in two different node, Node A and Node B. When Pod in Node A wants to communicate with Pod in Node B it will query the cluster DNS server (`/etc/resolv.conf`). Because there is no routes to Node B the packet will be sent to default gateway. When Node A receves the packet it won't have the routes either so it will be forward to default gateway. The Node's kernel will then create a trap and redirected the IP address of the Pod.
* Kubernetes uses cluster DNS as its service registry. It runs as a set of Pods with a Service object providing a stable network endpoint. The important components are:
  1) Pods: Managed by the `coredns` deployment
  2) Service: A ClusterIP Service called `kube-dns` listening on port 53 TCP/UDP
  3) EndPoint: The Endpoint is called kube-dns
* All storage on a Kubernetes cluster is called a **volume**
* **Persistent Volumes** are how we map external storage onto a cluster whereas **Persistent Volume Claims** are like tickets that authorize applications to use a **Persistent Volumes**.
* For **Persistent Volumes**, ***ReadWriteOnce*** can only be mounted as R/W by a single PVC. This is usually only supported by block storage. ***ReadWriteMany*** can only be mounted as R/W by a multiple PVC. This is usually only supported by file and object storage such as NFS. ***ReadOnlyMany*** allows multiple PVCs as R/O
* **Storage Classes** make it so that you don't have to create Persistent Volumes manually. You create **Storage Classes** object and use a plugin to tie it to a particular type of storage. It will watch the API server that refers to its name. If matching PVCs appear, it will dynamically create the required volume on back-end storage system as well as the PV on Kubernetes.
* You can inject **ConfigMap** into a container ***as environment variables***,***as arguments to container startup commands***,***as files in a volume***
* The different between **StatefulSet** and **Deployment** is that **StatefulSet** guarantees ***predictable and persistent Pod names***, ***perdictable and persistent DNS hostnames***, and ***predictable and persistent volume bindings***. These three properties form the **state** of a pod.
* **Deleting StatefulSets** does not terminate pods in order.
### References
[The Kubernetes Book](https://www.amazon.com/Kubernetes-Book-Version-November-2018-ebook/dp/B072TS9ZQZ/ref=sr_1_5?dchild=1&keywords=kubernetes&qid=1621828785&sr=8-5) </br>
[Kubernetes: Flannel network](https://blog.laputa.io/kubernetes-flannel-networking-6a1cb1f8ec7c) </br>
[Using Kubernetes Port, Target Port, Node Port](https://www.bmc.com/blogs/kubernetes-port-targetport-nodeport/) </br>

### Kubernetes API links
[Ivan's blog](https://iximiuz.com/en/posts/kubernetes-operator-pattern/) </br>
[Kubernetes-style APIs of the Future - Daniel Smith, Google (Any Skill Level)](https://www.youtube.com/watch?v=S2U8GNHewpk) </br>
[A Vision For API Machinery: Coming to Terms with the Platform We Built - Daniel Smith, Google](https://www.youtube.com/watch?v=u6weI_3WVTM) </br>
[The Kubernetes Control Plane for Busy People Who Like Pictures - Daniel Smith, Google](https://www.youtube.com/watch?v=zCXiXKMqnuE) </br>
