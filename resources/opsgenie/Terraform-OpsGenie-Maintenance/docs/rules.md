# Terraform::OpsGenie::Maintenance Rules

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#state" title="State">State</a>" : <i>String</i>,
    "<a href="#entity" title="Entity">Entity</a>" : <i>[ &lt;a href=&#34;rules-entity.md&#34;&gt;Entity&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#state" title="State">State</a>: <i>String</i>
<a href="#entity" title="Entity">Entity</a>: <i>
      - &lt;a href=&#34;rules-entity.md&#34;&gt;Entity&lt;/a&gt;</i>
</pre>

## Properties

#### State

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Entity

_Required_: No
_Type_: List of &lt;a href=&#34;rules-entity.md&#34;&gt;Entity&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

