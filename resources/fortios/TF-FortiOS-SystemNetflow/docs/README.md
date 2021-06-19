# TF::FortiOS::SystemNetflow

Configure NetFlow.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemNetflow",
    "Properties" : {
        "<a href="#activeflowtimeout" title="ActiveFlowTimeout">ActiveFlowTimeout</a>" : <i>Double</i>,
        "<a href="#collectorip" title="CollectorIp">CollectorIp</a>" : <i>String</i>,
        "<a href="#collectorport" title="CollectorPort">CollectorPort</a>" : <i>Double</i>,
        "<a href="#inactiveflowtimeout" title="InactiveFlowTimeout">InactiveFlowTimeout</a>" : <i>Double</i>,
        "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>String</i>,
        "<a href="#templatetxcounter" title="TemplateTxCounter">TemplateTxCounter</a>" : <i>Double</i>,
        "<a href="#templatetxtimeout" title="TemplateTxTimeout">TemplateTxTimeout</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemNetflow
Properties:
    <a href="#activeflowtimeout" title="ActiveFlowTimeout">ActiveFlowTimeout</a>: <i>Double</i>
    <a href="#collectorip" title="CollectorIp">CollectorIp</a>: <i>String</i>
    <a href="#collectorport" title="CollectorPort">CollectorPort</a>: <i>Double</i>
    <a href="#inactiveflowtimeout" title="InactiveFlowTimeout">InactiveFlowTimeout</a>: <i>Double</i>
    <a href="#sourceip" title="SourceIp">SourceIp</a>: <i>String</i>
    <a href="#templatetxcounter" title="TemplateTxCounter">TemplateTxCounter</a>: <i>Double</i>
    <a href="#templatetxtimeout" title="TemplateTxTimeout">TemplateTxTimeout</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### ActiveFlowTimeout

Timeout to report active flows (1 - 60 min, default = 30).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CollectorIp

Collector IP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CollectorPort

NetFlow collector port number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InactiveFlowTimeout

Timeout for periodic report of finished flows (10 - 600 sec, default = 15).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

Source IP address for communication with the NetFlow agent.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateTxCounter

Counter of flowset records before resending a template flowset record.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateTxTimeout

Timeout for periodic template flowset transmission (1 - 1440 min, default = 30).

_Required_: No

_Type_: Double

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

