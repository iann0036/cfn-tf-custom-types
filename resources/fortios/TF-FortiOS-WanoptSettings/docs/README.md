# TF::FortiOS::WanoptSettings

Configure WAN optimization settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::WanoptSettings",
    "Properties" : {
        "<a href="#autodetectalgorithm" title="AutoDetectAlgorithm">AutoDetectAlgorithm</a>" : <i>String</i>,
        "<a href="#hostid" title="HostId">HostId</a>" : <i>String</i>,
        "<a href="#tunnelsslalgorithm" title="TunnelSslAlgorithm">TunnelSslAlgorithm</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::WanoptSettings
Properties:
    <a href="#autodetectalgorithm" title="AutoDetectAlgorithm">AutoDetectAlgorithm</a>: <i>String</i>
    <a href="#hostid" title="HostId">HostId</a>: <i>String</i>
    <a href="#tunnelsslalgorithm" title="TunnelSslAlgorithm">TunnelSslAlgorithm</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### AutoDetectAlgorithm

Auto detection algorithms used in tunnel negotiations. Valid values: `simple`, `diff-req-resp`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostId

Local host ID (must also be entered in the remote FortiGate's peer list).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelSslAlgorithm

Relative strength of encryption algorithms accepted during tunnel negotiation. Valid values: `high`, `medium`, `low`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

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

