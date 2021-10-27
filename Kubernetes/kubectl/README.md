## Things I found out while working on kubectl

* Main kubectl function starts [here](https://github.com/kubernetes/kubernetes/blob/ea0764452222146c47ec826977f49d7001b0ea8c/staging/src/k8s.io/kubectl/pkg/cmd/cmd.go#L522-L525). This 
is where most of the setup starts branching out. Notice that the `MatchVersionFlags` will wrap around Config Flags using [Delegate design pattern](https://en.wikipedia.org/wiki/Delegation_pattern) to check the version of kubectl and API server before proceed.
* Config flags is very important because it implements [RestClientGetter](https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/cli-runtime/pkg/genericclioptions/config_flags.go#L76) which will given use the function `ToRestConfig()`, `ToDiscoveryClient`, `ToRestMapper`and `ToRawKubeConfigLoader`. It will be added [here](https://github.com/kubernetes/kubernetes/blob/ea0764452222146c47ec826977f49d7001b0ea8c/staging/src/k8s.io/kubectl/pkg/cmd/cmd.go#L522)
* While I am working on a feature to extend `kubectl wait`, I came across 3 very similar types
  * `runtime.Unstructured`
  * `runtime.Object`
  * `unstructured.Unstructured`
* Here are the explanations: 
  * [`runtime.Unstructured`](https://github.com/kubernetes/kubernetes/blob/907d62eac8bdbb8bceea8e3767f6f3b9061a17f5/staging/src/k8s.io/apimachinery/pkg/runtime/interfaces.go#L327-L344) is essentially an interface that defines how an `Unstructured` type should be. It provides some useful method which 
  * [`unstructured.Unstructured`](https://github.com/kubernetes/kubernetes/blob/907d62eac8bdbb8bceea8e3767f6f3b9061a17f5/staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/unstructured/unstructured.go#L48-L50) is a concrete Object that implements `metav1.Object`, `runtime.Unstructure`, and `metav1.ListInterface`. It has some useful function that can be used for example, [`NestedInt64`](https://github.com/kubernetes/kubernetes/blob/907d62eac8bdbb8bceea8e3767f6f3b9061a17f5/staging/src/k8s.io/apimachinery/pkg/apis/meta/v1/unstructured/helpers.go#L116) which will return only Int64 in the whole nested `unstructured.Unstructured`. `Unstructured` is essentially a raw JSON so we can unmarshal or marshal with
  * [`runtime.Object`](https://github.com/kubernetes/kubernetes/blob/907d62eac8bdbb8bceea8e3767f6f3b9061a17f5/staging/src/k8s.io/apimachinery/pkg/runtime/interfaces.go#L299-L302) is an interface that definies how a Kubernetes object should be like. For example, pods, deployments, service are all the implementation of [`runtime.Object`](https://github.com/kubernetes/kubernetes/blob/907d62eac8bdbb8bceea8e3767f6f3b9061a17f5/staging/src/k8s.io/apimachinery/pkg/runtime/interfaces.go#L299-L302)
  * Every Kubernetes Objects are implmentation of `runtime.Object` and they can be switch to `Unstructured` type to get sent over wire. More details on how to convert them can be found [here](https://stackoverflow.com/questions/53341727/how-to-submit-generic-runtime-object-to-kubernetes-api-using-client-go/53359468#53359468)
* The kubectl [`Builder`](https://github.com/kubernetes/kubernetes/blob/907d62eac8bdbb8bceea8e3767f6f3b9061a17f5/staging/src/k8s.io/cli-runtime/pkg/resource/builder.go#L52) uses a [`Visitor`](https://github.com/kubernetes/kubernetes/blob/4af19756bd1e21da288732d33d268f626adf1145/staging/src/k8s.io/cli-runtime/pkg/resource/interfaces.go#L94) interface to walk through all the resources. Usually if we set up a client, we need to call `GET`, `LIST` etc to make a request but it's so find where it is because of the Visitor pattern. I am not really sure if it's using the `Visitor` design pattern but basically what it does is **wrap one Visitor on another visit (kind of like delegate design pattern)** .So far, I have tried two ways, 
```
kubectl get pods
```
```
kubectl get pod [pod name]
```
* The first way will trigger a [`visitBySelector`](https://github.com/kubernetes/kubernetes/blob/4af19756bd1e21da288732d33d268f626adf1145/staging/src/k8s.io/cli-runtime/pkg/resource/builder.go#L875), and the second way will triger a [`visitByName`](https://github.com/kubernetes/kubernetes/blob/4af19756bd1e21da288732d33d268f626adf1145/staging/src/k8s.io/cli-runtime/pkg/resource/builder.go#L1029). [`visitBySelector`](https://github.com/kubernetes/kubernetes/blob/4af19756bd1e21da288732d33d268f626adf1145/staging/src/k8s.io/cli-runtime/pkg/resource/builder.go#L875) is way easier because it just creates a new [`Selector`](https://github.com/kubernetes/kubernetes/blob/4af19756bd1e21da288732d33d268f626adf1145/staging/src/k8s.io/cli-runtime/pkg/resource/builder.go#L914) and the Selector has a [`List`](https://github.com/kubernetes/kubernetes/blob/4af19756bd1e21da288732d33d268f626adf1145/staging/src/k8s.io/cli-runtime/pkg/resource/selector.go#L57) method. But what about [`visitByName`](https://github.com/kubernetes/kubernetes/blob/4af19756bd1e21da288732d33d268f626adf1145/staging/src/k8s.io/cli-runtime/pkg/resource/builder.go#L1029)?? It's actually using a [`NewDecorativeVisitor`](https://github.com/kubernetes/kubernetes/blob/4af19756bd1e21da288732d33d268f626adf1145/staging/src/k8s.io/cli-runtime/pkg/resource/builder.go#L1158) which will eventually call the [`RetrieveLatest`](https://github.com/kubernetes/kubernetes/blob/4af19756bd1e21da288732d33d268f626adf1145/staging/src/k8s.io/cli-runtime/pkg/resource/visitor.go#L668) and then the [`GET`](https://github.com/kubernetes/kubernetes/blob/4af19756bd1e21da288732d33d268f626adf1145/staging/src/k8s.io/cli-runtime/pkg/resource/visitor.go#L673) method
* There are two ways of calling the API server, either using **static client** or **dynamic client**. Dynamic client would need to provide REST mapping.
* [**Codecs**](https://pkg.go.dev/k8s.io/apimachinery/pkg/runtime#Codec) is a [Serializer](https://github.com/kubernetes/apimachinery/blob/v0.22.2/pkg/runtime/interfaces.go#L86) in Kubernetes which has **Encoder** and **Decoder** inside so you just need to insert a **Encoder** and **Decoder** and you can encode and decode the `runtime.Object` whenever you want
* We can create a fake Client to fake a HTTP response
```
		tf := cmdtesting.NewTestFactory().WithNamespace("test")
			defer tf.Cleanup()

			codec := runtime.NewCodec(scheme.DefaultJSONEncoder(), scheme.Codecs.UniversalDecoder(scheme.Scheme.PrioritizedVersionsAllGroups()...))
			ns := scheme.Codecs.WithoutConversion()

			tf.Client = &fake.RESTClient{
				GroupVersion:         schema.GroupVersion{Version: "v1"},
				NegotiatedSerializer: ns,
				Client: fake.CreateHTTPClient(func(req *http.Request) (*http.Response, error) {
					switch p, m := req.URL.Path, req.Method; {
					case p == "/namespaces/test/services/baz" && m == "GET":
						return &http.Response{StatusCode: 200, Header: cmdtesting.DefaultHeader(), Body: cmdtesting.ObjBody(codec, &corev1.Service{
							ObjectMeta: metav1.ObjectMeta{Name: "baz", Namespace: "test", ResourceVersion: "12"},
							Spec: corev1.ServiceSpec{
								Selector: map[string]string{"app": "go"},
							},
						})}, nil
					case p == "/namespaces/test/services" && m == "POST":
						return &http.Response{StatusCode: 200, Header: cmdtesting.DefaultHeader(), Body: cmdtesting.ObjBody(codec, &corev1.Service{
							ObjectMeta: metav1.ObjectMeta{Name: "foo", Namespace: "", Labels: map[string]string{"svc": "test"}},
							Spec: corev1.ServiceSpec{
								Ports: []corev1.ServicePort{
									{
										Protocol:   corev1.ProtocolUDP,
										Port:       14,
										TargetPort: intstr.FromInt(14),
									},
								},
								Selector: map[string]string{"app": "go"},
							},
						})}, nil
					default:
						t.Fatalf("unexpected request: %#v\n%#v", req.URL, req)
						return nil, nil
					}
```
* To test a command and capture its' output, You would usually want to 
     * Create a test factory `tf := cmdtesting.NewTestFactory().WithNamespace("test") defer tf.Cleanup()`
     * Set up factory (See above how to setup)
     * Create a new IOStreams (`ioStreams, _, buf, _ := genericclioptions.NewTestIOStreams()`)
     * Create a new Cobra command (`cmd := NewCmd(tf, ioStreams)`)
     * Set the output to buffer instead of `stdout` or `stderr` (`cmd.SetOut(buf)`)
     * Set flags (`cmd.Flags().Set("protocol", "UDP")`)
     * Run command (`cmd.Run(cmd, []string{"service", "baz"})`)



