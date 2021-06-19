# Icinga2 Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/icinga2**. The below arguments may be included as the key/value or JSON properties in the secret:

* ``api_url`` - (Required) The root API URL of an Icinga2 server.

* ``api_user`` - (Required) The API username to use to
  authenticate to the Icinga2 server.

* ``api_password`` - (Required) The password to use to
  authenticate to the Icinga2 server.

* ``insecure_skip_tls_verify`` - (optional) Defaults to false. If set to true,
  verification of the Icinga2 server's SSL certificate is disabled. This is a security
  risk and should be avoided.


## Supported Resources

* [TF::Icinga2::Checkcommand](../resources/icinga2/TF-Icinga2-Checkcommand/docs/README.md)
* [TF::Icinga2::Host](../resources/icinga2/TF-Icinga2-Host/docs/README.md)
* [TF::Icinga2::Hostgroup](../resources/icinga2/TF-Icinga2-Hostgroup/docs/README.md)
* [TF::Icinga2::Notification](../resources/icinga2/TF-Icinga2-Notification/docs/README.md)
* [TF::Icinga2::Service](../resources/icinga2/TF-Icinga2-Service/docs/README.md)
* [TF::Icinga2::User](../resources/icinga2/TF-Icinga2-User/docs/README.md)