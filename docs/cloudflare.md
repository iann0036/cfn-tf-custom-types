# Cloudflare Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/cloudflare**. The below arguments may be included as the key/value or JSON properties in the secret:

* `email` - (Optional) The email associated with the account.
* `api_key` - (Optional) The Cloudflare API key.
* `api_token` - (Optional) The Cloudflare API Token. This is an
  alternative to `email`+`api_key`. If both are specified, `api_token` will be
  used over `email`+`api_key` fields.
* `api_user_service_key` - (Optional) The Cloudflare API User Service Key. The value is 
  to be used in combination with an `api_token`, or `email` and `api_key`.
  This is used for a specific set of endpoints, such as creating Origin CA certificates.
* `rps` - (Optional) RPS limit to apply when making calls to the API. Default: 4.
* `retries` - (Optional) Maximum number of retries to perform when an API request fails. Default: 3.
* `min_backoff` - (Optional) Minimum backoff period in seconds after failed API calls. Default: 1.
* `max_backoff` - (Optional) Maximum backoff period in seconds after failed API calls Default: 30.
* `api_client_logging` - (Optional) Whether to print logs from the API client (using the default log library logger). Default: false.
* `account_id` - (Optional) Configure API client with this account ID, so calls use the account API rather than the (default) user API.
  This is required for other users in your account to have access to the resources you manage.


## Supported Resources

