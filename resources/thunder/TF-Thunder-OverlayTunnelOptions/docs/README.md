# TF::Thunder::OverlayTunnelOptions

`thunder_overlay_tunnel_options` Provides details about thunder overlay tunnel options

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::OverlayTunnelOptions",
    "Properties" : {
        "<a href="#gatewaymac" title="GatewayMac">GatewayMac</a>" : <i>String</i>,
        "<a href="#ipdscppreserve" title="IpDscpPreserve">IpDscpPreserve</a>" : <i>Double</i>,
        "<a href="#nvgredisableflowid" title="NvgreDisableFlowId">NvgreDisableFlowId</a>" : <i>Double</i>,
        "<a href="#nvgrekeymodelower24" title="NvgreKeyModeLower24">NvgreKeyModeLower24</a>" : <i>Double</i>,
        "<a href="#tcpmssadjustdisable" title="TcpMssAdjustDisable">TcpMssAdjustDisable</a>" : <i>Double</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#vxlandestport" title="VxlanDestPort">VxlanDestPort</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::OverlayTunnelOptions
Properties:
    <a href="#gatewaymac" title="GatewayMac">GatewayMac</a>: <i>String</i>
    <a href="#ipdscppreserve" title="IpDscpPreserve">IpDscpPreserve</a>: <i>Double</i>
    <a href="#nvgredisableflowid" title="NvgreDisableFlowId">NvgreDisableFlowId</a>: <i>Double</i>
    <a href="#nvgrekeymodelower24" title="NvgreKeyModeLower24">NvgreKeyModeLower24</a>: <i>Double</i>
    <a href="#tcpmssadjustdisable" title="TcpMssAdjustDisable">TcpMssAdjustDisable</a>: <i>Double</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#vxlandestport" title="VxlanDestPort">VxlanDestPort</a>: <i>Double</i>
</pre>

## Properties

#### GatewayMac

MAC to be used with Gateway segment Id (MAC Address for the Gateway segment).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpDscpPreserve

Copy DSCP bits from inner IP to outer IP header.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NvgreDisableFlowId

Disable Flow-ID computation for NVGRE.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NvgreKeyModeLower24

Use the lower 24-bits of the GRE key as the VSID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpMssAdjustDisable

Disable TCP MSS adjustment in SYN packet for tunnels.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VxlanDestPort

VXLAN UDP Destination Port (UDP Port Number (default 4789)).

_Required_: No

_Type_: Double

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

