# Civo Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/civo**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Optional) This is the Civo API token.

## Supported Resources

* [TF::Civo::DnsDomainName](../resources/civo/TF-Civo-DnsDomainName/docs/README.md)
* [TF::Civo::DnsDomainRecord](../resources/civo/TF-Civo-DnsDomainRecord/docs/README.md)
* [TF::Civo::FirewallRule](../resources/civo/TF-Civo-FirewallRule/docs/README.md)
* [TF::Civo::Firewall](../resources/civo/TF-Civo-Firewall/docs/README.md)
* [TF::Civo::Instance](../resources/civo/TF-Civo-Instance/docs/README.md)
* [TF::Civo::KubernetesCluster](../resources/civo/TF-Civo-KubernetesCluster/docs/README.md)
* [TF::Civo::KubernetesNodePool](../resources/civo/TF-Civo-KubernetesNodePool/docs/README.md)
* [TF::Civo::Loadbalancer](../resources/civo/TF-Civo-Loadbalancer/docs/README.md)
* [TF::Civo::Network](../resources/civo/TF-Civo-Network/docs/README.md)
* [TF::Civo::Snapshot](../resources/civo/TF-Civo-Snapshot/docs/README.md)
* [TF::Civo::SshKey](../resources/civo/TF-Civo-SshKey/docs/README.md)
* [TF::Civo::Template](../resources/civo/TF-Civo-Template/docs/README.md)
* [TF::Civo::VolumeAttachment](../resources/civo/TF-Civo-VolumeAttachment/docs/README.md)
* [TF::Civo::Volume](../resources/civo/TF-Civo-Volume/docs/README.md)