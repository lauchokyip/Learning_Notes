# Adding k8s endpoint
Tracking progress of me adding **Endpoint** to `kubectl`

### Goal
Adding Endpoint to `kubectl`
```
$ kubectl get service
NAME   TYPE       CLUSTER-IP    EXTERNAL-IP   PORT(S)          Endpoint(S)    AGE
web    NodePort   10.108.X.X    <none>        8080:32170/TCP   2              8s
```

### Day 1
Learning what [Kubernetes services](https://kubernetes.io/docs/concepts/services-networking/service/#motivation) is </br>
This [video](https://www.youtube.com/watch?v=T4Z7visMM4E) from Nana is pretty useful. </br>
So `kubectl get service` will make API call to the API server to get some information about the service. I am guessing
we want to find where all the request will end up from [Services Types](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types) Changes need to be done from **Printer codes** and the **server side** where it will calculate the all the [Endpoint](https://kubernetes.io/docs/concepts/services-networking/service/#services-without-selectors) object. 
</br>
</br>
Question:
* Does each Services has Endpoint Object? 
</br>
TODO:
* Watch [Google Open Source Live presents Kubernetes (R) | Full Event](https://www.youtube.com/watch?v=60fnBk14ifc) to understand how API call works
* Figure out how printer codes work
