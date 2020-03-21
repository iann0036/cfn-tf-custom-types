# Terraform::Panos::PanoramaIpsecTunnelProxyIdIpv4

CloudFormation equivalent of panos_panorama_ipsec_tunnel_proxy_id_ipv4

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaIpsecTunnelProxyIdIpv4",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
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
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
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

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecTunnel

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Local

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolAny

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolNumber

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolTcpLocal

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolTcpRemote

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolUdpLocal

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolUdpRemote

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Remote

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

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

