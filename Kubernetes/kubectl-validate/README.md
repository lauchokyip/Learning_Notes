# Code Walkthrough

* `hardcoded_builtins.go` uses `go:embed` to embed all the harcoded openapi in `builtins` and has the function `NewHardcodedBuiltins`
* `ValidatorFactory` takes `openapi.Client` which will has the mapping from group version openAPI.spec when `client.Path` is called
* `ValidatorsForGVK` has function 