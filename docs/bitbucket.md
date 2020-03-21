# Bitbucket Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/bitbucket**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `username` - (Required) Your username used to connect to bitbucket. `BITBUCKET_USERNAME`

* `password` - (Required) Your password used to connect to bitbucket. `BITBUCKET_PASSWORD`


## Supported Resources

* [Terraform::Bitbucket::BranchRestriction](../resources/bitbucket/Terraform-Bitbucket-BranchRestriction/docs/README.md)
* [Terraform::Bitbucket::DefaultReviewers](../resources/bitbucket/Terraform-Bitbucket-DefaultReviewers/docs/README.md)
* [Terraform::Bitbucket::Hook](../resources/bitbucket/Terraform-Bitbucket-Hook/docs/README.md)
* [Terraform::Bitbucket::Project](../resources/bitbucket/Terraform-Bitbucket-Project/docs/README.md)
* [Terraform::Bitbucket::RepositoryVariable](../resources/bitbucket/Terraform-Bitbucket-RepositoryVariable/docs/README.md)
* [Terraform::Bitbucket::Repository](../resources/bitbucket/Terraform-Bitbucket-Repository/docs/README.md)