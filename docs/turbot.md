# Turbot Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/turbot**. The below arguments may be included as the key/value or JSON properties in the secret:

* `workspace`  - Turbot workspace endpoint, e.g. `https://example.com/api/latest/graphql`.
* `access_key` - Turbot access key, e.g. `1wxxxxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxe6`.
* `secret_key` - Turbot secret key, e.g. `b90xxxxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxnp`.
* `profile`    - Turbot workspace profile, e.g. `testProfile`.
* `credentials_file`    - Turbot shared credentials path, e.g. `user/testUser/{{credential_file_path}}`.


## Supported Resources

* [TF::Turbot::File](../resources/turbot/TF-Turbot-File/docs/README.md)
* [TF::Turbot::Folder](../resources/turbot/TF-Turbot-Folder/docs/README.md)
* [TF::Turbot::GoogleDirectory](../resources/turbot/TF-Turbot-GoogleDirectory/docs/README.md)
* [TF::Turbot::GrantActivation](../resources/turbot/TF-Turbot-GrantActivation/docs/README.md)
* [TF::Turbot::Grant](../resources/turbot/TF-Turbot-Grant/docs/README.md)
* [TF::Turbot::LdapDirectory](../resources/turbot/TF-Turbot-LdapDirectory/docs/README.md)
* [TF::Turbot::LocalDirectoryUser](../resources/turbot/TF-Turbot-LocalDirectoryUser/docs/README.md)
* [TF::Turbot::LocalDirectory](../resources/turbot/TF-Turbot-LocalDirectory/docs/README.md)
* [TF::Turbot::Mod](../resources/turbot/TF-Turbot-Mod/docs/README.md)
* [TF::Turbot::PolicySetting](../resources/turbot/TF-Turbot-PolicySetting/docs/README.md)
* [TF::Turbot::Profile](../resources/turbot/TF-Turbot-Profile/docs/README.md)
* [TF::Turbot::Resource](../resources/turbot/TF-Turbot-Resource/docs/README.md)
* [TF::Turbot::SamlDirectory](../resources/turbot/TF-Turbot-SamlDirectory/docs/README.md)
* [TF::Turbot::ShadowResource](../resources/turbot/TF-Turbot-ShadowResource/docs/README.md)
* [TF::Turbot::SmartFolderAttachment](../resources/turbot/TF-Turbot-SmartFolderAttachment/docs/README.md)
* [TF::Turbot::SmartFolder](../resources/turbot/TF-Turbot-SmartFolder/docs/README.md)
* [TF::Turbot::TurbotDirectory](../resources/turbot/TF-Turbot-TurbotDirectory/docs/README.md)