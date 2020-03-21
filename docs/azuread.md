# Azure Active Directory Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/azuread**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `client_id` - (Optional) The Client ID which should be used. This can also be sourced from the `ARM_CLIENT_ID` Environment Variable.

* `environment` - (Optional) The Cloud Environment which be used. Possible values are `public`, `usgovernment`, `german` and `china`. Defaults to `public`.

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

When authenticating using Managed Service Identity, the following fields can be set:

* `msi_endpoint` - (Optional) The path to a custom endpoint for Managed Service Identity - in most circumstances this should be detected automatically. This can also be sourced from the `ARM_MSI_ENDPOINT` Environment Variable.

* `use_msi` - (Optional) Should Managed Service Identity be used for Authentication? This can also be sourced from the `ARM_USE_MSI` Environment Variable. Defaults to `false`.

More information on [how to configure a Service Principal using Managed Service Identity can be found in this guide](guides/managed_service_identity.html).

---

It's also possible to use multiple Provider blocks within a single Terraform configuration, for example to work with resources across multiple Azure Active Directory Environments - more information can be found [in the documentation for Providers](https://www.terraform.io/docs/configuration/providers.html#multiple-provider-instances).


## Supported Resources

* [Terraform::AzureAD::ApplicationPassword](../resources/azuread/Terraform-AzureAD-ApplicationPassword/docs/README.md)
* [Terraform::AzureAD::Application](../resources/azuread/Terraform-AzureAD-Application/docs/README.md)
* [Terraform::AzureAD::GroupMember](../resources/azuread/Terraform-AzureAD-GroupMember/docs/README.md)
* [Terraform::AzureAD::Group](../resources/azuread/Terraform-AzureAD-Group/docs/README.md)
* [Terraform::AzureAD::ServicePrincipalPassword](../resources/azuread/Terraform-AzureAD-ServicePrincipalPassword/docs/README.md)
* [Terraform::AzureAD::ServicePrincipal](../resources/azuread/Terraform-AzureAD-ServicePrincipal/docs/README.md)
* [Terraform::AzureAD::User](../resources/azuread/Terraform-AzureAD-User/docs/README.md)