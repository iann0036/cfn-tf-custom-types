# Terraform::Heroku::SpaceVpnConnection

CloudFormation equivalent of heroku_space_vpn_connection

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Heroku::SpaceVpnConnection",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#publicip" title="PublicIp">PublicIp</a>" : <i>String</i>,
        "<a href="#routablecidrs" title="RoutableCidrs">RoutableCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#space" title="Space">Space</a>" : <i>String</i>,
        "<a href="#tunnels" title="Tunnels">Tunnels</a>" : <i>[ <a href="tunnels.md">Tunnels</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Heroku::SpaceVpnConnection
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#publicip" title="PublicIp">PublicIp</a>: <i>String</i>
    <a href="#routablecidrs" title="RoutableCidrs">RoutableCidrs</a>: <i>
      - String</i>
    <a href="#space" title="Space">Space</a>: <i>String</i>
    <a href="#tunnels" title="Tunnels">Tunnels</a>: <i>
      - <a href="tunnels.md">Tunnels</a></i>
</pre>

## Properties

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIp

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoutableCidrs

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Space

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnels

_Required_: No

_Type_: List of <a href="tunnels.md">Tunnels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### IkeVersion

Returns the <code>IkeVersion</code> value.

#### SpaceCidrBlock

Returns the <code>SpaceCidrBlock</code> value.

