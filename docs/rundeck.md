# Rundeck Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/rundeck**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* ``url`` - (Required) The root URL of a Rundeck server.

* ``api_version`` - (Optional) The API version of the server. Defaults to `14`, the
  minium supported version. 

* ``auth_token`` - (Required) The API auth token to use when making requests.

Use the navigation to the left to read about the available resources.


## Supported Resources

* [Terraform::Rundeck::AclPolicy](../resources/rundeck/Terraform-Rundeck-AclPolicy/docs/README.md)
* [Terraform::Rundeck::Job](../resources/rundeck/Terraform-Rundeck-Job/docs/README.md)
* [Terraform::Rundeck::PrivateKey](../resources/rundeck/Terraform-Rundeck-PrivateKey/docs/README.md)
* [Terraform::Rundeck::Project](../resources/rundeck/Terraform-Rundeck-Project/docs/README.md)
* [Terraform::Rundeck::PublicKey](../resources/rundeck/Terraform-Rundeck-PublicKey/docs/README.md)