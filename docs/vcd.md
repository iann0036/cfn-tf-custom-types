# VMware vCloud Director Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/vcd**. The below arguments may be included as the key/value or JSON properties in the secret:

* `user` - (Required) This is the username for Cloud Director API operations. *v2.0+* `user` may be "administrator" (set `org` or
  `sysorg` to "System" in this case). 
  *v2.9+* When using with SAML and ADFS - username format must be in Active Directory format -
  `user@contoso.com` or `contoso.com\user` in combination with `use_saml_adfs` option.
  
* `password` - (Required) This is the password for Cloud Director API operations.

* `auth_type` - (Optional) `integrated`, `token` or `saml_adfs`. Default is `integrated`.
  * `integrated` - VCD local users and LDAP users (provided LDAP is configured for Organization).
  * `saml_adfs` allows to use SAML login flow with Active Directory Federation
  Services (ADFS) using "/adfs/services/trust/13/usernamemixed" endpoint. Please note that
  credentials for ADFS should be formatted as `user@contoso.com` or `contoso.com\user`.
  * `token` allows to specify token in [`token`](#token) field.
  
* `token` - (Optional; *v2.6+*) This is the token that can be used instead of username
   and password (in combination with field `auth_type=token`). When this is set, username and
   password will be ignored, but should be left in configuration either empty or with any custom
   values.
   Both a (deprecated) authorization token or a bearer token (*v3.1+*) can be used in this field.

* `saml_adfs_rpt_id` - (Optional) When using `auth_type=saml_adfs` VCD SAML entity ID will be used
  as Relaying Party Trust Identifier (RPT ID) by default. If a different RPT ID is needed - one can
  set it using this field.

* `org` - (Required) This is the Cloud Director Org on which to run API
  operations. Can also be specified with the `VCD_ORG` environment
  variable.  
  *v2.0+* `org` may be set to "System" when connection as Sys Admin is desired
  (set `user` to "administrator" in this case).  
  Note: `org` value is case sensitive.
  
* `sysorg` - (Optional; *v2.0+*) - Organization for user authentication. Set `sysorg` to "System" and
   `user` to "administrator" to free up `org` argument for setting a default organization
   for resources to use.
   
* `url` - (Required) This is the URL for the Cloud Director API endpoint. e.g.
  https://server.domain.com/api.
  
* `vdc` - (Optional) This is the virtual datacenter within Cloud Director to run
  API operations against. If not set the plugin will select the first virtual
  datacenter available to your Org. Can also be specified with the `VCD_VDC` environment
  variable.
  
* `max_retry_timeout` - (Optional) This provides you with the ability to specify the maximum
  amount of time (in seconds) you are prepared to wait for interactions on resources managed
  by Cloud Director to be successful. If a resource action fails, the action will be retried
  (as long as it is still within the `max_retry_timeout` value) to try and ensure success.
  Defaults to 60 seconds if not set.
  
* `maxRetryTimeout` - (Deprecated) Use `max_retry_timeout` instead.

* `allow_unverified_ssl` - (Optional) Boolean that can be set to true to
  disable SSL certificate verification. This should be used with care as it
  could allow an attacker to intercept your auth token. If omitted, default
  value is false.

* `logging` - (Optional; *v2.0+*) Boolean that enables API calls logging from upstream library `go-vcloud-director`. 
   The logging file will record all API requests and responses, plus some debug information that is part of this 
   provider.

* `logging_file` - (Optional; *v2.0+*) The name of the log file (when `logging` is enabled).
  
* `import_separator` - (Optional; *v2.5+*) The string to be used as separator with `terraform import`. By default
  it is a dot (`.`).


## Supported Resources

* [TF::VCD::CatalogItem](../resources/vcd/TF-VCD-CatalogItem/docs/README.md)
* [TF::VCD::CatalogMedia](../resources/vcd/TF-VCD-CatalogMedia/docs/README.md)
* [TF::VCD::Catalog](../resources/vcd/TF-VCD-Catalog/docs/README.md)
* [TF::VCD::EdgegatewaySettings](../resources/vcd/TF-VCD-EdgegatewaySettings/docs/README.md)
* [TF::VCD::EdgegatewayVpn](../resources/vcd/TF-VCD-EdgegatewayVpn/docs/README.md)
* [TF::VCD::Edgegateway](../resources/vcd/TF-VCD-Edgegateway/docs/README.md)
* [TF::VCD::ExternalNetworkV2](../resources/vcd/TF-VCD-ExternalNetworkV2/docs/README.md)
* [TF::VCD::ExternalNetwork](../resources/vcd/TF-VCD-ExternalNetwork/docs/README.md)
* [TF::VCD::IndependentDisk](../resources/vcd/TF-VCD-IndependentDisk/docs/README.md)
* [TF::VCD::InsertedMedia](../resources/vcd/TF-VCD-InsertedMedia/docs/README.md)
* [TF::VCD::LbAppProfile](../resources/vcd/TF-VCD-LbAppProfile/docs/README.md)
* [TF::VCD::LbAppRule](../resources/vcd/TF-VCD-LbAppRule/docs/README.md)
* [TF::VCD::LbServerPool](../resources/vcd/TF-VCD-LbServerPool/docs/README.md)
* [TF::VCD::LbServiceMonitor](../resources/vcd/TF-VCD-LbServiceMonitor/docs/README.md)
* [TF::VCD::LbVirtualServer](../resources/vcd/TF-VCD-LbVirtualServer/docs/README.md)
* [TF::VCD::NetworkDirect](../resources/vcd/TF-VCD-NetworkDirect/docs/README.md)
* [TF::VCD::NetworkIsolatedV2](../resources/vcd/TF-VCD-NetworkIsolatedV2/docs/README.md)
* [TF::VCD::NetworkIsolated](../resources/vcd/TF-VCD-NetworkIsolated/docs/README.md)
* [TF::VCD::NetworkRoutedV2](../resources/vcd/TF-VCD-NetworkRoutedV2/docs/README.md)
* [TF::VCD::NetworkRouted](../resources/vcd/TF-VCD-NetworkRouted/docs/README.md)
* [TF::VCD::NsxtEdgegateway](../resources/vcd/TF-VCD-NsxtEdgegateway/docs/README.md)
* [TF::VCD::NsxtNetworkDhcp](../resources/vcd/TF-VCD-NsxtNetworkDhcp/docs/README.md)
* [TF::VCD::NsxtNetworkImported](../resources/vcd/TF-VCD-NsxtNetworkImported/docs/README.md)
* [TF::VCD::NsxvDhcpRelay](../resources/vcd/TF-VCD-NsxvDhcpRelay/docs/README.md)
* [TF::VCD::NsxvDnat](../resources/vcd/TF-VCD-NsxvDnat/docs/README.md)
* [TF::VCD::NsxvFirewallRule](../resources/vcd/TF-VCD-NsxvFirewallRule/docs/README.md)
* [TF::VCD::NsxvIpSet](../resources/vcd/TF-VCD-NsxvIpSet/docs/README.md)
* [TF::VCD::NsxvSnat](../resources/vcd/TF-VCD-NsxvSnat/docs/README.md)
* [TF::VCD::OrgGroup](../resources/vcd/TF-VCD-OrgGroup/docs/README.md)
* [TF::VCD::OrgUser](../resources/vcd/TF-VCD-OrgUser/docs/README.md)
* [TF::VCD::OrgVdc](../resources/vcd/TF-VCD-OrgVdc/docs/README.md)
* [TF::VCD::Org](../resources/vcd/TF-VCD-Org/docs/README.md)
* [TF::VCD::VappAccessControl](../resources/vcd/TF-VCD-VappAccessControl/docs/README.md)
* [TF::VCD::VappFirewallRules](../resources/vcd/TF-VCD-VappFirewallRules/docs/README.md)
* [TF::VCD::VappNatRules](../resources/vcd/TF-VCD-VappNatRules/docs/README.md)
* [TF::VCD::VappNetwork](../resources/vcd/TF-VCD-VappNetwork/docs/README.md)
* [TF::VCD::VappOrgNetwork](../resources/vcd/TF-VCD-VappOrgNetwork/docs/README.md)
* [TF::VCD::VappStaticRouting](../resources/vcd/TF-VCD-VappStaticRouting/docs/README.md)
* [TF::VCD::VappVm](../resources/vcd/TF-VCD-VappVm/docs/README.md)
* [TF::VCD::Vapp](../resources/vcd/TF-VCD-Vapp/docs/README.md)
* [TF::VCD::VmAffinityRule](../resources/vcd/TF-VCD-VmAffinityRule/docs/README.md)
* [TF::VCD::VmInternalDisk](../resources/vcd/TF-VCD-VmInternalDisk/docs/README.md)
* [TF::VCD::VmSizingPolicy](../resources/vcd/TF-VCD-VmSizingPolicy/docs/README.md)
* [TF::VCD::Vm](../resources/vcd/TF-VCD-Vm/docs/README.md)