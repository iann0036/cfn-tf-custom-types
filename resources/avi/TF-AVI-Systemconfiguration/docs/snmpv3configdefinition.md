# TF::AVI::Systemconfiguration SnmpV3ConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#engineid" title="EngineId">EngineId</a>" : <i>String</i>,
    "<a href="#user" title="User">User</a>" : <i>[ <a href="userdefinition.md">UserDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#engineid" title="EngineId">EngineId</a>: <i>String</i>
<a href="#user" title="User">User</a>: <i>
      - <a href="userdefinition.md">UserDefinition</a></i>
</pre>

## Properties

#### EngineId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

_Required_: No

_Type_: List of <a href="userdefinition.md">UserDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

