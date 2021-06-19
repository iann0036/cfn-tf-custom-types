# ConfigCat Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/configcat**. The below arguments may be included as the key/value or JSON properties in the secret:

* `basic_auth_username` - (Required) Get your `basic_auth_username` at [ConfigCat Public API credentials](https://app.configcat.com/my-account/public-api-credentials).  
This can also be sourced from the `CONFIGCAT_BASIC_AUTH_USERNAME` Environment Variable.

* `basic_auth_password` - (Required) Get your `basic_auth_password` at [ConfigCat Public API credentials](https://app.configcat.com/my-account/public-api-credentials).  
This can also be sourced from the `CONFIGCAT_BASIC_AUTH_PASSWORD` Environment Variable.

* `base_path` - (Optional) ConfigCat Public Management API's `base_path`. Defaults to https://api.configcat.com.  
This can also be sourced from the `CONFIGCAT_BASE_PATH` Environment Variable.


## Supported Resources

* [TF::ConfigCat::Config](../resources/configcat/TF-ConfigCat-Config/docs/README.md)
* [TF::ConfigCat::Environment](../resources/configcat/TF-ConfigCat-Environment/docs/README.md)
* [TF::ConfigCat::Product](../resources/configcat/TF-ConfigCat-Product/docs/README.md)
* [TF::ConfigCat::SettingTag](../resources/configcat/TF-ConfigCat-SettingTag/docs/README.md)
* [TF::ConfigCat::SettingValue](../resources/configcat/TF-ConfigCat-SettingValue/docs/README.md)
* [TF::ConfigCat::Setting](../resources/configcat/TF-ConfigCat-Setting/docs/README.md)
* [TF::ConfigCat::Tag](../resources/configcat/TF-ConfigCat-Tag/docs/README.md)