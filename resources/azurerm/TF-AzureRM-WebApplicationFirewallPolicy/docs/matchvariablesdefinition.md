# TF::AzureRM::WebApplicationFirewallPolicy MatchVariablesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#selector" title="Selector">Selector</a>" : <i>String</i>,
    "<a href="#variablename" title="VariableName">VariableName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#selector" title="Selector">Selector</a>: <i>String</i>
<a href="#variablename" title="VariableName">VariableName</a>: <i>String</i>
</pre>

## Properties

#### Selector

Describes field of the matchVariable collection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VariableName

The name of the Match Variable.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

