# Terraform::Datadog::LogsCustomPipeline Processor CategoryProcessor

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#target" title="Target">Target</a>" : <i>String</i>,
    "<a href="#category" title="Category">Category</a>" : <i>[ &lt;a href=&#34;processor-categoryprocessor-category.md&#34;&gt;Category&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#target" title="Target">Target</a>: <i>String</i>
<a href="#category" title="Category">Category</a>: <i>
      - &lt;a href=&#34;processor-categoryprocessor-category.md&#34;&gt;Category&lt;/a&gt;</i>
</pre>

## Properties

#### IsEnabled

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Category

_Required_: No
_Type_: List of &lt;a href=&#34;processor-categoryprocessor-category.md&#34;&gt;Category&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

