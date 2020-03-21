# Terraform::RabbitMQ::Policy Policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#applyto" title="ApplyTo">ApplyTo</a>" : <i>String</i>,
    "<a href="#definition" title="Definition">Definition</a>" : <i>[ <a href="policy-definition.md">Definition</a>, ... ]</i>,
    "<a href="#pattern" title="Pattern">Pattern</a>" : <i>String</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#applyto" title="ApplyTo">ApplyTo</a>: <i>String</i>
<a href="#definition" title="Definition">Definition</a>: <i>
      - <a href="policy-definition.md">Definition</a></i>
<a href="#pattern" title="Pattern">Pattern</a>: <i>String</i>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
</pre>

## Properties

#### ApplyTo

Can either be "exchanges", "queues", or "all".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Definition

Key/value pairs of the policy definition. See the
RabbitMQ documentation for definition references and examples.

_Required_: Yes

_Type_: List of <a href="policy-definition.md">Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pattern

A pattern to match an exchange or queue name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

The policy with the greater priority is applied first.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

