# Brightbox Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/brightbox**. The below arguments may be included as the key/value or JSON properties in the secret:

* `apiclient` - (optional) This is the Brightbox client id for an
account.

* `apisecret` - (optional) This is the Brightbox client secret. This can
also be specified with the `BRIGHTBOX_CLIENT_SECRET` shell environment
variable.

* `username` - (optional) This is the Brightbox user logon. This can
also be specified with the `BRIGHTBOX_USER_NAME` shell environment
variable.

* `password` - (optional) This is the Brightbox user logon password. This
can also be specified with the `BRIGHTBOX_PASSWORD` shell environment
variable.

* `account` - (optional) This is the Brightbox account you wish to
operate upon.

* `apiurl` - (Optional) Use this to override the default endpoint URL
constructed for the region. It's typically used to connect to custom
Brightbox endpoints.

~> **NOTE:** At least one of `username` or `apiclient` must be specified.


## Supported Resources

* [TF::Brightbox::ApiClient](../resources/brightbox/TF-Brightbox-ApiClient/docs/README.md)
* [TF::Brightbox::Cloudip](../resources/brightbox/TF-Brightbox-Cloudip/docs/README.md)
* [TF::Brightbox::ConfigMap](../resources/brightbox/TF-Brightbox-ConfigMap/docs/README.md)
* [TF::Brightbox::DatabaseServer](../resources/brightbox/TF-Brightbox-DatabaseServer/docs/README.md)
* [TF::Brightbox::FirewallPolicy](../resources/brightbox/TF-Brightbox-FirewallPolicy/docs/README.md)
* [TF::Brightbox::FirewallRule](../resources/brightbox/TF-Brightbox-FirewallRule/docs/README.md)
* [TF::Brightbox::LoadBalancer](../resources/brightbox/TF-Brightbox-LoadBalancer/docs/README.md)
* [TF::Brightbox::OrbitContainer](../resources/brightbox/TF-Brightbox-OrbitContainer/docs/README.md)
* [TF::Brightbox::ServerGroup](../resources/brightbox/TF-Brightbox-ServerGroup/docs/README.md)
* [TF::Brightbox::Server](../resources/brightbox/TF-Brightbox-Server/docs/README.md)