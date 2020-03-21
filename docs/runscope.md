# RunScope Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/runscope**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `access_token` - (Required) The Runscope access token.
* `api_url` - (Optional) If set, specifies the Runscope api url, this
   defaults to `"https://api.runscope.com`.


## Supported Resources

* [Terraform::RunScope::Bucket](../resources/runscope/Terraform-RunScope-Bucket/docs/README.md)
* [Terraform::RunScope::Environment](../resources/runscope/Terraform-RunScope-Environment/docs/README.md)
* [Terraform::RunScope::Schedule](../resources/runscope/Terraform-RunScope-Schedule/docs/README.md)
* [Terraform::RunScope::Step](../resources/runscope/Terraform-RunScope-Step/docs/README.md)
* [Terraform::RunScope::Test](../resources/runscope/Terraform-RunScope-Test/docs/README.md)