# Dyn Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/dyn**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `customer_name` - (Required) The Dyn customer name.
* `username` - (Required) The Dyn username.
* `password` - (Required) The Dyn password.


## Supported Resources

* [Terraform::Dyn::Record](../resources/dyn/Terraform-Dyn-Record/docs/README.md)