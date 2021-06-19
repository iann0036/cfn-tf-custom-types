# Circonus Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/circonus**. The below arguments may be included as the key/value or JSON properties in the secret:

* `key` - (Required) The Circonus API Key.
* `api_url` - (Optional) The API URL to use to talk with. The default is `https://api.circonus.com/v2`.


## Supported Resources

* [TF::Circonus::Check](../resources/circonus/TF-Circonus-Check/docs/README.md)
* [TF::Circonus::ContactGroup](../resources/circonus/TF-Circonus-ContactGroup/docs/README.md)
* [TF::Circonus::Dashboard](../resources/circonus/TF-Circonus-Dashboard/docs/README.md)
* [TF::Circonus::Graph](../resources/circonus/TF-Circonus-Graph/docs/README.md)
* [TF::Circonus::Maintenance](../resources/circonus/TF-Circonus-Maintenance/docs/README.md)
* [TF::Circonus::Metric](../resources/circonus/TF-Circonus-Metric/docs/README.md)
* [TF::Circonus::OverlaySet](../resources/circonus/TF-Circonus-OverlaySet/docs/README.md)
* [TF::Circonus::RuleSetGroup](../resources/circonus/TF-Circonus-RuleSetGroup/docs/README.md)
* [TF::Circonus::RuleSet](../resources/circonus/TF-Circonus-RuleSet/docs/README.md)
* [TF::Circonus::Worksheet](../resources/circonus/TF-Circonus-Worksheet/docs/README.md)