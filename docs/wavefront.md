# Wavefront Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/wavefront**. The below arguments may be included as the key/value or JSON properties in the secret:

* `address` - (Optional) this is the URL of your cluster that you access Wavefront from without the 
leading `https://` or trailing `/` (e.g. `https://longboard.wavefront.com/` becomes `longboard.wavefront.com`)

* `token` - (Optional) this is a either a Users token or Service Account token with permissions necessary 
to manage your Wavefront account. 

* `http_proxy` - (Optional) The proxy type is determined by the URL scheme. `http`, `https`, and `socks5` are supported.  
If the scheme is empty `http` is assumed.


## Supported Resources

* [TF::Wavefront::AlertTarget](../resources/wavefront/TF-Wavefront-AlertTarget/docs/README.md)
* [TF::Wavefront::Alert](../resources/wavefront/TF-Wavefront-Alert/docs/README.md)
* [TF::Wavefront::CloudIntegrationAppDynamics](../resources/wavefront/TF-Wavefront-CloudIntegrationAppDynamics/docs/README.md)
* [TF::Wavefront::CloudIntegrationAwsExternalId](../resources/wavefront/TF-Wavefront-CloudIntegrationAwsExternalId/docs/README.md)
* [TF::Wavefront::CloudIntegrationAzureActivityLog](../resources/wavefront/TF-Wavefront-CloudIntegrationAzureActivityLog/docs/README.md)
* [TF::Wavefront::CloudIntegrationAzure](../resources/wavefront/TF-Wavefront-CloudIntegrationAzure/docs/README.md)
* [TF::Wavefront::CloudIntegrationCloudtrail](../resources/wavefront/TF-Wavefront-CloudIntegrationCloudtrail/docs/README.md)
* [TF::Wavefront::CloudIntegrationCloudwatch](../resources/wavefront/TF-Wavefront-CloudIntegrationCloudwatch/docs/README.md)
* [TF::Wavefront::CloudIntegrationEc2](../resources/wavefront/TF-Wavefront-CloudIntegrationEc2/docs/README.md)
* [TF::Wavefront::CloudIntegrationGcpBilling](../resources/wavefront/TF-Wavefront-CloudIntegrationGcpBilling/docs/README.md)
* [TF::Wavefront::CloudIntegrationGcp](../resources/wavefront/TF-Wavefront-CloudIntegrationGcp/docs/README.md)
* [TF::Wavefront::CloudIntegrationNewrelic](../resources/wavefront/TF-Wavefront-CloudIntegrationNewrelic/docs/README.md)
* [TF::Wavefront::CloudIntegrationTesla](../resources/wavefront/TF-Wavefront-CloudIntegrationTesla/docs/README.md)
* [TF::Wavefront::DashboardJson](../resources/wavefront/TF-Wavefront-DashboardJson/docs/README.md)
* [TF::Wavefront::Dashboard](../resources/wavefront/TF-Wavefront-Dashboard/docs/README.md)
* [TF::Wavefront::DerivedMetric](../resources/wavefront/TF-Wavefront-DerivedMetric/docs/README.md)
* [TF::Wavefront::ExternalLink](../resources/wavefront/TF-Wavefront-ExternalLink/docs/README.md)
* [TF::Wavefront::IngestionPolicy](../resources/wavefront/TF-Wavefront-IngestionPolicy/docs/README.md)
* [TF::Wavefront::MaintenanceWindow](../resources/wavefront/TF-Wavefront-MaintenanceWindow/docs/README.md)
* [TF::Wavefront::Role](../resources/wavefront/TF-Wavefront-Role/docs/README.md)
* [TF::Wavefront::ServiceAccount](../resources/wavefront/TF-Wavefront-ServiceAccount/docs/README.md)
* [TF::Wavefront::UserGroup](../resources/wavefront/TF-Wavefront-UserGroup/docs/README.md)
* [TF::Wavefront::User](../resources/wavefront/TF-Wavefront-User/docs/README.md)