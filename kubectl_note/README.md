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

### get Metrics From Metrics execution

1) call `metav1.NamespaceAll` </br>
2) Create PodMetricsList from ` &metricsv1beta1api.PodMetricsList{}`</br>
3) if there is no resourceName is provided, for example `kubectl top pod nginx-deployment-bdb48231-123zsdk` , `nginx-deployment-bdb48231-123zsdk` will be the resourceName
then 
 ```
 m, err := metricsClient.MetricsV1beta1().PodMetricses(ns).Get(context.TODO(), resourceName, metav1.GetOptions{})
		if err != nil {
			return nil, err
		}
		versionedMetrics.Items = []metricsv1beta1api.PodMetrics{*m}
 ``` 
 4) if resourceName is provided, then
 ```
 	versionedMetrics, err = metricsClient.MetricsV1beta1().PodMetricses(ns).List(context.TODO(), metav1.ListOptions{LabelSelector: selector.String()})
		if err != nil {
			return nil, err
		}
 ```
 
 5)Create PodMetricsList from ` &metricsapi.PodMetricsList{}`</br>
 
 Summary : Basically create PodMetricsList from `v1beta1api` and convert it to `metrics` PodMetricsList
 </br>
 
### 

### Question
How does builder work?
