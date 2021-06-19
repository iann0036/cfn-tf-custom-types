# TF::AzureRM::VirtualNetworkPeering

Manages a virtual network peering which allows resources to access other
resources in the linked virtual network.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::VirtualNetworkPeering",
    "Properties" : {
        "<a href="#allowforwardedtraffic" title="AllowForwardedTraffic">AllowForwardedTraffic</a>" : <i>Boolean</i>,
        "<a href="#allowgatewaytransit" title="AllowGatewayTransit">AllowGatewayTransit</a>" : <i>Boolean</i>,
        "<a href="#allowvirtualnetworkaccess" title="AllowVirtualNetworkAccess">AllowVirtualNetworkAccess</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#remotevirtualnetworkid" title="RemoteVirtualNetworkId">RemoteVirtualNetworkId</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#useremotegateways" title="UseRemoteGateways">UseRemoteGateways</a>" : <i>Boolean</i>,
        "<a href="#virtualnetworkname" title="VirtualNetworkName">VirtualNetworkName</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::VirtualNetworkPeering
Properties:
    <a href="#allowforwardedtraffic" title="AllowForwardedTraffic">AllowForwardedTraffic</a>: <i>Boolean</i>
    <a href="#allowgatewaytransit" title="AllowGatewayTransit">AllowGatewayTransit</a>: <i>Boolean</i>
    <a href="#allowvirtualnetworkaccess" title="AllowVirtualNetworkAccess">AllowVirtualNetworkAccess</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#remotevirtualnetworkid" title="RemoteVirtualNetworkId">RemoteVirtualNetworkId</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#useremotegateways" title="UseRemoteGateways">UseRemoteGateways</a>: <i>Boolean</i>
    <a href="#virtualnetworkname" title="VirtualNetworkName">VirtualNetworkName</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AllowForwardedTraffic

Controls if forwarded traffic from  VMs
in the remote virtual network is allowed. Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowGatewayTransit

Controls gatewayLinks can be used in the
remote virtual network’s link to the local virtual network.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowVirtualNetworkAccess

Controls if the VMs in the remote
virtual network can access VMs in the local virtual network. Defaults to
true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the virtual network peering. Changing this
forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteVirtualNetworkId

The full Azure resource ID of the
remote virtual network.  Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to
create the virtual network peering. Changing this forces a new resource to be
created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseRemoteGateways

Controls if remote gateways can be used on
the local virtual network. If the flag is set to `true`, and
`allow_gateway_transit` on the remote peering is also `true`, virtual network will
use gateways of remote virtual network for transit. Only one peering can
have this flag set to `true`. This flag cannot be set if virtual network
already has a gateway. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualNetworkName

The name of the virtual network. Changing
this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

