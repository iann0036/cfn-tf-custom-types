# TF::OneLogin::Privileges

Manage Privilege resources.

This resource allows you to create and configure Privilege.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OneLogin::Privileges",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#roleids" title="RoleIds">RoleIds</a>" : <i>[ Double, ... ]</i>,
        "<a href="#userids" title="UserIds">UserIds</a>" : <i>[ Double, ... ]</i>,
        "<a href="#privilege" title="Privilege">Privilege</a>" : <i>[ <a href="privilegedefinition.md">PrivilegeDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OneLogin::Privileges
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#roleids" title="RoleIds">RoleIds</a>: <i>
      - Double</i>
    <a href="#userids" title="UserIds">UserIds</a>: <i>
      - Double</i>
    <a href="#privilege" title="Privilege">Privilege</a>: <i>
      - <a href="privilegedefinition.md">PrivilegeDefinition</a></i>
</pre>

## Properties

#### Description

Description for the Privilege.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the privilege.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleIds

A list of role IDs for whom the role applies.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserIds

A list of user IDs for whom the privilege applies.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Privilege

_Required_: No

_Type_: List of <a href="privilegedefinition.md">PrivilegeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

