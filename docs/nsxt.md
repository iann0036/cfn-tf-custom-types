# VMware NSX-T Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/nsxt**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `host` - (Required) The host name or IP address of the NSX-T manager. Do not include
  `http://` or `https://` in the host.
* `username` - (Required) The user name to connect to the NSX-T manager as.
* `password` - (Required) The password for the NSX-T manager user.
* `client_auth_cert_file` - (Optional) The path to a certificate file for
  certificate authorization.
* `client_auth_key_file` - (Optional) The path to a private key file for the
  certificate supplied to `client_auth_cert_file`.
* `allow_unverified_ssl` - (Optional) Boolean that can be set to true to disable
  SSL certificate verification. This should be used with care as it could allow
  an attacker to intercept your auth token. If omitted, default value is
  `false`.
* `ca_file` - (Optional) The path to an optional CA certificate file for SSL
  validation. Can also be specified with the `NSXT_CA_FILE` environment
  variable.
* `max_retries` - (Optional) The maximum number of retires before failing an API
  request.
* `retry_min_delay` - (Optional) The minimum delay, in milliseconds, between
  retires made to the API. Default:`500`.
* `retry_max_delay` - (Optional) The maximum delay, in milliseconds, between
  retires made to the API. Default:`5000`.
* `retry_on_status_codes` - (Optional) A list of HTTP status codes to retry on.
  By default, the provider will retry on HTTP error 429 (too many requests),
  essentially retrying on throttled connections.
* `remote_auth` - (Optional) Would trigger remote authorization instead of basic
  authorization. This is required for users based on vIDM authentication.
  The default for this flag is false.
* `tolerate_partial_success` - (Optional) Setting this flag to true would treat
  partially succesful realization as valid state and not fail apply.
* `vmc_token` - (Optional) Long-lived API token for authenticating with VMware
  Cloud Services APIs. This token will be used to short-lived token that is
  needed to communicate with NSX Manager in VMC environment.
  Note that only subset of policy resources are supported with VMC environment.
* `vmc_auth_host` - (Optional) URL for VMC authorization service that is used
  to obtain short-lived token for NSX manager access. Defaults to VMC
  console authorization URL.
* `enforcement_point` - (Optional) Enforcement point, mostly relevant for policy
  data sources. For VMC environment, this should be set to `vmc-enforcementpoint`.
  For on-prem deployments, this setting should not be specified.


## Supported Resources

