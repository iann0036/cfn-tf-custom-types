# Spotinst Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/spotinst**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Required) A Personal API Access Token issued by Spotinst.
* `account` - (Optional) A valid Spotinst account ID.
* `feature_flags` - (Optional) Spotinst SDK feature flags.


## Supported Resources

* [TF::Spotinst::ElastigroupAwsBeanstalk](../resources/spotinst/TF-Spotinst-ElastigroupAwsBeanstalk/docs/README.md)
* [TF::Spotinst::ElastigroupAwsSuspension](../resources/spotinst/TF-Spotinst-ElastigroupAwsSuspension/docs/README.md)
* [TF::Spotinst::ElastigroupAws](../resources/spotinst/TF-Spotinst-ElastigroupAws/docs/README.md)
* [TF::Spotinst::ElastigroupAzureV3](../resources/spotinst/TF-Spotinst-ElastigroupAzureV3/docs/README.md)
* [TF::Spotinst::ElastigroupAzure](../resources/spotinst/TF-Spotinst-ElastigroupAzure/docs/README.md)
* [TF::Spotinst::ElastigroupGcp](../resources/spotinst/TF-Spotinst-ElastigroupGcp/docs/README.md)
* [TF::Spotinst::ElastigroupGke](../resources/spotinst/TF-Spotinst-ElastigroupGke/docs/README.md)
* [TF::Spotinst::HealthCheck](../resources/spotinst/TF-Spotinst-HealthCheck/docs/README.md)
* [TF::Spotinst::ManagedInstanceAws](../resources/spotinst/TF-Spotinst-ManagedInstanceAws/docs/README.md)
* [TF::Spotinst::MrscalerAws](../resources/spotinst/TF-Spotinst-MrscalerAws/docs/README.md)
* [TF::Spotinst::MultaiBalancer](../resources/spotinst/TF-Spotinst-MultaiBalancer/docs/README.md)
* [TF::Spotinst::MultaiDeployment](../resources/spotinst/TF-Spotinst-MultaiDeployment/docs/README.md)
* [TF::Spotinst::MultaiListener](../resources/spotinst/TF-Spotinst-MultaiListener/docs/README.md)
* [TF::Spotinst::MultaiRoutingRule](../resources/spotinst/TF-Spotinst-MultaiRoutingRule/docs/README.md)
* [TF::Spotinst::MultaiTargetSet](../resources/spotinst/TF-Spotinst-MultaiTargetSet/docs/README.md)
* [TF::Spotinst::MultaiTarget](../resources/spotinst/TF-Spotinst-MultaiTarget/docs/README.md)
* [TF::Spotinst::OceanAksVirtualNodeGroup](../resources/spotinst/TF-Spotinst-OceanAksVirtualNodeGroup/docs/README.md)
* [TF::Spotinst::OceanAks](../resources/spotinst/TF-Spotinst-OceanAks/docs/README.md)
* [TF::Spotinst::OceanAwsLaunchSpec](../resources/spotinst/TF-Spotinst-OceanAwsLaunchSpec/docs/README.md)
* [TF::Spotinst::OceanAws](../resources/spotinst/TF-Spotinst-OceanAws/docs/README.md)
* [TF::Spotinst::OceanEcsLaunchSpec](../resources/spotinst/TF-Spotinst-OceanEcsLaunchSpec/docs/README.md)
* [TF::Spotinst::OceanEcs](../resources/spotinst/TF-Spotinst-OceanEcs/docs/README.md)
* [TF::Spotinst::OceanGkeImport](../resources/spotinst/TF-Spotinst-OceanGkeImport/docs/README.md)
* [TF::Spotinst::OceanGkeLaunchSpecImport](../resources/spotinst/TF-Spotinst-OceanGkeLaunchSpecImport/docs/README.md)
* [TF::Spotinst::OceanGkeLaunchSpec](../resources/spotinst/TF-Spotinst-OceanGkeLaunchSpec/docs/README.md)
* [TF::Spotinst::Subscription](../resources/spotinst/TF-Spotinst-Subscription/docs/README.md)