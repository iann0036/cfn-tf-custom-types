# TF::Thunder::SlbAflow

`thunder_slb_aflow` Provides details about thunder SLB aflow

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbAflow",
    "Properties" : {
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>" : <i>[ <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbAflow
Properties:
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>: <i>
      - <a href="samplingenabledefinition.md">SamplingEnableDefinition</a></i>
</pre>

## Properties

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SamplingEnable

_Required_: No

_Type_: List of <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>

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

