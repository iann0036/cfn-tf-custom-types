# StackPath Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/stackpath**. The below arguments may be included as the key/value or JSON properties in the secret:

* `stack_id` - (Required) This is the ID of stack that all new services are provisioned to. Stacks are folder-like organizational units on the StackPath platform and are typically used to organize services by project or user. Stack IDs are UUID v4 formatted strings.
* `client_id` - (Required) This is the API client ID of the StackPath user that will interact with Terraform. All services provisioned at StackPath through Terraform belong to their creating user.
* `client_secret` - (Required) This is the API client secret of the StackPath user that will interact with Terraform. Client secrets should be stored securely and not exposed to the public.


## Supported Resources

* [TF::StackPath::ComputeNetworkPolicy](../resources/stackpath/TF-StackPath-ComputeNetworkPolicy/docs/README.md)
* [TF::StackPath::ComputeWorkload](../resources/stackpath/TF-StackPath-ComputeWorkload/docs/README.md)
* [TF::StackPath::ObjectStorageBucket](../resources/stackpath/TF-StackPath-ObjectStorageBucket/docs/README.md)