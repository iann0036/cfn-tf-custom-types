# Kubernetes Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/kubernetes**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `host` - (Optional) The hostname (in form of URI) of Kubernetes master.
* `username` - (Optional) The username to use for HTTP basic authentication when accessing the Kubernetes master endpoint.
* `password` - (Optional) The password to use for HTTP basic authentication when accessing the Kubernetes master endpoint.
* `insecure` - (Optional) Whether server should be accessed without verifying the TLS certificate. Defaults to `false`.
* `client_certificate` - (Optional) PEM-encoded client certificate for TLS authentication.
* `client_key` - (Optional) PEM-encoded client certificate key for TLS authentication.
* `cluster_ca_certificate` - (Optional) PEM-encoded root certificates bundle for TLS authentication.
* `config_path` - (Optional) Path to the kube config file. Defaults to `~/.kube/config`.
* `config_context` - (Optional) Context to choose from the config file.
* `config_context_auth_info` - (Optional) Authentication info context of the kube config (name of the kubeconfig user, `--user` flag in `kubectl`).
* `config_context_cluster` - (Optional) Cluster context of the kube config (name of the kubeconfig cluster, `--cluster` flag in `kubectl`).
* `token` - (Optional) Token of your service account.
* `load_config_file` - (Optional) By default the local config (~/.kube/config) is loaded when you use this provider. This option at false disables this behaviour which is desired when statically specifying the configuration or relying on in-cluster config.
* `exec` - (Optional) Configuration block to use an [exec-based credential plugin] (https://kubernetes.io/docs/reference/access-authn-authz/authentication/#client-go-credential-plugins), e.g. call an external command to receive user credentials.
  * `api_version` - (Required) API version to use when decoding the ExecCredentials resource, e.g. `client.authentication.k8s.io/v1beta1`.
  * `command` - (Required) Command to execute.
  * `args` - (Optional) List of arguments to pass when executing the plugin.


## Supported Resources

* [Terraform::Kubernetes::ApiService](../resources/kubernetes/Terraform-Kubernetes-ApiService/docs/README.md)
* [Terraform::Kubernetes::ClusterRoleBinding](../resources/kubernetes/Terraform-Kubernetes-ClusterRoleBinding/docs/README.md)
* [Terraform::Kubernetes::ClusterRole](../resources/kubernetes/Terraform-Kubernetes-ClusterRole/docs/README.md)
* [Terraform::Kubernetes::ConfigMap](../resources/kubernetes/Terraform-Kubernetes-ConfigMap/docs/README.md)
* [Terraform::Kubernetes::CronJob](../resources/kubernetes/Terraform-Kubernetes-CronJob/docs/README.md)
* [Terraform::Kubernetes::Daemonset](../resources/kubernetes/Terraform-Kubernetes-Daemonset/docs/README.md)
* [Terraform::Kubernetes::Deployment](../resources/kubernetes/Terraform-Kubernetes-Deployment/docs/README.md)
* [Terraform::Kubernetes::Endpoints](../resources/kubernetes/Terraform-Kubernetes-Endpoints/docs/README.md)
* [Terraform::Kubernetes::HorizontalPodAutoscaler](../resources/kubernetes/Terraform-Kubernetes-HorizontalPodAutoscaler/docs/README.md)
* [Terraform::Kubernetes::Ingress](../resources/kubernetes/Terraform-Kubernetes-Ingress/docs/README.md)
* [Terraform::Kubernetes::Job](../resources/kubernetes/Terraform-Kubernetes-Job/docs/README.md)
* [Terraform::Kubernetes::LimitRange](../resources/kubernetes/Terraform-Kubernetes-LimitRange/docs/README.md)
* [Terraform::Kubernetes::Namespace](../resources/kubernetes/Terraform-Kubernetes-Namespace/docs/README.md)
* [Terraform::Kubernetes::NetworkPolicy](../resources/kubernetes/Terraform-Kubernetes-NetworkPolicy/docs/README.md)
* [Terraform::Kubernetes::PersistentVolumeClaim](../resources/kubernetes/Terraform-Kubernetes-PersistentVolumeClaim/docs/README.md)
* [Terraform::Kubernetes::PersistentVolume](../resources/kubernetes/Terraform-Kubernetes-PersistentVolume/docs/README.md)
* [Terraform::Kubernetes::PodDisruptionBudget](../resources/kubernetes/Terraform-Kubernetes-PodDisruptionBudget/docs/README.md)
* [Terraform::Kubernetes::Pod](../resources/kubernetes/Terraform-Kubernetes-Pod/docs/README.md)
* [Terraform::Kubernetes::PriorityClass](../resources/kubernetes/Terraform-Kubernetes-PriorityClass/docs/README.md)
* [Terraform::Kubernetes::ReplicationController](../resources/kubernetes/Terraform-Kubernetes-ReplicationController/docs/README.md)
* [Terraform::Kubernetes::ResourceQuota](../resources/kubernetes/Terraform-Kubernetes-ResourceQuota/docs/README.md)
* [Terraform::Kubernetes::RoleBinding](../resources/kubernetes/Terraform-Kubernetes-RoleBinding/docs/README.md)
* [Terraform::Kubernetes::Role](../resources/kubernetes/Terraform-Kubernetes-Role/docs/README.md)
* [Terraform::Kubernetes::Secret](../resources/kubernetes/Terraform-Kubernetes-Secret/docs/README.md)
* [Terraform::Kubernetes::ServiceAccount](../resources/kubernetes/Terraform-Kubernetes-ServiceAccount/docs/README.md)
* [Terraform::Kubernetes::Service](../resources/kubernetes/Terraform-Kubernetes-Service/docs/README.md)
* [Terraform::Kubernetes::StatefulSet](../resources/kubernetes/Terraform-Kubernetes-StatefulSet/docs/README.md)
* [Terraform::Kubernetes::StorageClass](../resources/kubernetes/Terraform-Kubernetes-StorageClass/docs/README.md)