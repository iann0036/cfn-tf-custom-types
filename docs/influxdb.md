# InfluxDB Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/influxdb**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* ``url`` - (Optional) The root URL of a InfluxDB server. Defaults to
  `http://localhost:8086/`.

* ``username`` - (Optional) The name of the user to use when making requests.

* ``password`` - (Optional) The password to use when making requests.

* ``skip_ssl_verify`` - (Optional) If HTTPS enabled on server, and TLS/SSL
  certificate is, say, self-signed, can set to true to bypass what this client
  considers insecure server connections. May alternatively be set via the
  environment (i.e., ``INFLUXDB_SKIP_SSL_VERIFY=1``)

Use the navigation to the left to read about the available resources.


## Supported Resources

* [Terraform::InfluxDB::ContinuousQuery](../resources/influxdb/Terraform-InfluxDB-ContinuousQuery/docs/README.md)
* [Terraform::InfluxDB::Database](../resources/influxdb/Terraform-InfluxDB-Database/docs/README.md)
* [Terraform::InfluxDB::User](../resources/influxdb/Terraform-InfluxDB-User/docs/README.md)