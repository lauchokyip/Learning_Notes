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
 
### Builder
Usually looks like that, here I will use `kubectl get` as an example
```
r := f.NewBuilder().
		Unstructured().
		NamespaceParam(o.Namespace).DefaultNamespace().AllNamespaces(o.AllNamespaces).
		FilenameParam(o.ExplicitNamespace, &o.FilenameOptions).
		LabelSelectorParam(o.LabelSelector).
		FieldSelectorParam(o.FieldSelector).
		RequestChunksOf(chunkSize).
		ResourceTypeOrNameArgs(true, args...).
		ContinueOnError().
		Latest().
		Flatten().
		TransformRequests(o.transformRequests).
		Do()
```

1) [`NewBuilder()`](https://github.com/kubernetes/kubectl/blob/ac49920c0ccb0dd0899d5300fc43713ee2dfcdc9/pkg/cmd/testing/fake.go#L526) will build a new Builder and the rest of the function will be modifying the [Builder](https://github.com/kubernetes/kubernetes/blob/6a7572e4adaa209e09744092a9ac052f31fbeb9f/staging/src/k8s.io/cli-runtime/pkg/resource/builder.go#L52) 
2) [`Do()`](https://github.com/kubernetes/cli-runtime/blob/3cc3835b3ec298e5a3a277b03f7a133f156a45d9/pkg/resource/builder.go#L1109) will build the visitor which will be called to visit later. inside `Do()` [`visitorResult()`](https://github.com/kubernetes/cli-runtime/blob/3cc3835b3ec298e5a3a277b03f7a133f156a45d9/pkg/resource/builder.go#L1111) will be called to determine how do we want to visit the items whether by [path](https://github.com/kubernetes/cli-runtime/blob/3cc3835b3ec298e5a3a277b03f7a133f156a45d9/pkg/resource/builder.go#L817), by [selector](https://github.com/kubernetes/cli-runtime/blob/3cc3835b3ec298e5a3a277b03f7a133f156a45d9/pkg/resource/builder.go#L821), [resourcetuples](https://github.com/kubernetes/cli-runtime/blob/3cc3835b3ec298e5a3a277b03f7a133f156a45d9/pkg/resource/builder.go#L827),  [names](https://github.com/kubernetes/cli-runtime/blob/3cc3835b3ec298e5a3a277b03f7a133f156a45d9/pkg/resource/builder.go#L832), or by [resources](https://github.com/kubernetes/cli-runtime/blob/3cc3835b3ec298e5a3a277b03f7a133f156a45d9/pkg/resource/builder.go#L835) 

### Question
when calling `kubectl get pods` why do we have to call 
