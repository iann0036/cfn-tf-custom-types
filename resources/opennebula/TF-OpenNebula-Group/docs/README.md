# TF::OpenNebula::Group

Provides an OpenNebula group resource.

This resource allows you to manage groups on your OpenNebula clusters. When applied,
a new group is created. When destroyed, it is removed.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OpenNebula::Group",
    "Properties" : {
        "<a href="#admins" title="Admins">Admins</a>" : <i>[ Double, ... ]</i>,
        "<a href="#deleteondestruction" title="DeleteOnDestruction">DeleteOnDestruction</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#users" title="Users">Users</a>" : <i>[ Double, ... ]</i>,
        "<a href="#quotas" title="Quotas">Quotas</a>" : <i>[ <a href="quotasdefinition.md">QuotasDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OpenNebula::Group
Properties:
    <a href="#admins" title="Admins">Admins</a>: <i>
      - Double</i>
    <a href="#deleteondestruction" title="DeleteOnDestruction">DeleteOnDestruction</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#users" title="Users">Users</a>: <i>
      - Double</i>
    <a href="#quotas" title="Quotas">Quotas</a>: <i>
      - <a href="quotasdefinition.md">QuotasDefinition</a></i>
</pre>

## Properties

#### Admins

List of Administrator user IDs part of the group.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteOnDestruction

Flag to delete the group on destruction. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

Group template content in OpenNebula XML or String format. Used to provide SUSNTONE arguments.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Users

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Quotas

_Required_: No

_Type_: List of <a href="quotasdefinition.md">QuotasDefinition</a>

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

