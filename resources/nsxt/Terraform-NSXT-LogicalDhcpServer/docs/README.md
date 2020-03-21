# Terraform::NSXT::LogicalDhcpServer

Provides a resource to configure logical DHCP server on NSX-T manager

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NSXT::LogicalDhcpServer",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dhcpprofileid" title="DhcpProfileId">DhcpProfileId</a>" : <i>String</i>,
        "<a href="#dhcpserverip" title="DhcpServerIp">DhcpServerIp</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#dnsnameservers" title="DnsNameServers">DnsNameServers</a>" : <i>[ String, ... ]</i>,
        "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
        "<a href="#gatewayip" title="GatewayIp">GatewayIp</a>" : <i>String</i>,
        "<a href="#dhcpgenericoption" title="DhcpGenericOption">DhcpGenericOption</a>" : <i>[ <a href="dhcpgenericoption.md">DhcpGenericOption</a>, ... ]</i>,
        "<a href="#dhcpoption121" title="DhcpOption121">DhcpOption121</a>" : <i>[ <a href="dhcpoption121.md">DhcpOption121</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tag.md">Tag</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NSXT::LogicalDhcpServer
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dhcpprofileid" title="DhcpProfileId">DhcpProfileId</a>: <i>String</i>
    <a href="#dhcpserverip" title="DhcpServerIp">DhcpServerIp</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#dnsnameservers" title="DnsNameServers">DnsNameServers</a>: <i>
      - String</i>
    <a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
    <a href="#gatewayip" title="GatewayIp">GatewayIp</a>: <i>String</i>
    <a href="#dhcpgenericoption" title="DhcpGenericOption">DhcpGenericOption</a>: <i>
      - <a href="dhcpgenericoption.md">DhcpGenericOption</a></i>
    <a href="#dhcpoption121" title="DhcpOption121">DhcpOption121</a>: <i>
      - <a href="dhcpoption121.md">DhcpOption121</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tag.md">Tag</a></i>
</pre>

## Properties

#### Description

Description of this resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpProfileId

DHCP profile uuid.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpServerIp

DHCP server IP in cidr format.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The display name of this resource. Defaults to ID if not set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsNameServers

DNS IPs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainName

Domain name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayIp

Gateway IP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpGenericOption

_Required_: No

_Type_: List of <a href="dhcpgenericoption.md">DhcpGenericOption</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpOption121

_Required_: No

_Type_: List of <a href="dhcpoption121.md">DhcpOption121</a>

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

#### AttachedLogicalPortId

Returns the <code>AttachedLogicalPortId</code> value.

#### Revision

Returns the <code>Revision</code> value.

