# TF::OneLogin::Privileges PrivilegeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#version" title="Version">Version</a>" : <i>String</i>,
    "<a href="#statement" title="Statement">Statement</a>" : <i>[ <a href="statementdefinition.md">StatementDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#version" title="Version">Version</a>: <i>String</i>
<a href="#statement" title="Statement">Statement</a>: <i>
      - <a href="statementdefinition.md">StatementDefinition</a></i>
</pre>

## Properties

#### Version

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Statement

_Required_: No

_Type_: List of <a href="statementdefinition.md">StatementDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

