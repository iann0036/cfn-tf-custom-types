# phoenixNAP Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/pnap**. The below arguments may be included as the key/value or JSON properties in the secret:

* `hostname` - (Required) Server hostname.
* `description` - Server description.
* `os` - (Required) The server’s OS ID used when the server was created (e.g., ubuntu/bionic, centos/centos7). For a full list of available operating systems visit [API docs](https://developers.phoenixnap.com/docs/bmc/1).
* `type` - (Required) Server type ID. Cannot be changed once a server is created (e.g., s1.c1.small, s1.c1.medium). 
* `location` - (Required) Server Location ID. Cannot be changed once a server is created (e.g., PHX).
* `ssh_keys` - (Required) A list of SSH Keys that will be installed on the Linux server. Must contain at least 1 item.
* `action` - Action to perform on server. Allowed actions are: reboot, reset, powered-on, powered-off, shutdown.


## Supported Resources

* [TF::PNAP::Server](../resources/pnap/TF-PNAP-Server/docs/README.md)