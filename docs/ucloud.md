# UCloud Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/ucloud**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `public_key` - (Required) This is the UCloud public key.

* `private_key` - (Required) This is the UCloud private key.

* `region` - (Required) This is the UCloud region.

* `project_id` - (Required) This is the UCloud project id.

* `max_retries` - (Optional) This is the max retry attempts number. Default max retry attempts number is `0`.

* `insecure` - (Optional) This is a switch to disable/enable https.  (Default: `false`, means enable https). 
 ~> **Note** this argument conflicts with `base_url`. If this is not set and a profile is specified, `~/.ucloud/credential.json` will be used.

* `base_url` - (Optional) This is the base url.(Default: `https://api.ucloud.cn`).
 ~> **Note** this argument conflicts with `insecure`.


## Supported Resources

* [Terraform::UCloud::DbInstance](../resources/ucloud/Terraform-UCloud-DbInstance/docs/README.md)
* [Terraform::UCloud::DiskAttachment](../resources/ucloud/Terraform-UCloud-DiskAttachment/docs/README.md)
* [Terraform::UCloud::Disk](../resources/ucloud/Terraform-UCloud-Disk/docs/README.md)
* [Terraform::UCloud::EipAssociation](../resources/ucloud/Terraform-UCloud-EipAssociation/docs/README.md)
* [Terraform::UCloud::Eip](../resources/ucloud/Terraform-UCloud-Eip/docs/README.md)
* [Terraform::UCloud::Instance](../resources/ucloud/Terraform-UCloud-Instance/docs/README.md)
* [Terraform::UCloud::IsolationGroup](../resources/ucloud/Terraform-UCloud-IsolationGroup/docs/README.md)
* [Terraform::UCloud::LbAttachment](../resources/ucloud/Terraform-UCloud-LbAttachment/docs/README.md)
* [Terraform::UCloud::LbListener](../resources/ucloud/Terraform-UCloud-LbListener/docs/README.md)
* [Terraform::UCloud::LbRule](../resources/ucloud/Terraform-UCloud-LbRule/docs/README.md)
* [Terraform::UCloud::LbSsl](../resources/ucloud/Terraform-UCloud-LbSsl/docs/README.md)
* [Terraform::UCloud::Lb](../resources/ucloud/Terraform-UCloud-Lb/docs/README.md)
* [Terraform::UCloud::MemcacheInstance](../resources/ucloud/Terraform-UCloud-MemcacheInstance/docs/README.md)
* [Terraform::UCloud::NatGatewayRule](../resources/ucloud/Terraform-UCloud-NatGatewayRule/docs/README.md)
* [Terraform::UCloud::NatGateway](../resources/ucloud/Terraform-UCloud-NatGateway/docs/README.md)
* [Terraform::UCloud::RedisInstance](../resources/ucloud/Terraform-UCloud-RedisInstance/docs/README.md)
* [Terraform::UCloud::SecurityGroup](../resources/ucloud/Terraform-UCloud-SecurityGroup/docs/README.md)
* [Terraform::UCloud::Subnet](../resources/ucloud/Terraform-UCloud-Subnet/docs/README.md)
* [Terraform::UCloud::UdpnConnection](../resources/ucloud/Terraform-UCloud-UdpnConnection/docs/README.md)
* [Terraform::UCloud::Vip](../resources/ucloud/Terraform-UCloud-Vip/docs/README.md)
* [Terraform::UCloud::VpcPeeringConnection](../resources/ucloud/Terraform-UCloud-VpcPeeringConnection/docs/README.md)
* [Terraform::UCloud::Vpc](../resources/ucloud/Terraform-UCloud-Vpc/docs/README.md)
* [Terraform::UCloud::VpnConnection](../resources/ucloud/Terraform-UCloud-VpnConnection/docs/README.md)
* [Terraform::UCloud::VpnCustomerGateway](../resources/ucloud/Terraform-UCloud-VpnCustomerGateway/docs/README.md)
* [Terraform::UCloud::VpnGateway](../resources/ucloud/Terraform-UCloud-VpnGateway/docs/README.md)