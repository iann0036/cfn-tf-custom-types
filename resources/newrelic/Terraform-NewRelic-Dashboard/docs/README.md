# Terraform::NewRelic::Dashboard

CloudFormation equivalent of newrelic_dashboard

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NewRelic::Dashboard",
    "Properties" : {
        "<a href="#editable" title="Editable">Editable</a>" : <i>String</i>,
        "<a href="#icon" title="Icon">Icon</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
        "<a href="#visibility" title="Visibility">Visibility</a>" : <i>String</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>[ &lt;a href=&#34;filter.md&#34;&gt;Filter&lt;/a&gt;, ... ]</i>,
        "<a href="#widget" title="Widget">Widget</a>" : <i>[ &lt;a href=&#34;widget.md&#34;&gt;Widget&lt;/a&gt;, ... ]</i>,
        "<a href="#comparewith" title="CompareWith">CompareWith</a>" : <i>[ &lt;a href=&#34;comparewith.md&#34;&gt;CompareWith&lt;/a&gt;, ... ]</i>,
        "<a href="#metric" title="Metric">Metric</a>" : <i>[ &lt;a href=&#34;metric.md&#34;&gt;Metric&lt;/a&gt;, ... ]</i>,
        "<a href="#presentation" title="Presentation">Presentation</a>" : <i>[ &lt;a href=&#34;presentation.md&#34;&gt;Presentation&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NewRelic::Dashboard
Properties:
    <a href="#editable" title="Editable">Editable</a>: <i>String</i>
    <a href="#icon" title="Icon">Icon</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
    <a href="#visibility" title="Visibility">Visibility</a>: <i>String</i>
    <a href="#filter" title="Filter">Filter</a>: <i>
      - &lt;a href=&#34;filter.md&#34;&gt;Filter&lt;/a&gt;</i>
    <a href="#widget" title="Widget">Widget</a>: <i>
      - &lt;a href=&#34;widget.md&#34;&gt;Widget&lt;/a&gt;</i>
    <a href="#comparewith" title="CompareWith">CompareWith</a>: <i>
      - &lt;a href=&#34;comparewith.md&#34;&gt;CompareWith&lt;/a&gt;</i>
    <a href="#metric" title="Metric">Metric</a>: <i>
      - &lt;a href=&#34;metric.md&#34;&gt;Metric&lt;/a&gt;</i>
    <a href="#presentation" title="Presentation">Presentation</a>: <i>
      - &lt;a href=&#34;presentation.md&#34;&gt;Presentation&lt;/a&gt;</i>
</pre>

## Properties

#### Editable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Icon

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Visibility

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: List of &lt;a href=&#34;filter.md&#34;&gt;Filter&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Widget

_Required_: No

_Type_: List of &lt;a href=&#34;widget.md&#34;&gt;Widget&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompareWith

_Required_: No

_Type_: List of &lt;a href=&#34;comparewith.md&#34;&gt;CompareWith&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: No

_Type_: List of &lt;a href=&#34;metric.md&#34;&gt;Metric&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Presentation

_Required_: No

_Type_: List of &lt;a href=&#34;presentation.md&#34;&gt;Presentation&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DashboardUrl

Returns the &lt;code&gt;DashboardUrl&lt;/code&gt; value.

