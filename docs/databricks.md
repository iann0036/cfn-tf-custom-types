# Databricks Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/databricks**. The below arguments may be included as the key/value or JSON properties in the secret:

* `host` - (optional) This is the host of the Databricks workspace. It is a URL that you use to login to your workspace.
* `token` - (optional) This is the API token to authenticate into the workspace. 
* `username` - (optional) This is the username of the user that can log into the workspace. Recommended only for [creating workspaces in AWS](resources/mws_workspaces.md).
* `password` - (optional) This is the user's password that can log into the workspace. Recommended only for [creating workspaces in AWS](resources/mws_workspaces.md).
* `config_file` - (optional) Location of the Databricks CLI credentials file created by `databricks configure --token` command (~/.databrickscfg by default). Check [Databricks CLI documentation](https://docs.databricks.com/dev-tools/cli/index.html#set-up-authentication) for more details. The provider uses configuration file credentials when you don't specify host/token/username/password/azure attributes. This field defaults to `~/.databrickscfg`. 
* `profile` - (optional) Connection profile specified within ~/.databrickscfg. Please check [connection profiles section](https://docs.databricks.com/dev-tools/cli/index.html#connection-profiles) for more details. This field defaults to 
`DEFAULT`.


## Supported Resources

* [TF::Databricks::AwsS3Mount](../resources/databricks/TF-Databricks-AwsS3Mount/docs/README.md)
* [TF::Databricks::AzureAdlsGen1Mount](../resources/databricks/TF-Databricks-AzureAdlsGen1Mount/docs/README.md)
* [TF::Databricks::AzureAdlsGen2Mount](../resources/databricks/TF-Databricks-AzureAdlsGen2Mount/docs/README.md)
* [TF::Databricks::AzureBlobMount](../resources/databricks/TF-Databricks-AzureBlobMount/docs/README.md)
* [TF::Databricks::ClusterPolicy](../resources/databricks/TF-Databricks-ClusterPolicy/docs/README.md)
* [TF::Databricks::Cluster](../resources/databricks/TF-Databricks-Cluster/docs/README.md)
* [TF::Databricks::DbfsFile](../resources/databricks/TF-Databricks-DbfsFile/docs/README.md)
* [TF::Databricks::GlobalInitScript](../resources/databricks/TF-Databricks-GlobalInitScript/docs/README.md)
* [TF::Databricks::GroupInstanceProfile](../resources/databricks/TF-Databricks-GroupInstanceProfile/docs/README.md)
* [TF::Databricks::GroupMember](../resources/databricks/TF-Databricks-GroupMember/docs/README.md)
* [TF::Databricks::Group](../resources/databricks/TF-Databricks-Group/docs/README.md)
* [TF::Databricks::InstancePool](../resources/databricks/TF-Databricks-InstancePool/docs/README.md)
* [TF::Databricks::InstanceProfile](../resources/databricks/TF-Databricks-InstanceProfile/docs/README.md)
* [TF::Databricks::IpAccessList](../resources/databricks/TF-Databricks-IpAccessList/docs/README.md)
* [TF::Databricks::Job](../resources/databricks/TF-Databricks-Job/docs/README.md)
* [TF::Databricks::MwsCredentials](../resources/databricks/TF-Databricks-MwsCredentials/docs/README.md)
* [TF::Databricks::MwsCustomerManagedKeys](../resources/databricks/TF-Databricks-MwsCustomerManagedKeys/docs/README.md)
* [TF::Databricks::MwsLogDelivery](../resources/databricks/TF-Databricks-MwsLogDelivery/docs/README.md)
* [TF::Databricks::MwsNetworks](../resources/databricks/TF-Databricks-MwsNetworks/docs/README.md)
* [TF::Databricks::MwsPrivateAccessSettings](../resources/databricks/TF-Databricks-MwsPrivateAccessSettings/docs/README.md)
* [TF::Databricks::MwsStorageConfigurations](../resources/databricks/TF-Databricks-MwsStorageConfigurations/docs/README.md)
* [TF::Databricks::MwsVpcEndpoint](../resources/databricks/TF-Databricks-MwsVpcEndpoint/docs/README.md)
* [TF::Databricks::MwsWorkspaces](../resources/databricks/TF-Databricks-MwsWorkspaces/docs/README.md)
* [TF::Databricks::Notebook](../resources/databricks/TF-Databricks-Notebook/docs/README.md)
* [TF::Databricks::Permissions](../resources/databricks/TF-Databricks-Permissions/docs/README.md)
* [TF::Databricks::Pipeline](../resources/databricks/TF-Databricks-Pipeline/docs/README.md)
* [TF::Databricks::SecretAcl](../resources/databricks/TF-Databricks-SecretAcl/docs/README.md)
* [TF::Databricks::SecretScope](../resources/databricks/TF-Databricks-SecretScope/docs/README.md)
* [TF::Databricks::Secret](../resources/databricks/TF-Databricks-Secret/docs/README.md)
* [TF::Databricks::ServicePrincipal](../resources/databricks/TF-Databricks-ServicePrincipal/docs/README.md)
* [TF::Databricks::SqlDashboard](../resources/databricks/TF-Databricks-SqlDashboard/docs/README.md)
* [TF::Databricks::SqlEndpoint](../resources/databricks/TF-Databricks-SqlEndpoint/docs/README.md)
* [TF::Databricks::SqlPermissions](../resources/databricks/TF-Databricks-SqlPermissions/docs/README.md)
* [TF::Databricks::SqlQuery](../resources/databricks/TF-Databricks-SqlQuery/docs/README.md)
* [TF::Databricks::SqlVisualization](../resources/databricks/TF-Databricks-SqlVisualization/docs/README.md)
* [TF::Databricks::SqlWidget](../resources/databricks/TF-Databricks-SqlWidget/docs/README.md)
* [TF::Databricks::Token](../resources/databricks/TF-Databricks-Token/docs/README.md)
* [TF::Databricks::UserInstanceProfile](../resources/databricks/TF-Databricks-UserInstanceProfile/docs/README.md)
* [TF::Databricks::User](../resources/databricks/TF-Databricks-User/docs/README.md)
* [TF::Databricks::WorkspaceConf](../resources/databricks/TF-Databricks-WorkspaceConf/docs/README.md)