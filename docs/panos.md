# Palo Alto Networks Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/panos**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `hostname` - (Optional) This is the hostname / IP address of the firewall.
* `username` - (Optional) The username to authenticate to the firewall as.
* `password` - (Optional) The password for the given username. It must be
  provided, but can also be defined via the `PANOS_PASSWORD` environment
  variable.
* `api_key` - (Optional) The API key for the firewall.  If this is given, then
  the `username` and `password` settings are ignored.
* `protocol` - (Optional) The communication protocol.  This can be set to
  either `https` or `http`.  If left unspecified, this defaults to `https`.
* `port` - (Optional) If the port number is non-standard for the desired
  protocol, then the port number to use.
* `timeout` - (Optional) The timeout for all communications with the
  firewall.  If left unspecified, this will be set to 10 seconds.
* `logging` - (Optional) List of logging options for the provider's connection
  to the API.  If this is unspecified, then it defaults to
  `["action", "uid"]`.
* `verify_certificate` - (Optional, bool, added in v1.6.1) For HTTPS protocol
  connections, verify that the certificate is valid.
* `json_config_file` - (Optional) The path to a JSON configuration file that
  contains any number of the provider's parameters.  If specified, the params
  present act as a last resort for any other provider param that has not been
  specified yet.

The list of strings supported for `logging` are as follows:

* `quiet` - Disables logging.  This is ignored, however, if other logging
  flags are present.
* `action` - Log `set` / `edit` / `delete`.
* `query` - Log `get`.
* `op` - Log `op`.
* `uid` - Log user-id envocations.
* `xpath` - Log the XPATH associated with various actions.
* `send` - Log the raw request sent to the device.  This is probably
  only useful in development of the provider itself.
* `receive` - Log the raw response sent back from the device.  This is probably
  only useful in development of the provider itself.


## Supported Resources

