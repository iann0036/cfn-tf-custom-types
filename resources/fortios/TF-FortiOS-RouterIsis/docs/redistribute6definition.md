# TF::FortiOS::RouterIsis Redistribute6Definition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#level" title="Level">Level</a>" : <i>String</i>,
    "<a href="#metric" title="Metric">Metric</a>" : <i>Double</i>,
    "<a href="#metrictype" title="MetricType">MetricType</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#routemap" title="Routemap">Routemap</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#level" title="Level">Level</a>: <i>String</i>
<a href="#metric" title="Metric">Metric</a>: <i>Double</i>
<a href="#metrictype" title="MetricType">MetricType</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#routemap" title="Routemap">Routemap</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
</pre>

## Properties

#### Level

Level. Valid values: `level-1-2`, `level-1`, `level-2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

Metric.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricType

Metric type. Valid values: `external`, `internal`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Protocol name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Routemap

Route map name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable redistribution. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

