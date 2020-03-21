# Gitlab Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/gitlab**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `token` - (Optional) This is the GitLab personal access token.

* `base_url` - (Optional) This is the target GitLab base API endpoint. Providing a value is a
  requirement when working with GitLab CE or GitLab Enterprise e.g. `https://my.gitlab.server/api/v4/`.
  The value must end with a slash.

* `cacert_file` - (Optional) This is a file containing the ca cert to verify the gitlab instance.  This is available
  for use when working with GitLab CE or Gitlab Enterprise with a locally-issued or self-signed certificate chain.

* `insecure` - (Optional; boolean, defaults to false) When set to true this disables SSL verification of the connection to the
  GitLab instance.


## Supported Resources

* [Terraform::Gitlab::BranchProtection](../resources/gitlab/Terraform-Gitlab-BranchProtection/docs/README.md)
* [Terraform::Gitlab::DeployKeyEnable](../resources/gitlab/Terraform-Gitlab-DeployKeyEnable/docs/README.md)
* [Terraform::Gitlab::DeployKey](../resources/gitlab/Terraform-Gitlab-DeployKey/docs/README.md)
* [Terraform::Gitlab::GroupCluster](../resources/gitlab/Terraform-Gitlab-GroupCluster/docs/README.md)
* [Terraform::Gitlab::GroupLabel](../resources/gitlab/Terraform-Gitlab-GroupLabel/docs/README.md)
* [Terraform::Gitlab::GroupMembership](../resources/gitlab/Terraform-Gitlab-GroupMembership/docs/README.md)
* [Terraform::Gitlab::GroupVariable](../resources/gitlab/Terraform-Gitlab-GroupVariable/docs/README.md)
* [Terraform::Gitlab::Group](../resources/gitlab/Terraform-Gitlab-Group/docs/README.md)
* [Terraform::Gitlab::Label](../resources/gitlab/Terraform-Gitlab-Label/docs/README.md)
* [Terraform::Gitlab::PipelineScheduleVariable](../resources/gitlab/Terraform-Gitlab-PipelineScheduleVariable/docs/README.md)
* [Terraform::Gitlab::PipelineSchedule](../resources/gitlab/Terraform-Gitlab-PipelineSchedule/docs/README.md)
* [Terraform::Gitlab::PipelineTrigger](../resources/gitlab/Terraform-Gitlab-PipelineTrigger/docs/README.md)
* [Terraform::Gitlab::ProjectCluster](../resources/gitlab/Terraform-Gitlab-ProjectCluster/docs/README.md)
* [Terraform::Gitlab::ProjectHook](../resources/gitlab/Terraform-Gitlab-ProjectHook/docs/README.md)
* [Terraform::Gitlab::ProjectMembership](../resources/gitlab/Terraform-Gitlab-ProjectMembership/docs/README.md)
* [Terraform::Gitlab::ProjectPushRules](../resources/gitlab/Terraform-Gitlab-ProjectPushRules/docs/README.md)
* [Terraform::Gitlab::ProjectShareGroup](../resources/gitlab/Terraform-Gitlab-ProjectShareGroup/docs/README.md)
* [Terraform::Gitlab::ProjectVariable](../resources/gitlab/Terraform-Gitlab-ProjectVariable/docs/README.md)
* [Terraform::Gitlab::Project](../resources/gitlab/Terraform-Gitlab-Project/docs/README.md)
* [Terraform::Gitlab::ServiceJira](../resources/gitlab/Terraform-Gitlab-ServiceJira/docs/README.md)
* [Terraform::Gitlab::ServiceSlack](../resources/gitlab/Terraform-Gitlab-ServiceSlack/docs/README.md)
* [Terraform::Gitlab::TagProtection](../resources/gitlab/Terraform-Gitlab-TagProtection/docs/README.md)
* [Terraform::Gitlab::User](../resources/gitlab/Terraform-Gitlab-User/docs/README.md)