# TF::FortiOS::VpnL2tp

Configure L2TP.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::VpnL2tp",
    "Properties" : {
        "<a href="#compress" title="Compress">Compress</a>" : <i>String</i>,
        "<a href="#eip" title="Eip">Eip</a>" : <i>String</i>,
        "<a href="#enforceipsec" title="EnforceIpsec">EnforceIpsec</a>" : <i>String</i>,
        "<a href="#lcpechointerval" title="LcpEchoInterval">LcpEchoInterval</a>" : <i>Double</i>,
        "<a href="#lcpmaxechofails" title="LcpMaxEchoFails">LcpMaxEchoFails</a>" : <i>Double</i>,
        "<a href="#sip" title="Sip">Sip</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#usrgrp" title="Usrgrp">Usrgrp</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::VpnL2tp
Properties:
    <a href="#compress" title="Compress">Compress</a>: <i>String</i>
    <a href="#eip" title="Eip">Eip</a>: <i>String</i>
    <a href="#enforceipsec" title="EnforceIpsec">EnforceIpsec</a>: <i>String</i>
    <a href="#lcpechointerval" title="LcpEchoInterval">LcpEchoInterval</a>: <i>Double</i>
    <a href="#lcpmaxechofails" title="LcpMaxEchoFails">LcpMaxEchoFails</a>: <i>Double</i>
    <a href="#sip" title="Sip">Sip</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#usrgrp" title="Usrgrp">Usrgrp</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### Compress

Enable/disable data compression. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Eip

End IP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnforceIpsec

Enable/disable IPsec enforcement. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LcpEchoInterval

Time in seconds between PPPoE Link Control Protocol (LCP) echo requests.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LcpMaxEchoFails

Maximum number of missed LCP echo messages before disconnect.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sip

Start IP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable FortiGate as a L2TP gateway. Valid values: `enable`, `disable`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Usrgrp

User group.

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

