# TF::Dynatrace::ApplicationAnomalies

CloudFormation equivalent of dynatrace_application_anomalies

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Dynatrace::ApplicationAnomalies",
    "Properties" : {
        "<a href="#failurerate" title="FailureRate">FailureRate</a>" : <i>[ <a href="failureratedefinition.md">FailureRateDefinition</a>, ... ]</i>,
        "<a href="#responsetime" title="ResponseTime">ResponseTime</a>" : <i>[ <a href="responsetimedefinition.md">ResponseTimeDefinition</a>, ... ]</i>,
        "<a href="#traffic" title="Traffic">Traffic</a>" : <i>[ <a href="trafficdefinition.md">TrafficDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Dynatrace::ApplicationAnomalies
Properties:
    <a href="#failurerate" title="FailureRate">FailureRate</a>: <i>
      - <a href="failureratedefinition.md">FailureRateDefinition</a></i>
    <a href="#responsetime" title="ResponseTime">ResponseTime</a>: <i>
      - <a href="responsetimedefinition.md">ResponseTimeDefinition</a></i>
    <a href="#traffic" title="Traffic">Traffic</a>: <i>
      - <a href="trafficdefinition.md">TrafficDefinition</a></i>
</pre>

## Properties

#### FailureRate

_Required_: No

_Type_: List of <a href="failureratedefinition.md">FailureRateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseTime

_Required_: No

_Type_: List of <a href="responsetimedefinition.md">ResponseTimeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Traffic

_Required_: No

_Type_: List of <a href="trafficdefinition.md">TrafficDefinition</a>

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

