# Kubernetes Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/kubernetes**. The below arguments may be included as the key/value or JSON properties in the secret:

* `host` - (Optional) The hostname (in form of URI) of the Kubernetes API.
* `username` - (Optional) The username to use for HTTP basic authentication when accessing the Kubernetes API.
* `password` - (Optional) The password to use for HTTP basic authentication when accessing the Kubernetes API.
* `insecure` - (Optional) Whether the server should be accessed without verifying the TLS certificate. Defaults to `false`.
* `client_certificate` - (Optional) PEM-encoded client certificate for TLS authentication.
* `client_key` - (Optional) PEM-encoded client certificate key for TLS authentication.
* `cluster_ca_certificate` - (Optional) PEM-encoded root certificates bundle for TLS authentication.
* `config_path` - (Optional) A path to a kube config file.
* `config_paths` - (Optional) A list of paths to the kube config files.
* `config_context` - (Optional) Context to choose from the config file.
* `config_context_auth_info` - (Optional) Authentication info context of the kube config (name of the kubeconfig user, `--user` flag in `kubectl`).
* `config_context_cluster` - (Optional) Cluster context of the kube config (name of the kubeconfig cluster, `--cluster` flag in `kubectl`).
* `token` - (Optional) Token of your service account.
* `exec` - (Optional) Configuration block to use an [exec-based credential plugin] (https://kubernetes.io/docs/reference/access-authn-authz/authentication/#client-go-credential-plugins), e.g. call an external command to receive user credentials.
    * `api_version` - (Required) API version to use when decoding the ExecCredentials resource, e.g. `client.authentication.k8s.io/v1beta1`.
    * `command` - (Required) Command to execute.
    * `args` - (Optional) List of arguments to pass when executing the plugin.


## Supported Resources

* [TF::Kubernetes::ApiService](../resources/kubernetes/TF-Kubernetes-ApiService/docs/README.md)
* [TF::Kubernetes::CertificateSigningRequest](../resources/kubernetes/TF-Kubernetes-CertificateSigningRequest/docs/README.md)
* [TF::Kubernetes::ClusterRoleBinding](../resources/kubernetes/TF-Kubernetes-ClusterRoleBinding/docs/README.md)
* [TF::Kubernetes::ClusterRole](../resources/kubernetes/TF-Kubernetes-ClusterRole/docs/README.md)
* [TF::Kubernetes::ConfigMap](../resources/kubernetes/TF-Kubernetes-ConfigMap/docs/README.md)
* [TF::Kubernetes::CronJob](../resources/kubernetes/TF-Kubernetes-CronJob/docs/README.md)
* [TF::Kubernetes::CsiDriver](../resources/kubernetes/TF-Kubernetes-CsiDriver/docs/README.md)
* [TF::Kubernetes::Daemonset](../resources/kubernetes/TF-Kubernetes-Daemonset/docs/README.md)
* [TF::Kubernetes::DefaultServiceAccount](../resources/kubernetes/TF-Kubernetes-DefaultServiceAccount/docs/README.md)
* [TF::Kubernetes::Deployment](../resources/kubernetes/TF-Kubernetes-Deployment/docs/README.md)
* [TF::Kubernetes::Endpoints](../resources/kubernetes/TF-Kubernetes-Endpoints/docs/README.md)
* [TF::Kubernetes::HorizontalPodAutoscaler](../resources/kubernetes/TF-Kubernetes-HorizontalPodAutoscaler/docs/README.md)
* [TF::Kubernetes::Ingress](../resources/kubernetes/TF-Kubernetes-Ingress/docs/README.md)
* [TF::Kubernetes::Job](../resources/kubernetes/TF-Kubernetes-Job/docs/README.md)
* [TF::Kubernetes::LimitRange](../resources/kubernetes/TF-Kubernetes-LimitRange/docs/README.md)
* [TF::Kubernetes::MutatingWebhookConfiguration](../resources/kubernetes/TF-Kubernetes-MutatingWebhookConfiguration/docs/README.md)
* [TF::Kubernetes::Namespace](../resources/kubernetes/TF-Kubernetes-Namespace/docs/README.md)
* [TF::Kubernetes::NetworkPolicy](../resources/kubernetes/TF-Kubernetes-NetworkPolicy/docs/README.md)
* [TF::Kubernetes::PersistentVolumeClaim](../resources/kubernetes/TF-Kubernetes-PersistentVolumeClaim/docs/README.md)
* [TF::Kubernetes::PersistentVolume](../resources/kubernetes/TF-Kubernetes-PersistentVolume/docs/README.md)
* [TF::Kubernetes::PodDisruptionBudget](../resources/kubernetes/TF-Kubernetes-PodDisruptionBudget/docs/README.md)
* [TF::Kubernetes::PodSecurityPolicy](../resources/kubernetes/TF-Kubernetes-PodSecurityPolicy/docs/README.md)
* [TF::Kubernetes::Pod](../resources/kubernetes/TF-Kubernetes-Pod/docs/README.md)
* [TF::Kubernetes::PriorityClass](../resources/kubernetes/TF-Kubernetes-PriorityClass/docs/README.md)
* [TF::Kubernetes::ReplicationController](../resources/kubernetes/TF-Kubernetes-ReplicationController/docs/README.md)
* [TF::Kubernetes::ResourceQuota](../resources/kubernetes/TF-Kubernetes-ResourceQuota/docs/README.md)
* [TF::Kubernetes::RoleBinding](../resources/kubernetes/TF-Kubernetes-RoleBinding/docs/README.md)
* [TF::Kubernetes::Role](../resources/kubernetes/TF-Kubernetes-Role/docs/README.md)
* [TF::Kubernetes::Secret](../resources/kubernetes/TF-Kubernetes-Secret/docs/README.md)
* [TF::Kubernetes::ServiceAccount](../resources/kubernetes/TF-Kubernetes-ServiceAccount/docs/README.md)
* [TF::Kubernetes::Service](../resources/kubernetes/TF-Kubernetes-Service/docs/README.md)
* [TF::Kubernetes::StatefulSet](../resources/kubernetes/TF-Kubernetes-StatefulSet/docs/README.md)
* [TF::Kubernetes::StorageClass](../resources/kubernetes/TF-Kubernetes-StorageClass/docs/README.md)
* [TF::Kubernetes::ValidatingWebhookConfiguration](../resources/kubernetes/TF-Kubernetes-ValidatingWebhookConfiguration/docs/README.md)