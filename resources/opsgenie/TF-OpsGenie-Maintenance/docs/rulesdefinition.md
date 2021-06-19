# TF::OpsGenie::Maintenance RulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#state" title="State">State</a>" : <i>String</i>,
    "<a href="#entity" title="Entity">Entity</a>" : <i>[ <a href="entitydefinition.md">EntityDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#state" title="State">State</a>: <i>String</i>
<a href="#entity" title="Entity">Entity</a>: <i>
      - <a href="entitydefinition.md">EntityDefinition</a></i>
</pre>

## Properties

#### State

State of rule that will be defined in maintenance and can take either enabled or disabled for policy type rules. This field has to be disabled for integration type entity rules.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Entity

_Required_: No

_Type_: List of <a href="entitydefinition.md">EntityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

