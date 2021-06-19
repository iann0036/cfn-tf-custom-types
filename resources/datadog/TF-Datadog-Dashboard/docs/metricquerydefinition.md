# TF::Datadog::Dashboard MetricQueryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#aggregator" title="Aggregator">Aggregator</a>" : <i>String</i>,
    "<a href="#datasource" title="DataSource">DataSource</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#query" title="Query">Query</a>" : <i>[ <a href="querydefinition.md">QueryDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#aggregator" title="Aggregator">Aggregator</a>: <i>String</i>
<a href="#datasource" title="DataSource">DataSource</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#query" title="Query">Query</a>: <i>
      - <a href="querydefinition.md">QueryDefinition</a></i>
</pre>

## Properties

#### Aggregator

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataSource

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

_Required_: Yes

_Type_: List of <a href="querydefinition.md">QueryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

