# DigitalOcean Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/digitalocean**. The below arguments may be included as the key/value or JSON properties in the secret:

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
* `spaces_endpoint` - (Optional) This can be used to override the endpoint URL
  used for DigitalOcean Spaces requests. (It defaults to the value of the
  `SPACES_ENDPOINT_URL` environment variable or `https://{{.Region}}.digitaloceanspaces.com`
  if unset.) The provider will replace `{{.Region}}` (via Go's templating engine) with the slug
  of the applicable Spaces region.


## Supported Resources

* [TF::DigitalOcean::App](../resources/digitalocean/TF-DigitalOcean-App/docs/README.md)
* [TF::DigitalOcean::Cdn](../resources/digitalocean/TF-DigitalOcean-Cdn/docs/README.md)
* [TF::DigitalOcean::Certificate](../resources/digitalocean/TF-DigitalOcean-Certificate/docs/README.md)
* [TF::DigitalOcean::ContainerRegistryDockerCredentials](../resources/digitalocean/TF-DigitalOcean-ContainerRegistryDockerCredentials/docs/README.md)
* [TF::DigitalOcean::ContainerRegistry](../resources/digitalocean/TF-DigitalOcean-ContainerRegistry/docs/README.md)
* [TF::DigitalOcean::CustomImage](../resources/digitalocean/TF-DigitalOcean-CustomImage/docs/README.md)
* [TF::DigitalOcean::DatabaseCluster](../resources/digitalocean/TF-DigitalOcean-DatabaseCluster/docs/README.md)
* [TF::DigitalOcean::DatabaseConnectionPool](../resources/digitalocean/TF-DigitalOcean-DatabaseConnectionPool/docs/README.md)
* [TF::DigitalOcean::DatabaseDb](../resources/digitalocean/TF-DigitalOcean-DatabaseDb/docs/README.md)
* [TF::DigitalOcean::DatabaseFirewall](../resources/digitalocean/TF-DigitalOcean-DatabaseFirewall/docs/README.md)
* [TF::DigitalOcean::DatabaseReplica](../resources/digitalocean/TF-DigitalOcean-DatabaseReplica/docs/README.md)
* [TF::DigitalOcean::DatabaseUser](../resources/digitalocean/TF-DigitalOcean-DatabaseUser/docs/README.md)
* [TF::DigitalOcean::Domain](../resources/digitalocean/TF-DigitalOcean-Domain/docs/README.md)
* [TF::DigitalOcean::DropletSnapshot](../resources/digitalocean/TF-DigitalOcean-DropletSnapshot/docs/README.md)
* [TF::DigitalOcean::Droplet](../resources/digitalocean/TF-DigitalOcean-Droplet/docs/README.md)
* [TF::DigitalOcean::Firewall](../resources/digitalocean/TF-DigitalOcean-Firewall/docs/README.md)
* [TF::DigitalOcean::FloatingIpAssignment](../resources/digitalocean/TF-DigitalOcean-FloatingIpAssignment/docs/README.md)
* [TF::DigitalOcean::FloatingIp](../resources/digitalocean/TF-DigitalOcean-FloatingIp/docs/README.md)
* [TF::DigitalOcean::KubernetesCluster](../resources/digitalocean/TF-DigitalOcean-KubernetesCluster/docs/README.md)
* [TF::DigitalOcean::KubernetesNodePool](../resources/digitalocean/TF-DigitalOcean-KubernetesNodePool/docs/README.md)
* [TF::DigitalOcean::Loadbalancer](../resources/digitalocean/TF-DigitalOcean-Loadbalancer/docs/README.md)
* [TF::DigitalOcean::ProjectResources](../resources/digitalocean/TF-DigitalOcean-ProjectResources/docs/README.md)
* [TF::DigitalOcean::Project](../resources/digitalocean/TF-DigitalOcean-Project/docs/README.md)
* [TF::DigitalOcean::Record](../resources/digitalocean/TF-DigitalOcean-Record/docs/README.md)
* [TF::DigitalOcean::SpacesBucketObject](../resources/digitalocean/TF-DigitalOcean-SpacesBucketObject/docs/README.md)
* [TF::DigitalOcean::SpacesBucket](../resources/digitalocean/TF-DigitalOcean-SpacesBucket/docs/README.md)
* [TF::DigitalOcean::SshKey](../resources/digitalocean/TF-DigitalOcean-SshKey/docs/README.md)
* [TF::DigitalOcean::Tag](../resources/digitalocean/TF-DigitalOcean-Tag/docs/README.md)
* [TF::DigitalOcean::VolumeAttachment](../resources/digitalocean/TF-DigitalOcean-VolumeAttachment/docs/README.md)
* [TF::DigitalOcean::VolumeSnapshot](../resources/digitalocean/TF-DigitalOcean-VolumeSnapshot/docs/README.md)
* [TF::DigitalOcean::Volume](../resources/digitalocean/TF-DigitalOcean-Volume/docs/README.md)
* [TF::DigitalOcean::Vpc](../resources/digitalocean/TF-DigitalOcean-Vpc/docs/README.md)