# TF::Datadog::Dashboard RequestDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#q" title="Q">Q</a>" : <i>String</i>,
    "<a href="#apmquery" title="ApmQuery">ApmQuery</a>" : <i>[ <a href="apmquerydefinition.md">ApmQueryDefinition</a>, ... ]</i>,
    "<a href="#conditionalformats" title="ConditionalFormats">ConditionalFormats</a>" : <i>[ <a href="conditionalformatsdefinition.md">ConditionalFormatsDefinition</a>, ... ]</i>,
    "<a href="#formula" title="Formula">Formula</a>" : <i>[ <a href="formuladefinition.md">FormulaDefinition</a>, ... ]</i>,
    "<a href="#logquery" title="LogQuery">LogQuery</a>" : <i>[ <a href="logquerydefinition.md">LogQueryDefinition</a>, ... ]</i>,
    "<a href="#processquery" title="ProcessQuery">ProcessQuery</a>" : <i>[ <a href="processquerydefinition.md">ProcessQueryDefinition</a>, ... ]</i>,
    "<a href="#query" title="Query">Query</a>" : <i>[ <a href="querydefinition.md">QueryDefinition</a>, ... ]</i>,
    "<a href="#rumquery" title="RumQuery">RumQuery</a>" : <i>[ <a href="rumquerydefinition.md">RumQueryDefinition</a>, ... ]</i>,
    "<a href="#securityquery" title="SecurityQuery">SecurityQuery</a>" : <i>[ <a href="securityquerydefinition.md">SecurityQueryDefinition</a>, ... ]</i>,
    "<a href="#style" title="Style">Style</a>" : <i>[ <a href="styledefinition.md">StyleDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#q" title="Q">Q</a>: <i>String</i>
<a href="#apmquery" title="ApmQuery">ApmQuery</a>: <i>
      - <a href="apmquerydefinition.md">ApmQueryDefinition</a></i>
<a href="#conditionalformats" title="ConditionalFormats">ConditionalFormats</a>: <i>
      - <a href="conditionalformatsdefinition.md">ConditionalFormatsDefinition</a></i>
<a href="#formula" title="Formula">Formula</a>: <i>
      - <a href="formuladefinition.md">FormulaDefinition</a></i>
<a href="#logquery" title="LogQuery">LogQuery</a>: <i>
      - <a href="logquerydefinition.md">LogQueryDefinition</a></i>
<a href="#processquery" title="ProcessQuery">ProcessQuery</a>: <i>
      - <a href="processquerydefinition.md">ProcessQueryDefinition</a></i>
<a href="#query" title="Query">Query</a>: <i>
      - <a href="querydefinition.md">QueryDefinition</a></i>
<a href="#rumquery" title="RumQuery">RumQuery</a>: <i>
      - <a href="rumquerydefinition.md">RumQueryDefinition</a></i>
<a href="#securityquery" title="SecurityQuery">SecurityQuery</a>: <i>
      - <a href="securityquerydefinition.md">SecurityQueryDefinition</a></i>
<a href="#style" title="Style">Style</a>: <i>
      - <a href="styledefinition.md">StyleDefinition</a></i>
</pre>

## Properties

#### Q

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApmQuery

_Required_: No

_Type_: List of <a href="apmquerydefinition.md">ApmQueryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConditionalFormats

_Required_: No

_Type_: List of <a href="conditionalformatsdefinition.md">ConditionalFormatsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Formula

_Required_: No

_Type_: List of <a href="formuladefinition.md">FormulaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogQuery

_Required_: No

_Type_: List of <a href="logquerydefinition.md">LogQueryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessQuery

_Required_: No

_Type_: List of <a href="processquerydefinition.md">ProcessQueryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

_Required_: No

_Type_: List of <a href="querydefinition.md">QueryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RumQuery

_Required_: No

_Type_: List of <a href="rumquerydefinition.md">RumQueryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityQuery

_Required_: No

_Type_: List of <a href="securityquerydefinition.md">SecurityQueryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Style

_Required_: No

_Type_: List of <a href="styledefinition.md">StyleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

