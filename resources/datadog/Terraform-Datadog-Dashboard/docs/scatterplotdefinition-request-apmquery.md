# Terraform::Datadog::Dashboard ScatterplotDefinition Request ApmQuery

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#compute" title="Compute">Compute</a>" : <i>[ <a href="scatterplotdefinition-request-apmquery-compute.md">Compute</a>, ... ]</i>,
    "<a href="#index" title="Index">Index</a>" : <i>String</i>,
    "<a href="#search" title="Search">Search</a>" : <i>[ <a href="scatterplotdefinition-request-apmquery-search.md">Search</a>, ... ]</i>,
    "<a href="#groupby" title="GroupBy">GroupBy</a>" : <i>[ <a href="scatterplotdefinition-request-apmquery-groupby.md">GroupBy</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#compute" title="Compute">Compute</a>: <i>
      - <a href="scatterplotdefinition-request-apmquery-compute.md">Compute</a></i>
<a href="#index" title="Index">Index</a>: <i>String</i>
<a href="#search" title="Search">Search</a>: <i>
      - <a href="scatterplotdefinition-request-apmquery-search.md">Search</a></i>
<a href="#groupby" title="GroupBy">GroupBy</a>: <i>
      - <a href="scatterplotdefinition-request-apmquery-groupby.md">GroupBy</a></i>
</pre>

## Properties

#### Compute

_Required_: Yes

_Type_: List of <a href="scatterplotdefinition-request-apmquery-compute.md">Compute</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Index

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Search

_Required_: No

_Type_: List of <a href="scatterplotdefinition-request-apmquery-search.md">Search</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupBy

_Required_: No

_Type_: List of <a href="scatterplotdefinition-request-apmquery-groupby.md">GroupBy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

