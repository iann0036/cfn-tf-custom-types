# Terraform::RabbitMQ::Policy Policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#applyto" title="ApplyTo">ApplyTo</a>" : <i>String</i>,
    "<a href="#definition" title="Definition">Definition</a>" : <i>[ &lt;a href=&#34;policy-definition.md&#34;&gt;Definition&lt;/a&gt;, ... ]</i>,
    "<a href="#pattern" title="Pattern">Pattern</a>" : <i>String</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#applyto" title="ApplyTo">ApplyTo</a>: <i>String</i>
<a href="#definition" title="Definition">Definition</a>: <i>
      - &lt;a href=&#34;policy-definition.md&#34;&gt;Definition&lt;/a&gt;</i>
<a href="#pattern" title="Pattern">Pattern</a>: <i>String</i>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
</pre>

## Properties

#### ApplyTo

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Definition

_Required_: Yes
_Type_: List of &lt;a href=&#34;policy-definition.md&#34;&gt;Definition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pattern

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