* [Terraform::NSXT::AlgorithmTypeNsService](../resources/nsxt/Terraform-NSXT-AlgorithmTypeNsService/docs/README.md)
* [Terraform::NSXT::DhcpRelayProfile](../resources/nsxt/Terraform-NSXT-DhcpRelayProfile/docs/README.md)
* [Terraform::NSXT::DhcpRelayService](../resources/nsxt/Terraform-NSXT-DhcpRelayService/docs/README.md)
* [Terraform::NSXT::DhcpServerIpPool](../resources/nsxt/Terraform-NSXT-DhcpServerIpPool/docs/README.md)
* [Terraform::NSXT::DhcpServerProfile](../resources/nsxt/Terraform-NSXT-DhcpServerProfile/docs/README.md)
* [Terraform::NSXT::EtherTypeNsService](../resources/nsxt/Terraform-NSXT-EtherTypeNsService/docs/README.md)
* [Terraform::NSXT::FirewallSection](../resources/nsxt/Terraform-NSXT-FirewallSection/docs/README.md)
* [Terraform::NSXT::IcmpTypeNsService](../resources/nsxt/Terraform-NSXT-IcmpTypeNsService/docs/README.md)
* [Terraform::NSXT::IgmpTypeNsService](../resources/nsxt/Terraform-NSXT-IgmpTypeNsService/docs/README.md)
* [Terraform::NSXT::IpBlockSubnet](../resources/nsxt/Terraform-NSXT-IpBlockSubnet/docs/README.md)
* [Terraform::NSXT::IpBlock](../resources/nsxt/Terraform-NSXT-IpBlock/docs/README.md)
* [Terraform::NSXT::IpDiscoverySwitchingProfile](../resources/nsxt/Terraform-NSXT-IpDiscoverySwitchingProfile/docs/README.md)
* [Terraform::NSXT::IpPoolAllocationIpAddress](../resources/nsxt/Terraform-NSXT-IpPoolAllocationIpAddress/docs/README.md)
* [Terraform::NSXT::IpPool](../resources/nsxt/Terraform-NSXT-IpPool/docs/README.md)
* [Terraform::NSXT::IpProtocolNsService](../resources/nsxt/Terraform-NSXT-IpProtocolNsService/docs/README.md)
* [Terraform::NSXT::IpSet](../resources/nsxt/Terraform-NSXT-IpSet/docs/README.md)
* [Terraform::NSXT::L4PortSetNsService](../resources/nsxt/Terraform-NSXT-L4PortSetNsService/docs/README.md)
* [Terraform::NSXT::LbClientSslProfile](../resources/nsxt/Terraform-NSXT-LbClientSslProfile/docs/README.md)
* [Terraform::NSXT::LbCookiePersistenceProfile](../resources/nsxt/Terraform-NSXT-LbCookiePersistenceProfile/docs/README.md)
* [Terraform::NSXT::LbFastTcpApplicationProfile](../resources/nsxt/Terraform-NSXT-LbFastTcpApplicationProfile/docs/README.md)
* [Terraform::NSXT::LbFastUdpApplicationProfile](../resources/nsxt/Terraform-NSXT-LbFastUdpApplicationProfile/docs/README.md)
* [Terraform::NSXT::LbHttpApplicationProfile](../resources/nsxt/Terraform-NSXT-LbHttpApplicationProfile/docs/README.md)
* [Terraform::NSXT::LbHttpForwardingRule](../resources/nsxt/Terraform-NSXT-LbHttpForwardingRule/docs/README.md)
* [Terraform::NSXT::LbHttpMonitor](../resources/nsxt/Terraform-NSXT-LbHttpMonitor/docs/README.md)
* [Terraform::NSXT::LbHttpRequestRewriteRule](../resources/nsxt/Terraform-NSXT-LbHttpRequestRewriteRule/docs/README.md)
* [Terraform::NSXT::LbHttpResponseRewriteRule](../resources/nsxt/Terraform-NSXT-LbHttpResponseRewriteRule/docs/README.md)
* [Terraform::NSXT::LbHttpVirtualServer](../resources/nsxt/Terraform-NSXT-LbHttpVirtualServer/docs/README.md)
* [Terraform::NSXT::LbHttpsMonitor](../resources/nsxt/Terraform-NSXT-LbHttpsMonitor/docs/README.md)
* [Terraform::NSXT::LbIcmpMonitor](../resources/nsxt/Terraform-NSXT-LbIcmpMonitor/docs/README.md)
* [Terraform::NSXT::LbPassiveMonitor](../resources/nsxt/Terraform-NSXT-LbPassiveMonitor/docs/README.md)
* [Terraform::NSXT::LbPool](../resources/nsxt/Terraform-NSXT-LbPool/docs/README.md)
* [Terraform::NSXT::LbServerSslProfile](../resources/nsxt/Terraform-NSXT-LbServerSslProfile/docs/README.md)
* [Terraform::NSXT::LbService](../resources/nsxt/Terraform-NSXT-LbService/docs/README.md)
* [Terraform::NSXT::LbSourceIpPersistenceProfile](../resources/nsxt/Terraform-NSXT-LbSourceIpPersistenceProfile/docs/README.md)
* [Terraform::NSXT::LbTcpMonitor](../resources/nsxt/Terraform-NSXT-LbTcpMonitor/docs/README.md)
* [Terraform::NSXT::LbTcpVirtualServer](../resources/nsxt/Terraform-NSXT-LbTcpVirtualServer/docs/README.md)
* [Terraform::NSXT::LbUdpMonitor](../resources/nsxt/Terraform-NSXT-LbUdpMonitor/docs/README.md)
* [Terraform::NSXT::LbUdpVirtualServer](../resources/nsxt/Terraform-NSXT-LbUdpVirtualServer/docs/README.md)
* [Terraform::NSXT::LogicalDhcpPort](../resources/nsxt/Terraform-NSXT-LogicalDhcpPort/docs/README.md)
* [Terraform::NSXT::LogicalDhcpServer](../resources/nsxt/Terraform-NSXT-LogicalDhcpServer/docs/README.md)
* [Terraform::NSXT::LogicalPort](../resources/nsxt/Terraform-NSXT-LogicalPort/docs/README.md)
* [Terraform::NSXT::LogicalRouterCentralizedServicePort](../resources/nsxt/Terraform-NSXT-LogicalRouterCentralizedServicePort/docs/README.md)
* [Terraform::NSXT::LogicalRouterDownlinkPort](../resources/nsxt/Terraform-NSXT-LogicalRouterDownlinkPort/docs/README.md)
* [Terraform::NSXT::LogicalRouterLinkPortOnTier0](../resources/nsxt/Terraform-NSXT-LogicalRouterLinkPortOnTier0/docs/README.md)
* [Terraform::NSXT::LogicalRouterLinkPortOnTier1](../resources/nsxt/Terraform-NSXT-LogicalRouterLinkPortOnTier1/docs/README.md)
* [Terraform::NSXT::LogicalSwitch](../resources/nsxt/Terraform-NSXT-LogicalSwitch/docs/README.md)
* [Terraform::NSXT::LogicalTier0Router](../resources/nsxt/Terraform-NSXT-LogicalTier0Router/docs/README.md)
* [Terraform::NSXT::LogicalTier1Router](../resources/nsxt/Terraform-NSXT-LogicalTier1Router/docs/README.md)
* [Terraform::NSXT::MacManagementSwitchingProfile](../resources/nsxt/Terraform-NSXT-MacManagementSwitchingProfile/docs/README.md)
* [Terraform::NSXT::NatRule](../resources/nsxt/Terraform-NSXT-NatRule/docs/README.md)
* [Terraform::NSXT::NsGroup](../resources/nsxt/Terraform-NSXT-NsGroup/docs/README.md)
* [Terraform::NSXT::NsServiceGroup](../resources/nsxt/Terraform-NSXT-NsServiceGroup/docs/README.md)
* [Terraform::NSXT::PolicyBgpNeighbor](../resources/nsxt/Terraform-NSXT-PolicyBgpNeighbor/docs/README.md)
* [Terraform::NSXT::PolicyDhcpRelay](../resources/nsxt/Terraform-NSXT-PolicyDhcpRelay/docs/README.md)
* [Terraform::NSXT::PolicyDhcpServer](../resources/nsxt/Terraform-NSXT-PolicyDhcpServer/docs/README.md)
* [Terraform::NSXT::PolicyGatewayPolicy](../resources/nsxt/Terraform-NSXT-PolicyGatewayPolicy/docs/README.md)
* [Terraform::NSXT::PolicyGroup](../resources/nsxt/Terraform-NSXT-PolicyGroup/docs/README.md)
* [Terraform::NSXT::PolicyIpAddressAllocation](../resources/nsxt/Terraform-NSXT-PolicyIpAddressAllocation/docs/README.md)
* [Terraform::NSXT::PolicyIpBlock](../resources/nsxt/Terraform-NSXT-PolicyIpBlock/docs/README.md)
* [Terraform::NSXT::PolicyIpPoolBlockSubnet](../resources/nsxt/Terraform-NSXT-PolicyIpPoolBlockSubnet/docs/README.md)
* [Terraform::NSXT::PolicyIpPoolStaticSubnet](../resources/nsxt/Terraform-NSXT-PolicyIpPoolStaticSubnet/docs/README.md)
* [Terraform::NSXT::PolicyIpPool](../resources/nsxt/Terraform-NSXT-PolicyIpPool/docs/README.md)
* [Terraform::NSXT::PolicyLbPool](../resources/nsxt/Terraform-NSXT-PolicyLbPool/docs/README.md)
* [Terraform::NSXT::PolicyLbService](../resources/nsxt/Terraform-NSXT-PolicyLbService/docs/README.md)
* [Terraform::NSXT::PolicyLbVirtualServer](../resources/nsxt/Terraform-NSXT-PolicyLbVirtualServer/docs/README.md)
* [Terraform::NSXT::PolicyNatRule](../resources/nsxt/Terraform-NSXT-PolicyNatRule/docs/README.md)
* [Terraform::NSXT::PolicySecurityPolicy](../resources/nsxt/Terraform-NSXT-PolicySecurityPolicy/docs/README.md)
* [Terraform::NSXT::PolicySegment](../resources/nsxt/Terraform-NSXT-PolicySegment/docs/README.md)
* [Terraform::NSXT::PolicyService](../resources/nsxt/Terraform-NSXT-PolicyService/docs/README.md)
* [Terraform::NSXT::PolicyStaticRoute](../resources/nsxt/Terraform-NSXT-PolicyStaticRoute/docs/README.md)
* [Terraform::NSXT::PolicyTier0Gateway](../resources/nsxt/Terraform-NSXT-PolicyTier0Gateway/docs/README.md)
* [Terraform::NSXT::PolicyTier1Gateway](../resources/nsxt/Terraform-NSXT-PolicyTier1Gateway/docs/README.md)
* [Terraform::NSXT::PolicyVlanSegment](../resources/nsxt/Terraform-NSXT-PolicyVlanSegment/docs/README.md)
* [Terraform::NSXT::PolicyVmTags](../resources/nsxt/Terraform-NSXT-PolicyVmTags/docs/README.md)
* [Terraform::NSXT::QosSwitchingProfile](../resources/nsxt/Terraform-NSXT-QosSwitchingProfile/docs/README.md)
* [Terraform::NSXT::SpoofguardSwitchingProfile](../resources/nsxt/Terraform-NSXT-SpoofguardSwitchingProfile/docs/README.md)
* [Terraform::NSXT::StaticRoute](../resources/nsxt/Terraform-NSXT-StaticRoute/docs/README.md)
* [Terraform::NSXT::SwitchSecuritySwitchingProfile](../resources/nsxt/Terraform-NSXT-SwitchSecuritySwitchingProfile/docs/README.md)
* [Terraform::NSXT::VlanLogicalSwitch](../resources/nsxt/Terraform-NSXT-VlanLogicalSwitch/docs/README.md)
* [Terraform::NSXT::VmTags](../resources/nsxt/Terraform-NSXT-VmTags/docs/README.md)