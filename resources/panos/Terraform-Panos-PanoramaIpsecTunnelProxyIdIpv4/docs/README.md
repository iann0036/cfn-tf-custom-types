# Terraform::Panos::PanoramaIpsecTunnelProxyIdIpv4

This resource allows you to add/update/delete Panorama IPSec tunnel proxy IDs
to a parent auto key IPSec tunnel for templates.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaIpsecTunnelProxyIdIpv4",
    "Properties" : {
        "<a href="#ipsectunnel" title="IpsecTunnel">IpsecTunnel</a>" : <i>String</i>,
        "<a href="#local" title="Local">Local</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#protocolany" title="ProtocolAny">ProtocolAny</a>" : <i>Boolean</i>,
        "<a href="#protocolnumber" title="ProtocolNumber">ProtocolNumber</a>" : <i>Double</i>,
        "<a href="#protocoltcplocal" title="ProtocolTcpLocal">ProtocolTcpLocal</a>" : <i>Double</i>,
        "<a href="#protocoltcpremote" title="ProtocolTcpRemote">ProtocolTcpRemote</a>" : <i>Double</i>,
        "<a href="#protocoludplocal" title="ProtocolUdpLocal">ProtocolUdpLocal</a>" : <i>Double</i>,
        "<a href="#protocoludpremote" title="ProtocolUdpRemote">ProtocolUdpRemote</a>" : <i>Double</i>,
        "<a href="#remote" title="Remote">Remote</a>" : <i>String</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::PanoramaIpsecTunnelProxyIdIpv4
Properties:
    <a href="#ipsectunnel" title="IpsecTunnel">IpsecTunnel</a>: <i>String</i>
    <a href="#local" title="Local">Local</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#protocolany" title="ProtocolAny">ProtocolAny</a>: <i>Boolean</i>
    <a href="#protocolnumber" title="ProtocolNumber">ProtocolNumber</a>: <i>Double</i>
    <a href="#protocoltcplocal" title="ProtocolTcpLocal">ProtocolTcpLocal</a>: <i>Double</i>
    <a href="#protocoltcpremote" title="ProtocolTcpRemote">ProtocolTcpRemote</a>: <i>Double</i>
    <a href="#protocoludplocal" title="ProtocolUdpLocal">ProtocolUdpLocal</a>: <i>Double</i>
    <a href="#protocoludpremote" title="ProtocolUdpRemote">ProtocolUdpRemote</a>: <i>Double</i>
    <a href="#remote" title="Remote">Remote</a>: <i>String</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
</pre>

## Properties

#### IpsecTunnel

The auto key IPSec tunnel to attach this
proxy ID to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Local

IP subnet or IP address represents local network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The object's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolAny

Set to `true` for any IP protocol.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolNumber

IP protocol number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolTcpLocal

Local TCP port number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolTcpRemote

Remote TCP port number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolUdpLocal

Local UDP port number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolUdpRemote

Remote UDP port number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Remote

IP subnet or IP address represents remote network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

The template name.

_Required_: Yes

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

