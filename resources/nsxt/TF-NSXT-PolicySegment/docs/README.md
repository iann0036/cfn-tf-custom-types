# TF::NSXT::PolicySegment

This resource provides a method for the management of Segments.

This resource is applicable to NSX Global Manager, NSX Policy Manager and VMC.

~> **NOTE:** For best user experience, it is recommended to use `nsxt_policy_fixed_segment` resource on VMC. Flexible segments and not supported in early versions of VMC UI.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NSXT::PolicySegment",
    "Properties" : {
        "<a href="#connectivitypath" title="ConnectivityPath">ConnectivityPath</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dhcpconfigpath" title="DhcpConfigPath">DhcpConfigPath</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
        "<a href="#nsxid" title="NsxId">NsxId</a>" : <i>String</i>,
        "<a href="#overlayid" title="OverlayId">OverlayId</a>" : <i>Double</i>,
        "<a href="#transportzonepath" title="TransportZonePath">TransportZonePath</a>" : <i>String</i>,
        "<a href="#vlanids" title="VlanIds">VlanIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#advancedconfig" title="AdvancedConfig">AdvancedConfig</a>" : <i>[ <a href="advancedconfigdefinition.md">AdvancedConfigDefinition</a>, ... ]</i>,
        "<a href="#discoveryprofile" title="DiscoveryProfile">DiscoveryProfile</a>" : <i>[ <a href="discoveryprofiledefinition.md">DiscoveryProfileDefinition</a>, ... ]</i>,
        "<a href="#l2extension" title="L2Extension">L2Extension</a>" : <i>[ <a href="l2extensiondefinition.md">L2ExtensionDefinition</a>, ... ]</i>,
        "<a href="#qosprofile" title="QosProfile">QosProfile</a>" : <i>[ <a href="qosprofiledefinition.md">QosProfileDefinition</a>, ... ]</i>,
        "<a href="#securityprofile" title="SecurityProfile">SecurityProfile</a>" : <i>[ <a href="securityprofiledefinition.md">SecurityProfileDefinition</a>, ... ]</i>,
        "<a href="#subnet" title="Subnet">Subnet</a>" : <i>[ <a href="subnetdefinition.md">SubnetDefinition</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NSXT::PolicySegment
Properties:
    <a href="#connectivitypath" title="ConnectivityPath">ConnectivityPath</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dhcpconfigpath" title="DhcpConfigPath">DhcpConfigPath</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
    <a href="#nsxid" title="NsxId">NsxId</a>: <i>String</i>
    <a href="#overlayid" title="OverlayId">OverlayId</a>: <i>Double</i>
    <a href="#transportzonepath" title="TransportZonePath">TransportZonePath</a>: <i>String</i>
    <a href="#vlanids" title="VlanIds">VlanIds</a>: <i>
      - String</i>
    <a href="#advancedconfig" title="AdvancedConfig">AdvancedConfig</a>: <i>
      - <a href="advancedconfigdefinition.md">AdvancedConfigDefinition</a></i>
    <a href="#discoveryprofile" title="DiscoveryProfile">DiscoveryProfile</a>: <i>
      - <a href="discoveryprofiledefinition.md">DiscoveryProfileDefinition</a></i>
    <a href="#l2extension" title="L2Extension">L2Extension</a>: <i>
      - <a href="l2extensiondefinition.md">L2ExtensionDefinition</a></i>
    <a href="#qosprofile" title="QosProfile">QosProfile</a>: <i>
      - <a href="qosprofiledefinition.md">QosProfileDefinition</a></i>
    <a href="#securityprofile" title="SecurityProfile">SecurityProfile</a>: <i>
      - <a href="securityprofiledefinition.md">SecurityProfileDefinition</a></i>
    <a href="#subnet" title="Subnet">Subnet</a>: <i>
      - <a href="subnetdefinition.md">SubnetDefinition</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### ConnectivityPath

Policy path to the connecting Tier-0 or Tier-1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpConfigPath

Policy path to DHCP server or relay configuration to use for subnets configured on this segment. This attribute is supported with NSX 3.0.0 onwards.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Display name of the resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainName

DNS domain names.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxId

The NSX ID of this resource. If set, this ID will be used to create the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverlayId

Overlay connectivity ID for this Segment.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransportZonePath

Policy path to the Overlay transport zone. This property is required for NSX Local Manager, and should not be specified for NSX Global Manager, where NSX will automatically assign default transport zone on each site.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanIds

List of VLAN IDs or ranges. Specifying vlan ids can be useful for overlay segments, f.e. for EVPN.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvancedConfig

_Required_: No

_Type_: List of <a href="advancedconfigdefinition.md">AdvancedConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiscoveryProfile

_Required_: No

_Type_: List of <a href="discoveryprofiledefinition.md">DiscoveryProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L2Extension

_Required_: No

_Type_: List of <a href="l2extensiondefinition.md">L2ExtensionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QosProfile

_Required_: No

_Type_: List of <a href="qosprofiledefinition.md">QosProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityProfile

_Required_: No

_Type_: List of <a href="securityprofiledefinition.md">SecurityProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

_Required_: No

_Type_: List of <a href="subnetdefinition.md">SubnetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### Path

Returns the <code>Path</code> value.

#### Revision

Returns the <code>Revision</code> value.

