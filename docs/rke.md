# Rancher Kubernetes Engine Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/rke**. The below arguments may be included as the key/value or JSON properties in the secret:

* `debug` - (Optional) Enable RKE debug logs. Default `false` (bool)
* `log_file` - (Optional) Save RKE logs to a file

## Supported Resources

* [TF::RKE::Cluster](../resources/rke/TF-RKE-Cluster/docs/README.md)