# CloudSigma Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/cloudsigma**. The below arguments may be included as the key/value or JSON properties in the secret:

* `username` - (Required) Your Cloudsigma email address.
* `password` - (Required) Your Cloudsigma password.cloudsigma.com/api/2.0/` if unset).


## Supported Resources

* [TF::CloudSigma::Acl](../resources/cloudsigma/TF-CloudSigma-Acl/docs/README.md)
* [TF::CloudSigma::Drive](../resources/cloudsigma/TF-CloudSigma-Drive/docs/README.md)
* [TF::CloudSigma::FirewallPolicy](../resources/cloudsigma/TF-CloudSigma-FirewallPolicy/docs/README.md)
* [TF::CloudSigma::RemoteSnapshot](../resources/cloudsigma/TF-CloudSigma-RemoteSnapshot/docs/README.md)
* [TF::CloudSigma::Server](../resources/cloudsigma/TF-CloudSigma-Server/docs/README.md)
* [TF::CloudSigma::Snapshot](../resources/cloudsigma/TF-CloudSigma-Snapshot/docs/README.md)
* [TF::CloudSigma::SshKey](../resources/cloudsigma/TF-CloudSigma-SshKey/docs/README.md)
* [TF::CloudSigma::Tag](../resources/cloudsigma/TF-CloudSigma-Tag/docs/README.md)