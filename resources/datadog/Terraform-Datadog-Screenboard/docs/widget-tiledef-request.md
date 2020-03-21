# Terraform::Datadog::Screenboard Widget TileDef Request

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#aggregator" title="Aggregator">Aggregator</a>" : <i>String</i>,
    "<a href="#changetype" title="ChangeType">ChangeType</a>" : <i>String</i>,
    "<a href="#compareto" title="CompareTo">CompareTo</a>" : <i>String</i>,
    "<a href="#extracol" title="ExtraCol">ExtraCol</a>" : <i>String</i>,
    "<a href="#increasegood" title="IncreaseGood">IncreaseGood</a>" : <i>Boolean</i>,
    "<a href="#limit" title="Limit">Limit</a>" : <i>Double</i>,
    "<a href="#metadatajson" title="MetadataJson">MetadataJson</a>" : <i>String</i>,
    "<a href="#metric" title="Metric">Metric</a>" : <i>String</i>,
    "<a href="#orderby" title="OrderBy">OrderBy</a>" : <i>String</i>,
    "<a href="#orderdir" title="OrderDir">OrderDir</a>" : <i>String</i>,
    "<a href="#q" title="Q">Q</a>" : <i>String</i>,
    "<a href="#querytype" title="QueryType">QueryType</a>" : <i>String</i>,
    "<a href="#style" title="Style">Style</a>" : <i>[ &lt;a href=&#34;widget-tiledef-request-style.md&#34;&gt;Style&lt;/a&gt;, ... ]</i>,
    "<a href="#tagfilters" title="TagFilters">TagFilters</a>" : <i>[ String, ... ]</i>,
    "<a href="#textfilter" title="TextFilter">TextFilter</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#apmquery" title="ApmQuery">ApmQuery</a>" : <i>[ &lt;a href=&#34;widget-tiledef-request-apmquery.md&#34;&gt;ApmQuery&lt;/a&gt;, ... ]</i>,
    "<a href="#conditionalformat" title="ConditionalFormat">ConditionalFormat</a>" : <i>[ &lt;a href=&#34;widget-tiledef-request-conditionalformat.md&#34;&gt;ConditionalFormat&lt;/a&gt;, ... ]</i>,
    "<a href="#logquery" title="LogQuery">LogQuery</a>" : <i>[ &lt;a href=&#34;widget-tiledef-request-logquery.md&#34;&gt;LogQuery&lt;/a&gt;, ... ]</i>,
    "<a href="#processquery" title="ProcessQuery">ProcessQuery</a>" : <i>[ &lt;a href=&#34;widget-tiledef-request-processquery.md&#34;&gt;ProcessQuery&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#aggregator" title="Aggregator">Aggregator</a>: <i>String</i>
<a href="#changetype" title="ChangeType">ChangeType</a>: <i>String</i>
<a href="#compareto" title="CompareTo">CompareTo</a>: <i>String</i>
<a href="#extracol" title="ExtraCol">ExtraCol</a>: <i>String</i>
<a href="#increasegood" title="IncreaseGood">IncreaseGood</a>: <i>Boolean</i>
<a href="#limit" title="Limit">Limit</a>: <i>Double</i>
<a href="#metadatajson" title="MetadataJson">MetadataJson</a>: <i>String</i>
<a href="#metric" title="Metric">Metric</a>: <i>String</i>
<a href="#orderby" title="OrderBy">OrderBy</a>: <i>String</i>
<a href="#orderdir" title="OrderDir">OrderDir</a>: <i>String</i>
<a href="#q" title="Q">Q</a>: <i>String</i>
<a href="#querytype" title="QueryType">QueryType</a>: <i>String</i>
<a href="#style" title="Style">Style</a>: <i>
      - &lt;a href=&#34;widget-tiledef-request-style.md&#34;&gt;Style&lt;/a&gt;</i>
<a href="#tagfilters" title="TagFilters">TagFilters</a>: <i>
      - String</i>
<a href="#textfilter" title="TextFilter">TextFilter</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#apmquery" title="ApmQuery">ApmQuery</a>: <i>
      - &lt;a href=&#34;widget-tiledef-request-apmquery.md&#34;&gt;ApmQuery&lt;/a&gt;</i>
<a href="#conditionalformat" title="ConditionalFormat">ConditionalFormat</a>: <i>
      - &lt;a href=&#34;widget-tiledef-request-conditionalformat.md&#34;&gt;ConditionalFormat&lt;/a&gt;</i>
<a href="#logquery" title="LogQuery">LogQuery</a>: <i>
      - &lt;a href=&#34;widget-tiledef-request-logquery.md&#34;&gt;LogQuery&lt;/a&gt;</i>
<a href="#processquery" title="ProcessQuery">ProcessQuery</a>: <i>
      - &lt;a href=&#34;widget-tiledef-request-processquery.md&#34;&gt;ProcessQuery&lt;/a&gt;</i>
</pre>

## Properties

#### Aggregator

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChangeType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompareTo

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraCol

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncreaseGood

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Limit

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetadataJson

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrderBy

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrderDir

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Q

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Style

_Required_: No
_Type_: List of &lt;a href=&#34;widget-tiledef-request-style.md&#34;&gt;Style&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagFilters

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TextFilter

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApmQuery

_Required_: No
_Type_: List of &lt;a href=&#34;widget-tiledef-request-apmquery.md&#34;&gt;ApmQuery&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConditionalFormat

_Required_: No
_Type_: List of &lt;a href=&#34;widget-tiledef-request-conditionalformat.md&#34;&gt;ConditionalFormat&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogQuery

_Required_: No
_Type_: List of &lt;a href=&#34;widget-tiledef-request-logquery.md&#34;&gt;LogQuery&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessQuery

_Required_: No
_Type_: List of &lt;a href=&#34;widget-tiledef-request-processquery.md&#34;&gt;ProcessQuery&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
