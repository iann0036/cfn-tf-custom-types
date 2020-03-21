# Circonus Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/circonus**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `key` - (Required) The Circonus API Key.
* `api_url` - (Optional) The API URL to use to talk with. The default is `https://api.circonus.com/v2`.


## Supported Resources

* [Terraform::Circonus::Check](../resources/circonus/Terraform-Circonus-Check/docs/README.md)
* [Terraform::Circonus::ContactGroup](../resources/circonus/Terraform-Circonus-ContactGroup/docs/README.md)
* [Terraform::Circonus::Dashboard](../resources/circonus/Terraform-Circonus-Dashboard/docs/README.md)
* [Terraform::Circonus::Graph](../resources/circonus/Terraform-Circonus-Graph/docs/README.md)
* [Terraform::Circonus::Maintenance](../resources/circonus/Terraform-Circonus-Maintenance/docs/README.md)
* [Terraform::Circonus::MetricCluster](../resources/circonus/Terraform-Circonus-MetricCluster/docs/README.md)
* [Terraform::Circonus::Metric](../resources/circonus/Terraform-Circonus-Metric/docs/README.md)
* [Terraform::Circonus::RuleSetGroup](../resources/circonus/Terraform-Circonus-RuleSetGroup/docs/README.md)
* [Terraform::Circonus::RuleSet](../resources/circonus/Terraform-Circonus-RuleSet/docs/README.md)
* [Terraform::Circonus::Worksheet](../resources/circonus/Terraform-Circonus-Worksheet/docs/README.md)