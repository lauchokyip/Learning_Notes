# Kubectl to API server note
![API lifecycle](APIlifecycle.png)
### Day 1
Learning what [Kubernetes services](https://kubernetes.io/docs/concepts/services-networking/service/#motivation) is </br>
This [video](https://www.youtube.com/watch?v=T4Z7visMM4E) from Nana is pretty useful. </br>
So `kubectl get service` will make API call to the API server to get some information about the service. I am guessing
we want to find where all the request will end up from [Services Types](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types) Changes need to be done from **[Printer codes](https://github.com/kubernetes/cli-runtime/tree/master/pkg/printers)** and the **server side** where it will calculate the all the [Endpoint](https://kubernetes.io/docs/concepts/services-networking/service/#services-without-selectors) object. 
</br>
</br>
Question:
* Does each Services has Endpoint Object? 

### Day 2
Watching  [Google Open Source Live presents Kubernetes (R) | Full Event](https://www.youtube.com/watch?v=60fnBk14ifc) <br>
Notes: <br>
kubectl makes HTTP POST request to kube-api-server and kube-api-server returns with HTTP response. Let's dive deep into it.
* kubectl will use [Factory abstraction](https://github.com/kubernetes/kubernetes/blob/7cea81ce34c4aa7d0e952d7f9957db254e3fbc83/staging/src/k8s.io/kubectl/pkg/cmd/util/factory.go#L40) to execute kubectl
* Inside [Factory](https://github.com/kubernetes/kubernetes/blob/7cea81ce34c4aa7d0e952d7f9957db254e3fbc83/staging/src/k8s.io/kubectl/pkg/cmd/util/factory.go#L40) we will have a [builder](https://github.com/kubernetes/kubernetes/blob/7cea81ce34c4aa7d0e952d7f9957db254e3fbc83/staging/src/k8s.io/kubectl/pkg/cmd/util/factory.go#L54) 
* This [line](https://github.com/kubernetes/kubernetes/blob/7cea81ce34c4aa7d0e952d7f9957db254e3fbc83/staging/src/k8s.io/kubectl/pkg/cmd/create/create.go#L252) will create a [builder](https://github.com/kubernetes/kubernetes/blob/7cea81ce34c4aa7d0e952d7f9957db254e3fbc83/staging/src/k8s.io/kubectl/pkg/cmd/util/factory.go#L54) which is responsible for taking the data that pass in via `-f` flag or `-k` flags (which is usually a YAML file), unpack it and turn it into Kubernetes Objects such that each Object will have generic REST operation performed on it.
* For each resource a [NewHelper](https://github.com/kubernetes/kubernetes/blob/7cea81ce34c4aa7d0e952d7f9957db254e3fbc83/staging/src/k8s.io/kubectl/pkg/cmd/create/create.go#L286) function will be created which will provide methods for running generic RESTful operations. This helper executes HTTP request([Get](https://github.com/kubernetes/kubernetes/blob/7cea81ce34c4aa7d0e952d7f9957db254e3fbc83/staging/src/k8s.io/cli-runtime/pkg/resource/helper.go#L78),[POST](https://github.com/kubernetes/kubernetes/blob/7cea81ce34c4aa7d0e952d7f9957db254e3fbc83/staging/src/k8s.io/cli-runtime/pkg/resource/helper.go#L167) , etc etc)
* As we saw, the helper uses [REST client to build and execute the POST request](https://github.com/kubernetes/kubernetes/blob/7cea81ce34c4aa7d0e952d7f9957db254e3fbc83/staging/src/k8s.io/cli-runtime/pkg/resource/helper.go#L167) and a big part of that is to build the [body](https://github.com/kubernetes/kubernetes/blob/7cea81ce34c4aa7d0e952d7f9957db254e3fbc83/staging/src/k8s.io/cli-runtime/pkg/resource/helper.go#L171) of the request. (Building this body will allow us to send HTTP request.)
* [This](https://github.com/kubernetes/kubernetes/tree/master/staging/src/k8s.io/client-go/rest) is where REST API lives and REST client lives [here](https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/client-go/rest/client.go) 
* Before sending any requests, we would need to [build a new **Request**](https://github.com/kubernetes/kubernetes/blob/7cea81ce34c4aa7d0e952d7f9957db254e3fbc83/staging/src/k8s.io/client-go/rest/client.go#L170) that can be send across the wire and understood by the API server and must be [serialized](https://github.com/kubernetes/kubernetes/blob/d88d9ac3b4eff86de439d65558a918a4d5fe962d/staging/src/k8s.io/client-go/rest/request.go#L453). [Here](https://github.com/kubernetes/kubernetes/blob/d88d9ac3b4eff86de439d65558a918a4d5fe962d/staging/src/k8s.io/client-go/rest/request.go#L425) we will fill out the **Request** using string, []byte, io.Reader and runtime.Object. The last step will be to send the HTTP request which will be done [here](https://github.com/kubernetes/kubernetes/blob/d88d9ac3b4eff86de439d65558a918a4d5fe962d/staging/src/k8s.io/client-go/rest/request.go#L978).
* Now, let's look at how seriliazation work. [Here](https://github.com/kubernetes/kubernetes/blob/d88d9ac3b4eff86de439d65558a918a4d5fe962d/staging/src/k8s.io/apimachinery/pkg/runtime/interfaces.go#L86) is where Serializer Object sits at.

### Day 3


