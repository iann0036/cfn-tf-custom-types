# Netlify Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/netlify**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `token` - (Required) Environment Variable: `NETLIFY_TOKEN`
* `base_url` - (Optional) Environment Variable: `NETLIFY_BASE_URL`


## Supported Resources

* [Terraform::Netlify::BuildHook](../resources/netlify/Terraform-Netlify-BuildHook/docs/README.md)
* [Terraform::Netlify::DeployKey](../resources/netlify/Terraform-Netlify-DeployKey/docs/README.md)
* [Terraform::Netlify::Hook](../resources/netlify/Terraform-Netlify-Hook/docs/README.md)
* [Terraform::Netlify::Site](../resources/netlify/Terraform-Netlify-Site/docs/README.md)