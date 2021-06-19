# TF::NSXT::PolicyTier1GatewayInterface

This resource provides a method for the management of a Tier-1 gateway Interface. Note that edge cluster must be configured on Tier-1 Gateway in order to configure interfaces on it.

This resource is applicable to NSX Global Manager, NSX Policy Manager and VMC.

# Example Usage

```hcl
data "nsxt_policy_tier1_gateway" "gw1" {
  display_name = "gw1"
}

data "nsxt_policy_ipv6_ndra_profile" "slaac" {
  display_name = "slaac"
}

resource "nsxt_policy_vlan_segment" "segment1" {
  display_name = "segment1"
  vlan_ids     = [12]
}

resource "nsxt_policy_tier1_gateway_interface" "if1" {
  display_name           = "segment1_interface"
  description            = "connection to segment1"
  gateway_path           = data.nsxt_policy_tier1_gateway.gw1.path
  segment_path           = nsxt_policy_vlan_segment.segment1.path
  subnets                = ["12.12.2.13/24"]
  mtu                    = 1500
  ipv6_ndra_profile_path = data.nsxt_policy_ipv6_ndra_profile.slaac.path
}
```

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NSXT::PolicyTier1GatewayInterface",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#gatewaypath" title="GatewayPath">GatewayPath</a>" : <i>String</i>,
        "<a href="#ipv6ndraprofilepath" title="Ipv6NdraProfilePath">Ipv6NdraProfilePath</a>" : <i>String</i>,
        "<a href="#mtu" title="Mtu">Mtu</a>" : <i>Double</i>,
        "<a href="#nsxid" title="NsxId">NsxId</a>" : <i>String</i>,
        "<a href="#segmentpath" title="SegmentPath">SegmentPath</a>" : <i>String</i>,
        "<a href="#sitepath" title="SitePath">SitePath</a>" : <i>String</i>,
        "<a href="#subnets" title="Subnets">Subnets</a>" : <i>[ String, ... ]</i>,
        "<a href="#urpfmode" title="UrpfMode">UrpfMode</a>" : <i>String</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NSXT::PolicyTier1GatewayInterface
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#gatewaypath" title="GatewayPath">GatewayPath</a>: <i>String</i>
    <a href="#ipv6ndraprofilepath" title="Ipv6NdraProfilePath">Ipv6NdraProfilePath</a>: <i>String</i>
    <a href="#mtu" title="Mtu">Mtu</a>: <i>Double</i>
    <a href="#nsxid" title="NsxId">NsxId</a>: <i>String</i>
    <a href="#segmentpath" title="SegmentPath">SegmentPath</a>: <i>String</i>
    <a href="#sitepath" title="SitePath">SitePath</a>: <i>String</i>
    <a href="#subnets" title="Subnets">Subnets</a>: <i>
      - String</i>
    <a href="#urpfmode" title="UrpfMode">UrpfMode</a>: <i>String</i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### Description

Description of the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Display name of the resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayPath

Policy path for the Tier-1 Gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6NdraProfilePath

IPv6 NDRA profile to be associated with this interface.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mtu

Maximum Transmission Unit for this interface.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxId

The NSX ID of this resource. If set, this ID will be used to create the policy resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SegmentPath

Policy path for segment to be connected with this Tier1 Gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SitePath

Path of the site the Tier1 edge cluster belongs to. This configuration is required for global manager only. `path` field of the existing `nsxt_policy_site` can be used here.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnets

list of Ip Addresses/Prefixes in CIDR format, to be associated with this interface.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrpfMode

Unicast Reverse Path Forwarding mode, one of `NONE`, `STRICT`. Default is `STRICT`. This attribute is supported with NSX 3.0.0 onwards.

_Required_: No

_Type_: String

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

#### LocaleServiceId

Returns the <code>LocaleServiceId</code> value.

#### Path

Returns the <code>Path</code> value.

#### Revision

Returns the <code>Revision</code> value.

