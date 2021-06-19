# Vault Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/vault**. The below arguments may be included as the key/value or JSON properties in the secret:

* `path` - (Required) The login path of the auth backend. For example, login with
  approle by setting this path to `auth/approle/login`. Additionally, some mounts use parameters
  in the URL, like with `userpass`: `auth/userpass/login/:username`.

* `namespace` - (Optional) The path to the namespace that has the mounted auth method.
  This defaults to the root namespace. Cannot contain any leading or trailing slashes.
  *Available only for Vault Enterprise*

* `method` - (Optional) When configured, will enable auth method specific operations.
  For example, when set to `aws`, the provider will automatically sign login requests
  for AWS authentication. Valid values include: `aws`.

* `parameters` - (Optional) A map of key-value parameters to send when authenticating
  against the auth backend. Refer to [Vault API documentation](https://www.vaultproject.io/api-docs/auth) for a particular auth method
  to see what can go here.


* `cert_file` - (Required) Path to a file on local disk that contains the
  PEM-encoded certificate to present to the server.

* `key_file` - (Required) Path to a file on local disk that contains the
  PEM-encoded private key for which the authentication certificate was issued.


* `name` - (Required) The name of the header.

* `value` - (Required) The value of the header.


## Supported Resources

* [TF::Vault::AdSecretBackend](../resources/vault/TF-Vault-AdSecretBackend/docs/README.md)
* [TF::Vault::AdSecretLibrary](../resources/vault/TF-Vault-AdSecretLibrary/docs/README.md)
* [TF::Vault::AdSecretRole](../resources/vault/TF-Vault-AdSecretRole/docs/README.md)
* [TF::Vault::AlicloudAuthBackendRole](../resources/vault/TF-Vault-AlicloudAuthBackendRole/docs/README.md)
* [TF::Vault::ApproleAuthBackendLogin](../resources/vault/TF-Vault-ApproleAuthBackendLogin/docs/README.md)
* [TF::Vault::ApproleAuthBackendRoleSecretId](../resources/vault/TF-Vault-ApproleAuthBackendRoleSecretId/docs/README.md)
* [TF::Vault::ApproleAuthBackendRole](../resources/vault/TF-Vault-ApproleAuthBackendRole/docs/README.md)
* [TF::Vault::Audit](../resources/vault/TF-Vault-Audit/docs/README.md)
* [TF::Vault::AuthBackend](../resources/vault/TF-Vault-AuthBackend/docs/README.md)
* [TF::Vault::AwsAuthBackendCert](../resources/vault/TF-Vault-AwsAuthBackendCert/docs/README.md)
* [TF::Vault::AwsAuthBackendClient](../resources/vault/TF-Vault-AwsAuthBackendClient/docs/README.md)
* [TF::Vault::AwsAuthBackendIdentityWhitelist](../resources/vault/TF-Vault-AwsAuthBackendIdentityWhitelist/docs/README.md)
* [TF::Vault::AwsAuthBackendLogin](../resources/vault/TF-Vault-AwsAuthBackendLogin/docs/README.md)
* [TF::Vault::AwsAuthBackendRoleTag](../resources/vault/TF-Vault-AwsAuthBackendRoleTag/docs/README.md)
* [TF::Vault::AwsAuthBackendRole](../resources/vault/TF-Vault-AwsAuthBackendRole/docs/README.md)
* [TF::Vault::AwsAuthBackendRoletagBlacklist](../resources/vault/TF-Vault-AwsAuthBackendRoletagBlacklist/docs/README.md)
* [TF::Vault::AwsAuthBackendStsRole](../resources/vault/TF-Vault-AwsAuthBackendStsRole/docs/README.md)
* [TF::Vault::AwsSecretBackendRole](../resources/vault/TF-Vault-AwsSecretBackendRole/docs/README.md)
* [TF::Vault::AwsSecretBackend](../resources/vault/TF-Vault-AwsSecretBackend/docs/README.md)
* [TF::Vault::AzureAuthBackendConfig](../resources/vault/TF-Vault-AzureAuthBackendConfig/docs/README.md)
* [TF::Vault::AzureAuthBackendRole](../resources/vault/TF-Vault-AzureAuthBackendRole/docs/README.md)
* [TF::Vault::AzureSecretBackendRole](../resources/vault/TF-Vault-AzureSecretBackendRole/docs/README.md)
* [TF::Vault::AzureSecretBackend](../resources/vault/TF-Vault-AzureSecretBackend/docs/README.md)
* [TF::Vault::CertAuthBackendRole](../resources/vault/TF-Vault-CertAuthBackendRole/docs/README.md)
* [TF::Vault::ConsulSecretBackendRole](../resources/vault/TF-Vault-ConsulSecretBackendRole/docs/README.md)
* [TF::Vault::ConsulSecretBackend](../resources/vault/TF-Vault-ConsulSecretBackend/docs/README.md)
* [TF::Vault::DatabaseSecretBackendConnection](../resources/vault/TF-Vault-DatabaseSecretBackendConnection/docs/README.md)
* [TF::Vault::DatabaseSecretBackendRole](../resources/vault/TF-Vault-DatabaseSecretBackendRole/docs/README.md)
* [TF::Vault::DatabaseSecretBackendStaticRole](../resources/vault/TF-Vault-DatabaseSecretBackendStaticRole/docs/README.md)
* [TF::Vault::EgpPolicy](../resources/vault/TF-Vault-EgpPolicy/docs/README.md)
* [TF::Vault::GcpAuthBackendRole](../resources/vault/TF-Vault-GcpAuthBackendRole/docs/README.md)
* [TF::Vault::GcpAuthBackend](../resources/vault/TF-Vault-GcpAuthBackend/docs/README.md)
* [TF::Vault::GcpSecretBackend](../resources/vault/TF-Vault-GcpSecretBackend/docs/README.md)
* [TF::Vault::GcpSecretRoleset](../resources/vault/TF-Vault-GcpSecretRoleset/docs/README.md)
* [TF::Vault::GenericEndpoint](../resources/vault/TF-Vault-GenericEndpoint/docs/README.md)
* [TF::Vault::GenericSecret](../resources/vault/TF-Vault-GenericSecret/docs/README.md)
* [TF::Vault::GithubAuthBackend](../resources/vault/TF-Vault-GithubAuthBackend/docs/README.md)
* [TF::Vault::GithubTeam](../resources/vault/TF-Vault-GithubTeam/docs/README.md)
* [TF::Vault::GithubUser](../resources/vault/TF-Vault-GithubUser/docs/README.md)
* [TF::Vault::IdentityEntityAlias](../resources/vault/TF-Vault-IdentityEntityAlias/docs/README.md)
* [TF::Vault::IdentityEntityPolicies](../resources/vault/TF-Vault-IdentityEntityPolicies/docs/README.md)
* [TF::Vault::IdentityEntity](../resources/vault/TF-Vault-IdentityEntity/docs/README.md)
* [TF::Vault::IdentityGroupAlias](../resources/vault/TF-Vault-IdentityGroupAlias/docs/README.md)
* [TF::Vault::IdentityGroupMemberEntityIds](../resources/vault/TF-Vault-IdentityGroupMemberEntityIds/docs/README.md)
* [TF::Vault::IdentityGroupPolicies](../resources/vault/TF-Vault-IdentityGroupPolicies/docs/README.md)
* [TF::Vault::IdentityGroup](../resources/vault/TF-Vault-IdentityGroup/docs/README.md)
* [TF::Vault::IdentityOidcKeyAllowedClientId](../resources/vault/TF-Vault-IdentityOidcKeyAllowedClientId/docs/README.md)
* [TF::Vault::IdentityOidcKey](../resources/vault/TF-Vault-IdentityOidcKey/docs/README.md)
* [TF::Vault::IdentityOidcRole](../resources/vault/TF-Vault-IdentityOidcRole/docs/README.md)
* [TF::Vault::IdentityOidc](../resources/vault/TF-Vault-IdentityOidc/docs/README.md)
* [TF::Vault::JwtAuthBackendRole](../resources/vault/TF-Vault-JwtAuthBackendRole/docs/README.md)
* [TF::Vault::JwtAuthBackend](../resources/vault/TF-Vault-JwtAuthBackend/docs/README.md)
* [TF::Vault::KubernetesAuthBackendConfig](../resources/vault/TF-Vault-KubernetesAuthBackendConfig/docs/README.md)
* [TF::Vault::KubernetesAuthBackendRole](../resources/vault/TF-Vault-KubernetesAuthBackendRole/docs/README.md)
* [TF::Vault::LdapAuthBackendGroup](../resources/vault/TF-Vault-LdapAuthBackendGroup/docs/README.md)
* [TF::Vault::LdapAuthBackendUser](../resources/vault/TF-Vault-LdapAuthBackendUser/docs/README.md)
* [TF::Vault::LdapAuthBackend](../resources/vault/TF-Vault-LdapAuthBackend/docs/README.md)
* [TF::Vault::MfaDuo](../resources/vault/TF-Vault-MfaDuo/docs/README.md)
* [TF::Vault::Mount](../resources/vault/TF-Vault-Mount/docs/README.md)
* [TF::Vault::Namespace](../resources/vault/TF-Vault-Namespace/docs/README.md)
* [TF::Vault::NomadSecretBackend](../resources/vault/TF-Vault-NomadSecretBackend/docs/README.md)
* [TF::Vault::NomadSecretRole](../resources/vault/TF-Vault-NomadSecretRole/docs/README.md)
* [TF::Vault::OktaAuthBackendGroup](../resources/vault/TF-Vault-OktaAuthBackendGroup/docs/README.md)
* [TF::Vault::OktaAuthBackendUser](../resources/vault/TF-Vault-OktaAuthBackendUser/docs/README.md)
* [TF::Vault::OktaAuthBackend](../resources/vault/TF-Vault-OktaAuthBackend/docs/README.md)
* [TF::Vault::PasswordPolicy](../resources/vault/TF-Vault-PasswordPolicy/docs/README.md)
* [TF::Vault::PkiSecretBackendCert](../resources/vault/TF-Vault-PkiSecretBackendCert/docs/README.md)
* [TF::Vault::PkiSecretBackendConfigCa](../resources/vault/TF-Vault-PkiSecretBackendConfigCa/docs/README.md)
* [TF::Vault::PkiSecretBackendConfigUrls](../resources/vault/TF-Vault-PkiSecretBackendConfigUrls/docs/README.md)
* [TF::Vault::PkiSecretBackendCrlConfig](../resources/vault/TF-Vault-PkiSecretBackendCrlConfig/docs/README.md)
* [TF::Vault::PkiSecretBackendIntermediateCertRequest](../resources/vault/TF-Vault-PkiSecretBackendIntermediateCertRequest/docs/README.md)
* [TF::Vault::PkiSecretBackendIntermediateSetSigned](../resources/vault/TF-Vault-PkiSecretBackendIntermediateSetSigned/docs/README.md)
* [TF::Vault::PkiSecretBackendRole](../resources/vault/TF-Vault-PkiSecretBackendRole/docs/README.md)
* [TF::Vault::PkiSecretBackendRootCert](../resources/vault/TF-Vault-PkiSecretBackendRootCert/docs/README.md)
* [TF::Vault::PkiSecretBackendRootSignIntermediate](../resources/vault/TF-Vault-PkiSecretBackendRootSignIntermediate/docs/README.md)
* [TF::Vault::PkiSecretBackendSign](../resources/vault/TF-Vault-PkiSecretBackendSign/docs/README.md)
* [TF::Vault::PkiSecretBackend](../resources/vault/TF-Vault-PkiSecretBackend/docs/README.md)
* [TF::Vault::Policy](../resources/vault/TF-Vault-Policy/docs/README.md)
* [TF::Vault::QuotaRateLimit](../resources/vault/TF-Vault-QuotaRateLimit/docs/README.md)
* [TF::Vault::RabbitmqSecretBackendRole](../resources/vault/TF-Vault-RabbitmqSecretBackendRole/docs/README.md)
* [TF::Vault::RabbitmqSecretBackend](../resources/vault/TF-Vault-RabbitmqSecretBackend/docs/README.md)
* [TF::Vault::RgpPolicy](../resources/vault/TF-Vault-RgpPolicy/docs/README.md)
* [TF::Vault::SshSecretBackendCa](../resources/vault/TF-Vault-SshSecretBackendCa/docs/README.md)
* [TF::Vault::SshSecretBackendRole](../resources/vault/TF-Vault-SshSecretBackendRole/docs/README.md)
* [TF::Vault::TerraformCloudSecretBackend](../resources/vault/TF-Vault-TerraformCloudSecretBackend/docs/README.md)
* [TF::Vault::TerraformCloudSecretCreds](../resources/vault/TF-Vault-TerraformCloudSecretCreds/docs/README.md)
* [TF::Vault::TerraformCloudSecretRole](../resources/vault/TF-Vault-TerraformCloudSecretRole/docs/README.md)
* [TF::Vault::TokenAuthBackendRole](../resources/vault/TF-Vault-TokenAuthBackendRole/docs/README.md)
* [TF::Vault::Token](../resources/vault/TF-Vault-Token/docs/README.md)
* [TF::Vault::TransformAlphabet](../resources/vault/TF-Vault-TransformAlphabet/docs/README.md)
* [TF::Vault::TransformRole](../resources/vault/TF-Vault-TransformRole/docs/README.md)
* [TF::Vault::TransformTemplate](../resources/vault/TF-Vault-TransformTemplate/docs/README.md)
* [TF::Vault::TransformTransformation](../resources/vault/TF-Vault-TransformTransformation/docs/README.md)
* [TF::Vault::TransitSecretBackendKey](../resources/vault/TF-Vault-TransitSecretBackendKey/docs/README.md)
* [TF::Vault::TransitSecretCacheConfig](../resources/vault/TF-Vault-TransitSecretCacheConfig/docs/README.md)