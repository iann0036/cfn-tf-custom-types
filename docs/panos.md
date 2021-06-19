# Palo Alto Networks Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/panos**. The below arguments may be included as the key/value or JSON properties in the secret:

* `hostname` - (Optional, env:`PANOS_HOSTNAME`) The hostname / IP address of PAN-OS.
* `username` - (Optional, env:`PANOS_USERNAME`) The PAN-OS username.  This is ignored
  if the `api_key` is given.
* `password` - (Optional, env:`PANOS_PASSWORD`) The PAN-OS password.  This is ignored
  if the `api_key` is given.
* `api_key` - (Optional, env:`PANOS_API_KEY`) The API key for the firewall.
* `protocol` - (Optional, env:`PANOS_PROTOCOL`) The communication protocol.  Valid
  values are `https` (the default) or `http`.
* `port` - (Optional, int, env:`PANOS_PORT`) If the port number is non-standard for
  the desired protocol, then the port number to use.
* `timeout` - (Optional, int, env:`PANOS_TIMEOUT`) The timeout for all communications
  with PAN-OS (default: `10`).
* `target` - (Optional, env:`PANOS_TARGET`) The firewall serial number to target
  configuration commands to (the `hostname` should be a Panorama PAN-OS).
* `logging` - (Optional, env:`PANOS_LOGGING`) List of logging options for the
  provider's connection to the API.  If this is unspecified, then it defaults to
  `["action", "uid"]`.
* `verify_certificate` - (Optional, bool, env:`PANOS_VERIFY_CERTIFICATE`) For HTTPS
  protocol connections, verify that the certificate is valid.
* `json_config_file` - (Optional) The path to a JSON configuration file that
  contains any number of the provider's parameters.  If specified, the params
  present act as a last resort for any other provider param that has not been
  specified yet.  Params in the JSON config file match what the provider block
  supports, both in naming convention and data types.  See below for an example of
  the JSON config file contents.

The list of strings supported for `logging` are as follows:

* `quiet` - Disables logging if only `quiet` is specified.
* `action` - Log `set` / `edit` / `delete`.
* `query` - Log `get`.
* `op` - Log `op`.
* `uid` - Log user-id envocations.
* `xpath` - Log the XPATH associated with various actions.
* `send` - Log the raw request sent to the device.  This is probably
  only useful in development of the provider itself.
* `receive` - Log the raw response sent back from the device.  This is probably
  only useful in development of the provider itself.

The following is an example of the contents of a JSON config file:

```json
{
    "hostname": "127.0.0.1",
    "api_key": "secret",
    "timeout": 10,
    "logging": ["action", "op", "uid"],
    "verify_certificate": false
}
```


## Supported Resources

