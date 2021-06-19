# VMware NSX-T Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/nsxt**. The below arguments may be included as the key/value or JSON properties in the secret:

* `host` - (Required) The host name or IP address of the NSX-T manager. Do not include
  `http://` or `https://` in the host.
* `username` - (Required) The user name to connect to the NSX-T manager as.
* `password` - (Required) The password for the NSX-T manager user.
* `client_auth_cert_file` - (Optional) The path to a certificate file for client
  certificate authorization.
* `client_auth_key_file` - (Optional) The path to a private key file for the
  certificate supplied to `client_auth_cert_file`.
* `client_auth_cert` - (Optional) Client certificate string.
* `client_auth_key` - (Optional) Client certificate private key string.
* `allow_unverified_ssl` - (Optional) Boolean that can be set to true to disable
  SSL certificate verification. This should be used with care as it could allow
  an attacker to intercept your auth token. If omitted, default value is
  `false`.
* `ca_file` - (Optional) The path to an optional CA certificate file for SSL
  validation. Can also be specified with the `NSXT_CA_FILE` environment
  variable.
* `ca` - (Optional) CA certificate string for SSL validation.
* `max_retries` - (Optional) The maximum number of retires before failing an API
  request. Not supported yet for policy resources.
* `retry_min_delay` - (Optional) The minimum delay, in milliseconds, between
  retires made to the API. Default:`500`. Not supported yet for policy resources.
* `retry_max_delay` - (Optional) The maximum delay, in milliseconds, between
  retires made to the API. Default:`5000`. Not supported yet for policy resources.
* `retry_on_status_codes` - (Optional) A list of HTTP status codes to retry on.
  By default, the provider will retry on HTTP error 429 (too many requests),
  essentially retrying on throttled connections. Not supported yet for policy resources.
* `remote_auth` - (Optional) Would trigger remote authorization instead of basic
  authorization. This is required for users based on vIDM authentication.
  The default for this flag is false.
* `tolerate_partial_success` - (Optional) Setting this flag to true would treat
  partially successful realization as valid state and not fail apply.
* `vmc_token` - (Optional) Long-lived API token for authenticating with VMware
  Cloud Services APIs. This token will be used to short-lived token that is
  needed to communicate with NSX Manager in VMC environment.
  Note that only subset of policy resources are supported with VMC environment.
* `vmc_auth_host` - (Optional) URL for VMC authorization service that is used
  to obtain short-lived token for NSX manager access. Defaults to VMC
  console authorization URL.
* `vmc_auth_mode` - (Optional) VMC authorization mode, that determines what HTTP
  header is used for authorization. Accepted values are `Default`, `Bearer`, `Basic`.
  For direct VMC connections with a token, use `Bearer` mode. For PCI mode with basic
  authentication, use `Basic`. Otherwise no need to specify this setting.
* `enforcement_point` - (Optional) Enforcement point, mostly relevant for policy
  data sources. For VMC environment, this should be set to `vmc-enforcementpoint`.
  For on-prem deployments, this setting should not be specified.
* `global_manager` - (Optional) True if this is a global manager endpoint.
  False by default.
* `license_keys` - (Optional) List of NSX-T license keys. License keys are applied
  during plan and will not be deleted if they are removed from the configuration.


## Supported Resources

