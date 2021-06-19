# TF::AzureRM::CostManagementExportResourceGroup QueryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#timeframe" title="TimeFrame">TimeFrame</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#timeframe" title="TimeFrame">TimeFrame</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### TimeFrame

The time frame for pulling data for the query. If custom, then a specific time period must be provided. Possible values include: `WeekToDate`, `MonthToDate`, `YearToDate`, `TheLastWeek`, `TheLastMonth`, `TheLastYear`, `Custom`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of the query.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

