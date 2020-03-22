# Terraform::Alicloud::VpnRouteEntry

Provides a VPN Route Entry resource.

-> **NOTE:** Terraform will build vpn route entry instance while it uses `alicloud_vpn_route_entry` to build a VPN Route Entry resource.

-> **NOTE:** Available in 1.57.0+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::VpnRouteEntry",
    "Properties" : {
        "<a href="#nexthop" title="NextHop">NextHop</a>" : <i>String</i>,
        "<a href="#publishvpc" title="PublishVpc">PublishVpc</a>" : <i>Boolean</i>,
        "<a href="#routedest" title="RouteDest">RouteDest</a>" : <i>String</i>,
        "<a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>" : <i>String</i>,
        "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::VpnRouteEntry
Properties:
    <a href="#nexthop" title="NextHop">NextHop</a>: <i>String</i>
    <a href="#publishvpc" title="PublishVpc">PublishVpc</a>: <i>Boolean</i>
    <a href="#routedest" title="RouteDest">RouteDest</a>: <i>String</i>
    <a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>: <i>String</i>
    <a href="#weight" title="Weight">Weight</a>: <i>Double</i>
</pre>

## Properties

#### NextHop

The next hop of the destination route.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublishVpc

Whether to issue the destination route to the VPC.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteDest

The destination network segment of the destination route.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnGatewayId

The id of the vpn gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

The value should be 0 or 100.

_Required_: Yes

_Type_: Double

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

