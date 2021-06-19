# TF::OpenNebula::VirtualMachineGroup

Provides an OpenNebula virtual machine group resource.

This resource allows you to manage virtual machine groups on your OpenNebula clusters. When applied,
a new virtual machine group is created. When destroyed, this virtual machine group is removed.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OpenNebula::VirtualMachineGroup",
    "Properties" : {
        "<a href="#group" title="Group">Group</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#permissions" title="Permissions">Permissions</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#role" title="Role">Role</a>" : <i>[ <a href="roledefinition.md">RoleDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OpenNebula::VirtualMachineGroup
Properties:
    <a href="#group" title="Group">Group</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#permissions" title="Permissions">Permissions</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#role" title="Role">Role</a>: <i>
      - <a href="roledefinition.md">RoleDefinition</a></i>
</pre>

## Properties

#### Group

Name of the group which owns the virtual machine group. Defaults to the caller primary group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the virtual machine group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permissions

Permissions applied on virtual machine group. Defaults to the UMASK in OpenNebula (in UNIX Format: owner-group-other => Use-Manage-Admin.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Virtual Machine group tags.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

_Required_: No

_Type_: List of <a href="roledefinition.md">RoleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Gid

Returns the <code>Gid</code> value.

#### Gname

Returns the <code>Gname</code> value.

#### Id

Returns the <code>Id</code> value.

#### Uid

Returns the <code>Uid</code> value.

#### Uname

Returns the <code>Uname</code> value.

