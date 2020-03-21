# Terraform Enterprise Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/tfe**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `hostname` - (Optional) The Terraform Enterprise hostname to connect to.
  Defaults to `app.terraform.io`.
* `token` - (Optional) The token used to authenticate with Terraform Enterprise.
  Only set this argument when running in a Terraform Enterprise workspace; for
  CLI usage, omit the token from the configuration and set it as `credentials`
  in the [CLI config file](/docs/commands/cli-config. See [Authentication](#authentication)
  above for more.


## Supported Resources

* [Terraform::Tfe::NotificationConfiguration](../resources/tfe/Terraform-Tfe-NotificationConfiguration/docs/README.md)
* [Terraform::Tfe::OauthClient](../resources/tfe/Terraform-Tfe-OauthClient/docs/README.md)
* [Terraform::Tfe::OrganizationToken](../resources/tfe/Terraform-Tfe-OrganizationToken/docs/README.md)
* [Terraform::Tfe::Organization](../resources/tfe/Terraform-Tfe-Organization/docs/README.md)
* [Terraform::Tfe::PolicySetParameter](../resources/tfe/Terraform-Tfe-PolicySetParameter/docs/README.md)
* [Terraform::Tfe::PolicySet](../resources/tfe/Terraform-Tfe-PolicySet/docs/README.md)
* [Terraform::Tfe::RunTrigger](../resources/tfe/Terraform-Tfe-RunTrigger/docs/README.md)
* [Terraform::Tfe::SentinelPolicy](../resources/tfe/Terraform-Tfe-SentinelPolicy/docs/README.md)
* [Terraform::Tfe::SshKey](../resources/tfe/Terraform-Tfe-SshKey/docs/README.md)
* [Terraform::Tfe::TeamAccess](../resources/tfe/Terraform-Tfe-TeamAccess/docs/README.md)
* [Terraform::Tfe::TeamMember](../resources/tfe/Terraform-Tfe-TeamMember/docs/README.md)
* [Terraform::Tfe::TeamMembers](../resources/tfe/Terraform-Tfe-TeamMembers/docs/README.md)
* [Terraform::Tfe::TeamToken](../resources/tfe/Terraform-Tfe-TeamToken/docs/README.md)
* [Terraform::Tfe::Team](../resources/tfe/Terraform-Tfe-Team/docs/README.md)
* [Terraform::Tfe::Variable](../resources/tfe/Terraform-Tfe-Variable/docs/README.md)
* [Terraform::Tfe::Workspace](../resources/tfe/Terraform-Tfe-Workspace/docs/README.md)