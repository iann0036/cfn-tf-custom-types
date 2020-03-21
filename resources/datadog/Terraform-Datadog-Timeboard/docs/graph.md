# Terraform::Datadog::Timeboard Graph

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoscale" title="Autoscale">Autoscale</a>" : <i>Boolean</i>,
    "<a href="#customunit" title="CustomUnit">CustomUnit</a>" : <i>String</i>,
    "<a href="#events" title="Events">Events</a>" : <i>[ String, ... ]</i>,
    "<a href="#group" title="Group">Group</a>" : <i>[ String, ... ]</i>,
    "<a href="#includenometrichosts" title="IncludeNoMetricHosts">IncludeNoMetricHosts</a>" : <i>Boolean</i>,
    "<a href="#includeungroupedhosts" title="IncludeUngroupedHosts">IncludeUngroupedHosts</a>" : <i>Boolean</i>,
    "<a href="#nodetype" title="NodeType">NodeType</a>" : <i>String</i>,
    "<a href="#precision" title="Precision">Precision</a>" : <i>String</i>,
    "<a href="#scope" title="Scope">Scope</a>" : <i>[ String, ... ]</i>,
    "<a href="#style" title="Style">Style</a>" : <i>[ &lt;a href=&#34;graph-style.md&#34;&gt;Style&lt;/a&gt;, ... ]</i>,
    "<a href="#textalign" title="TextAlign">TextAlign</a>" : <i>String</i>,
    "<a href="#title" title="Title">Title</a>" : <i>String</i>,
    "<a href="#viz" title="Viz">Viz</a>" : <i>String</i>,
    "<a href="#yaxis" title="Yaxis">Yaxis</a>" : <i>[ &lt;a href=&#34;graph-yaxis.md&#34;&gt;Yaxis&lt;/a&gt;, ... ]</i>,
    "<a href="#marker" title="Marker">Marker</a>" : <i>[ &lt;a href=&#34;graph-marker.md&#34;&gt;Marker&lt;/a&gt;, ... ]</i>,
    "<a href="#request" title="Request">Request</a>" : <i>[ &lt;a href=&#34;graph-request.md&#34;&gt;Request&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autoscale" title="Autoscale">Autoscale</a>: <i>Boolean</i>
<a href="#customunit" title="CustomUnit">CustomUnit</a>: <i>String</i>
<a href="#events" title="Events">Events</a>: <i>
      - String</i>
<a href="#group" title="Group">Group</a>: <i>
      - String</i>
<a href="#includenometrichosts" title="IncludeNoMetricHosts">IncludeNoMetricHosts</a>: <i>Boolean</i>
<a href="#includeungroupedhosts" title="IncludeUngroupedHosts">IncludeUngroupedHosts</a>: <i>Boolean</i>
<a href="#nodetype" title="NodeType">NodeType</a>: <i>String</i>
<a href="#precision" title="Precision">Precision</a>: <i>String</i>
<a href="#scope" title="Scope">Scope</a>: <i>
      - String</i>
<a href="#style" title="Style">Style</a>: <i>
      - &lt;a href=&#34;graph-style.md&#34;&gt;Style&lt;/a&gt;</i>
<a href="#textalign" title="TextAlign">TextAlign</a>: <i>String</i>
<a href="#title" title="Title">Title</a>: <i>String</i>
<a href="#viz" title="Viz">Viz</a>: <i>String</i>
<a href="#yaxis" title="Yaxis">Yaxis</a>: <i>
      - &lt;a href=&#34;graph-yaxis.md&#34;&gt;Yaxis&lt;/a&gt;</i>
<a href="#marker" title="Marker">Marker</a>: <i>
      - &lt;a href=&#34;graph-marker.md&#34;&gt;Marker&lt;/a&gt;</i>
<a href="#request" title="Request">Request</a>: <i>
      - &lt;a href=&#34;graph-request.md&#34;&gt;Request&lt;/a&gt;</i>
</pre>

## Properties

#### Autoscale

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomUnit

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Events

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeNoMetricHosts

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeUngroupedHosts

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Precision

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Style

_Required_: No
_Type_: List of &lt;a href=&#34;graph-style.md&#34;&gt;Style&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TextAlign

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Viz

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Yaxis

_Required_: No
_Type_: List of &lt;a href=&#34;graph-yaxis.md&#34;&gt;Yaxis&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Marker

_Required_: No
_Type_: List of &lt;a href=&#34;graph-marker.md&#34;&gt;Marker&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Request

_Required_: No
_Type_: List of &lt;a href=&#34;graph-request.md&#34;&gt;Request&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

