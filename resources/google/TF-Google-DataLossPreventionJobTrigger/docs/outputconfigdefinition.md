# TF::Google::DataLossPreventionJobTrigger OutputConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#outputschema" title="OutputSchema">OutputSchema</a>" : <i>String</i>,
    "<a href="#table" title="Table">Table</a>" : <i>[ <a href="tabledefinition.md">TableDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#outputschema" title="OutputSchema">OutputSchema</a>: <i>String</i>
<a href="#table" title="Table">Table</a>: <i>
      - <a href="tabledefinition.md">TableDefinition</a></i>
</pre>

## Properties

#### OutputSchema

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Table

_Required_: No

_Type_: List of <a href="tabledefinition.md">TableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

