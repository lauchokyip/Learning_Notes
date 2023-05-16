## Useful Guide
* https://github.com/kubernetes-sigs/kubebuilder/discussions/3283
* [Whole process of how a plugin is added](https://github.com/kubernetes-sigs/kubebuilder/issues/2765)
* [kubebuilder talk](https://www.youtube.com/watch?v=CD33-TRYwJc)

### Code Walkthrough
* Start with `/cmd/main` , the `cli.New` create a new `Cli` instant and run it
* `/pkg/config/interface.go` specify for the interfaces and different version implement the interface in `pkg/config/v3/config.go` . I believe `PROJECT` is the "config" file where the `kubebuilder` will read to scaffold new components
* When `main.go` imports `sigs.k8s.io/kubebuilder/v3/pkg/config/v3` , there is a sneaky function which will be run
```go 
func init() {
	config.Register(Version, New)
}
```
* the `config` will be called in two ways. First one is from `func (c *CLI) getInfoFromConfigFile()`. This function will read from the yaml file. Second way is from `func (factory *executionHooksFactory) preRunEFunc(options *resourceOptions,reateConfig bool)` . This function is part of the `applySubcommandHooks` which will be called in `api.go` , `edit.go`, `init.go` and `webhook.go` which help them to check if the `config` file exists. One thing to note is both use `yamlstore` to load the config yaml