* [TF::Panos::AddressGroup](../resources/panos/TF-Panos-AddressGroup/docs/README.md)
* [TF::Panos::AddressObject](../resources/panos/TF-Panos-AddressObject/docs/README.md)
* [TF::Panos::AdministrativeTag](../resources/panos/TF-Panos-AdministrativeTag/docs/README.md)
* [TF::Panos::AggregateInterface](../resources/panos/TF-Panos-AggregateInterface/docs/README.md)
* [TF::Panos::AntiSpywareSecurityProfile](../resources/panos/TF-Panos-AntiSpywareSecurityProfile/docs/README.md)
* [TF::Panos::AntivirusSecurityProfile](../resources/panos/TF-Panos-AntivirusSecurityProfile/docs/README.md)
* [TF::Panos::ApplicationGroup](../resources/panos/TF-Panos-ApplicationGroup/docs/README.md)
* [TF::Panos::ApplicationObject](../resources/panos/TF-Panos-ApplicationObject/docs/README.md)
* [TF::Panos::ApplicationSignature](../resources/panos/TF-Panos-ApplicationSignature/docs/README.md)
* [TF::Panos::Arp](../resources/panos/TF-Panos-Arp/docs/README.md)
* [TF::Panos::BfdProfile](../resources/panos/TF-Panos-BfdProfile/docs/README.md)
* [TF::Panos::BgpAggregateAdvertiseFilter](../resources/panos/TF-Panos-BgpAggregateAdvertiseFilter/docs/README.md)
* [TF::Panos::BgpAggregateSuppressFilter](../resources/panos/TF-Panos-BgpAggregateSuppressFilter/docs/README.md)
* [TF::Panos::BgpAggregate](../resources/panos/TF-Panos-BgpAggregate/docs/README.md)
* [TF::Panos::BgpAuthProfile](../resources/panos/TF-Panos-BgpAuthProfile/docs/README.md)
* [TF::Panos::BgpConditionalAdvAdvertiseFilter](../resources/panos/TF-Panos-BgpConditionalAdvAdvertiseFilter/docs/README.md)
* [TF::Panos::BgpConditionalAdvNonExistFilter](../resources/panos/TF-Panos-BgpConditionalAdvNonExistFilter/docs/README.md)
* [TF::Panos::BgpConditionalAdv](../resources/panos/TF-Panos-BgpConditionalAdv/docs/README.md)
* [TF::Panos::BgpDampeningProfile](../resources/panos/TF-Panos-BgpDampeningProfile/docs/README.md)
* [TF::Panos::BgpExportRuleGroup](../resources/panos/TF-Panos-BgpExportRuleGroup/docs/README.md)
* [TF::Panos::BgpImportRuleGroup](../resources/panos/TF-Panos-BgpImportRuleGroup/docs/README.md)
* [TF::Panos::BgpPeerGroup](../resources/panos/TF-Panos-BgpPeerGroup/docs/README.md)
* [TF::Panos::BgpPeer](../resources/panos/TF-Panos-BgpPeer/docs/README.md)
* [TF::Panos::BgpRedistRule](../resources/panos/TF-Panos-BgpRedistRule/docs/README.md)
* [TF::Panos::Bgp](../resources/panos/TF-Panos-Bgp/docs/README.md)
* [TF::Panos::CustomDataPatternObject](../resources/panos/TF-Panos-CustomDataPatternObject/docs/README.md)
* [TF::Panos::DagTags](../resources/panos/TF-Panos-DagTags/docs/README.md)
* [TF::Panos::DataFilteringSecurityProfile](../resources/panos/TF-Panos-DataFilteringSecurityProfile/docs/README.md)
* [TF::Panos::DeviceGroupParent](../resources/panos/TF-Panos-DeviceGroupParent/docs/README.md)
* [TF::Panos::DosProtectionProfile](../resources/panos/TF-Panos-DosProtectionProfile/docs/README.md)
* [TF::Panos::DynamicUserGroup](../resources/panos/TF-Panos-DynamicUserGroup/docs/README.md)
* [TF::Panos::Edl](../resources/panos/TF-Panos-Edl/docs/README.md)
* [TF::Panos::EmailServerProfile](../resources/panos/TF-Panos-EmailServerProfile/docs/README.md)
* [TF::Panos::EthernetInterface](../resources/panos/TF-Panos-EthernetInterface/docs/README.md)
* [TF::Panos::FileBlockingSecurityProfile](../resources/panos/TF-Panos-FileBlockingSecurityProfile/docs/README.md)
* [TF::Panos::GeneralSettings](../resources/panos/TF-Panos-GeneralSettings/docs/README.md)
* [TF::Panos::GreTunnel](../resources/panos/TF-Panos-GreTunnel/docs/README.md)
* [TF::Panos::HttpServerProfile](../resources/panos/TF-Panos-HttpServerProfile/docs/README.md)
* [TF::Panos::IkeCryptoProfile](../resources/panos/TF-Panos-IkeCryptoProfile/docs/README.md)
* [TF::Panos::IkeGateway](../resources/panos/TF-Panos-IkeGateway/docs/README.md)
* [TF::Panos::IpTag](../resources/panos/TF-Panos-IpTag/docs/README.md)
* [TF::Panos::IpsecCryptoProfile](../resources/panos/TF-Panos-IpsecCryptoProfile/docs/README.md)
* [TF::Panos::IpsecTunnelProxyIdIpv4](../resources/panos/TF-Panos-IpsecTunnelProxyIdIpv4/docs/README.md)
* [TF::Panos::IpsecTunnel](../resources/panos/TF-Panos-IpsecTunnel/docs/README.md)
* [TF::Panos::Layer2Subinterface](../resources/panos/TF-Panos-Layer2Subinterface/docs/README.md)
* [TF::Panos::Layer3Subinterface](../resources/panos/TF-Panos-Layer3Subinterface/docs/README.md)
* [TF::Panos::LicenseApiKey](../resources/panos/TF-Panos-LicenseApiKey/docs/README.md)
* [TF::Panos::Licensing](../resources/panos/TF-Panos-Licensing/docs/README.md)
* [TF::Panos::LogForwardingProfile](../resources/panos/TF-Panos-LogForwardingProfile/docs/README.md)
* [TF::Panos::LoopbackInterface](../resources/panos/TF-Panos-LoopbackInterface/docs/README.md)
* [TF::Panos::ManagementProfile](../resources/panos/TF-Panos-ManagementProfile/docs/README.md)
* [TF::Panos::MonitorProfile](../resources/panos/TF-Panos-MonitorProfile/docs/README.md)
* [TF::Panos::NatPolicy](../resources/panos/TF-Panos-NatPolicy/docs/README.md)
* [TF::Panos::NatRuleGroup](../resources/panos/TF-Panos-NatRuleGroup/docs/README.md)
* [TF::Panos::NatRule](../resources/panos/TF-Panos-NatRule/docs/README.md)
* [TF::Panos::OspfAreaInterface](../resources/panos/TF-Panos-OspfAreaInterface/docs/README.md)
* [TF::Panos::OspfAreaVirtualLink](../resources/panos/TF-Panos-OspfAreaVirtualLink/docs/README.md)
* [TF::Panos::OspfArea](../resources/panos/TF-Panos-OspfArea/docs/README.md)
* [TF::Panos::OspfAuthProfile](../resources/panos/TF-Panos-OspfAuthProfile/docs/README.md)
* [TF::Panos::OspfExport](../resources/panos/TF-Panos-OspfExport/docs/README.md)
* [TF::Panos::Ospf](../resources/panos/TF-Panos-Ospf/docs/README.md)
* [TF::Panos::PanoramaAddressGroup](../resources/panos/TF-Panos-PanoramaAddressGroup/docs/README.md)
* [TF::Panos::PanoramaAddressObject](../resources/panos/TF-Panos-PanoramaAddressObject/docs/README.md)
* [TF::Panos::PanoramaAdministrativeTag](../resources/panos/TF-Panos-PanoramaAdministrativeTag/docs/README.md)
* [TF::Panos::PanoramaAggregateInterface](../resources/panos/TF-Panos-PanoramaAggregateInterface/docs/README.md)
* [TF::Panos::PanoramaApplicationGroup](../resources/panos/TF-Panos-PanoramaApplicationGroup/docs/README.md)
* [TF::Panos::PanoramaApplicationObject](../resources/panos/TF-Panos-PanoramaApplicationObject/docs/README.md)
* [TF::Panos::PanoramaApplicationSignature](../resources/panos/TF-Panos-PanoramaApplicationSignature/docs/README.md)
* [TF::Panos::PanoramaBfdProfile](../resources/panos/TF-Panos-PanoramaBfdProfile/docs/README.md)
* [TF::Panos::PanoramaBgpAggregateAdvertiseFilter](../resources/panos/TF-Panos-PanoramaBgpAggregateAdvertiseFilter/docs/README.md)
* [TF::Panos::PanoramaBgpAggregateSuppressFilter](../resources/panos/TF-Panos-PanoramaBgpAggregateSuppressFilter/docs/README.md)
* [TF::Panos::PanoramaBgpAggregate](../resources/panos/TF-Panos-PanoramaBgpAggregate/docs/README.md)
* [TF::Panos::PanoramaBgpAuthProfile](../resources/panos/TF-Panos-PanoramaBgpAuthProfile/docs/README.md)
* [TF::Panos::PanoramaBgpConditionalAdvAdvertiseFilter](../resources/panos/TF-Panos-PanoramaBgpConditionalAdvAdvertiseFilter/docs/README.md)
* [TF::Panos::PanoramaBgpConditionalAdvNonExistFilter](../resources/panos/TF-Panos-PanoramaBgpConditionalAdvNonExistFilter/docs/README.md)
* [TF::Panos::PanoramaBgpConditionalAdv](../resources/panos/TF-Panos-PanoramaBgpConditionalAdv/docs/README.md)
* [TF::Panos::PanoramaBgpDampeningProfile](../resources/panos/TF-Panos-PanoramaBgpDampeningProfile/docs/README.md)
* [TF::Panos::PanoramaBgpExportRuleGroup](../resources/panos/TF-Panos-PanoramaBgpExportRuleGroup/docs/README.md)
* [TF::Panos::PanoramaBgpImportRuleGroup](../resources/panos/TF-Panos-PanoramaBgpImportRuleGroup/docs/README.md)
* [TF::Panos::PanoramaBgpPeerGroup](../resources/panos/TF-Panos-PanoramaBgpPeerGroup/docs/README.md)
* [TF::Panos::PanoramaBgpPeer](../resources/panos/TF-Panos-PanoramaBgpPeer/docs/README.md)
* [TF::Panos::PanoramaBgpRedistRule](../resources/panos/TF-Panos-PanoramaBgpRedistRule/docs/README.md)
* [TF::Panos::PanoramaBgp](../resources/panos/TF-Panos-PanoramaBgp/docs/README.md)
* [TF::Panos::PanoramaDeviceGroupEntry](../resources/panos/TF-Panos-PanoramaDeviceGroupEntry/docs/README.md)
* [TF::Panos::PanoramaDeviceGroup](../resources/panos/TF-Panos-PanoramaDeviceGroup/docs/README.md)
* [TF::Panos::PanoramaEdl](../resources/panos/TF-Panos-PanoramaEdl/docs/README.md)
* [TF::Panos::PanoramaEmailServerProfile](../resources/panos/TF-Panos-PanoramaEmailServerProfile/docs/README.md)
* [TF::Panos::PanoramaEthernetInterface](../resources/panos/TF-Panos-PanoramaEthernetInterface/docs/README.md)
* [TF::Panos::PanoramaGcpAccount](../resources/panos/TF-Panos-PanoramaGcpAccount/docs/README.md)
* [TF::Panos::PanoramaGkeClusterGroup](../resources/panos/TF-Panos-PanoramaGkeClusterGroup/docs/README.md)
* [TF::Panos::PanoramaGkeCluster](../resources/panos/TF-Panos-PanoramaGkeCluster/docs/README.md)
* [TF::Panos::PanoramaGreTunnel](../resources/panos/TF-Panos-PanoramaGreTunnel/docs/README.md)
* [TF::Panos::PanoramaHttpServerProfile](../resources/panos/TF-Panos-PanoramaHttpServerProfile/docs/README.md)
* [TF::Panos::PanoramaIkeCryptoProfile](../resources/panos/TF-Panos-PanoramaIkeCryptoProfile/docs/README.md)
* [TF::Panos::PanoramaIkeGateway](../resources/panos/TF-Panos-PanoramaIkeGateway/docs/README.md)
* [TF::Panos::PanoramaIpsecCryptoProfile](../resources/panos/TF-Panos-PanoramaIpsecCryptoProfile/docs/README.md)
* [TF::Panos::PanoramaIpsecTunnelProxyIdIpv4](../resources/panos/TF-Panos-PanoramaIpsecTunnelProxyIdIpv4/docs/README.md)
* [TF::Panos::PanoramaIpsecTunnel](../resources/panos/TF-Panos-PanoramaIpsecTunnel/docs/README.md)
* [TF::Panos::PanoramaLayer2Subinterface](../resources/panos/TF-Panos-PanoramaLayer2Subinterface/docs/README.md)
* [TF::Panos::PanoramaLayer3Subinterface](../resources/panos/TF-Panos-PanoramaLayer3Subinterface/docs/README.md)
* [TF::Panos::PanoramaLogForwardingProfile](../resources/panos/TF-Panos-PanoramaLogForwardingProfile/docs/README.md)
* [TF::Panos::PanoramaLoopbackInterface](../resources/panos/TF-Panos-PanoramaLoopbackInterface/docs/README.md)
* [TF::Panos::PanoramaManagementProfile](../resources/panos/TF-Panos-PanoramaManagementProfile/docs/README.md)
* [TF::Panos::PanoramaMonitorProfile](../resources/panos/TF-Panos-PanoramaMonitorProfile/docs/README.md)
* [TF::Panos::PanoramaNatPolicy](../resources/panos/TF-Panos-PanoramaNatPolicy/docs/README.md)
* [TF::Panos::PanoramaNatRuleGroup](../resources/panos/TF-Panos-PanoramaNatRuleGroup/docs/README.md)
* [TF::Panos::PanoramaNatRule](../resources/panos/TF-Panos-PanoramaNatRule/docs/README.md)
* [TF::Panos::PanoramaPbfRuleGroup](../resources/panos/TF-Panos-PanoramaPbfRuleGroup/docs/README.md)
* [TF::Panos::PanoramaRedistributionProfileIpv4](../resources/panos/TF-Panos-PanoramaRedistributionProfileIpv4/docs/README.md)
* [TF::Panos::PanoramaSecurityPolicies](../resources/panos/TF-Panos-PanoramaSecurityPolicies/docs/README.md)
* [TF::Panos::PanoramaSecurityPolicyGroup](../resources/panos/TF-Panos-PanoramaSecurityPolicyGroup/docs/README.md)
* [TF::Panos::PanoramaSecurityPolicy](../resources/panos/TF-Panos-PanoramaSecurityPolicy/docs/README.md)
* [TF::Panos::PanoramaSecurityRuleGroup](../resources/panos/TF-Panos-PanoramaSecurityRuleGroup/docs/README.md)
* [TF::Panos::PanoramaServiceGroup](../resources/panos/TF-Panos-PanoramaServiceGroup/docs/README.md)
* [TF::Panos::PanoramaServiceObject](../resources/panos/TF-Panos-PanoramaServiceObject/docs/README.md)
* [TF::Panos::PanoramaSnmptrapServerProfile](../resources/panos/TF-Panos-PanoramaSnmptrapServerProfile/docs/README.md)
* [TF::Panos::PanoramaStaticRouteIpv4](../resources/panos/TF-Panos-PanoramaStaticRouteIpv4/docs/README.md)
* [TF::Panos::PanoramaSyslogServerProfile](../resources/panos/TF-Panos-PanoramaSyslogServerProfile/docs/README.md)
* [TF::Panos::PanoramaTemplateEntry](../resources/panos/TF-Panos-PanoramaTemplateEntry/docs/README.md)
* [TF::Panos::PanoramaTemplateStackEntry](../resources/panos/TF-Panos-PanoramaTemplateStackEntry/docs/README.md)
* [TF::Panos::PanoramaTemplateStack](../resources/panos/TF-Panos-PanoramaTemplateStack/docs/README.md)
* [TF::Panos::PanoramaTemplateVariable](../resources/panos/TF-Panos-PanoramaTemplateVariable/docs/README.md)
* [TF::Panos::PanoramaTemplate](../resources/panos/TF-Panos-PanoramaTemplate/docs/README.md)
* [TF::Panos::PanoramaTunnelInterface](../resources/panos/TF-Panos-PanoramaTunnelInterface/docs/README.md)
* [TF::Panos::PanoramaVirtualRouterEntry](../resources/panos/TF-Panos-PanoramaVirtualRouterEntry/docs/README.md)
* [TF::Panos::PanoramaVirtualRouter](../resources/panos/TF-Panos-PanoramaVirtualRouter/docs/README.md)
* [TF::Panos::PanoramaVlanEntry](../resources/panos/TF-Panos-PanoramaVlanEntry/docs/README.md)
* [TF::Panos::PanoramaVlanInterface](../resources/panos/TF-Panos-PanoramaVlanInterface/docs/README.md)
* [TF::Panos::PanoramaVlan](../resources/panos/TF-Panos-PanoramaVlan/docs/README.md)
* [TF::Panos::PanoramaZoneEntry](../resources/panos/TF-Panos-PanoramaZoneEntry/docs/README.md)
* [TF::Panos::PanoramaZone](../resources/panos/TF-Panos-PanoramaZone/docs/README.md)
* [TF::Panos::PbfRuleGroup](../resources/panos/TF-Panos-PbfRuleGroup/docs/README.md)
* [TF::Panos::RedistributionProfileIpv4](../resources/panos/TF-Panos-RedistributionProfileIpv4/docs/README.md)
* [TF::Panos::SecurityPolicies](../resources/panos/TF-Panos-SecurityPolicies/docs/README.md)
* [TF::Panos::SecurityPolicyGroup](../resources/panos/TF-Panos-SecurityPolicyGroup/docs/README.md)
* [TF::Panos::SecurityPolicy](../resources/panos/TF-Panos-SecurityPolicy/docs/README.md)
* [TF::Panos::SecurityRuleGroup](../resources/panos/TF-Panos-SecurityRuleGroup/docs/README.md)
* [TF::Panos::ServiceGroup](../resources/panos/TF-Panos-ServiceGroup/docs/README.md)
* [TF::Panos::ServiceObject](../resources/panos/TF-Panos-ServiceObject/docs/README.md)
* [TF::Panos::SnmptrapServerProfile](../resources/panos/TF-Panos-SnmptrapServerProfile/docs/README.md)
* [TF::Panos::StaticRouteIpv4](../resources/panos/TF-Panos-StaticRouteIpv4/docs/README.md)
* [TF::Panos::SyslogServerProfile](../resources/panos/TF-Panos-SyslogServerProfile/docs/README.md)
* [TF::Panos::Telemetry](../resources/panos/TF-Panos-Telemetry/docs/README.md)
* [TF::Panos::TunnelInterface](../resources/panos/TF-Panos-TunnelInterface/docs/README.md)
* [TF::Panos::UrlFilteringSecurityProfile](../resources/panos/TF-Panos-UrlFilteringSecurityProfile/docs/README.md)
* [TF::Panos::UserTag](../resources/panos/TF-Panos-UserTag/docs/README.md)
* [TF::Panos::UseridLogin](../resources/panos/TF-Panos-UseridLogin/docs/README.md)
* [TF::Panos::VirtualRouterEntry](../resources/panos/TF-Panos-VirtualRouterEntry/docs/README.md)
* [TF::Panos::VirtualRouter](../resources/panos/TF-Panos-VirtualRouter/docs/README.md)
* [TF::Panos::VlanEntry](../resources/panos/TF-Panos-VlanEntry/docs/README.md)
* [TF::Panos::VlanInterface](../resources/panos/TF-Panos-VlanInterface/docs/README.md)
* [TF::Panos::Vlan](../resources/panos/TF-Panos-Vlan/docs/README.md)
* [TF::Panos::VmAuthKey](../resources/panos/TF-Panos-VmAuthKey/docs/README.md)
* [TF::Panos::VulnerabilitySecurityProfile](../resources/panos/TF-Panos-VulnerabilitySecurityProfile/docs/README.md)
* [TF::Panos::WildfireAnalysisSecurityProfile](../resources/panos/TF-Panos-WildfireAnalysisSecurityProfile/docs/README.md)
* [TF::Panos::ZoneEntry](../resources/panos/TF-Panos-ZoneEntry/docs/README.md)
* [TF::Panos::Zone](../resources/panos/TF-Panos-Zone/docs/README.md)