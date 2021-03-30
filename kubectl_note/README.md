# Kubectl notes

* Everything starts at creating a [Factory](https://github.com/kubernetes/kubectl/blob/0149779a03735a5d483115ca4220a7b6c861430c/pkg/cmd/util/factory.go#L41). Factory provides abstractions that allow the Kubectl command to be extended across multiple types
of resources and different API sets.


### RunTopPod execution
<ol>
<li>selector := labels.Everything()</li>
<li>Find the apiGroup by using o.DiscoveryClient.ServerGroups()</li>
<li>check if Supported Metrics API Version is Available</li>
<li>if Metrics API version is available then get Metrics From Metrics API</li>
</ol> 

### Get Metrics From Metrics API execution
<ol>
<li>what is metav1.NamespaceAll?</li>
 <li> Create a PodMetricsList </li>
</ol> 

### Question
How does builder work?
