# TF::Panos::PanoramaSnmptrapServerProfile V3ServerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authpassword" title="AuthPassword">AuthPassword</a>" : <i>String</i>,
    "<a href="#engineid" title="EngineId">EngineId</a>" : <i>String</i>,
    "<a href="#manager" title="Manager">Manager</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#privpassword" title="PrivPassword">PrivPassword</a>" : <i>String</i>,
    "<a href="#user" title="User">User</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#authpassword" title="AuthPassword">AuthPassword</a>: <i>String</i>
<a href="#engineid" title="EngineId">EngineId</a>: <i>String</i>
<a href="#manager" title="Manager">Manager</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#privpassword" title="PrivPassword">PrivPassword</a>: <i>String</i>
<a href="#user" title="User">User</a>: <i>String</i>
</pre>

## Properties

#### AuthPassword

SNMP auth password.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngineId

The engine ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Manager

The hostname.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The server name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivPassword

SNMP priv password.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

Username.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

