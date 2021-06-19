# Gitlab Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/gitlab**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Optional) This is the GitLab personal access token.

* `base_url` - (Optional) This is the target GitLab base API endpoint. Providing a value is a
  requirement when working with GitLab CE or GitLab Enterprise e.g. `https://my.gitlab.server/api/v4/`.
  The value must end with a slash.

* `cacert_file` - (Optional) This is a file containing the ca cert to verify the gitlab instance.  This is available
  for use when working with GitLab CE or Gitlab Enterprise with a locally-issued or self-signed certificate chain.

* `insecure` - (Optional; boolean, defaults to false) When set to true this disables SSL verification of the connection to the
  GitLab instance.

* `client_cert` - (Optional) File path to client certificate when GitLab instance is behind company proxy. File  must contain PEM encoded data.

* `client_key` - (Optional) File path to client key when GitLab instance is behind company proxy. File must contain PEM encoded data. Required when `client_cert` is set.


## Supported Resources

* [TF::Gitlab::BranchProtection](../resources/gitlab/TF-Gitlab-BranchProtection/docs/README.md)
* [TF::Gitlab::DeployKeyEnable](../resources/gitlab/TF-Gitlab-DeployKeyEnable/docs/README.md)
* [TF::Gitlab::DeployKey](../resources/gitlab/TF-Gitlab-DeployKey/docs/README.md)
* [TF::Gitlab::DeployToken](../resources/gitlab/TF-Gitlab-DeployToken/docs/README.md)
* [TF::Gitlab::GroupCluster](../resources/gitlab/TF-Gitlab-GroupCluster/docs/README.md)
* [TF::Gitlab::GroupLabel](../resources/gitlab/TF-Gitlab-GroupLabel/docs/README.md)
* [TF::Gitlab::GroupLdapLink](../resources/gitlab/TF-Gitlab-GroupLdapLink/docs/README.md)
* [TF::Gitlab::GroupMembership](../resources/gitlab/TF-Gitlab-GroupMembership/docs/README.md)
* [TF::Gitlab::GroupShareGroup](../resources/gitlab/TF-Gitlab-GroupShareGroup/docs/README.md)
* [TF::Gitlab::GroupVariable](../resources/gitlab/TF-Gitlab-GroupVariable/docs/README.md)
* [TF::Gitlab::Group](../resources/gitlab/TF-Gitlab-Group/docs/README.md)
* [TF::Gitlab::InstanceCluster](../resources/gitlab/TF-Gitlab-InstanceCluster/docs/README.md)
* [TF::Gitlab::InstanceVariable](../resources/gitlab/TF-Gitlab-InstanceVariable/docs/README.md)
* [TF::Gitlab::Label](../resources/gitlab/TF-Gitlab-Label/docs/README.md)
* [TF::Gitlab::PipelineScheduleVariable](../resources/gitlab/TF-Gitlab-PipelineScheduleVariable/docs/README.md)
* [TF::Gitlab::PipelineSchedule](../resources/gitlab/TF-Gitlab-PipelineSchedule/docs/README.md)
* [TF::Gitlab::PipelineTrigger](../resources/gitlab/TF-Gitlab-PipelineTrigger/docs/README.md)
* [TF::Gitlab::ProjectApprovalRule](../resources/gitlab/TF-Gitlab-ProjectApprovalRule/docs/README.md)
* [TF::Gitlab::ProjectCluster](../resources/gitlab/TF-Gitlab-ProjectCluster/docs/README.md)
* [TF::Gitlab::ProjectFreezePeriod](../resources/gitlab/TF-Gitlab-ProjectFreezePeriod/docs/README.md)
* [TF::Gitlab::ProjectHook](../resources/gitlab/TF-Gitlab-ProjectHook/docs/README.md)
* [TF::Gitlab::ProjectLevelMrApprovals](../resources/gitlab/TF-Gitlab-ProjectLevelMrApprovals/docs/README.md)
* [TF::Gitlab::ProjectMembership](../resources/gitlab/TF-Gitlab-ProjectMembership/docs/README.md)
* [TF::Gitlab::ProjectMirror](../resources/gitlab/TF-Gitlab-ProjectMirror/docs/README.md)
* [TF::Gitlab::ProjectShareGroup](../resources/gitlab/TF-Gitlab-ProjectShareGroup/docs/README.md)
* [TF::Gitlab::ProjectVariable](../resources/gitlab/TF-Gitlab-ProjectVariable/docs/README.md)
* [TF::Gitlab::Project](../resources/gitlab/TF-Gitlab-Project/docs/README.md)
* [TF::Gitlab::ServiceGithub](../resources/gitlab/TF-Gitlab-ServiceGithub/docs/README.md)
* [TF::Gitlab::ServiceJira](../resources/gitlab/TF-Gitlab-ServiceJira/docs/README.md)
* [TF::Gitlab::ServicePipelinesEmail](../resources/gitlab/TF-Gitlab-ServicePipelinesEmail/docs/README.md)
* [TF::Gitlab::ServiceSlack](../resources/gitlab/TF-Gitlab-ServiceSlack/docs/README.md)
* [TF::Gitlab::TagProtection](../resources/gitlab/TF-Gitlab-TagProtection/docs/README.md)
* [TF::Gitlab::User](../resources/gitlab/TF-Gitlab-User/docs/README.md)