* [TF::NSXT::AlgorithmTypeNsService](../resources/nsxt/TF-NSXT-AlgorithmTypeNsService/docs/README.md)
* [TF::NSXT::DhcpRelayProfile](../resources/nsxt/TF-NSXT-DhcpRelayProfile/docs/README.md)
* [TF::NSXT::DhcpRelayService](../resources/nsxt/TF-NSXT-DhcpRelayService/docs/README.md)
* [TF::NSXT::DhcpServerIpPool](../resources/nsxt/TF-NSXT-DhcpServerIpPool/docs/README.md)
* [TF::NSXT::DhcpServerProfile](../resources/nsxt/TF-NSXT-DhcpServerProfile/docs/README.md)
* [TF::NSXT::EtherTypeNsService](../resources/nsxt/TF-NSXT-EtherTypeNsService/docs/README.md)
* [TF::NSXT::FirewallSection](../resources/nsxt/TF-NSXT-FirewallSection/docs/README.md)
* [TF::NSXT::IcmpTypeNsService](../resources/nsxt/TF-NSXT-IcmpTypeNsService/docs/README.md)
* [TF::NSXT::IgmpTypeNsService](../resources/nsxt/TF-NSXT-IgmpTypeNsService/docs/README.md)
* [TF::NSXT::IpBlockSubnet](../resources/nsxt/TF-NSXT-IpBlockSubnet/docs/README.md)
* [TF::NSXT::IpBlock](../resources/nsxt/TF-NSXT-IpBlock/docs/README.md)
* [TF::NSXT::IpDiscoverySwitchingProfile](../resources/nsxt/TF-NSXT-IpDiscoverySwitchingProfile/docs/README.md)
* [TF::NSXT::IpPoolAllocationIpAddress](../resources/nsxt/TF-NSXT-IpPoolAllocationIpAddress/docs/README.md)
* [TF::NSXT::IpPool](../resources/nsxt/TF-NSXT-IpPool/docs/README.md)
* [TF::NSXT::IpProtocolNsService](../resources/nsxt/TF-NSXT-IpProtocolNsService/docs/README.md)
* [TF::NSXT::IpSet](../resources/nsxt/TF-NSXT-IpSet/docs/README.md)
* [TF::NSXT::L4PortSetNsService](../resources/nsxt/TF-NSXT-L4PortSetNsService/docs/README.md)
* [TF::NSXT::LbClientSslProfile](../resources/nsxt/TF-NSXT-LbClientSslProfile/docs/README.md)
* [TF::NSXT::LbCookiePersistenceProfile](../resources/nsxt/TF-NSXT-LbCookiePersistenceProfile/docs/README.md)
* [TF::NSXT::LbFastTcpApplicationProfile](../resources/nsxt/TF-NSXT-LbFastTcpApplicationProfile/docs/README.md)
* [TF::NSXT::LbFastUdpApplicationProfile](../resources/nsxt/TF-NSXT-LbFastUdpApplicationProfile/docs/README.md)
* [TF::NSXT::LbHttpApplicationProfile](../resources/nsxt/TF-NSXT-LbHttpApplicationProfile/docs/README.md)
* [TF::NSXT::LbHttpForwardingRule](../resources/nsxt/TF-NSXT-LbHttpForwardingRule/docs/README.md)
* [TF::NSXT::LbHttpMonitor](../resources/nsxt/TF-NSXT-LbHttpMonitor/docs/README.md)
* [TF::NSXT::LbHttpRequestRewriteRule](../resources/nsxt/TF-NSXT-LbHttpRequestRewriteRule/docs/README.md)
* [TF::NSXT::LbHttpResponseRewriteRule](../resources/nsxt/TF-NSXT-LbHttpResponseRewriteRule/docs/README.md)
* [TF::NSXT::LbHttpVirtualServer](../resources/nsxt/TF-NSXT-LbHttpVirtualServer/docs/README.md)
* [TF::NSXT::LbHttpsMonitor](../resources/nsxt/TF-NSXT-LbHttpsMonitor/docs/README.md)
* [TF::NSXT::LbIcmpMonitor](../resources/nsxt/TF-NSXT-LbIcmpMonitor/docs/README.md)
* [TF::NSXT::LbPassiveMonitor](../resources/nsxt/TF-NSXT-LbPassiveMonitor/docs/README.md)
* [TF::NSXT::LbPool](../resources/nsxt/TF-NSXT-LbPool/docs/README.md)
* [TF::NSXT::LbServerSslProfile](../resources/nsxt/TF-NSXT-LbServerSslProfile/docs/README.md)
* [TF::NSXT::LbService](../resources/nsxt/TF-NSXT-LbService/docs/README.md)
* [TF::NSXT::LbSourceIpPersistenceProfile](../resources/nsxt/TF-NSXT-LbSourceIpPersistenceProfile/docs/README.md)
* [TF::NSXT::LbTcpMonitor](../resources/nsxt/TF-NSXT-LbTcpMonitor/docs/README.md)
* [TF::NSXT::LbTcpVirtualServer](../resources/nsxt/TF-NSXT-LbTcpVirtualServer/docs/README.md)
* [TF::NSXT::LbUdpMonitor](../resources/nsxt/TF-NSXT-LbUdpMonitor/docs/README.md)
* [TF::NSXT::LbUdpVirtualServer](../resources/nsxt/TF-NSXT-LbUdpVirtualServer/docs/README.md)
* [TF::NSXT::LogicalDhcpPort](../resources/nsxt/TF-NSXT-LogicalDhcpPort/docs/README.md)
* [TF::NSXT::LogicalDhcpServer](../resources/nsxt/TF-NSXT-LogicalDhcpServer/docs/README.md)
* [TF::NSXT::LogicalPort](../resources/nsxt/TF-NSXT-LogicalPort/docs/README.md)
* [TF::NSXT::LogicalRouterCentralizedServicePort](../resources/nsxt/TF-NSXT-LogicalRouterCentralizedServicePort/docs/README.md)
* [TF::NSXT::LogicalRouterDownlinkPort](../resources/nsxt/TF-NSXT-LogicalRouterDownlinkPort/docs/README.md)
* [TF::NSXT::LogicalRouterLinkPortOnTier0](../resources/nsxt/TF-NSXT-LogicalRouterLinkPortOnTier0/docs/README.md)
* [TF::NSXT::LogicalRouterLinkPortOnTier1](../resources/nsxt/TF-NSXT-LogicalRouterLinkPortOnTier1/docs/README.md)
* [TF::NSXT::LogicalSwitch](../resources/nsxt/TF-NSXT-LogicalSwitch/docs/README.md)
* [TF::NSXT::LogicalTier0Router](../resources/nsxt/TF-NSXT-LogicalTier0Router/docs/README.md)
* [TF::NSXT::LogicalTier1Router](../resources/nsxt/TF-NSXT-LogicalTier1Router/docs/README.md)
* [TF::NSXT::MacManagementSwitchingProfile](../resources/nsxt/TF-NSXT-MacManagementSwitchingProfile/docs/README.md)
* [TF::NSXT::NatRule](../resources/nsxt/TF-NSXT-NatRule/docs/README.md)
* [TF::NSXT::NsGroup](../resources/nsxt/TF-NSXT-NsGroup/docs/README.md)
* [TF::NSXT::NsServiceGroup](../resources/nsxt/TF-NSXT-NsServiceGroup/docs/README.md)
* [TF::NSXT::PolicyBgpConfig](../resources/nsxt/TF-NSXT-PolicyBgpConfig/docs/README.md)
* [TF::NSXT::PolicyBgpNeighbor](../resources/nsxt/TF-NSXT-PolicyBgpNeighbor/docs/README.md)
* [TF::NSXT::PolicyContextProfile](../resources/nsxt/TF-NSXT-PolicyContextProfile/docs/README.md)
* [TF::NSXT::PolicyDhcpRelay](../resources/nsxt/TF-NSXT-PolicyDhcpRelay/docs/README.md)
* [TF::NSXT::PolicyDhcpServer](../resources/nsxt/TF-NSXT-PolicyDhcpServer/docs/README.md)
* [TF::NSXT::PolicyDhcpV4StaticBinding](../resources/nsxt/TF-NSXT-PolicyDhcpV4StaticBinding/docs/README.md)
* [TF::NSXT::PolicyDhcpV6StaticBinding](../resources/nsxt/TF-NSXT-PolicyDhcpV6StaticBinding/docs/README.md)
* [TF::NSXT::PolicyDnsForwarderZone](../resources/nsxt/TF-NSXT-PolicyDnsForwarderZone/docs/README.md)
* [TF::NSXT::PolicyDomain](../resources/nsxt/TF-NSXT-PolicyDomain/docs/README.md)
* [TF::NSXT::PolicyEvpnConfig](../resources/nsxt/TF-NSXT-PolicyEvpnConfig/docs/README.md)
* [TF::NSXT::PolicyEvpnTenant](../resources/nsxt/TF-NSXT-PolicyEvpnTenant/docs/README.md)
* [TF::NSXT::PolicyEvpnTunnelEndpoint](../resources/nsxt/TF-NSXT-PolicyEvpnTunnelEndpoint/docs/README.md)
* [TF::NSXT::PolicyFixedSegment](../resources/nsxt/TF-NSXT-PolicyFixedSegment/docs/README.md)
* [TF::NSXT::PolicyGatewayCommunityList](../resources/nsxt/TF-NSXT-PolicyGatewayCommunityList/docs/README.md)
* [TF::NSXT::PolicyGatewayDnsForwarder](../resources/nsxt/TF-NSXT-PolicyGatewayDnsForwarder/docs/README.md)
* [TF::NSXT::PolicyGatewayPolicy](../resources/nsxt/TF-NSXT-PolicyGatewayPolicy/docs/README.md)
* [TF::NSXT::PolicyGatewayPrefixList](../resources/nsxt/TF-NSXT-PolicyGatewayPrefixList/docs/README.md)
* [TF::NSXT::PolicyGatewayRedistributionConfig](../resources/nsxt/TF-NSXT-PolicyGatewayRedistributionConfig/docs/README.md)
* [TF::NSXT::PolicyGatewayRouteMap](../resources/nsxt/TF-NSXT-PolicyGatewayRouteMap/docs/README.md)
* [TF::NSXT::PolicyGroup](../resources/nsxt/TF-NSXT-PolicyGroup/docs/README.md)
* [TF::NSXT::PolicyIntrusionServicePolicy](../resources/nsxt/TF-NSXT-PolicyIntrusionServicePolicy/docs/README.md)
* [TF::NSXT::PolicyIntrusionServiceProfile](../resources/nsxt/TF-NSXT-PolicyIntrusionServiceProfile/docs/README.md)
* [TF::NSXT::PolicyIpAddressAllocation](../resources/nsxt/TF-NSXT-PolicyIpAddressAllocation/docs/README.md)
* [TF::NSXT::PolicyIpBlock](../resources/nsxt/TF-NSXT-PolicyIpBlock/docs/README.md)
* [TF::NSXT::PolicyIpPoolBlockSubnet](../resources/nsxt/TF-NSXT-PolicyIpPoolBlockSubnet/docs/README.md)
* [TF::NSXT::PolicyIpPoolStaticSubnet](../resources/nsxt/TF-NSXT-PolicyIpPoolStaticSubnet/docs/README.md)
* [TF::NSXT::PolicyIpPool](../resources/nsxt/TF-NSXT-PolicyIpPool/docs/README.md)
* [TF::NSXT::PolicyLbPool](../resources/nsxt/TF-NSXT-PolicyLbPool/docs/README.md)
* [TF::NSXT::PolicyLbService](../resources/nsxt/TF-NSXT-PolicyLbService/docs/README.md)
* [TF::NSXT::PolicyLbVirtualServer](../resources/nsxt/TF-NSXT-PolicyLbVirtualServer/docs/README.md)
* [TF::NSXT::PolicyNatRule](../resources/nsxt/TF-NSXT-PolicyNatRule/docs/README.md)
* [TF::NSXT::PolicyOspfArea](../resources/nsxt/TF-NSXT-PolicyOspfArea/docs/README.md)
* [TF::NSXT::PolicyOspfConfig](../resources/nsxt/TF-NSXT-PolicyOspfConfig/docs/README.md)
* [TF::NSXT::PolicyPredefinedGatewayPolicy](../resources/nsxt/TF-NSXT-PolicyPredefinedGatewayPolicy/docs/README.md)
* [TF::NSXT::PolicyPredefinedSecurityPolicy](../resources/nsxt/TF-NSXT-PolicyPredefinedSecurityPolicy/docs/README.md)
* [TF::NSXT::PolicyQosProfile](../resources/nsxt/TF-NSXT-PolicyQosProfile/docs/README.md)
* [TF::NSXT::PolicySecurityPolicy](../resources/nsxt/TF-NSXT-PolicySecurityPolicy/docs/README.md)
* [TF::NSXT::PolicySegment](../resources/nsxt/TF-NSXT-PolicySegment/docs/README.md)
* [TF::NSXT::PolicyService](../resources/nsxt/TF-NSXT-PolicyService/docs/README.md)
* [TF::NSXT::PolicyStaticRouteBfdPeer](../resources/nsxt/TF-NSXT-PolicyStaticRouteBfdPeer/docs/README.md)
* [TF::NSXT::PolicyStaticRoute](../resources/nsxt/TF-NSXT-PolicyStaticRoute/docs/README.md)
* [TF::NSXT::PolicyTier0GatewayHaVipConfig](../resources/nsxt/TF-NSXT-PolicyTier0GatewayHaVipConfig/docs/README.md)
* [TF::NSXT::PolicyTier0GatewayInterface](../resources/nsxt/TF-NSXT-PolicyTier0GatewayInterface/docs/README.md)
* [TF::NSXT::PolicyTier0Gateway](../resources/nsxt/TF-NSXT-PolicyTier0Gateway/docs/README.md)
* [TF::NSXT::PolicyTier1GatewayInterface](../resources/nsxt/TF-NSXT-PolicyTier1GatewayInterface/docs/README.md)
* [TF::NSXT::PolicyTier1Gateway](../resources/nsxt/TF-NSXT-PolicyTier1Gateway/docs/README.md)
* [TF::NSXT::PolicyVlanSegment](../resources/nsxt/TF-NSXT-PolicyVlanSegment/docs/README.md)
* [TF::NSXT::PolicyVmTags](../resources/nsxt/TF-NSXT-PolicyVmTags/docs/README.md)
* [TF::NSXT::QosSwitchingProfile](../resources/nsxt/TF-NSXT-QosSwitchingProfile/docs/README.md)
* [TF::NSXT::SpoofguardSwitchingProfile](../resources/nsxt/TF-NSXT-SpoofguardSwitchingProfile/docs/README.md)
* [TF::NSXT::StaticRoute](../resources/nsxt/TF-NSXT-StaticRoute/docs/README.md)
* [TF::NSXT::SwitchSecuritySwitchingProfile](../resources/nsxt/TF-NSXT-SwitchSecuritySwitchingProfile/docs/README.md)
* [TF::NSXT::VlanLogicalSwitch](../resources/nsxt/TF-NSXT-VlanLogicalSwitch/docs/README.md)
* [TF::NSXT::VmTags](../resources/nsxt/TF-NSXT-VmTags/docs/README.md)