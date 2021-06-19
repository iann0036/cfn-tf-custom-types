# Azure Active Directory Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/azuread**. The below arguments may be included as the key/value or JSON properties in the secret:

* `client_id` - (Optional) The Client ID which should be used when authenticating as a service principal. This can also be sourced from the `ARM_CLIENT_ID` Environment Variable.

* `environment` - (Optional) The Cloud Environment which be used. Possible values are `public`, `usgovernment`, `german` and `china`. Defaults to `public`.

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


## Supported Resources

* [TF::AzureAD::ApplicationAppRole](../resources/azuread/TF-AzureAD-ApplicationAppRole/docs/README.md)
* [TF::AzureAD::ApplicationCertificate](../resources/azuread/TF-AzureAD-ApplicationCertificate/docs/README.md)
* [TF::AzureAD::ApplicationOauth2PermissionScope](../resources/azuread/TF-AzureAD-ApplicationOauth2PermissionScope/docs/README.md)
* [TF::AzureAD::ApplicationOauth2Permission](../resources/azuread/TF-AzureAD-ApplicationOauth2Permission/docs/README.md)
* [TF::AzureAD::ApplicationPassword](../resources/azuread/TF-AzureAD-ApplicationPassword/docs/README.md)
* [TF::AzureAD::Application](../resources/azuread/TF-AzureAD-Application/docs/README.md)
* [TF::AzureAD::GroupMember](../resources/azuread/TF-AzureAD-GroupMember/docs/README.md)
* [TF::AzureAD::Group](../resources/azuread/TF-AzureAD-Group/docs/README.md)
* [TF::AzureAD::ServicePrincipalCertificate](../resources/azuread/TF-AzureAD-ServicePrincipalCertificate/docs/README.md)
* [TF::AzureAD::ServicePrincipalPassword](../resources/azuread/TF-AzureAD-ServicePrincipalPassword/docs/README.md)
* [TF::AzureAD::ServicePrincipal](../resources/azuread/TF-AzureAD-ServicePrincipal/docs/README.md)
* [TF::AzureAD::User](../resources/azuread/TF-AzureAD-User/docs/README.md)