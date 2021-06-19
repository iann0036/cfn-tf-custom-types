# VMware vRealize Automation Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/vra**. The below arguments may be included as the key/value or JSON properties in the secret:

* `url` - (Required) This is the URL to the VMware Cloud Automation
  Services endpoint.
* `access_token` - (Optional) This is the access token used to create an API
  refresh token.
* `refresh_token` - (Optional) This is a refresh_token used for API access that
  has been pre-generated. One of `access_token` or `refresh_token` is required.


## Supported Resources

* [TF::VRA::BlockDeviceSnapshot](../resources/vra/TF-VRA-BlockDeviceSnapshot/docs/README.md)
* [TF::VRA::BlockDevice](../resources/vra/TF-VRA-BlockDevice/docs/README.md)
* [TF::VRA::BlueprintVersion](../resources/vra/TF-VRA-BlueprintVersion/docs/README.md)
* [TF::VRA::Blueprint](../resources/vra/TF-VRA-Blueprint/docs/README.md)
* [TF::VRA::CatalogSourceBlueprint](../resources/vra/TF-VRA-CatalogSourceBlueprint/docs/README.md)
* [TF::VRA::CatalogSourceEntitlement](../resources/vra/TF-VRA-CatalogSourceEntitlement/docs/README.md)
* [TF::VRA::CloudAccountAws](../resources/vra/TF-VRA-CloudAccountAws/docs/README.md)
* [TF::VRA::CloudAccountAzure](../resources/vra/TF-VRA-CloudAccountAzure/docs/README.md)
* [TF::VRA::CloudAccountGcp](../resources/vra/TF-VRA-CloudAccountGcp/docs/README.md)
* [TF::VRA::CloudAccountNsxt](../resources/vra/TF-VRA-CloudAccountNsxt/docs/README.md)
* [TF::VRA::CloudAccountNsxv](../resources/vra/TF-VRA-CloudAccountNsxv/docs/README.md)
* [TF::VRA::CloudAccountVmc](../resources/vra/TF-VRA-CloudAccountVmc/docs/README.md)
* [TF::VRA::CloudAccountVsphere](../resources/vra/TF-VRA-CloudAccountVsphere/docs/README.md)
* [TF::VRA::ContentSource](../resources/vra/TF-VRA-ContentSource/docs/README.md)
* [TF::VRA::Deployment](../resources/vra/TF-VRA-Deployment/docs/README.md)
* [TF::VRA::FabricNetworkVsphere](../resources/vra/TF-VRA-FabricNetworkVsphere/docs/README.md)
* [TF::VRA::FlavorProfile](../resources/vra/TF-VRA-FlavorProfile/docs/README.md)
* [TF::VRA::ImageProfile](../resources/vra/TF-VRA-ImageProfile/docs/README.md)
* [TF::VRA::LoadBalancer](../resources/vra/TF-VRA-LoadBalancer/docs/README.md)
* [TF::VRA::Machine](../resources/vra/TF-VRA-Machine/docs/README.md)
* [TF::VRA::NetworkIpRange](../resources/vra/TF-VRA-NetworkIpRange/docs/README.md)
* [TF::VRA::NetworkProfile](../resources/vra/TF-VRA-NetworkProfile/docs/README.md)
* [TF::VRA::Network](../resources/vra/TF-VRA-Network/docs/README.md)
* [TF::VRA::Project](../resources/vra/TF-VRA-Project/docs/README.md)
* [TF::VRA::StorageProfileAws](../resources/vra/TF-VRA-StorageProfileAws/docs/README.md)
* [TF::VRA::StorageProfileAzure](../resources/vra/TF-VRA-StorageProfileAzure/docs/README.md)
* [TF::VRA::StorageProfileVsphere](../resources/vra/TF-VRA-StorageProfileVsphere/docs/README.md)
* [TF::VRA::StorageProfile](../resources/vra/TF-VRA-StorageProfile/docs/README.md)
* [TF::VRA::Zone](../resources/vra/TF-VRA-Zone/docs/README.md)