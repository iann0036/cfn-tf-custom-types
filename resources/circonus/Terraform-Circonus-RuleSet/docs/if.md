# Terraform::Circonus::RuleSet If

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#then" title="Then">Then</a>" : <i>[ <a href="if-then.md">Then</a>, ... ]</i>,
    "<a href="#value" title="Value">Value</a>" : <i>[ <a href="if-value.md">Value</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#then" title="Then">Then</a>: <i>
      - <a href="if-then.md">Then</a></i>
<a href="#value" title="Value">Value</a>: <i>
      - <a href="if-value.md">Value</a></i>
</pre>

## Properties

#### Then

_Required_: No

_Type_: List of <a href="if-then.md">Then</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

_Required_: No

_Type_: List of <a href="if-value.md">Value</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

