# Terraform::Circonus::Graph

CloudFormation equivalent of circonus_graph

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Circonus::Graph",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#graphstyle" title="GraphStyle">GraphStyle</a>" : <i>String</i>,
        "<a href="#left" title="Left">Left</a>" : <i>[ &lt;a href=&#34;left.md&#34;&gt;Left&lt;/a&gt;, ... ]</i>,
        "<a href="#linestyle" title="LineStyle">LineStyle</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notes" title="Notes">Notes</a>" : <i>String</i>,
        "<a href="#right" title="Right">Right</a>" : <i>[ &lt;a href=&#34;right.md&#34;&gt;Right&lt;/a&gt;, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#guide" title="Guide">Guide</a>" : <i>[ &lt;a href=&#34;guide.md&#34;&gt;Guide&lt;/a&gt;, ... ]</i>,
        "<a href="#metric" title="Metric">Metric</a>" : <i>[ &lt;a href=&#34;metric.md&#34;&gt;Metric&lt;/a&gt;, ... ]</i>,
        "<a href="#metriccluster" title="MetricCluster">MetricCluster</a>" : <i>[ &lt;a href=&#34;metriccluster.md&#34;&gt;MetricCluster&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Circonus::Graph
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#graphstyle" title="GraphStyle">GraphStyle</a>: <i>String</i>
    <a href="#left" title="Left">Left</a>: <i>
      - &lt;a href=&#34;left.md&#34;&gt;Left&lt;/a&gt;</i>
    <a href="#linestyle" title="LineStyle">LineStyle</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notes" title="Notes">Notes</a>: <i>String</i>
    <a href="#right" title="Right">Right</a>: <i>
      - &lt;a href=&#34;right.md&#34;&gt;Right&lt;/a&gt;</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#guide" title="Guide">Guide</a>: <i>
      - &lt;a href=&#34;guide.md&#34;&gt;Guide&lt;/a&gt;</i>
    <a href="#metric" title="Metric">Metric</a>: <i>
      - &lt;a href=&#34;metric.md&#34;&gt;Metric&lt;/a&gt;</i>
    <a href="#metriccluster" title="MetricCluster">MetricCluster</a>: <i>
      - &lt;a href=&#34;metriccluster.md&#34;&gt;MetricCluster&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GraphStyle

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Left

_Required_: No

_Type_: List of &lt;a href=&#34;left.md&#34;&gt;Left&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LineStyle

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Right

_Required_: No

_Type_: List of &lt;a href=&#34;right.md&#34;&gt;Right&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Guide

_Required_: No

_Type_: List of &lt;a href=&#34;guide.md&#34;&gt;Guide&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: No

_Type_: List of &lt;a href=&#34;metric.md&#34;&gt;Metric&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricCluster

_Required_: No

_Type_: List of &lt;a href=&#34;metriccluster.md&#34;&gt;MetricCluster&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

