# Volterra Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/volterra**. The below arguments may be included as the key/value or JSON properties in the secret:

* `api_p12_file` - API credential p12 file path. Either api p12 file or (`api_cert` and `api_key`) must be given. This can also be sourced from `VOLT_API_P12_FILE` env variable.

* `api_cert` - API certificate file path. `api_cert` and `api_key` combo must be given. This can also be sourced from `VOLT_API_CERT` env variable (`String`).

* `api_key` - API certificate private key file path. This can also be sourced from `VOLT_API_KEY` env variable (`String`).

* `url` - (Required) Tenant API url file path. This can also be sourced from `VOLT_API_URL` env variable (`String`).

* `timeout` - Volterra api call timeout, by default its 10 seconds. This can also be sourced from `VOLT_API_TIMEOUT` env variable (`String`).

## Supported Resources

* [TF::Volterra::ActiveAlertPolicies](../resources/volterra/TF-Volterra-ActiveAlertPolicies/docs/README.md)
* [TF::Volterra::ActiveNetworkPolicies](../resources/volterra/TF-Volterra-ActiveNetworkPolicies/docs/README.md)
* [TF::Volterra::ActiveServicePolicies](../resources/volterra/TF-Volterra-ActiveServicePolicies/docs/README.md)
* [TF::Volterra::AdvertisePolicy](../resources/volterra/TF-Volterra-AdvertisePolicy/docs/README.md)
* [TF::Volterra::AlertPolicy](../resources/volterra/TF-Volterra-AlertPolicy/docs/README.md)
* [TF::Volterra::AlertReceiver](../resources/volterra/TF-Volterra-AlertReceiver/docs/README.md)
* [TF::Volterra::ApiCredential](../resources/volterra/TF-Volterra-ApiCredential/docs/README.md)
* [TF::Volterra::AppType](../resources/volterra/TF-Volterra-AppType/docs/README.md)
* [TF::Volterra::AwsTgwSite](../resources/volterra/TF-Volterra-AwsTgwSite/docs/README.md)
* [TF::Volterra::AwsVpcSite](../resources/volterra/TF-Volterra-AwsVpcSite/docs/README.md)
* [TF::Volterra::AzureVnetSite](../resources/volterra/TF-Volterra-AzureVnetSite/docs/README.md)
* [TF::Volterra::BgpAsnSet](../resources/volterra/TF-Volterra-BgpAsnSet/docs/README.md)
* [TF::Volterra::Bgp](../resources/volterra/TF-Volterra-Bgp/docs/README.md)
* [TF::Volterra::CloudCredentials](../resources/volterra/TF-Volterra-CloudCredentials/docs/README.md)
* [TF::Volterra::Cluster](../resources/volterra/TF-Volterra-Cluster/docs/README.md)
* [TF::Volterra::DcClusterGroup](../resources/volterra/TF-Volterra-DcClusterGroup/docs/README.md)
* [TF::Volterra::Discovery](../resources/volterra/TF-Volterra-Discovery/docs/README.md)
* [TF::Volterra::Endpoint](../resources/volterra/TF-Volterra-Endpoint/docs/README.md)
* [TF::Volterra::FastAclForInternetVips](../resources/volterra/TF-Volterra-FastAclForInternetVips/docs/README.md)
* [TF::Volterra::FastAclRule](../resources/volterra/TF-Volterra-FastAclRule/docs/README.md)
* [TF::Volterra::FastAcl](../resources/volterra/TF-Volterra-FastAcl/docs/README.md)
* [TF::Volterra::Fleet](../resources/volterra/TF-Volterra-Fleet/docs/README.md)
* [TF::Volterra::ForwardProxyPolicy](../resources/volterra/TF-Volterra-ForwardProxyPolicy/docs/README.md)
* [TF::Volterra::GcpVpcSite](../resources/volterra/TF-Volterra-GcpVpcSite/docs/README.md)
* [TF::Volterra::Healthcheck](../resources/volterra/TF-Volterra-Healthcheck/docs/README.md)
* [TF::Volterra::HttpLoadbalancer](../resources/volterra/TF-Volterra-HttpLoadbalancer/docs/README.md)
* [TF::Volterra::IpPrefixSet](../resources/volterra/TF-Volterra-IpPrefixSet/docs/README.md)
* [TF::Volterra::K8sClusterRoleBinding](../resources/volterra/TF-Volterra-K8sClusterRoleBinding/docs/README.md)
* [TF::Volterra::K8sClusterRole](../resources/volterra/TF-Volterra-K8sClusterRole/docs/README.md)
* [TF::Volterra::K8sCluster](../resources/volterra/TF-Volterra-K8sCluster/docs/README.md)
* [TF::Volterra::K8sPodSecurityPolicy](../resources/volterra/TF-Volterra-K8sPodSecurityPolicy/docs/README.md)
* [TF::Volterra::MaliciousUserMitigation](../resources/volterra/TF-Volterra-MaliciousUserMitigation/docs/README.md)
* [TF::Volterra::ModifySite](../resources/volterra/TF-Volterra-ModifySite/docs/README.md)
* [TF::Volterra::Namespace](../resources/volterra/TF-Volterra-Namespace/docs/README.md)
* [TF::Volterra::NetworkConnector](../resources/volterra/TF-Volterra-NetworkConnector/docs/README.md)
* [TF::Volterra::NetworkFirewall](../resources/volterra/TF-Volterra-NetworkFirewall/docs/README.md)
* [TF::Volterra::NetworkInterface](../resources/volterra/TF-Volterra-NetworkInterface/docs/README.md)
* [TF::Volterra::NetworkPolicyRule](../resources/volterra/TF-Volterra-NetworkPolicyRule/docs/README.md)
* [TF::Volterra::NetworkPolicyView](../resources/volterra/TF-Volterra-NetworkPolicyView/docs/README.md)
* [TF::Volterra::NetworkPolicy](../resources/volterra/TF-Volterra-NetworkPolicy/docs/README.md)
* [TF::Volterra::OriginPool](../resources/volterra/TF-Volterra-OriginPool/docs/README.md)
* [TF::Volterra::Policer](../resources/volterra/TF-Volterra-Policer/docs/README.md)
* [TF::Volterra::ProtocolPolicer](../resources/volterra/TF-Volterra-ProtocolPolicer/docs/README.md)
* [TF::Volterra::PublicIp](../resources/volterra/TF-Volterra-PublicIp/docs/README.md)
* [TF::Volterra::RateLimiter](../resources/volterra/TF-Volterra-RateLimiter/docs/README.md)
* [TF::Volterra::RegistrationApproval](../resources/volterra/TF-Volterra-RegistrationApproval/docs/README.md)
* [TF::Volterra::Role](../resources/volterra/TF-Volterra-Role/docs/README.md)
* [TF::Volterra::Route](../resources/volterra/TF-Volterra-Route/docs/README.md)
* [TF::Volterra::SecretPolicyRule](../resources/volterra/TF-Volterra-SecretPolicyRule/docs/README.md)
* [TF::Volterra::ServicePolicyRule](../resources/volterra/TF-Volterra-ServicePolicyRule/docs/README.md)
* [TF::Volterra::ServicePolicy](../resources/volterra/TF-Volterra-ServicePolicy/docs/README.md)
* [TF::Volterra::SiteSetVipInfo](../resources/volterra/TF-Volterra-SiteSetVipInfo/docs/README.md)
* [TF::Volterra::SiteState](../resources/volterra/TF-Volterra-SiteState/docs/README.md)
* [TF::Volterra::TcpLoadbalancer](../resources/volterra/TF-Volterra-TcpLoadbalancer/docs/README.md)
* [TF::Volterra::TfParamsAction](../resources/volterra/TF-Volterra-TfParamsAction/docs/README.md)
* [TF::Volterra::TgwInfo](../resources/volterra/TF-Volterra-TgwInfo/docs/README.md)
* [TF::Volterra::TgwVpcIpPrefixes](../resources/volterra/TF-Volterra-TgwVpcIpPrefixes/docs/README.md)
* [TF::Volterra::TgwVpnTunnels](../resources/volterra/TF-Volterra-TgwVpnTunnels/docs/README.md)
* [TF::Volterra::Token](../resources/volterra/TF-Volterra-Token/docs/README.md)
* [TF::Volterra::UsbPolicy](../resources/volterra/TF-Volterra-UsbPolicy/docs/README.md)
* [TF::Volterra::User](../resources/volterra/TF-Volterra-User/docs/README.md)
* [TF::Volterra::VirtualHost](../resources/volterra/TF-Volterra-VirtualHost/docs/README.md)
* [TF::Volterra::VirtualK8s](../resources/volterra/TF-Volterra-VirtualK8s/docs/README.md)
* [TF::Volterra::VirtualNetwork](../resources/volterra/TF-Volterra-VirtualNetwork/docs/README.md)
* [TF::Volterra::VirtualSite](../resources/volterra/TF-Volterra-VirtualSite/docs/README.md)
* [TF::Volterra::VoltstackSite](../resources/volterra/TF-Volterra-VoltstackSite/docs/README.md)
* [TF::Volterra::VpcK8sHostnames](../resources/volterra/TF-Volterra-VpcK8sHostnames/docs/README.md)
* [TF::Volterra::WafRuleList](../resources/volterra/TF-Volterra-WafRuleList/docs/README.md)
* [TF::Volterra::WafRules](../resources/volterra/TF-Volterra-WafRules/docs/README.md)
* [TF::Volterra::Waf](../resources/volterra/TF-Volterra-Waf/docs/README.md)