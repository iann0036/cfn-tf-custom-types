# Terraform::Datadog::Timeboard Graph Request

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
    "<a href="#metadatajson" title="MetadataJson">MetadataJson</a>" : <i>String</i>,
    "<a href="#orderby" title="OrderBy">OrderBy</a>" : <i>String</i>,
    "<a href="#orderdirection" title="OrderDirection">OrderDirection</a>" : <i>String</i>,
    "<a href="#q" title="Q">Q</a>" : <i>String</i>,
    "<a href="#stacked" title="Stacked">Stacked</a>" : <i>Boolean</i>,
    "<a href="#style" title="Style">Style</a>" : <i>[ <a href="graph-request-style.md">Style</a>, ... ]</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#apmquery" title="ApmQuery">ApmQuery</a>" : <i>[ <a href="graph-request-apmquery.md">ApmQuery</a>, ... ]</i>,
    "<a href="#conditionalformat" title="ConditionalFormat">ConditionalFormat</a>" : <i>[ <a href="graph-request-conditionalformat.md">ConditionalFormat</a>, ... ]</i>,
    "<a href="#logquery" title="LogQuery">LogQuery</a>" : <i>[ <a href="graph-request-logquery.md">LogQuery</a>, ... ]</i>,
    "<a href="#processquery" title="ProcessQuery">ProcessQuery</a>" : <i>[ <a href="graph-request-processquery.md">ProcessQuery</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#aggregator" title="Aggregator">Aggregator</a>: <i>String</i>
<a href="#changetype" title="ChangeType">ChangeType</a>: <i>String</i>
<a href="#compareto" title="CompareTo">CompareTo</a>: <i>String</i>
<a href="#extracol" title="ExtraCol">ExtraCol</a>: <i>String</i>
<a href="#increasegood" title="IncreaseGood">IncreaseGood</a>: <i>Boolean</i>
<a href="#metadatajson" title="MetadataJson">MetadataJson</a>: <i>String</i>
<a href="#orderby" title="OrderBy">OrderBy</a>: <i>String</i>
<a href="#orderdirection" title="OrderDirection">OrderDirection</a>: <i>String</i>
<a href="#q" title="Q">Q</a>: <i>String</i>
<a href="#stacked" title="Stacked">Stacked</a>: <i>Boolean</i>
<a href="#style" title="Style">Style</a>: <i>
      - <a href="graph-request-style.md">Style</a></i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#apmquery" title="ApmQuery">ApmQuery</a>: <i>
      - <a href="graph-request-apmquery.md">ApmQuery</a></i>
<a href="#conditionalformat" title="ConditionalFormat">ConditionalFormat</a>: <i>
      - <a href="graph-request-conditionalformat.md">ConditionalFormat</a></i>
<a href="#logquery" title="LogQuery">LogQuery</a>: <i>
      - <a href="graph-request-logquery.md">LogQuery</a></i>
<a href="#processquery" title="ProcessQuery">ProcessQuery</a>: <i>
      - <a href="graph-request-processquery.md">ProcessQuery</a></i>
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

#### MetadataJson

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrderBy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrderDirection

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Q

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stacked

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Style

_Required_: No

_Type_: List of <a href="graph-request-style.md">Style</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApmQuery

_Required_: No

_Type_: List of <a href="graph-request-apmquery.md">ApmQuery</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConditionalFormat

_Required_: No

_Type_: List of <a href="graph-request-conditionalformat.md">ConditionalFormat</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogQuery

_Required_: No

_Type_: List of <a href="graph-request-logquery.md">LogQuery</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessQuery

_Required_: No

_Type_: List of <a href="graph-request-processquery.md">ProcessQuery</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

