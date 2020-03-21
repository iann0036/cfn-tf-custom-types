# Terraform::Datadog::LogsCustomPipeline Pipeline

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#filter" title="Filter">Filter</a>" : <i>[ &lt;a href=&#34;pipeline-filter.md&#34;&gt;Filter&lt;/a&gt;, ... ]</i>,
    "<a href="#processor" title="Processor">Processor</a>" : <i>[ &lt;a href=&#34;pipeline-processor.md&#34;&gt;Processor&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#filter" title="Filter">Filter</a>: <i>
      - &lt;a href=&#34;pipeline-filter.md&#34;&gt;Filter&lt;/a&gt;</i>
<a href="#processor" title="Processor">Processor</a>: <i>
      - &lt;a href=&#34;pipeline-processor.md&#34;&gt;Processor&lt;/a&gt;</i>
</pre>

## Properties

#### IsEnabled

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No
_Type_: List of &lt;a href=&#34;pipeline-filter.md&#34;&gt;Filter&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Processor

_Required_: No
_Type_: List of &lt;a href=&#34;pipeline-processor.md&#34;&gt;Processor&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

