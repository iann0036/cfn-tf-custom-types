# Terraform::NewRelic::Dashboard Widget

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#column" title="Column">Column</a>" : <i>Double</i>,
    "<a href="#drilldowndashboardid" title="DrilldownDashboardId">DrilldownDashboardId</a>" : <i>Double</i>,
    "<a href="#duration" title="Duration">Duration</a>" : <i>Double</i>,
    "<a href="#endtime" title="EndTime">EndTime</a>" : <i>Double</i>,
    "<a href="#entityids" title="EntityIds">EntityIds</a>" : <i>[ Double, ... ]</i>,
    "<a href="#facet" title="Facet">Facet</a>" : <i>String</i>,
    "<a href="#height" title="Height">Height</a>" : <i>Double</i>,
    "<a href="#limit" title="Limit">Limit</a>" : <i>Double</i>,
    "<a href="#notes" title="Notes">Notes</a>" : <i>String</i>,
    "<a href="#nrql" title="Nrql">Nrql</a>" : <i>String</i>,
    "<a href="#orderby" title="OrderBy">OrderBy</a>" : <i>String</i>,
    "<a href="#row" title="Row">Row</a>" : <i>Double</i>,
    "<a href="#source" title="Source">Source</a>" : <i>String</i>,
    "<a href="#thresholdred" title="ThresholdRed">ThresholdRed</a>" : <i>Double</i>,
    "<a href="#thresholdyellow" title="ThresholdYellow">ThresholdYellow</a>" : <i>Double</i>,
    "<a href="#title" title="Title">Title</a>" : <i>String</i>,
    "<a href="#visualization" title="Visualization">Visualization</a>" : <i>String</i>,
    "<a href="#width" title="Width">Width</a>" : <i>Double</i>,
    "<a href="#comparewith" title="CompareWith">CompareWith</a>" : <i>[ &lt;a href=&#34;widget-comparewith.md&#34;&gt;CompareWith&lt;/a&gt;, ... ]</i>,
    "<a href="#metric" title="Metric">Metric</a>" : <i>[ &lt;a href=&#34;widget-metric.md&#34;&gt;Metric&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#column" title="Column">Column</a>: <i>Double</i>
<a href="#drilldowndashboardid" title="DrilldownDashboardId">DrilldownDashboardId</a>: <i>Double</i>
<a href="#duration" title="Duration">Duration</a>: <i>Double</i>
<a href="#endtime" title="EndTime">EndTime</a>: <i>Double</i>
<a href="#entityids" title="EntityIds">EntityIds</a>: <i>
      - Double</i>
<a href="#facet" title="Facet">Facet</a>: <i>String</i>
<a href="#height" title="Height">Height</a>: <i>Double</i>
<a href="#limit" title="Limit">Limit</a>: <i>Double</i>
<a href="#notes" title="Notes">Notes</a>: <i>String</i>
<a href="#nrql" title="Nrql">Nrql</a>: <i>String</i>
<a href="#orderby" title="OrderBy">OrderBy</a>: <i>String</i>
<a href="#row" title="Row">Row</a>: <i>Double</i>
<a href="#source" title="Source">Source</a>: <i>String</i>
<a href="#thresholdred" title="ThresholdRed">ThresholdRed</a>: <i>Double</i>
<a href="#thresholdyellow" title="ThresholdYellow">ThresholdYellow</a>: <i>Double</i>
<a href="#title" title="Title">Title</a>: <i>String</i>
<a href="#visualization" title="Visualization">Visualization</a>: <i>String</i>
<a href="#width" title="Width">Width</a>: <i>Double</i>
<a href="#comparewith" title="CompareWith">CompareWith</a>: <i>
      - &lt;a href=&#34;widget-comparewith.md&#34;&gt;CompareWith&lt;/a&gt;</i>
<a href="#metric" title="Metric">Metric</a>: <i>
      - &lt;a href=&#34;widget-metric.md&#34;&gt;Metric&lt;/a&gt;</i>
</pre>

## Properties

#### Column

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrilldownDashboardId

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndTime

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EntityIds

_Required_: No
_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Facet

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Height

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Limit

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notes

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nrql

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrderBy

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Row

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdRed

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdYellow

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Visualization

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Width

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompareWith

_Required_: No
_Type_: List of &lt;a href=&#34;widget-comparewith.md&#34;&gt;CompareWith&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: No
_Type_: List of &lt;a href=&#34;widget-metric.md&#34;&gt;Metric&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

