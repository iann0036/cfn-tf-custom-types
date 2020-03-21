# MySQL Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/mysql**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `endpoint` - (Required) The address of the MySQL server to use. Most often a "hostname:port" pair, but may also be an absolute path to a Unix socket when the host OS is Unix-compatible.
* `tls` - (Optional) The TLS configuration. One of `false`, `true`, or `skip-verify`. Defaults to `false`.
* `max_conn_lifetime_sec` - (Optional) Sets the maximum amount of time a connection may be reused. If d <= 0, connections are reused forever.
* `max_open_conns` - (Optional) Sets the maximum number of open connections to the database. If n <= 0, then there is no limit on the number of open connections.
* `authentication_plugin` - (Optional) Sets the authentication plugin, it can be one of the following: `native` or `cleartext`. Defaults to `native`.


## Supported Resources

* [Terraform::MySQL::Database](../resources/mysql/Terraform-MySQL-Database/docs/README.md)
* [Terraform::MySQL::Grant](../resources/mysql/Terraform-MySQL-Grant/docs/README.md)
* [Terraform::MySQL::Role](../resources/mysql/Terraform-MySQL-Role/docs/README.md)
* [Terraform::MySQL::UserPassword](../resources/mysql/Terraform-MySQL-UserPassword/docs/README.md)
* [Terraform::MySQL::User](../resources/mysql/Terraform-MySQL-User/docs/README.md)