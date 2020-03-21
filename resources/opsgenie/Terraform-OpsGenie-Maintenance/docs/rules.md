# Terraform::OpsGenie::Maintenance Rules

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#state" title="State">State</a>" : <i>String</i>,
    "<a href="#entity" title="Entity">Entity</a>" : <i>[ <a href="rules-entity.md">Entity</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#state" title="State">State</a>: <i>String</i>
<a href="#entity" title="Entity">Entity</a>: <i>
      - <a href="rules-entity.md">Entity</a></i>
</pre>

## Properties

#### State

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Entity

_Required_: No
_Type_: List of <a href="rules-entity.md">Entity</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

