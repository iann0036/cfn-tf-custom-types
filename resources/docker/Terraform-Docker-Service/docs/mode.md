# Terraform::Docker::Service Mode

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#global" title="Global">Global</a>" : <i>Boolean</i>,
    "<a href="#replicated" title="Replicated">Replicated</a>" : <i>[ &lt;a href=&#34;mode-replicated.md&#34;&gt;Replicated&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#global" title="Global">Global</a>: <i>Boolean</i>
<a href="#replicated" title="Replicated">Replicated</a>: <i>
      - &lt;a href=&#34;mode-replicated.md&#34;&gt;Replicated&lt;/a&gt;</i>
</pre>

## Properties

#### Global

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Replicated

_Required_: No
_Type_: List of &lt;a href=&#34;mode-replicated.md&#34;&gt;Replicated&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

