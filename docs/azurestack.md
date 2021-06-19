# Azure Stack Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/azurestack**. The below arguments may be included as the key/value or JSON properties in the secret:

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

* [TF::AzureStack::AvailabilitySet](../resources/azurestack/TF-AzureStack-AvailabilitySet/docs/README.md)
* [TF::AzureStack::DnsARecord](../resources/azurestack/TF-AzureStack-DnsARecord/docs/README.md)
* [TF::AzureStack::DnsZone](../resources/azurestack/TF-AzureStack-DnsZone/docs/README.md)
* [TF::AzureStack::LbBackendAddressPool](../resources/azurestack/TF-AzureStack-LbBackendAddressPool/docs/README.md)
* [TF::AzureStack::LbNatPool](../resources/azurestack/TF-AzureStack-LbNatPool/docs/README.md)
* [TF::AzureStack::LbNatRule](../resources/azurestack/TF-AzureStack-LbNatRule/docs/README.md)
* [TF::AzureStack::LbProbe](../resources/azurestack/TF-AzureStack-LbProbe/docs/README.md)
* [TF::AzureStack::LbRule](../resources/azurestack/TF-AzureStack-LbRule/docs/README.md)
* [TF::AzureStack::Lb](../resources/azurestack/TF-AzureStack-Lb/docs/README.md)
* [TF::AzureStack::LocalNetworkGateway](../resources/azurestack/TF-AzureStack-LocalNetworkGateway/docs/README.md)
* [TF::AzureStack::ManagedDisk](../resources/azurestack/TF-AzureStack-ManagedDisk/docs/README.md)
* [TF::AzureStack::NetworkInterface](../resources/azurestack/TF-AzureStack-NetworkInterface/docs/README.md)
* [TF::AzureStack::NetworkSecurityGroup](../resources/azurestack/TF-AzureStack-NetworkSecurityGroup/docs/README.md)
* [TF::AzureStack::NetworkSecurityRule](../resources/azurestack/TF-AzureStack-NetworkSecurityRule/docs/README.md)
* [TF::AzureStack::PublicIp](../resources/azurestack/TF-AzureStack-PublicIp/docs/README.md)
* [TF::AzureStack::ResourceGroup](../resources/azurestack/TF-AzureStack-ResourceGroup/docs/README.md)
* [TF::AzureStack::RouteTable](../resources/azurestack/TF-AzureStack-RouteTable/docs/README.md)
* [TF::AzureStack::Route](../resources/azurestack/TF-AzureStack-Route/docs/README.md)
* [TF::AzureStack::StorageAccount](../resources/azurestack/TF-AzureStack-StorageAccount/docs/README.md)
* [TF::AzureStack::StorageBlob](../resources/azurestack/TF-AzureStack-StorageBlob/docs/README.md)
* [TF::AzureStack::StorageContainer](../resources/azurestack/TF-AzureStack-StorageContainer/docs/README.md)
* [TF::AzureStack::Subnet](../resources/azurestack/TF-AzureStack-Subnet/docs/README.md)
* [TF::AzureStack::TemplateDeployment](../resources/azurestack/TF-AzureStack-TemplateDeployment/docs/README.md)
* [TF::AzureStack::VirtualMachineExtension](../resources/azurestack/TF-AzureStack-VirtualMachineExtension/docs/README.md)
* [TF::AzureStack::VirtualMachineScaleSet](../resources/azurestack/TF-AzureStack-VirtualMachineScaleSet/docs/README.md)
* [TF::AzureStack::VirtualMachine](../resources/azurestack/TF-AzureStack-VirtualMachine/docs/README.md)
* [TF::AzureStack::VirtualNetworkGatewayConnection](../resources/azurestack/TF-AzureStack-VirtualNetworkGatewayConnection/docs/README.md)
* [TF::AzureStack::VirtualNetworkGateway](../resources/azurestack/TF-AzureStack-VirtualNetworkGateway/docs/README.md)
* [TF::AzureStack::VirtualNetwork](../resources/azurestack/TF-AzureStack-VirtualNetwork/docs/README.md)