# Docker Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/docker**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `host` - (Required) This is the address to the Docker host.

* `cert_path` - (Optional) Path to a directory with certificate information
  for connecting to the Docker host via TLS. It is expected that the 3 files `{ca, cert, key}.pem` 
  are present in the path. If the path is blank, the `DOCKER_CERT_PATH` will also be checked.

* `ca_material`, `cert_material`, `key_material`, - (Optional) Content of `ca.pem`, `cert.pem`, and `key.pem` files
  for TLS authentication. Cannot be used together with `cert_path`. If `ca_material` is omitted
  the client does not check the servers certificate chain and host name.

* `registry_auth` - (Optional) A block specifying the credentials for a target
  v2 Docker registry.
   
  * `address` - (Required) The address of the registry.
 
  * `username` - (Optional) The username to use for authenticating to the registry.
  Cannot be used with the `config_file` option. If this is blank, the `DOCKER_REGISTRY_USER`
  will also be checked.
 
  * `password` - (Optional) The password to use for authenticating to the registry.
  Cannot be used with the `config_file` option. If this is blank, the `DOCKER_REGISTRY_PASS`
  will also be checked.
 
  * `config_file` - (Optional) The path to a config file containing credentials for
  authenticating to the registry. Cannot be used with the `username`/`password` or `config_file_content` options.
  If this is blank, the `DOCKER_CONFIG` will also be checked.
  
  * `config_file_content` - (Optional) The content of a config file as string containing credentials for
  authenticating to the registry. Cannot be used with the `username`/`password` or `config_file` options.
 
 

~> **NOTE on Certificates and `docker-machine`:**  As per [Docker Remote API
documentation](https://docs.docker.com/engine/reference/api/docker_remote_api/),
in any docker-machine environment, the Docker daemon uses an encrypted TCP
socket (TLS) and requires `cert_path` for a successful connection. As an alternative,
if using `docker-machine`, run `eval $(docker-machine env <machine-name>)` prior
to running Terraform, and the host and certificate path will be extracted from
the environment.


## Supported Resources

* [Terraform::Docker::Config](../resources/docker/Terraform-Docker-Config/docs/README.md)
* [Terraform::Docker::Container](../resources/docker/Terraform-Docker-Container/docs/README.md)
* [Terraform::Docker::Image](../resources/docker/Terraform-Docker-Image/docs/README.md)
* [Terraform::Docker::Network](../resources/docker/Terraform-Docker-Network/docs/README.md)
* [Terraform::Docker::Secret](../resources/docker/Terraform-Docker-Secret/docs/README.md)
* [Terraform::Docker::Service](../resources/docker/Terraform-Docker-Service/docs/README.md)
* [Terraform::Docker::Volume](../resources/docker/Terraform-Docker-Volume/docs/README.md)