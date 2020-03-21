# Terraform::AzureRM::StorageManagementPolicy Rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#actions" title="Actions">Actions</a>" : <i>[ &lt;a href=&#34;rule-actions.md&#34;&gt;Actions&lt;/a&gt;, ... ]</i>,
    "<a href="#filters" title="Filters">Filters</a>" : <i>[ &lt;a href=&#34;rule-filters.md&#34;&gt;Filters&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#actions" title="Actions">Actions</a>: <i>
      - &lt;a href=&#34;rule-actions.md&#34;&gt;Actions&lt;/a&gt;</i>
<a href="#filters" title="Filters">Filters</a>: <i>
      - &lt;a href=&#34;rule-filters.md&#34;&gt;Filters&lt;/a&gt;</i>
</pre>

## Properties

#### Enabled

_Required_: Yes
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Actions

_Required_: No
_Type_: List of &lt;a href=&#34;rule-actions.md&#34;&gt;Actions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filters

_Required_: No
_Type_: List of &lt;a href=&#34;rule-filters.md&#34;&gt;Filters&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

