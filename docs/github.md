# GitHub Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/github**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `token` - (Optional) This is the GitHub personal access token. If `anonymous` is false,
  `token` is required.

* `organization` - (Optional) This is the target GitHub organization to manage.
  The account corresponding to the token will need "owner" privileges for this
  organization. If `individual` is set to `false`, organization is required.

* `base_url` - (Optional) This is the target GitHub base API endpoint. Providing a value is a
  requirement when working with GitHub Enterprise.  The value must end with a slash,
  and generally includes the API version, for instance `https://github.someorg.example/api/v3/`.

* `insecure` - (Optional) Whether server should be accessed without verifying the TLS certificate.
  As the name suggests **this is insecure** and should not be used beyond experiments,
  accessing local (non-production) GHE instance etc.
  There is a number of ways to obtain trusted certificate for free, e.g. from [Let's Encrypt](https://letsencrypt.org/).
  Such trusted certificate *does not require* this option to be enabled.
  Defaults to `false`.

* `individual`: (Optional) Run outside an organization.  When `individual` is true, the provider will run outside
  the scope of an organization. Defaults to `false`.

* `anonymous`: (Optional) Authenticate without a token.  When `anonymous` is true, the provider will not be able to
  access resources that require authentication. Setting to true will lead the GitHub provider to work in an anonymous
  mode with the corresponding API [rate limits](https://developer.github.com/v3/#rate-limiting).  Defaults to `false`.

* `id`: (Computed) This is the ID of the target GitHub organization which is being managed. The value of this is set by
  provider based on the name specified in `organization`.

## Supported Resources

* [Terraform::GitHub::BranchProtection](../resources/github/Terraform-GitHub-BranchProtection/docs/README.md)
* [Terraform::GitHub::IssueLabel](../resources/github/Terraform-GitHub-IssueLabel/docs/README.md)
* [Terraform::GitHub::Membership](../resources/github/Terraform-GitHub-Membership/docs/README.md)
* [Terraform::GitHub::OrganizationBlock](../resources/github/Terraform-GitHub-OrganizationBlock/docs/README.md)
* [Terraform::GitHub::OrganizationProject](../resources/github/Terraform-GitHub-OrganizationProject/docs/README.md)
* [Terraform::GitHub::OrganizationWebhook](../resources/github/Terraform-GitHub-OrganizationWebhook/docs/README.md)
* [Terraform::GitHub::ProjectColumn](../resources/github/Terraform-GitHub-ProjectColumn/docs/README.md)
* [Terraform::GitHub::RepositoryCollaborator](../resources/github/Terraform-GitHub-RepositoryCollaborator/docs/README.md)
* [Terraform::GitHub::RepositoryDeployKey](../resources/github/Terraform-GitHub-RepositoryDeployKey/docs/README.md)
* [Terraform::GitHub::RepositoryFile](../resources/github/Terraform-GitHub-RepositoryFile/docs/README.md)
* [Terraform::GitHub::RepositoryProject](../resources/github/Terraform-GitHub-RepositoryProject/docs/README.md)
* [Terraform::GitHub::RepositoryWebhook](../resources/github/Terraform-GitHub-RepositoryWebhook/docs/README.md)
* [Terraform::GitHub::Repository](../resources/github/Terraform-GitHub-Repository/docs/README.md)
* [Terraform::GitHub::TeamMembership](../resources/github/Terraform-GitHub-TeamMembership/docs/README.md)
* [Terraform::GitHub::TeamRepository](../resources/github/Terraform-GitHub-TeamRepository/docs/README.md)
* [Terraform::GitHub::Team](../resources/github/Terraform-GitHub-Team/docs/README.md)
* [Terraform::GitHub::UserGpgKey](../resources/github/Terraform-GitHub-UserGpgKey/docs/README.md)
* [Terraform::GitHub::UserInvitationAccepter](../resources/github/Terraform-GitHub-UserInvitationAccepter/docs/README.md)
* [Terraform::GitHub::UserSshKey](../resources/github/Terraform-GitHub-UserSshKey/docs/README.md)