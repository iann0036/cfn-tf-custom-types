# TF::Databricks::SqlPermissions PrivilegeAssignmentsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#principal" title="Principal">Principal</a>" : <i>String</i>,
    "<a href="#privileges" title="Privileges">Privileges</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#principal" title="Principal">Principal</a>: <i>String</i>
<a href="#privileges" title="Privileges">Privileges</a>: <i>
      - String</i>
</pre>

## Properties

#### Principal

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Privileges

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

