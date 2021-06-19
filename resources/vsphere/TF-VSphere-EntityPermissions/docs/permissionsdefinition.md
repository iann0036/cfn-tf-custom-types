# TF::VSphere::EntityPermissions PermissionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#isgroup" title="IsGroup">IsGroup</a>" : <i>Boolean</i>,
    "<a href="#propagate" title="Propagate">Propagate</a>" : <i>Boolean</i>,
    "<a href="#roleid" title="RoleId">RoleId</a>" : <i>String</i>,
    "<a href="#userorgroup" title="UserOrGroup">UserOrGroup</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#isgroup" title="IsGroup">IsGroup</a>: <i>Boolean</i>
<a href="#propagate" title="Propagate">Propagate</a>: <i>Boolean</i>
<a href="#roleid" title="RoleId">RoleId</a>: <i>String</i>
<a href="#userorgroup" title="UserOrGroup">UserOrGroup</a>: <i>String</i>
</pre>

## Properties

#### IsGroup

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Propagate

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserOrGroup

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

