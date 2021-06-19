# Terraform Enterprise Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/tfe**. The below arguments may be included as the key/value or JSON properties in the secret:

* `hostname` - (Optional) The Terraform Cloud/Enterprise hostname to connect to.
  Defaults to `app.terraform.io`.
* `token` - (Optional) The token used to authenticate with Terraform Cloud/Enterprise.
  See [Authentication](#authentication) above for more information.
* `ssl_skip_verify` - (Optional) Whether or not to skip certificate verifications.
  Defaults to `false`.


## Supported Resources

* [TF::Tfe::AgentPool](../resources/tfe/TF-Tfe-AgentPool/docs/README.md)
* [TF::Tfe::AgentToken](../resources/tfe/TF-Tfe-AgentToken/docs/README.md)
* [TF::Tfe::NotificationConfiguration](../resources/tfe/TF-Tfe-NotificationConfiguration/docs/README.md)
* [TF::Tfe::OauthClient](../resources/tfe/TF-Tfe-OauthClient/docs/README.md)
* [TF::Tfe::OrganizationMembership](../resources/tfe/TF-Tfe-OrganizationMembership/docs/README.md)
* [TF::Tfe::OrganizationToken](../resources/tfe/TF-Tfe-OrganizationToken/docs/README.md)
* [TF::Tfe::Organization](../resources/tfe/TF-Tfe-Organization/docs/README.md)
* [TF::Tfe::PolicySetParameter](../resources/tfe/TF-Tfe-PolicySetParameter/docs/README.md)
* [TF::Tfe::PolicySet](../resources/tfe/TF-Tfe-PolicySet/docs/README.md)
* [TF::Tfe::RegistryModule](../resources/tfe/TF-Tfe-RegistryModule/docs/README.md)
* [TF::Tfe::RunTrigger](../resources/tfe/TF-Tfe-RunTrigger/docs/README.md)
* [TF::Tfe::SentinelPolicy](../resources/tfe/TF-Tfe-SentinelPolicy/docs/README.md)
* [TF::Tfe::SshKey](../resources/tfe/TF-Tfe-SshKey/docs/README.md)
* [TF::Tfe::TeamAccess](../resources/tfe/TF-Tfe-TeamAccess/docs/README.md)
* [TF::Tfe::TeamMember](../resources/tfe/TF-Tfe-TeamMember/docs/README.md)
* [TF::Tfe::TeamMembers](../resources/tfe/TF-Tfe-TeamMembers/docs/README.md)
* [TF::Tfe::TeamOrganizationMember](../resources/tfe/TF-Tfe-TeamOrganizationMember/docs/README.md)
* [TF::Tfe::TeamToken](../resources/tfe/TF-Tfe-TeamToken/docs/README.md)
* [TF::Tfe::Team](../resources/tfe/TF-Tfe-Team/docs/README.md)
* [TF::Tfe::Variable](../resources/tfe/TF-Tfe-Variable/docs/README.md)
* [TF::Tfe::Workspace](../resources/tfe/TF-Tfe-Workspace/docs/README.md)