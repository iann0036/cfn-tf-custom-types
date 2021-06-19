# TF::Google::BigqueryJob StatusDefinition3

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#errorresult" title="ErrorResult">ErrorResult</a>" : <i>[ <a href="statusdefinition.md">StatusDefinition</a>, ... ]</i>,
    "<a href="#errors" title="Errors">Errors</a>" : <i>[ <a href="statusdefinition2.md">StatusDefinition2</a>, ... ]</i>,
    "<a href="#state" title="State">State</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#errorresult" title="ErrorResult">ErrorResult</a>: <i>
      - <a href="statusdefinition.md">StatusDefinition</a></i>
<a href="#errors" title="Errors">Errors</a>: <i>
      - <a href="statusdefinition2.md">StatusDefinition2</a></i>
<a href="#state" title="State">State</a>: <i>String</i>
</pre>

## Properties

#### ErrorResult

_Required_: No

_Type_: List of <a href="statusdefinition.md">StatusDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Errors

_Required_: No

_Type_: List of <a href="statusdefinition2.md">StatusDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

