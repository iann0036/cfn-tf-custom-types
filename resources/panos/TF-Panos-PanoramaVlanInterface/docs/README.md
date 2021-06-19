# TF::Panos::PanoramaVlanInterface

This resource allows you to add/update/delete Panorama VLAN interfaces
for templates.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Panos::PanoramaVlanInterface",
    "Properties" : {
        "<a href="#adjusttcpmss" title="AdjustTcpMss">AdjustTcpMss</a>" : <i>Boolean</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#createdhcpdefaultroute" title="CreateDhcpDefaultRoute">CreateDhcpDefaultRoute</a>" : <i>Boolean</i>,
        "<a href="#dhcpdefaultroutemetric" title="DhcpDefaultRouteMetric">DhcpDefaultRouteMetric</a>" : <i>Double</i>,
        "<a href="#enabledhcp" title="EnableDhcp">EnableDhcp</a>" : <i>Boolean</i>,
        "<a href="#ipv4mssadjust" title="Ipv4MssAdjust">Ipv4MssAdjust</a>" : <i>Double</i>,
        "<a href="#ipv6mssadjust" title="Ipv6MssAdjust">Ipv6MssAdjust</a>" : <i>Double</i>,
        "<a href="#managementprofile" title="ManagementProfile">ManagementProfile</a>" : <i>String</i>,
        "<a href="#mtu" title="Mtu">Mtu</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#netflowprofile" title="NetflowProfile">NetflowProfile</a>" : <i>String</i>,
        "<a href="#staticips" title="StaticIps">StaticIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Panos::PanoramaVlanInterface
Properties:
    <a href="#adjusttcpmss" title="AdjustTcpMss">AdjustTcpMss</a>: <i>Boolean</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#createdhcpdefaultroute" title="CreateDhcpDefaultRoute">CreateDhcpDefaultRoute</a>: <i>Boolean</i>
    <a href="#dhcpdefaultroutemetric" title="DhcpDefaultRouteMetric">DhcpDefaultRouteMetric</a>: <i>Double</i>
    <a href="#enabledhcp" title="EnableDhcp">EnableDhcp</a>: <i>Boolean</i>
    <a href="#ipv4mssadjust" title="Ipv4MssAdjust">Ipv4MssAdjust</a>: <i>Double</i>
    <a href="#ipv6mssadjust" title="Ipv6MssAdjust">Ipv6MssAdjust</a>: <i>Double</i>
    <a href="#managementprofile" title="ManagementProfile">ManagementProfile</a>: <i>String</i>
    <a href="#mtu" title="Mtu">Mtu</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#netflowprofile" title="NetflowProfile">NetflowProfile</a>: <i>String</i>
    <a href="#staticips" title="StaticIps">StaticIps</a>: <i>
      - String</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
</pre>

## Properties

#### AdjustTcpMss

Adjust TCP MSS (default: false).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

The interface comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateDhcpDefaultRoute

Set to `true` to create a DHCP
default route.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpDefaultRouteMetric

The metric for the DHCP default
route.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDhcp

Set to `true` to enable DHCP on this interface.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4MssAdjust

The IPv4 MSS adjust value.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6MssAdjust

The IPv6 MSS adjust value.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementProfile

The management profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mtu

The MTU.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The interface's name.  Must start with `vlan.`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetflowProfile

The netflow profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticIps

List of static IPv4 addresses to set for this data
interface.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

The template name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vsys

The vsys that will use this interface (default: `vsys1`).

_Required_: No

_Type_: String

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

