# NS1 Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/ns1**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `apikey` - (Required) NS1 API token.
* `version` - (Optional, but recommended if you don't like surprises) From
  output of `terraform init`.
* `endpoint` - (Optional) NS1 API endpoint. For managed clients, this normally
  should not be set.
* `ignore_ssl` - (Optional) This normally does not need to be set.
* `enable_ddi` - (Optional) This sets the permission schema to a DDI-compatible schema. 
Users of the managed SaaS product should not need to set this.
Users of DDI should set this to true if managing teams, users, or API keys through this provider.
* `rate_limit_parallelism` - (Optional) Integer for parallelism amount
  (terraform's default is 10). If set, uses an alternate strategy to handle
  rate limiting from the NS1 API. Give this a try if you are processing a large
  number of resource and running into `429` rate-limiting errors.


## Supported Resources

* [Terraform::NS1::Apikey](../resources/ns1/Terraform-NS1-Apikey/docs/README.md)
* [Terraform::NS1::Datafeed](../resources/ns1/Terraform-NS1-Datafeed/docs/README.md)
* [Terraform::NS1::Datasource](../resources/ns1/Terraform-NS1-Datasource/docs/README.md)
* [Terraform::NS1::Monitoringjob](../resources/ns1/Terraform-NS1-Monitoringjob/docs/README.md)
* [Terraform::NS1::Notifylist](../resources/ns1/Terraform-NS1-Notifylist/docs/README.md)
* [Terraform::NS1::Record](../resources/ns1/Terraform-NS1-Record/docs/README.md)
* [Terraform::NS1::Team](../resources/ns1/Terraform-NS1-Team/docs/README.md)
* [Terraform::NS1::User](../resources/ns1/Terraform-NS1-User/docs/README.md)
* [Terraform::NS1::Zone](../resources/ns1/Terraform-NS1-Zone/docs/README.md)