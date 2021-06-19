# TF::FortiOS::LogmemoryGlobalsetting

Global settings for memory logging.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::LogmemoryGlobalsetting",
    "Properties" : {
        "<a href="#fullfinalwarningthreshold" title="FullFinalWarningThreshold">FullFinalWarningThreshold</a>" : <i>Double</i>,
        "<a href="#fullfirstwarningthreshold" title="FullFirstWarningThreshold">FullFirstWarningThreshold</a>" : <i>Double</i>,
        "<a href="#fullsecondwarningthreshold" title="FullSecondWarningThreshold">FullSecondWarningThreshold</a>" : <i>Double</i>,
        "<a href="#maxsize" title="MaxSize">MaxSize</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::LogmemoryGlobalsetting
Properties:
    <a href="#fullfinalwarningthreshold" title="FullFinalWarningThreshold">FullFinalWarningThreshold</a>: <i>Double</i>
    <a href="#fullfirstwarningthreshold" title="FullFirstWarningThreshold">FullFirstWarningThreshold</a>: <i>Double</i>
    <a href="#fullsecondwarningthreshold" title="FullSecondWarningThreshold">FullSecondWarningThreshold</a>: <i>Double</i>
    <a href="#maxsize" title="MaxSize">MaxSize</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### FullFinalWarningThreshold

Log full final warning threshold as a percent (3 - 100, default = 95).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FullFirstWarningThreshold

Log full first warning threshold as a percent (1 - 98, default = 75).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FullSecondWarningThreshold

Log full second warning threshold as a percent (2 - 99, default = 90).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSize

Maximum amount of memory that can be used for memory logging in bytes.

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

