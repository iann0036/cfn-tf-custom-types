# Cloudflare Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/cloudflare**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `email` - (Optional) The email associated with the account.
* `api_key` - (Optional) The Cloudflare API key.
* `api_token` - (Optional) The Cloudflare API Token. This is an
  alternative to `email`+`api_key`. If both are specified, `api_token` will be
  used over `email`+`api_key` fields.
* `api_user_service_key` - (Optional) The Cloudflare API User Service Key. 
  This is used for a specific set of endpoints, such as creating Origin CA certificates.
* `rps` - (Optional) RPS limit to apply when making calls to the API. Default: 4.
* `retries` - (Optional) Maximum number of retries to perform when an API request fails. Default: 3.
* `min_backoff` - (Optional) Minimum backoff period in seconds after failed API calls. Default: 1.
* `max_backoff` - (Optional) Maximum backoff period in seconds after failed API calls Default: 30.
* `api_client_logging` - (Optional) Whether to print logs from the API client (using the default log library logger). Default: false.
* `account_id` - (Optional) Configure API client with this account ID, so calls use the account API rather than the (default) user API.
  This is required for other users in your account to have access to the resources you manage.


## Supported Resources

* [Terraform::Cloudflare::AccessApplication](../resources/cloudflare/Terraform-Cloudflare-AccessApplication/docs/README.md)
* [Terraform::Cloudflare::AccessGroup](../resources/cloudflare/Terraform-Cloudflare-AccessGroup/docs/README.md)
* [Terraform::Cloudflare::AccessIdentityProvider](../resources/cloudflare/Terraform-Cloudflare-AccessIdentityProvider/docs/README.md)
* [Terraform::Cloudflare::AccessPolicy](../resources/cloudflare/Terraform-Cloudflare-AccessPolicy/docs/README.md)
* [Terraform::Cloudflare::AccessRule](../resources/cloudflare/Terraform-Cloudflare-AccessRule/docs/README.md)
* [Terraform::Cloudflare::AccessServiceToken](../resources/cloudflare/Terraform-Cloudflare-AccessServiceToken/docs/README.md)
* [Terraform::Cloudflare::AccountMember](../resources/cloudflare/Terraform-Cloudflare-AccountMember/docs/README.md)
* [Terraform::Cloudflare::Argo](../resources/cloudflare/Terraform-Cloudflare-Argo/docs/README.md)
* [Terraform::Cloudflare::CustomPages](../resources/cloudflare/Terraform-Cloudflare-CustomPages/docs/README.md)
* [Terraform::Cloudflare::CustomSsl](../resources/cloudflare/Terraform-Cloudflare-CustomSsl/docs/README.md)
* [Terraform::Cloudflare::Filter](../resources/cloudflare/Terraform-Cloudflare-Filter/docs/README.md)
* [Terraform::Cloudflare::FirewallRule](../resources/cloudflare/Terraform-Cloudflare-FirewallRule/docs/README.md)
* [Terraform::Cloudflare::LoadBalancerMonitor](../resources/cloudflare/Terraform-Cloudflare-LoadBalancerMonitor/docs/README.md)
* [Terraform::Cloudflare::LoadBalancerPool](../resources/cloudflare/Terraform-Cloudflare-LoadBalancerPool/docs/README.md)
* [Terraform::Cloudflare::LoadBalancer](../resources/cloudflare/Terraform-Cloudflare-LoadBalancer/docs/README.md)
* [Terraform::Cloudflare::LogpushJob](../resources/cloudflare/Terraform-Cloudflare-LogpushJob/docs/README.md)
* [Terraform::Cloudflare::OriginCaCertificate](../resources/cloudflare/Terraform-Cloudflare-OriginCaCertificate/docs/README.md)
* [Terraform::Cloudflare::PageRule](../resources/cloudflare/Terraform-Cloudflare-PageRule/docs/README.md)
* [Terraform::Cloudflare::RateLimit](../resources/cloudflare/Terraform-Cloudflare-RateLimit/docs/README.md)
* [Terraform::Cloudflare::Record](../resources/cloudflare/Terraform-Cloudflare-Record/docs/README.md)
* [Terraform::Cloudflare::SpectrumApplication](../resources/cloudflare/Terraform-Cloudflare-SpectrumApplication/docs/README.md)
* [Terraform::Cloudflare::WafGroup](../resources/cloudflare/Terraform-Cloudflare-WafGroup/docs/README.md)
* [Terraform::Cloudflare::WafPackage](../resources/cloudflare/Terraform-Cloudflare-WafPackage/docs/README.md)
* [Terraform::Cloudflare::WafRule](../resources/cloudflare/Terraform-Cloudflare-WafRule/docs/README.md)
* [Terraform::Cloudflare::WorkerRoute](../resources/cloudflare/Terraform-Cloudflare-WorkerRoute/docs/README.md)
* [Terraform::Cloudflare::WorkerScript](../resources/cloudflare/Terraform-Cloudflare-WorkerScript/docs/README.md)
* [Terraform::Cloudflare::WorkersKvNamespace](../resources/cloudflare/Terraform-Cloudflare-WorkersKvNamespace/docs/README.md)
* [Terraform::Cloudflare::WorkersKv](../resources/cloudflare/Terraform-Cloudflare-WorkersKv/docs/README.md)
* [Terraform::Cloudflare::ZoneLockdown](../resources/cloudflare/Terraform-Cloudflare-ZoneLockdown/docs/README.md)
* [Terraform::Cloudflare::ZoneSettingsOverride](../resources/cloudflare/Terraform-Cloudflare-ZoneSettingsOverride/docs/README.md)
* [Terraform::Cloudflare::Zone](../resources/cloudflare/Terraform-Cloudflare-Zone/docs/README.md)