* [TF::Cloudflare::AccessApplication](../resources/cloudflare/TF-Cloudflare-AccessApplication/docs/README.md)
* [TF::Cloudflare::AccessCaCertificate](../resources/cloudflare/TF-Cloudflare-AccessCaCertificate/docs/README.md)
* [TF::Cloudflare::AccessGroup](../resources/cloudflare/TF-Cloudflare-AccessGroup/docs/README.md)
* [TF::Cloudflare::AccessIdentityProvider](../resources/cloudflare/TF-Cloudflare-AccessIdentityProvider/docs/README.md)
* [TF::Cloudflare::AccessMutualTlsCertificate](../resources/cloudflare/TF-Cloudflare-AccessMutualTlsCertificate/docs/README.md)
* [TF::Cloudflare::AccessPolicy](../resources/cloudflare/TF-Cloudflare-AccessPolicy/docs/README.md)
* [TF::Cloudflare::AccessRule](../resources/cloudflare/TF-Cloudflare-AccessRule/docs/README.md)
* [TF::Cloudflare::AccessServiceToken](../resources/cloudflare/TF-Cloudflare-AccessServiceToken/docs/README.md)
* [TF::Cloudflare::AccountMember](../resources/cloudflare/TF-Cloudflare-AccountMember/docs/README.md)
* [TF::Cloudflare::ApiToken](../resources/cloudflare/TF-Cloudflare-ApiToken/docs/README.md)
* [TF::Cloudflare::ArgoTunnel](../resources/cloudflare/TF-Cloudflare-ArgoTunnel/docs/README.md)
* [TF::Cloudflare::Argo](../resources/cloudflare/TF-Cloudflare-Argo/docs/README.md)
* [TF::Cloudflare::AuthenticatedOriginPullsCertificate](../resources/cloudflare/TF-Cloudflare-AuthenticatedOriginPullsCertificate/docs/README.md)
* [TF::Cloudflare::AuthenticatedOriginPulls](../resources/cloudflare/TF-Cloudflare-AuthenticatedOriginPulls/docs/README.md)
* [TF::Cloudflare::ByoIpPrefix](../resources/cloudflare/TF-Cloudflare-ByoIpPrefix/docs/README.md)
* [TF::Cloudflare::CertificatePack](../resources/cloudflare/TF-Cloudflare-CertificatePack/docs/README.md)
* [TF::Cloudflare::CustomHostnameFallbackOrigin](../resources/cloudflare/TF-Cloudflare-CustomHostnameFallbackOrigin/docs/README.md)
* [TF::Cloudflare::CustomHostname](../resources/cloudflare/TF-Cloudflare-CustomHostname/docs/README.md)
* [TF::Cloudflare::CustomPages](../resources/cloudflare/TF-Cloudflare-CustomPages/docs/README.md)
* [TF::Cloudflare::CustomSsl](../resources/cloudflare/TF-Cloudflare-CustomSsl/docs/README.md)
* [TF::Cloudflare::DevicePostureRule](../resources/cloudflare/TF-Cloudflare-DevicePostureRule/docs/README.md)
* [TF::Cloudflare::Filter](../resources/cloudflare/TF-Cloudflare-Filter/docs/README.md)
* [TF::Cloudflare::FirewallRule](../resources/cloudflare/TF-Cloudflare-FirewallRule/docs/README.md)
* [TF::Cloudflare::Healthcheck](../resources/cloudflare/TF-Cloudflare-Healthcheck/docs/README.md)
* [TF::Cloudflare::IpList](../resources/cloudflare/TF-Cloudflare-IpList/docs/README.md)
* [TF::Cloudflare::LoadBalancerMonitor](../resources/cloudflare/TF-Cloudflare-LoadBalancerMonitor/docs/README.md)
* [TF::Cloudflare::LoadBalancerPool](../resources/cloudflare/TF-Cloudflare-LoadBalancerPool/docs/README.md)
* [TF::Cloudflare::LoadBalancer](../resources/cloudflare/TF-Cloudflare-LoadBalancer/docs/README.md)
* [TF::Cloudflare::LogpullRetention](../resources/cloudflare/TF-Cloudflare-LogpullRetention/docs/README.md)
* [TF::Cloudflare::LogpushJob](../resources/cloudflare/TF-Cloudflare-LogpushJob/docs/README.md)
* [TF::Cloudflare::LogpushOwnershipChallenge](../resources/cloudflare/TF-Cloudflare-LogpushOwnershipChallenge/docs/README.md)
* [TF::Cloudflare::MagicFirewallRuleset](../resources/cloudflare/TF-Cloudflare-MagicFirewallRuleset/docs/README.md)
* [TF::Cloudflare::OriginCaCertificate](../resources/cloudflare/TF-Cloudflare-OriginCaCertificate/docs/README.md)
* [TF::Cloudflare::PageRule](../resources/cloudflare/TF-Cloudflare-PageRule/docs/README.md)
* [TF::Cloudflare::RateLimit](../resources/cloudflare/TF-Cloudflare-RateLimit/docs/README.md)
* [TF::Cloudflare::Record](../resources/cloudflare/TF-Cloudflare-Record/docs/README.md)
* [TF::Cloudflare::SpectrumApplication](../resources/cloudflare/TF-Cloudflare-SpectrumApplication/docs/README.md)
* [TF::Cloudflare::TeamsList](../resources/cloudflare/TF-Cloudflare-TeamsList/docs/README.md)
* [TF::Cloudflare::WafGroup](../resources/cloudflare/TF-Cloudflare-WafGroup/docs/README.md)
* [TF::Cloudflare::WafOverride](../resources/cloudflare/TF-Cloudflare-WafOverride/docs/README.md)
* [TF::Cloudflare::WafPackage](../resources/cloudflare/TF-Cloudflare-WafPackage/docs/README.md)
* [TF::Cloudflare::WafRule](../resources/cloudflare/TF-Cloudflare-WafRule/docs/README.md)
* [TF::Cloudflare::WorkerCronTrigger](../resources/cloudflare/TF-Cloudflare-WorkerCronTrigger/docs/README.md)
* [TF::Cloudflare::WorkerRoute](../resources/cloudflare/TF-Cloudflare-WorkerRoute/docs/README.md)
* [TF::Cloudflare::WorkerScript](../resources/cloudflare/TF-Cloudflare-WorkerScript/docs/README.md)
* [TF::Cloudflare::WorkersKvNamespace](../resources/cloudflare/TF-Cloudflare-WorkersKvNamespace/docs/README.md)
* [TF::Cloudflare::WorkersKv](../resources/cloudflare/TF-Cloudflare-WorkersKv/docs/README.md)
* [TF::Cloudflare::ZoneDnssec](../resources/cloudflare/TF-Cloudflare-ZoneDnssec/docs/README.md)
* [TF::Cloudflare::ZoneLockdown](../resources/cloudflare/TF-Cloudflare-ZoneLockdown/docs/README.md)
* [TF::Cloudflare::ZoneSettingsOverride](../resources/cloudflare/TF-Cloudflare-ZoneSettingsOverride/docs/README.md)
* [TF::Cloudflare::Zone](../resources/cloudflare/TF-Cloudflare-Zone/docs/README.md)