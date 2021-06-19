# Palo Alto Networks Prisma Cloud Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/prismacloud**. The below arguments may be included as the key/value or JSON properties in the secret:

* `url` - (Env: `PRISMACLOUD_URL`) The API URL without the leading protocol.
* `username` - (Env: `PRISMACLOUD_USERNAME`) Access key ID.
* `password` - (Env: `PRISMACLOUD_PASSWORD`) Secret key.
* `customer_name` - (Env: `PRISMACLOUD_CUSTOMER_NAME`) Customer name.
* `protocol` - (Env: `PRISMACLOUD_PROTOCOL`) The protocol.  Valid values are `https` or `http`.
* `port` - (Env: `PRISMACLOUD_PORT`, int) If the port is non-standard for the protocol, the port number to use.
* `timeout` - The default timeout (in seconds) for all communications with Prisma Cloud (default: `90`).
* `skip_ssl_cert_verification` - (Env: `PRISMACLOUD_SKIP_SSL_CERT_VERIFICATION`, bool) Skip SSL certificate verification.
* `logging` - Map of logging options for the API connection.  Valid values are `quiet` (disable logging), `action`, `path`, `send`, and `receive`.
* `disable_reconnect` - (bool) Prisma Cloud invalidates authenticated sessions after 10minutes.  By default the provider will silently get a new JSON web token and continue deploying the plan.  If you do not want the provider to fetch a new JSON web token, set this to `true`.
* `json_web_token` - (Env: `PRISMACLOUD_JSON_WEB_TOKEN`) A JSON web token.  These are only valid for 10 minutes once issued.  If this is specified but not the `username` / `password` then the provider will not have a way to reauthenticate once the JSON web token expires.
* `json_config_file` - (Env: `PRISMACLOUD_JSON_CONFIG_FILE`) Retrieve the provider configuration from this JSON file.  When retrieving params from the JSON configuration file, the param names are the same as the provider params, except that underscores in provider params become hyphens in the JSON config file.  For example, the provider param `json_web_token` is `json-web-token` in the config file.


## Supported Resources

* [TF::PrismaCloud::AccountGroup](../resources/prismacloud/TF-PrismaCloud-AccountGroup/docs/README.md)
* [TF::PrismaCloud::AlertRule](../resources/prismacloud/TF-PrismaCloud-AlertRule/docs/README.md)
* [TF::PrismaCloud::CloudAccount](../resources/prismacloud/TF-PrismaCloud-CloudAccount/docs/README.md)
* [TF::PrismaCloud::ComplianceStandardRequirementSection](../resources/prismacloud/TF-PrismaCloud-ComplianceStandardRequirementSection/docs/README.md)
* [TF::PrismaCloud::ComplianceStandardRequirement](../resources/prismacloud/TF-PrismaCloud-ComplianceStandardRequirement/docs/README.md)
* [TF::PrismaCloud::ComplianceStandard](../resources/prismacloud/TF-PrismaCloud-ComplianceStandard/docs/README.md)
* [TF::PrismaCloud::EnterpriseSettings](../resources/prismacloud/TF-PrismaCloud-EnterpriseSettings/docs/README.md)
* [TF::PrismaCloud::Integration](../resources/prismacloud/TF-PrismaCloud-Integration/docs/README.md)
* [TF::PrismaCloud::Policy](../resources/prismacloud/TF-PrismaCloud-Policy/docs/README.md)
* [TF::PrismaCloud::RqlSearch](../resources/prismacloud/TF-PrismaCloud-RqlSearch/docs/README.md)
* [TF::PrismaCloud::SavedSearch](../resources/prismacloud/TF-PrismaCloud-SavedSearch/docs/README.md)
* [TF::PrismaCloud::UserRole](../resources/prismacloud/TF-PrismaCloud-UserRole/docs/README.md)