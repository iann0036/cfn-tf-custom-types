# Terraform::Packet::BgpSession

Provides a resource to manage BGP sessions in Packet Host. Refer to [Packet BGP documentation](https://www.packet.com/developers/docs/network/advanced/local-and-global-bgp/) for more details.

You need to have BGP config enabled in your project.

BGP session must be linked to a device running [BIRD](https://bird.network.cz) or other BGP routing daemon which will control route advertisements via the session to Packet's upstream routers.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Packet::BgpSession",
    "Properties" : {
        "<a href="#addressfamily" title="AddressFamily">AddressFamily</a>" : <i>String</i>,
        "<a href="#defaultroute" title="DefaultRoute">DefaultRoute</a>" : <i>Boolean</i>,
        "<a href="#deviceid" title="DeviceId">DeviceId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Packet::BgpSession
Properties:
    <a href="#addressfamily" title="AddressFamily">AddressFamily</a>: <i>String</i>
    <a href="#defaultroute" title="DefaultRoute">DefaultRoute</a>: <i>Boolean</i>
    <a href="#deviceid" title="DeviceId">DeviceId</a>: <i>String</i>
</pre>

## Properties

#### AddressFamily

`ipv4` or `ipv6`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRoute

Boolean flag to set the default route policy. False by default.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceId

ID of device.

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

#### Status

Returns the <code>Status</code> value.

