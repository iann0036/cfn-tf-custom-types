# Terraform::Panos::PanoramaGreTunnel

This resource allows you to add/update/delete Panorama GRE tunnels.

*Minimum PAN-OS version*: 9.0

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaGreTunnel",
    "Properties" : {
        "<a href="#copytos" title="CopyTos">CopyTos</a>" : <i>Boolean</i>,
        "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
        "<a href="#enablekeepalive" title="EnableKeepAlive">EnableKeepAlive</a>" : <i>Boolean</i>,
        "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
        "<a href="#keepaliveholdtimer" title="KeepAliveHoldTimer">KeepAliveHoldTimer</a>" : <i>Double</i>,
        "<a href="#keepaliveinterval" title="KeepAliveInterval">KeepAliveInterval</a>" : <i>Double</i>,
        "<a href="#keepaliveretry" title="KeepAliveRetry">KeepAliveRetry</a>" : <i>Double</i>,
        "<a href="#localaddresstype" title="LocalAddressType">LocalAddressType</a>" : <i>String</i>,
        "<a href="#localaddressvalue" title="LocalAddressValue">LocalAddressValue</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#peeraddress" title="PeerAddress">PeerAddress</a>" : <i>String</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>,
        "<a href="#tunnelinterface" title="TunnelInterface">TunnelInterface</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::PanoramaGreTunnel
Properties:
    <a href="#copytos" title="CopyTos">CopyTos</a>: <i>Boolean</i>
    <a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
    <a href="#enablekeepalive" title="EnableKeepAlive">EnableKeepAlive</a>: <i>Boolean</i>
    <a href="#interface" title="Interface">Interface</a>: <i>String</i>
    <a href="#keepaliveholdtimer" title="KeepAliveHoldTimer">KeepAliveHoldTimer</a>: <i>Double</i>
    <a href="#keepaliveinterval" title="KeepAliveInterval">KeepAliveInterval</a>: <i>Double</i>
    <a href="#keepaliveretry" title="KeepAliveRetry">KeepAliveRetry</a>: <i>Double</i>
    <a href="#localaddresstype" title="LocalAddressType">LocalAddressType</a>: <i>String</i>
    <a href="#localaddressvalue" title="LocalAddressValue">LocalAddressValue</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#peeraddress" title="PeerAddress">PeerAddress</a>: <i>String</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
    <a href="#tunnelinterface" title="TunnelInterface">TunnelInterface</a>: <i>String</i>
</pre>

## Properties

#### CopyTos

Copy IP TOS bits from inner packet to GRE packet.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

Disable the GRE tunnel.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableKeepAlive

Enable tunnel monitoring.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

Interface to terminate tunnel.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepAliveHoldTimer

Keep alive hold timer.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepAliveInterval

Keep alive interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepAliveRetry

Keep alive retry.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalAddressType

Type of local address.  Valid values are
`ip` (default) or `floating-ip`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalAddressValue

IP address value.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The GRE tunnel name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerAddress

Peer IP address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

The template name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

Time to live.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelInterface

Tunnel interface to apply the GRE tunnel to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

