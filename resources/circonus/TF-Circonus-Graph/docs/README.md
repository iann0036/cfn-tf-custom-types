# TF::Circonus::Graph

The ``circonus_graph`` resource creates and manages a
[Circonus Graph](https://login.circonus.com/user/docs/Visualization/Graph/Create).

https://login.circonus.com/resources/api/calls/graph).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Circonus::Graph",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#graphstyle" title="GraphStyle">GraphStyle</a>" : <i>String</i>,
        "<a href="#left" title="Left">Left</a>" : <i>[ <a href="leftdefinition.md">LeftDefinition</a>, ... ]</i>,
        "<a href="#linestyle" title="LineStyle">LineStyle</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notes" title="Notes">Notes</a>" : <i>String</i>,
        "<a href="#right" title="Right">Right</a>" : <i>[ <a href="rightdefinition.md">RightDefinition</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#guide" title="Guide">Guide</a>" : <i>[ <a href="guidedefinition.md">GuideDefinition</a>, ... ]</i>,
        "<a href="#metric" title="Metric">Metric</a>" : <i>[ <a href="metricdefinition.md">MetricDefinition</a>, ... ]</i>,
        "<a href="#metriccluster" title="MetricCluster">MetricCluster</a>" : <i>[ <a href="metricclusterdefinition.md">MetricClusterDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Circonus::Graph
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#graphstyle" title="GraphStyle">GraphStyle</a>: <i>String</i>
    <a href="#left" title="Left">Left</a>: <i>
      - <a href="leftdefinition.md">LeftDefinition</a></i>
    <a href="#linestyle" title="LineStyle">LineStyle</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notes" title="Notes">Notes</a>: <i>String</i>
    <a href="#right" title="Right">Right</a>: <i>
      - <a href="rightdefinition.md">RightDefinition</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#guide" title="Guide">Guide</a>: <i>
      - <a href="guidedefinition.md">GuideDefinition</a></i>
    <a href="#metric" title="Metric">Metric</a>: <i>
      - <a href="metricdefinition.md">MetricDefinition</a></i>
    <a href="#metriccluster" title="MetricCluster">MetricCluster</a>: <i>
      - <a href="metricclusterdefinition.md">MetricClusterDefinition</a></i>
</pre>

## Properties

#### Description

Description of what the graph is for.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GraphStyle

How the graph should be rendered.  Valid options
are `area` or `line` (default).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Left

A map of graph left axis options.  Valid values in `left`
include: `logarithmic` can be set to `0` (default) or `1`; `min` is the `min`
Y axis value on the left; and `max` is the Y axis max value on the left.

_Required_: No

_Type_: List of <a href="leftdefinition.md">LeftDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LineStyle

How the line should change between points.  Can be
either `stepped` (default) or `interpolated`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The title of the graph.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notes

A place for storing notes about this graph.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Right

A map of graph right axis options.  Valid values in
`right` include: `logarithmic` can be set to `0` (default) or `1`; `min` is
the `min` Y axis value on the right; and `max` is the Y axis max value on the
right.

_Required_: No

_Type_: List of <a href="rightdefinition.md">RightDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A list of tags assigned to this graph.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Guide

_Required_: No

_Type_: List of <a href="guidedefinition.md">GuideDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: No

_Type_: List of <a href="metricdefinition.md">MetricDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricCluster

_Required_: No

_Type_: List of <a href="metricclusterdefinition.md">MetricClusterDefinition</a>

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

