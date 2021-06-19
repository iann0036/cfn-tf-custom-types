# TF::FortiOS::RouterOspf RedistributeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#metric" title="Metric">Metric</a>" : <i>Double</i>,
    "<a href="#metrictype" title="MetricType">MetricType</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#routemap" title="Routemap">Routemap</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#tag" title="Tag">Tag</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#metric" title="Metric">Metric</a>: <i>Double</i>
<a href="#metrictype" title="MetricType">MetricType</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#routemap" title="Routemap">Routemap</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#tag" title="Tag">Tag</a>: <i>Double</i>
</pre>

## Properties

#### Metric

Redistribute metric setting.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricType

Metric type. Valid values: `1`, `2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Redistribute name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Routemap

Route map name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

status Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

Tag value.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

