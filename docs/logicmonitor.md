# LogicMonitor Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/logicmonitor**. The below arguments may be included as the key/value or JSON properties in the secret:

* `api_id` - (Required) LogicMonitor API id.
* `api_key` - (Required) LogicMonitor API key.
* `company` - (Required) LogicMonitor company name.


## Supported Resources

* [TF::LogicMonitor::CollectorGroup](../resources/logicmonitor/TF-LogicMonitor-CollectorGroup/docs/README.md)
* [TF::LogicMonitor::Collector](../resources/logicmonitor/TF-LogicMonitor-Collector/docs/README.md)
* [TF::LogicMonitor::DashboardGroup](../resources/logicmonitor/TF-LogicMonitor-DashboardGroup/docs/README.md)
* [TF::LogicMonitor::Dashboard](../resources/logicmonitor/TF-LogicMonitor-Dashboard/docs/README.md)
* [TF::LogicMonitor::DeviceGroup](../resources/logicmonitor/TF-LogicMonitor-DeviceGroup/docs/README.md)
* [TF::LogicMonitor::Device](../resources/logicmonitor/TF-LogicMonitor-Device/docs/README.md)