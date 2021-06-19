# NetApp ElementSW Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/netapp-elementsw**. The below arguments may be included as the key/value or JSON properties in the secret:

* `username` - (Required) This is the username for ElementSW API operations.
* `password` - (Required) This is the password for ElementSW API operations.
* `elementsw_server` - (Required) This is the ElementSW cluster name for ElementSW 
  API operations.
* `api_version` - (Required) This is the ElementSW cluster version for ElementSW
  API operations.


## Supported Resources

* [TF::NetAppElementSW::ElementswAccount](../resources/netapp-elementsw/TF-NetAppElementSW-Account/docs/README.md)
* [TF::NetAppElementSW::ElementswInitiator](../resources/netapp-elementsw/TF-NetAppElementSW-Initiator/docs/README.md)
* [TF::NetAppElementSW::ElementswVolumeAccessGroup](../resources/netapp-elementsw/TF-NetAppElementSW-VolumeAccessGroup/docs/README.md)
* [TF::NetAppElementSW::ElementswVolume](../resources/netapp-elementsw/TF-NetAppElementSW-Volume/docs/README.md)