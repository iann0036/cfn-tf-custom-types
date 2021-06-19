# TF::Logzio::AlertV2 SubComponentsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accountidstoqueryon" title="AccountIdsToQueryOn">AccountIdsToQueryOn</a>" : <i>[ Double, ... ]</i>,
    "<a href="#filtermust" title="FilterMust">FilterMust</a>" : <i>[ [ <a href="filtermustdefinition.md">FilterMustDefinition</a>, ... ], ... ]</i>,
    "<a href="#filtermustnot" title="FilterMustNot">FilterMustNot</a>" : <i>[ [ <a href="filtermustnotdefinition.md">FilterMustNotDefinition</a>, ... ], ... ]</i>,
    "<a href="#groupbyaggregationfields" title="GroupByAggregationFields">GroupByAggregationFields</a>" : <i>[ String, ... ]</i>,
    "<a href="#operation" title="Operation">Operation</a>" : <i>String</i>,
    "<a href="#querystring" title="QueryString">QueryString</a>" : <i>String</i>,
    "<a href="#shouldqueryonallaccounts" title="ShouldQueryOnAllAccounts">ShouldQueryOnAllAccounts</a>" : <i>Boolean</i>,
    "<a href="#valueaggregationfield" title="ValueAggregationField">ValueAggregationField</a>" : <i>String</i>,
    "<a href="#valueaggregationtype" title="ValueAggregationType">ValueAggregationType</a>" : <i>String</i>,
    "<a href="#columns" title="Columns">Columns</a>" : <i>[ <a href="columnsdefinition.md">ColumnsDefinition</a>, ... ]</i>,
    "<a href="#severitythresholdtiers" title="SeverityThresholdTiers">SeverityThresholdTiers</a>" : <i>[ <a href="severitythresholdtiersdefinition.md">SeverityThresholdTiersDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#accountidstoqueryon" title="AccountIdsToQueryOn">AccountIdsToQueryOn</a>: <i>
      - Double</i>
<a href="#filtermust" title="FilterMust">FilterMust</a>: <i>
      - 
      - <a href="filtermustdefinition.md">FilterMustDefinition</a></i>
<a href="#filtermustnot" title="FilterMustNot">FilterMustNot</a>: <i>
      - 
      - <a href="filtermustnotdefinition.md">FilterMustNotDefinition</a></i>
<a href="#groupbyaggregationfields" title="GroupByAggregationFields">GroupByAggregationFields</a>: <i>
      - String</i>
<a href="#operation" title="Operation">Operation</a>: <i>String</i>
<a href="#querystring" title="QueryString">QueryString</a>: <i>String</i>
<a href="#shouldqueryonallaccounts" title="ShouldQueryOnAllAccounts">ShouldQueryOnAllAccounts</a>: <i>Boolean</i>
<a href="#valueaggregationfield" title="ValueAggregationField">ValueAggregationField</a>: <i>String</i>
<a href="#valueaggregationtype" title="ValueAggregationType">ValueAggregationType</a>: <i>String</i>
<a href="#columns" title="Columns">Columns</a>: <i>
      - <a href="columnsdefinition.md">ColumnsDefinition</a></i>
<a href="#severitythresholdtiers" title="SeverityThresholdTiers">SeverityThresholdTiers</a>: <i>
      - <a href="severitythresholdtiersdefinition.md">SeverityThresholdTiersDefinition</a></i>
</pre>

## Properties

#### AccountIdsToQueryOn

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterMust

_Required_: No

_Type_: List of List of <a href="filtermustdefinition.md">FilterMustDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterMustNot

_Required_: No

_Type_: List of List of <a href="filtermustnotdefinition.md">FilterMustNotDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupByAggregationFields

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryString

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShouldQueryOnAllAccounts

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueAggregationField

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueAggregationType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Columns

_Required_: No

_Type_: List of <a href="columnsdefinition.md">ColumnsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeverityThresholdTiers

_Required_: No

_Type_: List of <a href="severitythresholdtiersdefinition.md">SeverityThresholdTiersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

