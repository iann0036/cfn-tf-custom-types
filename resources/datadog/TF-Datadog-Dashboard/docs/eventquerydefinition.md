# TF::Datadog::Dashboard EventQueryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#datasource" title="DataSource">DataSource</a>" : <i>String</i>,
    "<a href="#indexes" title="Indexes">Indexes</a>" : <i>[ String, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#compute" title="Compute">Compute</a>" : <i>[ <a href="computedefinition.md">ComputeDefinition</a>, ... ]</i>,
    "<a href="#groupby" title="GroupBy">GroupBy</a>" : <i>[ <a href="groupbydefinition.md">GroupByDefinition</a>, ... ]</i>,
    "<a href="#search" title="Search">Search</a>" : <i>[ <a href="searchdefinition.md">SearchDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#datasource" title="DataSource">DataSource</a>: <i>String</i>
<a href="#indexes" title="Indexes">Indexes</a>: <i>
      - String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#compute" title="Compute">Compute</a>: <i>
      - <a href="computedefinition.md">ComputeDefinition</a></i>
<a href="#groupby" title="GroupBy">GroupBy</a>: <i>
      - <a href="groupbydefinition.md">GroupByDefinition</a></i>
<a href="#search" title="Search">Search</a>: <i>
      - <a href="searchdefinition.md">SearchDefinition</a></i>
</pre>

## Properties

#### DataSource

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Indexes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Compute

_Required_: No

_Type_: List of <a href="computedefinition.md">ComputeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupBy

_Required_: No

_Type_: List of <a href="groupbydefinition.md">GroupByDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Search

_Required_: No

_Type_: List of <a href="searchdefinition.md">SearchDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

