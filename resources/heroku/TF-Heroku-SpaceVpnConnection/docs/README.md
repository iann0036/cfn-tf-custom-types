# TF::Heroku::SpaceVpnConnection

Provides a resource for creating a VPN connection between a network and a Heroku Private Space. For more information, see [Private Spaces VPN Connection](https://devcenter.heroku.com/articles/private-space-vpn-connection?preview=1) in the Heroku DevCenter.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Heroku::SpaceVpnConnection",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#publicip" title="PublicIp">PublicIp</a>" : <i>String</i>,
        "<a href="#routablecidrs" title="RoutableCidrs">RoutableCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#space" title="Space">Space</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#tunnels" title="Tunnels">Tunnels</a>" : <i>[ <a href="tunnelsdefinition.md">TunnelsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Heroku::SpaceVpnConnection
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#publicip" title="PublicIp">PublicIp</a>: <i>String</i>
    <a href="#routablecidrs" title="RoutableCidrs">RoutableCidrs</a>: <i>
      - String</i>
    <a href="#space" title="Space">Space</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#tunnels" title="Tunnels">Tunnels</a>: <i>
      - <a href="tunnelsdefinition.md">TunnelsDefinition</a></i>
</pre>

## Properties

#### Name

The name of the VPN connection.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIp

The public IP address of the VPN endpoint on the network where the VPN connection will be established.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoutableCidrs

A list of IPv4 CIDR blocks used by the network where the VPN connection will be established.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Space

The `UUID` of the Heroku Private Space where the VPN connection will be established.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnels

_Required_: No

_Type_: List of <a href="tunnelsdefinition.md">TunnelsDefinition</a>

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

#### IkeVersion

Returns the <code>IkeVersion</code> value.

#### SpaceCidrBlock

Returns the <code>SpaceCidrBlock</code> value.

