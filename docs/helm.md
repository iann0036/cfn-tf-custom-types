# Helm Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/helm**. The below arguments may be included as the key/value or JSON properties in the secret:

* `debug` - (Optional) - Debug indicates whether or not Helm is running in Debug mode. Defaults to `false`.
* `plugins_path` - (Optional) The path to the plugins directory. Defaults to `HELM_PLUGINS` env if it is set, otherwise uses the default path set by helm.
* `registry_config_path` - (Optional) The path to the registry config file. Defaults to `HELM_REGISTRY_CONFIG` env if it is set, otherwise uses the default path set by helm.
* `repository_config_path` - (Optional) The path to the file containing repository names and URLs. Defaults to `HELM_REPOSITORY_CONFIG` env if it is set, otherwise uses the default path set by helm.
* `repository_cache` - (Optional) The path to the file containing cached repository indexes. Defaults to `HELM_REPOSITORY_CACHE` env if it is set, otherwise uses the default path set by helm.
* `helm_driver` - (Optional) "The backend storage driver. Valid values are: `configmap`, `secret`, `memory`, `sql`. Defaults to `secret`.
  Note: Regarding the sql driver, as of helm v3.2.0 SQL support exists only for the postgres dialect.g. `HELM_DRIVER_SQL_CONNECTION_STRING=postgres://username:password@host/dbname` more info [here](https://pkg.go.dev/github.com/lib/pq).
* `kubernetes` - Kubernetes configuration block.

The `kubernetes` block supports:

* `config_path` - (Optional) Path to the kube config file.
* `config_paths` - (Optional) A list of paths to the kube config files.
* `host` - (Optional) The hostname (in form of URI) of the Kubernetes API.
* `username` - (Optional) The username to use for HTTP basic authentication when accessing the Kubernetes API.
* `password` - (Optional) The password to use for HTTP basic authentication when accessing the Kubernetes API.
* `token` - (Optional) The bearer token to use for authentication when accessing the Kubernetes API.
* `insecure` - (Optional) Whether server should be accessed without verifying the TLS certificate.
* `client_certificate` - (Optional) PEM-encoded client certificate for TLS authentication.
* `client_key` - (Optional) PEM-encoded client certificate key for TLS authentication.
* `cluster_ca_certificate` - (Optional) PEM-encoded root certificates bundle for TLS authentication.
* `config_context` - (Optional) Context to choose from the config file.
* `exec` - (Optional) Configuration block to use an [exec-based credential plugin](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#client-go-credential-plugins), e.g. call an external command to receive user credentials.
  * `api_version` - (Required) API version to use when decoding the ExecCredentials resource, e.g. `client.authentication.k8s.io/v1beta1`.
  * `command` - (Required) Command to execute.
  * `args` - (Optional) List of arguments to pass when executing the plugin.


## Supported Resources

* [TF::Helm::Release](../resources/helm/TF-Helm-Release/docs/README.md)