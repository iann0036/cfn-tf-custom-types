# Azure Stack Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/azurestack**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `arm_endpoint` - (Optional) The Azure Resource Manager Endpoint for your Azure Stack instance, for example `https://management.westus.mydomain.com`. This can also be sourceed from the `ARM_ENDPOINT` Environment Variable.

* `client_id` - (Optional) The Client ID which should be used. This can also be sourceed from the `ARM_CLIENT_ID` Environment Variable.

* `subscription_id` - (Optional) The Subscription ID which should be used. This can also be sourced from the `ARM_SUBSCRIPTION_ID` Environment Variable.

* `tenant_id` - (Optional) The Tenant ID which should be used. This can also be sourced from the `ARM_TENANT_ID` Environment Variable.

---

When authenticating as a Service Principal using a Client Certificate, the following fields can be set:

* `client_certificate_password` - (Optional) The password associated with the Client Certificate. This can also be sourced from the `ARM_CLIENT_CERTIFICATE_PASSWORD` Environment Variable.

* `client_certificate_path` - (Optional) The path to the Client Certificate associated with the Service Principal which should be used. This can also be sourced from the `ARM_CLIENT_CERTIFICATE_PATH` Environment Variable.

More information on [how to configure a Service Principal using a Client Certificate can be found in this guide](guides/service_principal_client_certificate.html).

---

When authenticating as a Service Principal using a Client Secret, the following fields can be set:

* `client_secret` - (Optional) The Client Secret which should be used. This can also be sourced from the `ARM_CLIENT_SECRET` Environment Variable.

More information on [how to configure a Service Principal using a Client Secret can be found in this guide](guides/service_principal_client_secret.html).

---

For some advanced scenarios, such as where more granular permissions are necessary - the following properties can be set:

* `skip_credentials_validation` - (Optional) Should the Azure Stack Provider skip verifying the credentials being used are valid? This can also be sourced from the `ARM_SKIP_CREDENTIALS_VALIDATION` Environment Variable. Defaults to `false`.

* `skip_provider_registration` - (Optional) Should the Azure Stack Provider skip registering any required Resource Providers? This can also be sourced from the `ARM_SKIP_PROVIDER_REGISTRATION` Environment Variable. Defaults to `false`.


## Supported Resources

* [Terraform::AzureStack::AvailabilitySet](../resources/azurestack/Terraform-AzureStack-AvailabilitySet/docs/README.md)
* [Terraform::AzureStack::DnsARecord](../resources/azurestack/Terraform-AzureStack-DnsARecord/docs/README.md)
* [Terraform::AzureStack::DnsZone](../resources/azurestack/Terraform-AzureStack-DnsZone/docs/README.md)
* [Terraform::AzureStack::LbBackendAddressPool](../resources/azurestack/Terraform-AzureStack-LbBackendAddressPool/docs/README.md)
* [Terraform::AzureStack::LbNatPool](../resources/azurestack/Terraform-AzureStack-LbNatPool/docs/README.md)
* [Terraform::AzureStack::LbNatRule](../resources/azurestack/Terraform-AzureStack-LbNatRule/docs/README.md)
* [Terraform::AzureStack::LbProbe](../resources/azurestack/Terraform-AzureStack-LbProbe/docs/README.md)
* [Terraform::AzureStack::LbRule](../resources/azurestack/Terraform-AzureStack-LbRule/docs/README.md)
* [Terraform::AzureStack::Lb](../resources/azurestack/Terraform-AzureStack-Lb/docs/README.md)
* [Terraform::AzureStack::LocalNetworkGateway](../resources/azurestack/Terraform-AzureStack-LocalNetworkGateway/docs/README.md)
* [Terraform::AzureStack::ManagedDisk](../resources/azurestack/Terraform-AzureStack-ManagedDisk/docs/README.md)
* [Terraform::AzureStack::NetworkInterface](../resources/azurestack/Terraform-AzureStack-NetworkInterface/docs/README.md)
* [Terraform::AzureStack::NetworkSecurityGroup](../resources/azurestack/Terraform-AzureStack-NetworkSecurityGroup/docs/README.md)
* [Terraform::AzureStack::NetworkSecurityRule](../resources/azurestack/Terraform-AzureStack-NetworkSecurityRule/docs/README.md)
* [Terraform::AzureStack::PublicIp](../resources/azurestack/Terraform-AzureStack-PublicIp/docs/README.md)
* [Terraform::AzureStack::ResourceGroup](../resources/azurestack/Terraform-AzureStack-ResourceGroup/docs/README.md)
* [Terraform::AzureStack::RouteTable](../resources/azurestack/Terraform-AzureStack-RouteTable/docs/README.md)
* [Terraform::AzureStack::Route](../resources/azurestack/Terraform-AzureStack-Route/docs/README.md)
* [Terraform::AzureStack::StorageAccount](../resources/azurestack/Terraform-AzureStack-StorageAccount/docs/README.md)
* [Terraform::AzureStack::StorageBlob](../resources/azurestack/Terraform-AzureStack-StorageBlob/docs/README.md)
* [Terraform::AzureStack::StorageContainer](../resources/azurestack/Terraform-AzureStack-StorageContainer/docs/README.md)
* [Terraform::AzureStack::Subnet](../resources/azurestack/Terraform-AzureStack-Subnet/docs/README.md)
* [Terraform::AzureStack::TemplateDeployment](../resources/azurestack/Terraform-AzureStack-TemplateDeployment/docs/README.md)
* [Terraform::AzureStack::VirtualMachineExtension](../resources/azurestack/Terraform-AzureStack-VirtualMachineExtension/docs/README.md)
* [Terraform::AzureStack::VirtualMachineScaleSet](../resources/azurestack/Terraform-AzureStack-VirtualMachineScaleSet/docs/README.md)
* [Terraform::AzureStack::VirtualMachine](../resources/azurestack/Terraform-AzureStack-VirtualMachine/docs/README.md)
* [Terraform::AzureStack::VirtualNetworkGatewayConnection](../resources/azurestack/Terraform-AzureStack-VirtualNetworkGatewayConnection/docs/README.md)
* [Terraform::AzureStack::VirtualNetworkGateway](../resources/azurestack/Terraform-AzureStack-VirtualNetworkGateway/docs/README.md)
* [Terraform::AzureStack::VirtualNetwork](../resources/azurestack/Terraform-AzureStack-VirtualNetwork/docs/README.md)