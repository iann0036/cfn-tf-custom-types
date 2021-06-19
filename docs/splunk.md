# Splunk Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/splunk**. The below arguments may be included as the key/value or JSON properties in the secret:

* `url` or `SPLUNK_URL` - (Required) The URL for the Splunk instance to be configured. (The provider uses `https` as the default schema as prefix to the URL)
* `username` or `SPLUNK_USERNAME`  - (Optional) The username to access the Splunk instance to be configured.
* `password` or `SPLUNK_PASSWORD` - (Optional) The password to access the Splunk instance to be configured.
* `auth_token` or `SPLUNK_AUTH_TOKEN` - (Optional) Use auth token instead of username and password to configure Splunk instance.
If specified, auth token takes priority over username/password.
* `insecure_skip_verify` or `SPLUNK_INSECURE_SKIP_VERIFY` - (Optional) Insecure skip verification flag (Defaults to `true`)
* `timeout` or `SPLUNK_TIMEOUT` -  (Optional) Timeout when making calls to Splunk server. (Defaults to `60 seconds`)

(NOTE: Auth token can only be used with certain type of Splunk deployments.
Read more on authentication with tokens here: https://docs.splunk.com/Documentation/Splunk/latest/Security/Setupauthenticationwithtokens)


## Supported Resources

* [TF::Splunk::AdminSamlGroups](../resources/splunk/TF-Splunk-AdminSamlGroups/docs/README.md)
* [TF::Splunk::AppsLocal](../resources/splunk/TF-Splunk-AppsLocal/docs/README.md)
* [TF::Splunk::AuthenticationUsers](../resources/splunk/TF-Splunk-AuthenticationUsers/docs/README.md)
* [TF::Splunk::AuthorizationRoles](../resources/splunk/TF-Splunk-AuthorizationRoles/docs/README.md)
* [TF::Splunk::ConfigsConf](../resources/splunk/TF-Splunk-ConfigsConf/docs/README.md)
* [TF::Splunk::DataUiViews](../resources/splunk/TF-Splunk-DataUiViews/docs/README.md)
* [TF::Splunk::GlobalHttpEventCollector](../resources/splunk/TF-Splunk-GlobalHttpEventCollector/docs/README.md)
* [TF::Splunk::Indexes](../resources/splunk/TF-Splunk-Indexes/docs/README.md)
* [TF::Splunk::InputsHttpEventCollector](../resources/splunk/TF-Splunk-InputsHttpEventCollector/docs/README.md)
* [TF::Splunk::InputsMonitor](../resources/splunk/TF-Splunk-InputsMonitor/docs/README.md)
* [TF::Splunk::InputsScript](../resources/splunk/TF-Splunk-InputsScript/docs/README.md)
* [TF::Splunk::InputsTcpCooked](../resources/splunk/TF-Splunk-InputsTcpCooked/docs/README.md)
* [TF::Splunk::InputsTcpRaw](../resources/splunk/TF-Splunk-InputsTcpRaw/docs/README.md)
* [TF::Splunk::InputsTcpSplunkTcpToken](../resources/splunk/TF-Splunk-InputsTcpSplunkTcpToken/docs/README.md)
* [TF::Splunk::InputsTcpSsl](../resources/splunk/TF-Splunk-InputsTcpSsl/docs/README.md)
* [TF::Splunk::InputsUdp](../resources/splunk/TF-Splunk-InputsUdp/docs/README.md)
* [TF::Splunk::OutputsTcpDefault](../resources/splunk/TF-Splunk-OutputsTcpDefault/docs/README.md)
* [TF::Splunk::OutputsTcpGroup](../resources/splunk/TF-Splunk-OutputsTcpGroup/docs/README.md)
* [TF::Splunk::OutputsTcpServer](../resources/splunk/TF-Splunk-OutputsTcpServer/docs/README.md)
* [TF::Splunk::OutputsTcpSyslog](../resources/splunk/TF-Splunk-OutputsTcpSyslog/docs/README.md)
* [TF::Splunk::SavedSearches](../resources/splunk/TF-Splunk-SavedSearches/docs/README.md)
* [TF::Splunk::ShIndexesManager](../resources/splunk/TF-Splunk-ShIndexesManager/docs/README.md)