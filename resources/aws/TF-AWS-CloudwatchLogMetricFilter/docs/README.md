# TF::AWS::CloudwatchLogMetricFilter

Provides a CloudWatch Log Metric Filter resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::CloudwatchLogMetricFilter",
    "Properties" : {
        "<a href="#loggroupname" title="LogGroupName">LogGroupName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pattern" title="Pattern">Pattern</a>" : <i>String</i>,
        "<a href="#metrictransformation" title="MetricTransformation">MetricTransformation</a>" : <i>[ <a href="metrictransformationdefinition.md">MetricTransformationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::CloudwatchLogMetricFilter
Properties:
    <a href="#loggroupname" title="LogGroupName">LogGroupName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pattern" title="Pattern">Pattern</a>: <i>String</i>
    <a href="#metrictransformation" title="MetricTransformation">MetricTransformation</a>: <i>
      - <a href="metrictransformationdefinition.md">MetricTransformationDefinition</a></i>
</pre>

## Properties

#### LogGroupName

The name of the log group to associate the metric filter with.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A name for the metric filter.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pattern

A valid [CloudWatch Logs filter pattern](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/FilterAndPatternSyntax.html)
for extracting metric data out of ingested log events.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricTransformation

_Required_: No

_Type_: List of <a href="metrictransformationdefinition.md">MetricTransformationDefinition</a>

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