* [Terraform::Panos::AddressGroup](../resources/panos/Terraform-Panos-AddressGroup/docs/README.md)
* [Terraform::Panos::AddressObject](../resources/panos/Terraform-Panos-AddressObject/docs/README.md)
* [Terraform::Panos::AdministrativeTag](../resources/panos/Terraform-Panos-AdministrativeTag/docs/README.md)
* [Terraform::Panos::AggregateInterface](../resources/panos/Terraform-Panos-AggregateInterface/docs/README.md)
* [Terraform::Panos::ApplicationGroup](../resources/panos/Terraform-Panos-ApplicationGroup/docs/README.md)
* [Terraform::Panos::ApplicationObject](../resources/panos/Terraform-Panos-ApplicationObject/docs/README.md)
* [Terraform::Panos::ApplicationSignature](../resources/panos/Terraform-Panos-ApplicationSignature/docs/README.md)
* [Terraform::Panos::BfdProfile](../resources/panos/Terraform-Panos-BfdProfile/docs/README.md)
* [Terraform::Panos::BgpAggregateAdvertiseFilter](../resources/panos/Terraform-Panos-BgpAggregateAdvertiseFilter/docs/README.md)
* [Terraform::Panos::BgpAggregateSuppressFilter](../resources/panos/Terraform-Panos-BgpAggregateSuppressFilter/docs/README.md)
* [Terraform::Panos::BgpAggregate](../resources/panos/Terraform-Panos-BgpAggregate/docs/README.md)
* [Terraform::Panos::BgpAuthProfile](../resources/panos/Terraform-Panos-BgpAuthProfile/docs/README.md)
* [Terraform::Panos::BgpConditionalAdvAdvertiseFilter](../resources/panos/Terraform-Panos-BgpConditionalAdvAdvertiseFilter/docs/README.md)
* [Terraform::Panos::BgpConditionalAdvNonExistFilter](../resources/panos/Terraform-Panos-BgpConditionalAdvNonExistFilter/docs/README.md)
* [Terraform::Panos::BgpConditionalAdv](../resources/panos/Terraform-Panos-BgpConditionalAdv/docs/README.md)
* [Terraform::Panos::BgpDampeningProfile](../resources/panos/Terraform-Panos-BgpDampeningProfile/docs/README.md)
* [Terraform::Panos::BgpExportRuleGroup](../resources/panos/Terraform-Panos-BgpExportRuleGroup/docs/README.md)
* [Terraform::Panos::BgpImportRuleGroup](../resources/panos/Terraform-Panos-BgpImportRuleGroup/docs/README.md)
* [Terraform::Panos::BgpPeerGroup](../resources/panos/Terraform-Panos-BgpPeerGroup/docs/README.md)
* [Terraform::Panos::BgpPeer](../resources/panos/Terraform-Panos-BgpPeer/docs/README.md)
* [Terraform::Panos::BgpRedistRule](../resources/panos/Terraform-Panos-BgpRedistRule/docs/README.md)
* [Terraform::Panos::Bgp](../resources/panos/Terraform-Panos-Bgp/docs/README.md)
* [Terraform::Panos::DagTags](../resources/panos/Terraform-Panos-DagTags/docs/README.md)
* [Terraform::Panos::Edl](../resources/panos/Terraform-Panos-Edl/docs/README.md)
* [Terraform::Panos::EmailServerProfile](../resources/panos/Terraform-Panos-EmailServerProfile/docs/README.md)
* [Terraform::Panos::EthernetInterface](../resources/panos/Terraform-Panos-EthernetInterface/docs/README.md)
* [Terraform::Panos::GeneralSettings](../resources/panos/Terraform-Panos-GeneralSettings/docs/README.md)
* [Terraform::Panos::GreTunnel](../resources/panos/Terraform-Panos-GreTunnel/docs/README.md)
* [Terraform::Panos::HttpServerProfile](../resources/panos/Terraform-Panos-HttpServerProfile/docs/README.md)
* [Terraform::Panos::IkeCryptoProfile](../resources/panos/Terraform-Panos-IkeCryptoProfile/docs/README.md)
* [Terraform::Panos::IkeGateway](../resources/panos/Terraform-Panos-IkeGateway/docs/README.md)
* [Terraform::Panos::IpsecCryptoProfile](../resources/panos/Terraform-Panos-IpsecCryptoProfile/docs/README.md)
* [Terraform::Panos::IpsecTunnelProxyIdIpv4](../resources/panos/Terraform-Panos-IpsecTunnelProxyIdIpv4/docs/README.md)
* [Terraform::Panos::IpsecTunnel](../resources/panos/Terraform-Panos-IpsecTunnel/docs/README.md)
* [Terraform::Panos::Layer2Subinterface](../resources/panos/Terraform-Panos-Layer2Subinterface/docs/README.md)
* [Terraform::Panos::Layer3Subinterface](../resources/panos/Terraform-Panos-Layer3Subinterface/docs/README.md)
* [Terraform::Panos::LicenseApiKey](../resources/panos/Terraform-Panos-LicenseApiKey/docs/README.md)
* [Terraform::Panos::Licensing](../resources/panos/Terraform-Panos-Licensing/docs/README.md)
* [Terraform::Panos::LogForwardingProfile](../resources/panos/Terraform-Panos-LogForwardingProfile/docs/README.md)
* [Terraform::Panos::LoopbackInterface](../resources/panos/Terraform-Panos-LoopbackInterface/docs/README.md)
* [Terraform::Panos::ManagementProfile](../resources/panos/Terraform-Panos-ManagementProfile/docs/README.md)
* [Terraform::Panos::MonitorProfile](../resources/panos/Terraform-Panos-MonitorProfile/docs/README.md)
* [Terraform::Panos::NatPolicy](../resources/panos/Terraform-Panos-NatPolicy/docs/README.md)
* [Terraform::Panos::NatRuleGroup](../resources/panos/Terraform-Panos-NatRuleGroup/docs/README.md)
* [Terraform::Panos::NatRule](../resources/panos/Terraform-Panos-NatRule/docs/README.md)
* [Terraform::Panos::PanoramaAddressGroup](../resources/panos/Terraform-Panos-PanoramaAddressGroup/docs/README.md)
* [Terraform::Panos::PanoramaAddressObject](../resources/panos/Terraform-Panos-PanoramaAddressObject/docs/README.md)
* [Terraform::Panos::PanoramaAdministrativeTag](../resources/panos/Terraform-Panos-PanoramaAdministrativeTag/docs/README.md)
* [Terraform::Panos::PanoramaAggregateInterface](../resources/panos/Terraform-Panos-PanoramaAggregateInterface/docs/README.md)
* [Terraform::Panos::PanoramaApplicationGroup](../resources/panos/Terraform-Panos-PanoramaApplicationGroup/docs/README.md)
* [Terraform::Panos::PanoramaApplicationObject](../resources/panos/Terraform-Panos-PanoramaApplicationObject/docs/README.md)
* [Terraform::Panos::PanoramaApplicationSignature](../resources/panos/Terraform-Panos-PanoramaApplicationSignature/docs/README.md)
* [Terraform::Panos::PanoramaBfdProfile](../resources/panos/Terraform-Panos-PanoramaBfdProfile/docs/README.md)
* [Terraform::Panos::PanoramaBgpAggregateAdvertiseFilter](../resources/panos/Terraform-Panos-PanoramaBgpAggregateAdvertiseFilter/docs/README.md)
* [Terraform::Panos::PanoramaBgpAggregateSuppressFilter](../resources/panos/Terraform-Panos-PanoramaBgpAggregateSuppressFilter/docs/README.md)
* [Terraform::Panos::PanoramaBgpAggregate](../resources/panos/Terraform-Panos-PanoramaBgpAggregate/docs/README.md)
* [Terraform::Panos::PanoramaBgpAuthProfile](../resources/panos/Terraform-Panos-PanoramaBgpAuthProfile/docs/README.md)
* [Terraform::Panos::PanoramaBgpConditionalAdvAdvertiseFilter](../resources/panos/Terraform-Panos-PanoramaBgpConditionalAdvAdvertiseFilter/docs/README.md)
* [Terraform::Panos::PanoramaBgpConditionalAdvNonExistFilter](../resources/panos/Terraform-Panos-PanoramaBgpConditionalAdvNonExistFilter/docs/README.md)
* [Terraform::Panos::PanoramaBgpConditionalAdv](../resources/panos/Terraform-Panos-PanoramaBgpConditionalAdv/docs/README.md)
* [Terraform::Panos::PanoramaBgpDampeningProfile](../resources/panos/Terraform-Panos-PanoramaBgpDampeningProfile/docs/README.md)
* [Terraform::Panos::PanoramaBgpExportRuleGroup](../resources/panos/Terraform-Panos-PanoramaBgpExportRuleGroup/docs/README.md)
* [Terraform::Panos::PanoramaBgpImportRuleGroup](../resources/panos/Terraform-Panos-PanoramaBgpImportRuleGroup/docs/README.md)
* [Terraform::Panos::PanoramaBgpPeerGroup](../resources/panos/Terraform-Panos-PanoramaBgpPeerGroup/docs/README.md)
* [Terraform::Panos::PanoramaBgpPeer](../resources/panos/Terraform-Panos-PanoramaBgpPeer/docs/README.md)
* [Terraform::Panos::PanoramaBgpRedistRule](../resources/panos/Terraform-Panos-PanoramaBgpRedistRule/docs/README.md)
* [Terraform::Panos::PanoramaBgp](../resources/panos/Terraform-Panos-PanoramaBgp/docs/README.md)
* [Terraform::Panos::PanoramaDeviceGroupEntry](../resources/panos/Terraform-Panos-PanoramaDeviceGroupEntry/docs/README.md)
* [Terraform::Panos::PanoramaDeviceGroup](../resources/panos/Terraform-Panos-PanoramaDeviceGroup/docs/README.md)
* [Terraform::Panos::PanoramaEdl](../resources/panos/Terraform-Panos-PanoramaEdl/docs/README.md)
* [Terraform::Panos::PanoramaEmailServerProfile](../resources/panos/Terraform-Panos-PanoramaEmailServerProfile/docs/README.md)
* [Terraform::Panos::PanoramaEthernetInterface](../resources/panos/Terraform-Panos-PanoramaEthernetInterface/docs/README.md)
* [Terraform::Panos::PanoramaGcpAccount](../resources/panos/Terraform-Panos-PanoramaGcpAccount/docs/README.md)
* [Terraform::Panos::PanoramaGkeClusterGroup](../resources/panos/Terraform-Panos-PanoramaGkeClusterGroup/docs/README.md)
* [Terraform::Panos::PanoramaGkeCluster](../resources/panos/Terraform-Panos-PanoramaGkeCluster/docs/README.md)
* [Terraform::Panos::PanoramaGreTunnel](../resources/panos/Terraform-Panos-PanoramaGreTunnel/docs/README.md)
* [Terraform::Panos::PanoramaHttpServerProfile](../resources/panos/Terraform-Panos-PanoramaHttpServerProfile/docs/README.md)
* [Terraform::Panos::PanoramaIkeCryptoProfile](../resources/panos/Terraform-Panos-PanoramaIkeCryptoProfile/docs/README.md)
* [Terraform::Panos::PanoramaIkeGateway](../resources/panos/Terraform-Panos-PanoramaIkeGateway/docs/README.md)
* [Terraform::Panos::PanoramaIpsecCryptoProfile](../resources/panos/Terraform-Panos-PanoramaIpsecCryptoProfile/docs/README.md)
* [Terraform::Panos::PanoramaIpsecTunnelProxyIdIpv4](../resources/panos/Terraform-Panos-PanoramaIpsecTunnelProxyIdIpv4/docs/README.md)
* [Terraform::Panos::PanoramaIpsecTunnel](../resources/panos/Terraform-Panos-PanoramaIpsecTunnel/docs/README.md)
* [Terraform::Panos::PanoramaLayer2Subinterface](../resources/panos/Terraform-Panos-PanoramaLayer2Subinterface/docs/README.md)
* [Terraform::Panos::PanoramaLayer3Subinterface](../resources/panos/Terraform-Panos-PanoramaLayer3Subinterface/docs/README.md)
* [Terraform::Panos::PanoramaLogForwardingProfile](../resources/panos/Terraform-Panos-PanoramaLogForwardingProfile/docs/README.md)
* [Terraform::Panos::PanoramaLoopbackInterface](../resources/panos/Terraform-Panos-PanoramaLoopbackInterface/docs/README.md)
* [Terraform::Panos::PanoramaManagementProfile](../resources/panos/Terraform-Panos-PanoramaManagementProfile/docs/README.md)
* [Terraform::Panos::PanoramaMonitorProfile](../resources/panos/Terraform-Panos-PanoramaMonitorProfile/docs/README.md)
* [Terraform::Panos::PanoramaNatPolicy](../resources/panos/Terraform-Panos-PanoramaNatPolicy/docs/README.md)
* [Terraform::Panos::PanoramaNatRuleGroup](../resources/panos/Terraform-Panos-PanoramaNatRuleGroup/docs/README.md)
* [Terraform::Panos::PanoramaNatRule](../resources/panos/Terraform-Panos-PanoramaNatRule/docs/README.md)
* [Terraform::Panos::PanoramaPbfRuleGroup](../resources/panos/Terraform-Panos-PanoramaPbfRuleGroup/docs/README.md)
* [Terraform::Panos::PanoramaRedistributionProfileIpv4](../resources/panos/Terraform-Panos-PanoramaRedistributionProfileIpv4/docs/README.md)
* [Terraform::Panos::PanoramaSecurityPolicies](../resources/panos/Terraform-Panos-PanoramaSecurityPolicies/docs/README.md)
* [Terraform::Panos::PanoramaSecurityPolicyGroup](../resources/panos/Terraform-Panos-PanoramaSecurityPolicyGroup/docs/README.md)
* [Terraform::Panos::PanoramaSecurityPolicy](../resources/panos/Terraform-Panos-PanoramaSecurityPolicy/docs/README.md)
* [Terraform::Panos::PanoramaSecurityRuleGroup](../resources/panos/Terraform-Panos-PanoramaSecurityRuleGroup/docs/README.md)
* [Terraform::Panos::PanoramaServiceGroup](../resources/panos/Terraform-Panos-PanoramaServiceGroup/docs/README.md)
* [Terraform::Panos::PanoramaServiceObject](../resources/panos/Terraform-Panos-PanoramaServiceObject/docs/README.md)
* [Terraform::Panos::PanoramaSnmptrapServerProfile](../resources/panos/Terraform-Panos-PanoramaSnmptrapServerProfile/docs/README.md)
* [Terraform::Panos::PanoramaStaticRouteIpv4](../resources/panos/Terraform-Panos-PanoramaStaticRouteIpv4/docs/README.md)
* [Terraform::Panos::PanoramaSyslogServerProfile](../resources/panos/Terraform-Panos-PanoramaSyslogServerProfile/docs/README.md)
* [Terraform::Panos::PanoramaTemplateEntry](../resources/panos/Terraform-Panos-PanoramaTemplateEntry/docs/README.md)
* [Terraform::Panos::PanoramaTemplateStackEntry](../resources/panos/Terraform-Panos-PanoramaTemplateStackEntry/docs/README.md)
* [Terraform::Panos::PanoramaTemplateStack](../resources/panos/Terraform-Panos-PanoramaTemplateStack/docs/README.md)
* [Terraform::Panos::PanoramaTemplateVariable](../resources/panos/Terraform-Panos-PanoramaTemplateVariable/docs/README.md)
* [Terraform::Panos::PanoramaTemplate](../resources/panos/Terraform-Panos-PanoramaTemplate/docs/README.md)
* [Terraform::Panos::PanoramaTunnelInterface](../resources/panos/Terraform-Panos-PanoramaTunnelInterface/docs/README.md)
* [Terraform::Panos::PanoramaVirtualRouterEntry](../resources/panos/Terraform-Panos-PanoramaVirtualRouterEntry/docs/README.md)
* [Terraform::Panos::PanoramaVirtualRouter](../resources/panos/Terraform-Panos-PanoramaVirtualRouter/docs/README.md)
* [Terraform::Panos::PanoramaVlanEntry](../resources/panos/Terraform-Panos-PanoramaVlanEntry/docs/README.md)
* [Terraform::Panos::PanoramaVlanInterface](../resources/panos/Terraform-Panos-PanoramaVlanInterface/docs/README.md)
* [Terraform::Panos::PanoramaVlan](../resources/panos/Terraform-Panos-PanoramaVlan/docs/README.md)
* [Terraform::Panos::PanoramaZoneEntry](../resources/panos/Terraform-Panos-PanoramaZoneEntry/docs/README.md)
* [Terraform::Panos::PanoramaZone](../resources/panos/Terraform-Panos-PanoramaZone/docs/README.md)
* [Terraform::Panos::PbfRuleGroup](../resources/panos/Terraform-Panos-PbfRuleGroup/docs/README.md)
* [Terraform::Panos::RedistributionProfileIpv4](../resources/panos/Terraform-Panos-RedistributionProfileIpv4/docs/README.md)
* [Terraform::Panos::SecurityPolicies](../resources/panos/Terraform-Panos-SecurityPolicies/docs/README.md)
* [Terraform::Panos::SecurityPolicyGroup](../resources/panos/Terraform-Panos-SecurityPolicyGroup/docs/README.md)
* [Terraform::Panos::SecurityPolicy](../resources/panos/Terraform-Panos-SecurityPolicy/docs/README.md)
* [Terraform::Panos::SecurityRuleGroup](../resources/panos/Terraform-Panos-SecurityRuleGroup/docs/README.md)
* [Terraform::Panos::ServiceGroup](../resources/panos/Terraform-Panos-ServiceGroup/docs/README.md)
* [Terraform::Panos::ServiceObject](../resources/panos/Terraform-Panos-ServiceObject/docs/README.md)
* [Terraform::Panos::SnmptrapServerProfile](../resources/panos/Terraform-Panos-SnmptrapServerProfile/docs/README.md)
* [Terraform::Panos::StaticRouteIpv4](../resources/panos/Terraform-Panos-StaticRouteIpv4/docs/README.md)
* [Terraform::Panos::SyslogServerProfile](../resources/panos/Terraform-Panos-SyslogServerProfile/docs/README.md)
* [Terraform::Panos::Telemetry](../resources/panos/Terraform-Panos-Telemetry/docs/README.md)
* [Terraform::Panos::TunnelInterface](../resources/panos/Terraform-Panos-TunnelInterface/docs/README.md)
* [Terraform::Panos::VirtualRouterEntry](../resources/panos/Terraform-Panos-VirtualRouterEntry/docs/README.md)
* [Terraform::Panos::VirtualRouter](../resources/panos/Terraform-Panos-VirtualRouter/docs/README.md)
* [Terraform::Panos::VlanEntry](../resources/panos/Terraform-Panos-VlanEntry/docs/README.md)
* [Terraform::Panos::VlanInterface](../resources/panos/Terraform-Panos-VlanInterface/docs/README.md)
* [Terraform::Panos::Vlan](../resources/panos/Terraform-Panos-Vlan/docs/README.md)
* [Terraform::Panos::ZoneEntry](../resources/panos/Terraform-Panos-ZoneEntry/docs/README.md)
* [Terraform::Panos::Zone](../resources/panos/Terraform-Panos-Zone/docs/README.md)