# Terraform::Google::BigqueryTable View

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#query" title="Query">Query</a>" : <i>String</i>,
    "<a href="#uselegacysql" title="UseLegacySql">UseLegacySql</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#query" title="Query">Query</a>: <i>String</i>
<a href="#uselegacysql" title="UseLegacySql">UseLegacySql</a>: <i>Boolean</i>
</pre>

## Properties

#### Query

A query that BigQuery executes when the view is referenced.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseLegacySql

Specifies whether to use BigQuery's legacy SQL for this view.
The default value is true. If set to false, the view will use BigQuery's standard SQL.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

