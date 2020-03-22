# Terraform::NSXT::DhcpServerIpPool

Provides a resource to configure IP Pool for logical DHCP server on NSX-T manager

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NSXT::DhcpServerIpPool",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#errorthreshold" title="ErrorThreshold">ErrorThreshold</a>" : <i>Double</i>,
        "<a href="#gatewayip" title="GatewayIp">GatewayIp</a>" : <i>String</i>,
        "<a href="#leasetime" title="LeaseTime">LeaseTime</a>" : <i>Double</i>,
        "<a href="#logicaldhcpserverid" title="LogicalDhcpServerId">LogicalDhcpServerId</a>" : <i>String</i>,
        "<a href="#warningthreshold" title="WarningThreshold">WarningThreshold</a>" : <i>Double</i>,
        "<a href="#dhcpgenericoption" title="DhcpGenericOption">DhcpGenericOption</a>" : <i>[ <a href="dhcpgenericoption.md">DhcpGenericOption</a>, ... ]</i>,
        "<a href="#dhcpoption121" title="DhcpOption121">DhcpOption121</a>" : <i>[ <a href="dhcpoption121.md">DhcpOption121</a>, ... ]</i>,
        "<a href="#iprange" title="IpRange">IpRange</a>" : <i>[ <a href="iprange.md">IpRange</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tag.md">Tag</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NSXT::DhcpServerIpPool
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#errorthreshold" title="ErrorThreshold">ErrorThreshold</a>: <i>Double</i>
    <a href="#gatewayip" title="GatewayIp">GatewayIp</a>: <i>String</i>
    <a href="#leasetime" title="LeaseTime">LeaseTime</a>: <i>Double</i>
    <a href="#logicaldhcpserverid" title="LogicalDhcpServerId">LogicalDhcpServerId</a>: <i>String</i>
    <a href="#warningthreshold" title="WarningThreshold">WarningThreshold</a>: <i>Double</i>
    <a href="#dhcpgenericoption" title="DhcpGenericOption">DhcpGenericOption</a>: <i>
      - <a href="dhcpgenericoption.md">DhcpGenericOption</a></i>
    <a href="#dhcpoption121" title="DhcpOption121">DhcpOption121</a>: <i>
      - <a href="dhcpoption121.md">DhcpOption121</a></i>
    <a href="#iprange" title="IpRange">IpRange</a>: <i>
      - <a href="iprange.md">IpRange</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tag.md">Tag</a></i>
</pre>

## Properties

#### Description

Description of this resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The display name of this resource. Defaults to ID if not set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ErrorThreshold

Error threshold in percent. Valid values are from 80 to 100, default is 100.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayIp

Gateway IP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LeaseTime

Lease time in seconds. Default is 86400.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogicalDhcpServerId

DHCP server uuid. Changing this would force new pool to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WarningThreshold

Warning threshold in percent. Valid values are from 50 to 80, default is 80.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpGenericOption

_Required_: No

_Type_: List of <a href="dhcpgenericoption.md">DhcpGenericOption</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpOption121

_Required_: No

_Type_: List of <a href="dhcpoption121.md">DhcpOption121</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpRange

_Required_: No

_Type_: List of <a href="iprange.md">IpRange</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tag.md">Tag</a>

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

#### Revision

Returns the <code>Revision</code> value.

