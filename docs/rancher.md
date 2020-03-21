# Rancher Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/rancher**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `api_url` - (Required) Rancher API url.
* `access_key` - (Optional) Rancher API access key.
* `secret_key` - (Optional) Rancher API access key.


## Supported Resources

* [Terraform::Rancher::Certificate](../resources/rancher/Terraform-Rancher-Certificate/docs/README.md)
* [Terraform::Rancher::Environment](../resources/rancher/Terraform-Rancher-Environment/docs/README.md)
* [Terraform::Rancher::Host](../resources/rancher/Terraform-Rancher-Host/docs/README.md)
* [Terraform::Rancher::RegistrationToken](../resources/rancher/Terraform-Rancher-RegistrationToken/docs/README.md)
* [Terraform::Rancher::RegistryCredential](../resources/rancher/Terraform-Rancher-RegistryCredential/docs/README.md)
* [Terraform::Rancher::Registry](../resources/rancher/Terraform-Rancher-Registry/docs/README.md)
* [Terraform::Rancher::Secrets](../resources/rancher/Terraform-Rancher-Secrets/docs/README.md)
* [Terraform::Rancher::Stack](../resources/rancher/Terraform-Rancher-Stack/docs/README.md)
* [Terraform::Rancher::Volumes](../resources/rancher/Terraform-Rancher-Volumes/docs/README.md)