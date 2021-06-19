# Vultr Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/vultr**. The below arguments may be included as the key/value or JSON properties in the secret:

* `api_key` - (Required) This is the [Vultr API key](https://my.vultr.com/settings/#settingsapi).
* `rate_limit` - (Optional) Vultr limits API calls to 3 calls per second. This field lets you configure how the rate limit using milliseconds. The default value if this field is omitted is `650 milliseconds` per call. 
* `retry_limit` - (Optional) This field lets you configure how many retries should be attempted on a failed call. The default value if this field is omitted is `3` retries.


## Supported Resources

* [TF::Vultr::BareMetalServer](../resources/vultr/TF-Vultr-BareMetalServer/docs/README.md)
* [TF::Vultr::BlockStorage](../resources/vultr/TF-Vultr-BlockStorage/docs/README.md)
* [TF::Vultr::DnsDomain](../resources/vultr/TF-Vultr-DnsDomain/docs/README.md)
* [TF::Vultr::DnsRecord](../resources/vultr/TF-Vultr-DnsRecord/docs/README.md)
* [TF::Vultr::FirewallGroup](../resources/vultr/TF-Vultr-FirewallGroup/docs/README.md)
* [TF::Vultr::FirewallRule](../resources/vultr/TF-Vultr-FirewallRule/docs/README.md)
* [TF::Vultr::InstanceIpv4](../resources/vultr/TF-Vultr-InstanceIpv4/docs/README.md)
* [TF::Vultr::Instance](../resources/vultr/TF-Vultr-Instance/docs/README.md)
* [TF::Vultr::IsoPrivate](../resources/vultr/TF-Vultr-IsoPrivate/docs/README.md)
* [TF::Vultr::LoadBalancer](../resources/vultr/TF-Vultr-LoadBalancer/docs/README.md)
* [TF::Vultr::ObjectStorage](../resources/vultr/TF-Vultr-ObjectStorage/docs/README.md)
* [TF::Vultr::PrivateNetwork](../resources/vultr/TF-Vultr-PrivateNetwork/docs/README.md)
* [TF::Vultr::ReservedIp](../resources/vultr/TF-Vultr-ReservedIp/docs/README.md)
* [TF::Vultr::ReverseIpv4](../resources/vultr/TF-Vultr-ReverseIpv4/docs/README.md)
* [TF::Vultr::ReverseIpv6](../resources/vultr/TF-Vultr-ReverseIpv6/docs/README.md)
* [TF::Vultr::SnapshotFromUrl](../resources/vultr/TF-Vultr-SnapshotFromUrl/docs/README.md)
* [TF::Vultr::Snapshot](../resources/vultr/TF-Vultr-Snapshot/docs/README.md)
* [TF::Vultr::SshKey](../resources/vultr/TF-Vultr-SshKey/docs/README.md)
* [TF::Vultr::StartupScript](../resources/vultr/TF-Vultr-StartupScript/docs/README.md)
* [TF::Vultr::User](../resources/vultr/TF-Vultr-User/docs/README.md)