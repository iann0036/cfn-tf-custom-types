# TF::Datadog::Dashboard ProcessQueryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#aggregator" title="Aggregator">Aggregator</a>" : <i>String</i>,
    "<a href="#datasource" title="DataSource">DataSource</a>" : <i>String</i>,
    "<a href="#isnormalizedcpu" title="IsNormalizedCpu">IsNormalizedCpu</a>" : <i>Boolean</i>,
    "<a href="#limit" title="Limit">Limit</a>" : <i>[ <a href="limitdefinition.md">LimitDefinition</a>, ... ]</i>,
    "<a href="#metric" title="Metric">Metric</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#sort" title="Sort">Sort</a>" : <i>[ <a href="sortdefinition.md">SortDefinition</a>, ... ]</i>,
    "<a href="#tagfilters" title="TagFilters">TagFilters</a>" : <i>[ String, ... ]</i>,
    "<a href="#textfilter" title="TextFilter">TextFilter</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#aggregator" title="Aggregator">Aggregator</a>: <i>String</i>
<a href="#datasource" title="DataSource">DataSource</a>: <i>String</i>
<a href="#isnormalizedcpu" title="IsNormalizedCpu">IsNormalizedCpu</a>: <i>Boolean</i>
<a href="#limit" title="Limit">Limit</a>: <i>
      - <a href="limitdefinition.md">LimitDefinition</a></i>
<a href="#metric" title="Metric">Metric</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#sort" title="Sort">Sort</a>: <i>
      - <a href="sortdefinition.md">SortDefinition</a></i>
<a href="#tagfilters" title="TagFilters">TagFilters</a>: <i>
      - String</i>
<a href="#textfilter" title="TextFilter">TextFilter</a>: <i>String</i>
</pre>

## Properties

#### Aggregator

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataSource

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsNormalizedCpu

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Limit

_Required_: No

_Type_: List of <a href="limitdefinition.md">LimitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sort

_Required_: No

_Type_: List of <a href="sortdefinition.md">SortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagFilters

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TextFilter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

