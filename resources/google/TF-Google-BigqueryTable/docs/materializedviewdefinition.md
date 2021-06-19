# TF::Google::BigqueryTable MaterializedViewDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enablerefresh" title="EnableRefresh">EnableRefresh</a>" : <i>Boolean</i>,
    "<a href="#query" title="Query">Query</a>" : <i>String</i>,
    "<a href="#refreshintervalms" title="RefreshIntervalMs">RefreshIntervalMs</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#enablerefresh" title="EnableRefresh">EnableRefresh</a>: <i>Boolean</i>
<a href="#query" title="Query">Query</a>: <i>String</i>
<a href="#refreshintervalms" title="RefreshIntervalMs">RefreshIntervalMs</a>: <i>Double</i>
</pre>

## Properties

#### EnableRefresh

Specifies whether to use BigQuery's automatic refresh for this materialized view when the base table is updated.
The default value is true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

A query whose result is persisted.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RefreshIntervalMs

The maximum frequency at which this materialized view will be refreshed.
The default value is 1800000.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

