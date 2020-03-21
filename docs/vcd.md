# VMware vCloud Director Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/vcd**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `user` - (Required) This is the username for vCloud Director API operations.  
  *v2.0+* `user` may be "administrator" (set `org` or `sysorg` to "System" in this case).
  
* `password` - (Required) This is the password for vCloud Director API operations.
  
* `token` - (Optional; *v2.6+*) This is the authorization token that can be used
   instead of username and password. When this is set, username and password will
    be ignored, but should be left in configuration either empty or with any custom values.
    
* `org` - (Required) This is the vCloud Director Org on which to run API
  operations. Can also be specified with the `VCD_ORG` environment
  variable.  
  *v2.0+* `org` may be set to "System" when connection as Sys Admin is desired
  (set `user` to "administrator" in this case).  
  Note: `org` value is case sensitive.
  
* `sysorg` - (Optional; *v2.0+*) - Organization for user authentication. Set `sysorg` to "System" and
   `user` to "administrator" to free up `org` argument for setting a default organization
   for resources to use.
   
* `url` - (Required) This is the URL for the vCloud Director API endpoint. e.g.
  https://server.domain.com/api.
  
* `vdc` - (Optional) This is the virtual datacenter within vCloud Director to run
  API operations against. If not set the plugin will select the first virtual
  datacenter available to your Org. Can also be specified with the `VCD_VDC` environment
  variable.
  
* `max_retry_timeout` - (Optional) This provides you with the ability to specify the maximum
  amount of time (in seconds) you are prepared to wait for interactions on resources managed
  by vCloud Director to be successful. If a resource action fails, the action will be retried
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

* [Terraform::VCD::CatalogItem](../resources/vcd/Terraform-VCD-CatalogItem/docs/README.md)
* [Terraform::VCD::CatalogMedia](../resources/vcd/Terraform-VCD-CatalogMedia/docs/README.md)
* [Terraform::VCD::Catalog](../resources/vcd/Terraform-VCD-Catalog/docs/README.md)
* [Terraform::VCD::Dnat](../resources/vcd/Terraform-VCD-Dnat/docs/README.md)
* [Terraform::VCD::EdgegatewayVpn](../resources/vcd/Terraform-VCD-EdgegatewayVpn/docs/README.md)
* [Terraform::VCD::Edgegateway](../resources/vcd/Terraform-VCD-Edgegateway/docs/README.md)
* [Terraform::VCD::ExternalNetwork](../resources/vcd/Terraform-VCD-ExternalNetwork/docs/README.md)
* [Terraform::VCD::FirewallRules](../resources/vcd/Terraform-VCD-FirewallRules/docs/README.md)
* [Terraform::VCD::IndependentDisk](../resources/vcd/Terraform-VCD-IndependentDisk/docs/README.md)
* [Terraform::VCD::InsertedMedia](../resources/vcd/Terraform-VCD-InsertedMedia/docs/README.md)
* [Terraform::VCD::LbAppProfile](../resources/vcd/Terraform-VCD-LbAppProfile/docs/README.md)
* [Terraform::VCD::LbAppRule](../resources/vcd/Terraform-VCD-LbAppRule/docs/README.md)
* [Terraform::VCD::LbServerPool](../resources/vcd/Terraform-VCD-LbServerPool/docs/README.md)
* [Terraform::VCD::LbServiceMonitor](../resources/vcd/Terraform-VCD-LbServiceMonitor/docs/README.md)
* [Terraform::VCD::LbVirtualServer](../resources/vcd/Terraform-VCD-LbVirtualServer/docs/README.md)
* [Terraform::VCD::Network (Deprecated)](../resources/vcd/Terraform-VCD-Network (Deprecated)/docs/README.md)
* [Terraform::VCD::NetworkDirect](../resources/vcd/Terraform-VCD-NetworkDirect/docs/README.md)
* [Terraform::VCD::NetworkIsolated](../resources/vcd/Terraform-VCD-NetworkIsolated/docs/README.md)
* [Terraform::VCD::NetworkRouted](../resources/vcd/Terraform-VCD-NetworkRouted/docs/README.md)
* [Terraform::VCD::NsxvDhcpRelay](../resources/vcd/Terraform-VCD-NsxvDhcpRelay/docs/README.md)
* [Terraform::VCD::NsxvDnat](../resources/vcd/Terraform-VCD-NsxvDnat/docs/README.md)
* [Terraform::VCD::NsxvFirewallRule](../resources/vcd/Terraform-VCD-NsxvFirewallRule/docs/README.md)
* [Terraform::VCD::NsxvIpSet](../resources/vcd/Terraform-VCD-NsxvIpSet/docs/README.md)
* [Terraform::VCD::NsxvSnat](../resources/vcd/Terraform-VCD-NsxvSnat/docs/README.md)
* [Terraform::VCD::OrgUser](../resources/vcd/Terraform-VCD-OrgUser/docs/README.md)
* [Terraform::VCD::OrgVdc](../resources/vcd/Terraform-VCD-OrgVdc/docs/README.md)
* [Terraform::VCD::Org](../resources/vcd/Terraform-VCD-Org/docs/README.md)
* [Terraform::VCD::Snat](../resources/vcd/Terraform-VCD-Snat/docs/README.md)
* [Terraform::VCD::VappNetwork](../resources/vcd/Terraform-VCD-VappNetwork/docs/README.md)
* [Terraform::VCD::VappOrgNetwork](../resources/vcd/Terraform-VCD-VappOrgNetwork/docs/README.md)
* [Terraform::VCD::VappVm](../resources/vcd/Terraform-VCD-VappVm/docs/README.md)
* [Terraform::VCD::Vapp](../resources/vcd/Terraform-VCD-Vapp/docs/README.md)
* [Terraform::VCD::VmInternalDisk](../resources/vcd/Terraform-VCD-VmInternalDisk/docs/README.md)