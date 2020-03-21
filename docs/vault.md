# Vault Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/vault**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `path` - (Required) The login path of the auth backend. For example, login with
  approle by setting this path to `auth/approle/login`. Additionally, some mounts use parameters
  in the URL, like with `userpass`: `auth/userpass/login/:username`. 

* `namespace` - (Optional) The path to the namespace that has the mounted auth method.
  This defaults to the root namespace. Cannot contain any leading or trailing slashes.
  *Available only for Vault Enterprise*

* `parameters` - (Optional) A map of key-value parameters to send when authenticating
  against the auth backend. Refer to [Vault API documentation](https://www.vaultproject.io/api/auth/index.html) for a particular auth method
  to see what can go here.


* `cert_file` - (Required) Path to a file on local disk that contains the
  PEM-encoded certificate to present to the server.

* `key_file` - (Required) Path to a file on local disk that contains the
  PEM-encoded private key for which the authentication certificate was issued.


## Supported Resources

* [Terraform::Vault::AlicloudAuthBackendRole](../resources/vault/Terraform-Vault-AlicloudAuthBackendRole/docs/README.md)
* [Terraform::Vault::ApproleAuthBackendLogin](../resources/vault/Terraform-Vault-ApproleAuthBackendLogin/docs/README.md)
* [Terraform::Vault::ApproleAuthBackendRoleSecretId](../resources/vault/Terraform-Vault-ApproleAuthBackendRoleSecretId/docs/README.md)
* [Terraform::Vault::ApproleAuthBackendRole](../resources/vault/Terraform-Vault-ApproleAuthBackendRole/docs/README.md)
* [Terraform::Vault::Audit](../resources/vault/Terraform-Vault-Audit/docs/README.md)
* [Terraform::Vault::AuthBackend](../resources/vault/Terraform-Vault-AuthBackend/docs/README.md)
* [Terraform::Vault::AwsAuthBackendCert](../resources/vault/Terraform-Vault-AwsAuthBackendCert/docs/README.md)
* [Terraform::Vault::AwsAuthBackendClient](../resources/vault/Terraform-Vault-AwsAuthBackendClient/docs/README.md)
* [Terraform::Vault::AwsAuthBackendIdentityWhitelist](../resources/vault/Terraform-Vault-AwsAuthBackendIdentityWhitelist/docs/README.md)
* [Terraform::Vault::AwsAuthBackendLogin](../resources/vault/Terraform-Vault-AwsAuthBackendLogin/docs/README.md)
* [Terraform::Vault::AwsAuthBackendRoleTag](../resources/vault/Terraform-Vault-AwsAuthBackendRoleTag/docs/README.md)
* [Terraform::Vault::AwsAuthBackendRole](../resources/vault/Terraform-Vault-AwsAuthBackendRole/docs/README.md)
* [Terraform::Vault::AwsAuthBackendRoletagBlacklist](../resources/vault/Terraform-Vault-AwsAuthBackendRoletagBlacklist/docs/README.md)
* [Terraform::Vault::AwsAuthBackendStsRole](../resources/vault/Terraform-Vault-AwsAuthBackendStsRole/docs/README.md)
* [Terraform::Vault::AwsSecretBackendRole](../resources/vault/Terraform-Vault-AwsSecretBackendRole/docs/README.md)
* [Terraform::Vault::AwsSecretBackend](../resources/vault/Terraform-Vault-AwsSecretBackend/docs/README.md)
* [Terraform::Vault::AzureAuthBackendConfig](../resources/vault/Terraform-Vault-AzureAuthBackendConfig/docs/README.md)
* [Terraform::Vault::AzureAuthBackendRole](../resources/vault/Terraform-Vault-AzureAuthBackendRole/docs/README.md)
* [Terraform::Vault::AzureSecretBackendRole](../resources/vault/Terraform-Vault-AzureSecretBackendRole/docs/README.md)
* [Terraform::Vault::AzureSecretBackend](../resources/vault/Terraform-Vault-AzureSecretBackend/docs/README.md)
* [Terraform::Vault::CertAuthBackendRole](../resources/vault/Terraform-Vault-CertAuthBackendRole/docs/README.md)
* [Terraform::Vault::ConsulSecretBackendRole](../resources/vault/Terraform-Vault-ConsulSecretBackendRole/docs/README.md)
* [Terraform::Vault::ConsulSecretBackend](../resources/vault/Terraform-Vault-ConsulSecretBackend/docs/README.md)
* [Terraform::Vault::DatabaseSecretBackendConnection](../resources/vault/Terraform-Vault-DatabaseSecretBackendConnection/docs/README.md)
* [Terraform::Vault::DatabaseSecretBackendRole](../resources/vault/Terraform-Vault-DatabaseSecretBackendRole/docs/README.md)
* [Terraform::Vault::DatabaseSecretBackendStaticRole](../resources/vault/Terraform-Vault-DatabaseSecretBackendStaticRole/docs/README.md)
* [Terraform::Vault::EgpPolicy](../resources/vault/Terraform-Vault-EgpPolicy/docs/README.md)
* [Terraform::Vault::GcpAuthBackendRole](../resources/vault/Terraform-Vault-GcpAuthBackendRole/docs/README.md)
* [Terraform::Vault::GcpAuthBackend](../resources/vault/Terraform-Vault-GcpAuthBackend/docs/README.md)
* [Terraform::Vault::GcpSecretBackend](../resources/vault/Terraform-Vault-GcpSecretBackend/docs/README.md)
* [Terraform::Vault::GcpSecretRoleset](../resources/vault/Terraform-Vault-GcpSecretRoleset/docs/README.md)
* [Terraform::Vault::GenericEndpoint](../resources/vault/Terraform-Vault-GenericEndpoint/docs/README.md)
* [Terraform::Vault::GenericSecret](../resources/vault/Terraform-Vault-GenericSecret/docs/README.md)
* [Terraform::Vault::GithubAuthBackend](../resources/vault/Terraform-Vault-GithubAuthBackend/docs/README.md)
* [Terraform::Vault::GithubTeam](../resources/vault/Terraform-Vault-GithubTeam/docs/README.md)
* [Terraform::Vault::GithubUser](../resources/vault/Terraform-Vault-GithubUser/docs/README.md)
* [Terraform::Vault::IdentityEntityAlias](../resources/vault/Terraform-Vault-IdentityEntityAlias/docs/README.md)
* [Terraform::Vault::IdentityEntityPolicies](../resources/vault/Terraform-Vault-IdentityEntityPolicies/docs/README.md)
* [Terraform::Vault::IdentityEntity](../resources/vault/Terraform-Vault-IdentityEntity/docs/README.md)
* [Terraform::Vault::IdentityGroupAlias](../resources/vault/Terraform-Vault-IdentityGroupAlias/docs/README.md)
* [Terraform::Vault::IdentityGroupPolicies](../resources/vault/Terraform-Vault-IdentityGroupPolicies/docs/README.md)
* [Terraform::Vault::IdentityGroup](../resources/vault/Terraform-Vault-IdentityGroup/docs/README.md)
* [Terraform::Vault::IdentityOidcKeyAllowedClientId](../resources/vault/Terraform-Vault-IdentityOidcKeyAllowedClientId/docs/README.md)
* [Terraform::Vault::IdentityOidcKey](../resources/vault/Terraform-Vault-IdentityOidcKey/docs/README.md)
* [Terraform::Vault::IdentityOidcRole](../resources/vault/Terraform-Vault-IdentityOidcRole/docs/README.md)
* [Terraform::Vault::IdentityOidc](../resources/vault/Terraform-Vault-IdentityOidc/docs/README.md)
* [Terraform::Vault::JwtAuthBackendRole](../resources/vault/Terraform-Vault-JwtAuthBackendRole/docs/README.md)
* [Terraform::Vault::JwtAuthBackend](../resources/vault/Terraform-Vault-JwtAuthBackend/docs/README.md)
* [Terraform::Vault::KubernetesAuthBackendConfig](../resources/vault/Terraform-Vault-KubernetesAuthBackendConfig/docs/README.md)
* [Terraform::Vault::KubernetesAuthBackendRole](../resources/vault/Terraform-Vault-KubernetesAuthBackendRole/docs/README.md)
* [Terraform::Vault::LdapAuthBackendGroup](../resources/vault/Terraform-Vault-LdapAuthBackendGroup/docs/README.md)
* [Terraform::Vault::LdapAuthBackendUser](../resources/vault/Terraform-Vault-LdapAuthBackendUser/docs/README.md)
* [Terraform::Vault::LdapAuthBackend](../resources/vault/Terraform-Vault-LdapAuthBackend/docs/README.md)
* [Terraform::Vault::Mfa-duo](../resources/vault/Terraform-Vault-Mfa-duo/docs/README.md)
* [Terraform::Vault::Mount](../resources/vault/Terraform-Vault-Mount/docs/README.md)
* [Terraform::Vault::Namespace](../resources/vault/Terraform-Vault-Namespace/docs/README.md)
* [Terraform::Vault::OktaAuthBackendGroup](../resources/vault/Terraform-Vault-OktaAuthBackendGroup/docs/README.md)
* [Terraform::Vault::OktaAuthBackendUser](../resources/vault/Terraform-Vault-OktaAuthBackendUser/docs/README.md)
* [Terraform::Vault::OktaAuthBackend](../resources/vault/Terraform-Vault-OktaAuthBackend/docs/README.md)
* [Terraform::Vault::PkiSecretBackendCert](../resources/vault/Terraform-Vault-PkiSecretBackendCert/docs/README.md)
* [Terraform::Vault::PkiSecretBackendConfigCa](../resources/vault/Terraform-Vault-PkiSecretBackendConfigCa/docs/README.md)
* [Terraform::Vault::PkiSecretBackendConfigUrls](../resources/vault/Terraform-Vault-PkiSecretBackendConfigUrls/docs/README.md)
* [Terraform::Vault::PkiSecretBackendCrlConfig](../resources/vault/Terraform-Vault-PkiSecretBackendCrlConfig/docs/README.md)
* [Terraform::Vault::PkiSecretBackendIntermediateCertRequest](../resources/vault/Terraform-Vault-PkiSecretBackendIntermediateCertRequest/docs/README.md)
* [Terraform::Vault::PkiSecretBackendIntermediateSetSigned](../resources/vault/Terraform-Vault-PkiSecretBackendIntermediateSetSigned/docs/README.md)
* [Terraform::Vault::PkiSecretBackendRole](../resources/vault/Terraform-Vault-PkiSecretBackendRole/docs/README.md)
* [Terraform::Vault::PkiSecretBackendRootCert](../resources/vault/Terraform-Vault-PkiSecretBackendRootCert/docs/README.md)
* [Terraform::Vault::PkiSecretBackendRootSignIntermediate](../resources/vault/Terraform-Vault-PkiSecretBackendRootSignIntermediate/docs/README.md)
* [Terraform::Vault::PkiSecretBackendSign](../resources/vault/Terraform-Vault-PkiSecretBackendSign/docs/README.md)
* [Terraform::Vault::PkiSecretBackend](../resources/vault/Terraform-Vault-PkiSecretBackend/docs/README.md)
* [Terraform::Vault::Policy](../resources/vault/Terraform-Vault-Policy/docs/README.md)
* [Terraform::Vault::RabbitmqSecretBackendRole](../resources/vault/Terraform-Vault-RabbitmqSecretBackendRole/docs/README.md)
* [Terraform::Vault::RabbitmqSecretBackend](../resources/vault/Terraform-Vault-RabbitmqSecretBackend/docs/README.md)
* [Terraform::Vault::RgpPolicy](../resources/vault/Terraform-Vault-RgpPolicy/docs/README.md)
* [Terraform::Vault::SshSecretBackendCa](../resources/vault/Terraform-Vault-SshSecretBackendCa/docs/README.md)
* [Terraform::Vault::SshSecretBackendRole](../resources/vault/Terraform-Vault-SshSecretBackendRole/docs/README.md)
* [Terraform::Vault::TokenAuthBackendRole](../resources/vault/Terraform-Vault-TokenAuthBackendRole/docs/README.md)
* [Terraform::Vault::Token](../resources/vault/Terraform-Vault-Token/docs/README.md)
* [Terraform::Vault::TransitSecretBackendCacheConfig](../resources/vault/Terraform-Vault-TransitSecretBackendCacheConfig/docs/README.md)
* [Terraform::Vault::TransitSecretBackendKey](../resources/vault/Terraform-Vault-TransitSecretBackendKey/docs/README.md)