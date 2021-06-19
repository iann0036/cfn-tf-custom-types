# TF::AWS::CloudwatchLogMetricFilter MetricTransformationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultvalue" title="DefaultValue">DefaultValue</a>" : <i>String</i>,
    "<a href="#dimensions" title="Dimensions">Dimensions</a>" : <i>[ <a href="dimensionsdefinition.md">DimensionsDefinition</a>, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
    "<a href="#unit" title="Unit">Unit</a>" : <i>String</i>,
    "<a href="#value" title="Value">Value</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#defaultvalue" title="DefaultValue">DefaultValue</a>: <i>String</i>
<a href="#dimensions" title="Dimensions">Dimensions</a>: <i>
      - <a href="dimensionsdefinition.md">DimensionsDefinition</a></i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
<a href="#unit" title="Unit">Unit</a>: <i>String</i>
<a href="#value" title="Value">Value</a>: <i>String</i>
</pre>

## Properties

#### DefaultValue

The value to emit when a filter pattern does not match a log event. Conflicts with `dimensions`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dimensions

Map of fields to use as dimensions for the metric. Up to 3 dimensions are allowed. Conflicts with `default_value`.

_Required_: No

_Type_: List of <a href="dimensionsdefinition.md">DimensionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the CloudWatch metric to which the monitored log information should be published (e.g. `ErrorCount`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

The destination namespace of the CloudWatch metric.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unit

The unit to assign to the metric. If you omit this, the unit is set as `None`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

What to publish to the metric. For example, if you're counting the occurrences of a particular term like "Error", the value will be "1" for each occurrence. If you're counting the bytes transferred the published value will be the value in the log event.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

