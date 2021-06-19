# OpenNebula Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/opennebula**. The below arguments may be included as the key/value or JSON properties in the secret:

* `endpoint` - (Required) This is the URL of OpenNebula XML-RPC Endpoint API.
* `flow_endpoint` - (Optional) This is the OneFlow HTTP Endpoint API.
* `username` - (Required) This is the OpenNebula Username.
* `password` - (Required) This is the Opennebula Password of the username.


## Supported Resources

* [TF::OpenNebula::Acl](../resources/opennebula/TF-OpenNebula-Acl/docs/README.md)
* [TF::OpenNebula::Group](../resources/opennebula/TF-OpenNebula-Group/docs/README.md)
* [TF::OpenNebula::Image](../resources/opennebula/TF-OpenNebula-Image/docs/README.md)
* [TF::OpenNebula::SecurityGroup](../resources/opennebula/TF-OpenNebula-SecurityGroup/docs/README.md)
* [TF::OpenNebula::ServiceTemplate](../resources/opennebula/TF-OpenNebula-ServiceTemplate/docs/README.md)
* [TF::OpenNebula::Service](../resources/opennebula/TF-OpenNebula-Service/docs/README.md)
* [TF::OpenNebula::Template](../resources/opennebula/TF-OpenNebula-Template/docs/README.md)
* [TF::OpenNebula::User](../resources/opennebula/TF-OpenNebula-User/docs/README.md)
* [TF::OpenNebula::VirtualDataCenter](../resources/opennebula/TF-OpenNebula-VirtualDataCenter/docs/README.md)
* [TF::OpenNebula::VirtualMachineGroup](../resources/opennebula/TF-OpenNebula-VirtualMachineGroup/docs/README.md)
* [TF::OpenNebula::VirtualMachine](../resources/opennebula/TF-OpenNebula-VirtualMachine/docs/README.md)
* [TF::OpenNebula::VirtualNetwork](../resources/opennebula/TF-OpenNebula-VirtualNetwork/docs/README.md)