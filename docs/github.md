# GitHub Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/github**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Optional) A GitHub OAuth / Personal Access Token.

* `base_url` - (Optional) This is the target GitHub base API endpoint. Providing a value is a requirement when working with GitHub Enterprise.  The value must end with a slash, for example: `https://terraformtesting-ghe.westus.cloudapp.azure.com/`

* `owner` - (Optional) This is the target GitHub individual account to manage. For example, `torvalds` is a valid owner. When not provided and a `token` is available, the individual account owning the `token` will be used. When not provided and no `token` is available, the provider may not function correctly. Conflicts with `organization`.

* `organization` - (Optional) This is the target GitHub organization account to manage. For example, `github` is a valid organization. Conflicts with `owner`and requires `token`, as the individual account corresponding to provided `token` will need "owner" privileges for this organization.


## Supported Resources

* [TF::GitHub::ActionsEnvironmentSecret](../resources/github/TF-GitHub-ActionsEnvironmentSecret/docs/README.md)
* [TF::GitHub::ActionsOrganizationSecret](../resources/github/TF-GitHub-ActionsOrganizationSecret/docs/README.md)
* [TF::GitHub::ActionsSecret](../resources/github/TF-GitHub-ActionsSecret/docs/README.md)
* [TF::GitHub::AppInstallationRepository](../resources/github/TF-GitHub-AppInstallationRepository/docs/README.md)
* [TF::GitHub::BranchDefault](../resources/github/TF-GitHub-BranchDefault/docs/README.md)
* [TF::GitHub::BranchProtectionV3](../resources/github/TF-GitHub-BranchProtectionV3/docs/README.md)
* [TF::GitHub::BranchProtection](../resources/github/TF-GitHub-BranchProtection/docs/README.md)
* [TF::GitHub::Branch](../resources/github/TF-GitHub-Branch/docs/README.md)
* [TF::GitHub::IssueLabel](../resources/github/TF-GitHub-IssueLabel/docs/README.md)
* [TF::GitHub::Membership](../resources/github/TF-GitHub-Membership/docs/README.md)
* [TF::GitHub::OrganizationBlock](../resources/github/TF-GitHub-OrganizationBlock/docs/README.md)
* [TF::GitHub::OrganizationProject](../resources/github/TF-GitHub-OrganizationProject/docs/README.md)
* [TF::GitHub::OrganizationWebhook](../resources/github/TF-GitHub-OrganizationWebhook/docs/README.md)
* [TF::GitHub::ProjectCard](../resources/github/TF-GitHub-ProjectCard/docs/README.md)
* [TF::GitHub::ProjectColumn](../resources/github/TF-GitHub-ProjectColumn/docs/README.md)
* [TF::GitHub::RepositoryCollaborator](../resources/github/TF-GitHub-RepositoryCollaborator/docs/README.md)
* [TF::GitHub::RepositoryDeployKey](../resources/github/TF-GitHub-RepositoryDeployKey/docs/README.md)
* [TF::GitHub::RepositoryEnvironment](../resources/github/TF-GitHub-RepositoryEnvironment/docs/README.md)
* [TF::GitHub::RepositoryFile](../resources/github/TF-GitHub-RepositoryFile/docs/README.md)
* [TF::GitHub::RepositoryMilestone](../resources/github/TF-GitHub-RepositoryMilestone/docs/README.md)
* [TF::GitHub::RepositoryProject](../resources/github/TF-GitHub-RepositoryProject/docs/README.md)
* [TF::GitHub::RepositoryPullRequest](../resources/github/TF-GitHub-RepositoryPullRequest/docs/README.md)
* [TF::GitHub::RepositoryWebhook](../resources/github/TF-GitHub-RepositoryWebhook/docs/README.md)
* [TF::GitHub::Repository](../resources/github/TF-GitHub-Repository/docs/README.md)
* [TF::GitHub::TeamMembership](../resources/github/TF-GitHub-TeamMembership/docs/README.md)
* [TF::GitHub::TeamRepository](../resources/github/TF-GitHub-TeamRepository/docs/README.md)
* [TF::GitHub::TeamSyncGroupMapping](../resources/github/TF-GitHub-TeamSyncGroupMapping/docs/README.md)
* [TF::GitHub::Team](../resources/github/TF-GitHub-Team/docs/README.md)
* [TF::GitHub::UserGpgKey](../resources/github/TF-GitHub-UserGpgKey/docs/README.md)
* [TF::GitHub::UserInvitationAccepter](../resources/github/TF-GitHub-UserInvitationAccepter/docs/README.md)
* [TF::GitHub::UserSshKey](../resources/github/TF-GitHub-UserSshKey/docs/README.md)