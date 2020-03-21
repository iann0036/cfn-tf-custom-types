# Terraform::Datadog::Dashboard Widget QueryValueDefinition Request ApmQuery

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#compute" title="Compute">Compute</a>" : <i>[ &lt;a href=&#34;widget-queryvaluedefinition-request-apmquery-compute.md&#34;&gt;Compute&lt;/a&gt;, ... ]</i>,
    "<a href="#index" title="Index">Index</a>" : <i>String</i>,
    "<a href="#search" title="Search">Search</a>" : <i>[ &lt;a href=&#34;widget-queryvaluedefinition-request-apmquery-search.md&#34;&gt;Search&lt;/a&gt;, ... ]</i>,
    "<a href="#groupby" title="GroupBy">GroupBy</a>" : <i>[ &lt;a href=&#34;widget-queryvaluedefinition-request-apmquery-groupby.md&#34;&gt;GroupBy&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#compute" title="Compute">Compute</a>: <i>
      - &lt;a href=&#34;widget-queryvaluedefinition-request-apmquery-compute.md&#34;&gt;Compute&lt;/a&gt;</i>
<a href="#index" title="Index">Index</a>: <i>String</i>
<a href="#search" title="Search">Search</a>: <i>
      - &lt;a href=&#34;widget-queryvaluedefinition-request-apmquery-search.md&#34;&gt;Search&lt;/a&gt;</i>
<a href="#groupby" title="GroupBy">GroupBy</a>: <i>
      - &lt;a href=&#34;widget-queryvaluedefinition-request-apmquery-groupby.md&#34;&gt;GroupBy&lt;/a&gt;</i>
</pre>

## Properties

#### Compute

_Required_: Yes
_Type_: List of &lt;a href=&#34;widget-queryvaluedefinition-request-apmquery-compute.md&#34;&gt;Compute&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Index

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Search

_Required_: No
_Type_: List of &lt;a href=&#34;widget-queryvaluedefinition-request-apmquery-search.md&#34;&gt;Search&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupBy

_Required_: No
_Type_: List of &lt;a href=&#34;widget-queryvaluedefinition-request-apmquery-groupby.md&#34;&gt;GroupBy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

