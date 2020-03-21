# LogicMonitor Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/logicmonitor**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `api_id` - (Required) LogicMonitor API id.
* `api_key` - (Required) LogicMonitor API key.
* `company` - (Required) LogicMonitor company name.


## Supported Resources

* [Terraform::LogicMonitor::CollectorGroup](../resources/logicmonitor/Terraform-LogicMonitor-CollectorGroup/docs/README.md)
* [Terraform::LogicMonitor::Collector](../resources/logicmonitor/Terraform-LogicMonitor-Collector/docs/README.md)
* [Terraform::LogicMonitor::DashboardGroup](../resources/logicmonitor/Terraform-LogicMonitor-DashboardGroup/docs/README.md)
* [Terraform::LogicMonitor::Dashboard](../resources/logicmonitor/Terraform-LogicMonitor-Dashboard/docs/README.md)
* [Terraform::LogicMonitor::DeviceGroup](../resources/logicmonitor/Terraform-LogicMonitor-DeviceGroup/docs/README.md)
* [Terraform::LogicMonitor::Device](../resources/logicmonitor/Terraform-LogicMonitor-Device/docs/README.md)