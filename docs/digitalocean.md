# DigitalOcean Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/digitalocean**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `token` - (Required) This is the DO API token. Alternatively, this can also be specified
  using environment variables ordered by precedence:
  * `DIGITALOCEAN_TOKEN`
  * `DIGITALOCEAN_ACCESS_TOKEN`
* `spaces_access_id` - (Optional) The access key ID used for Spaces API
  operations (Defaults to the value of the `SPACES_ACCESS_KEY_ID` environment
  variable).
* `spaces_secret_key` - (Optional) The secret access key used for Spaces API
  operations (Defaults to the value of the `SPACES_SECRET_ACCESS_KEY`
  environment variable).
* `api_endpoint` - (Optional) This can be used to override the base URL for
  DigitalOcean API requests (Defaults to the value of the `DIGITALOCEAN_API_URL`
  environment variable or `https://api.digitalocean.com` if unset).


## Supported Resources

* [Terraform::DigitalOcean::Cdn](../resources/digitalocean/Terraform-DigitalOcean-Cdn/docs/README.md)
* [Terraform::DigitalOcean::Certificate](../resources/digitalocean/Terraform-DigitalOcean-Certificate/docs/README.md)
* [Terraform::DigitalOcean::DatabaseCluster](../resources/digitalocean/Terraform-DigitalOcean-DatabaseCluster/docs/README.md)
* [Terraform::DigitalOcean::DatabaseConnectionPool](../resources/digitalocean/Terraform-DigitalOcean-DatabaseConnectionPool/docs/README.md)
* [Terraform::DigitalOcean::DatabaseDb](../resources/digitalocean/Terraform-DigitalOcean-DatabaseDb/docs/README.md)
* [Terraform::DigitalOcean::DatabaseFirewall](../resources/digitalocean/Terraform-DigitalOcean-DatabaseFirewall/docs/README.md)
* [Terraform::DigitalOcean::DatabaseReplica](../resources/digitalocean/Terraform-DigitalOcean-DatabaseReplica/docs/README.md)
* [Terraform::DigitalOcean::DatabaseUser](../resources/digitalocean/Terraform-DigitalOcean-DatabaseUser/docs/README.md)
* [Terraform::DigitalOcean::Domain](../resources/digitalocean/Terraform-DigitalOcean-Domain/docs/README.md)
* [Terraform::DigitalOcean::DropletSnapshot](../resources/digitalocean/Terraform-DigitalOcean-DropletSnapshot/docs/README.md)
* [Terraform::DigitalOcean::Droplet](../resources/digitalocean/Terraform-DigitalOcean-Droplet/docs/README.md)
* [Terraform::DigitalOcean::Firewall](../resources/digitalocean/Terraform-DigitalOcean-Firewall/docs/README.md)
* [Terraform::DigitalOcean::FloatingIpAssignment](../resources/digitalocean/Terraform-DigitalOcean-FloatingIpAssignment/docs/README.md)
* [Terraform::DigitalOcean::FloatingIp](../resources/digitalocean/Terraform-DigitalOcean-FloatingIp/docs/README.md)
* [Terraform::DigitalOcean::KubernetesCluster](../resources/digitalocean/Terraform-DigitalOcean-KubernetesCluster/docs/README.md)
* [Terraform::DigitalOcean::KubernetesNodePool](../resources/digitalocean/Terraform-DigitalOcean-KubernetesNodePool/docs/README.md)
* [Terraform::DigitalOcean::Loadbalancer](../resources/digitalocean/Terraform-DigitalOcean-Loadbalancer/docs/README.md)
* [Terraform::DigitalOcean::ProjectResources](../resources/digitalocean/Terraform-DigitalOcean-ProjectResources/docs/README.md)
* [Terraform::DigitalOcean::Project](../resources/digitalocean/Terraform-DigitalOcean-Project/docs/README.md)
* [Terraform::DigitalOcean::Record](../resources/digitalocean/Terraform-DigitalOcean-Record/docs/README.md)
* [Terraform::DigitalOcean::SpacesBucket](../resources/digitalocean/Terraform-DigitalOcean-SpacesBucket/docs/README.md)
* [Terraform::DigitalOcean::SshKey](../resources/digitalocean/Terraform-DigitalOcean-SshKey/docs/README.md)
* [Terraform::DigitalOcean::Tag](../resources/digitalocean/Terraform-DigitalOcean-Tag/docs/README.md)
* [Terraform::DigitalOcean::VolumeAttachment](../resources/digitalocean/Terraform-DigitalOcean-VolumeAttachment/docs/README.md)
* [Terraform::DigitalOcean::VolumeSnapshot](../resources/digitalocean/Terraform-DigitalOcean-VolumeSnapshot/docs/README.md)
* [Terraform::DigitalOcean::Volume](../resources/digitalocean/Terraform-DigitalOcean-Volume/docs/README.md)