# Rancher v2 Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/rancher2**. The below arguments may be included as the key/value or JSON properties in the secret:

* `api_url` - (Required) Rancher API url.
* `access_key` - (Optional/Sensitive) Rancher API access key to connect to rancher.
* `secret_key` - (Optional/Sensitive) Rancher API secret key to connect to rancher.
* `token_key` - (Optional/Sensitive) Rancher API token key to connect to rancher. Could be used instead `access_key` and `secret_key`.
* `ca_certs` - CA certificates used to sign Rancher server tls certificates. Mandatory if self signed tls and insecure option false.
* `insecure` - (Optional) Allow insecure connection to Rancher. Mandatory if self signed tls and not ca_certs provided.
* `bootstrap` - (Optional) Enable bootstrap mode to manage `rancher2_bootstrap` resource. Default: `false`
* `retries` - (Deprecated) Use timeout instead
* `timeout` - (Optional) Timeout duration to retry for Rancher connectivity and resource operations. Default: `"120s"`


## Supported Resources

* [TF::Rancher2::AppV2](../resources/rancher2/TF-Rancher2-AppV2/docs/README.md)
* [TF::Rancher2::App](../resources/rancher2/TF-Rancher2-App/docs/README.md)
* [TF::Rancher2::AuthConfigActivedirectory](../resources/rancher2/TF-Rancher2-AuthConfigActivedirectory/docs/README.md)
* [TF::Rancher2::AuthConfigAdfs](../resources/rancher2/TF-Rancher2-AuthConfigAdfs/docs/README.md)
* [TF::Rancher2::AuthConfigAzuread](../resources/rancher2/TF-Rancher2-AuthConfigAzuread/docs/README.md)
* [TF::Rancher2::AuthConfigFreeipa](../resources/rancher2/TF-Rancher2-AuthConfigFreeipa/docs/README.md)
* [TF::Rancher2::AuthConfigGithub](../resources/rancher2/TF-Rancher2-AuthConfigGithub/docs/README.md)
* [TF::Rancher2::AuthConfigKeycloak](../resources/rancher2/TF-Rancher2-AuthConfigKeycloak/docs/README.md)
* [TF::Rancher2::AuthConfigOkta](../resources/rancher2/TF-Rancher2-AuthConfigOkta/docs/README.md)
* [TF::Rancher2::AuthConfigOpenldap](../resources/rancher2/TF-Rancher2-AuthConfigOpenldap/docs/README.md)
* [TF::Rancher2::AuthConfigPing](../resources/rancher2/TF-Rancher2-AuthConfigPing/docs/README.md)
* [TF::Rancher2::Bootstrap](../resources/rancher2/TF-Rancher2-Bootstrap/docs/README.md)
* [TF::Rancher2::CatalogV2](../resources/rancher2/TF-Rancher2-CatalogV2/docs/README.md)
* [TF::Rancher2::Catalog](../resources/rancher2/TF-Rancher2-Catalog/docs/README.md)
* [TF::Rancher2::Certificate](../resources/rancher2/TF-Rancher2-Certificate/docs/README.md)
* [TF::Rancher2::CloudCredential](../resources/rancher2/TF-Rancher2-CloudCredential/docs/README.md)
* [TF::Rancher2::ClusterAlertGroup](../resources/rancher2/TF-Rancher2-ClusterAlertGroup/docs/README.md)
* [TF::Rancher2::ClusterAlertRule](../resources/rancher2/TF-Rancher2-ClusterAlertRule/docs/README.md)
* [TF::Rancher2::ClusterDriver](../resources/rancher2/TF-Rancher2-ClusterDriver/docs/README.md)
* [TF::Rancher2::ClusterLogging](../resources/rancher2/TF-Rancher2-ClusterLogging/docs/README.md)
* [TF::Rancher2::ClusterRoleTemplateBinding](../resources/rancher2/TF-Rancher2-ClusterRoleTemplateBinding/docs/README.md)
* [TF::Rancher2::ClusterSync](../resources/rancher2/TF-Rancher2-ClusterSync/docs/README.md)
* [TF::Rancher2::ClusterTemplate](../resources/rancher2/TF-Rancher2-ClusterTemplate/docs/README.md)
* [TF::Rancher2::Cluster](../resources/rancher2/TF-Rancher2-Cluster/docs/README.md)
* [TF::Rancher2::EtcdBackup](../resources/rancher2/TF-Rancher2-EtcdBackup/docs/README.md)
* [TF::Rancher2::Feature](../resources/rancher2/TF-Rancher2-Feature/docs/README.md)
* [TF::Rancher2::GlobalDnsProvider](../resources/rancher2/TF-Rancher2-GlobalDnsProvider/docs/README.md)
* [TF::Rancher2::GlobalDns](../resources/rancher2/TF-Rancher2-GlobalDns/docs/README.md)
* [TF::Rancher2::GlobalRoleBinding](../resources/rancher2/TF-Rancher2-GlobalRoleBinding/docs/README.md)
* [TF::Rancher2::GlobalRole](../resources/rancher2/TF-Rancher2-GlobalRole/docs/README.md)
* [TF::Rancher2::MultiClusterApp](../resources/rancher2/TF-Rancher2-MultiClusterApp/docs/README.md)
* [TF::Rancher2::Namespace](../resources/rancher2/TF-Rancher2-Namespace/docs/README.md)
* [TF::Rancher2::NodeDriver](../resources/rancher2/TF-Rancher2-NodeDriver/docs/README.md)
* [TF::Rancher2::NodePool](../resources/rancher2/TF-Rancher2-NodePool/docs/README.md)
* [TF::Rancher2::NodeTemplate](../resources/rancher2/TF-Rancher2-NodeTemplate/docs/README.md)
* [TF::Rancher2::Notifier](../resources/rancher2/TF-Rancher2-Notifier/docs/README.md)
* [TF::Rancher2::PodSecurityPolicyTemplate](../resources/rancher2/TF-Rancher2-PodSecurityPolicyTemplate/docs/README.md)
* [TF::Rancher2::ProjectAlertGroup](../resources/rancher2/TF-Rancher2-ProjectAlertGroup/docs/README.md)
* [TF::Rancher2::ProjectAlertRule](../resources/rancher2/TF-Rancher2-ProjectAlertRule/docs/README.md)
* [TF::Rancher2::ProjectLogging](../resources/rancher2/TF-Rancher2-ProjectLogging/docs/README.md)
* [TF::Rancher2::ProjectRoleTemplateBinding](../resources/rancher2/TF-Rancher2-ProjectRoleTemplateBinding/docs/README.md)
* [TF::Rancher2::Project](../resources/rancher2/TF-Rancher2-Project/docs/README.md)
* [TF::Rancher2::Registry](../resources/rancher2/TF-Rancher2-Registry/docs/README.md)
* [TF::Rancher2::RoleTemplate](../resources/rancher2/TF-Rancher2-RoleTemplate/docs/README.md)
* [TF::Rancher2::SecretV2](../resources/rancher2/TF-Rancher2-SecretV2/docs/README.md)
* [TF::Rancher2::Secret](../resources/rancher2/TF-Rancher2-Secret/docs/README.md)
* [TF::Rancher2::Setting](../resources/rancher2/TF-Rancher2-Setting/docs/README.md)
* [TF::Rancher2::Token](../resources/rancher2/TF-Rancher2-Token/docs/README.md)
* [TF::Rancher2::User](../resources/rancher2/TF-Rancher2-User/docs/README.md)