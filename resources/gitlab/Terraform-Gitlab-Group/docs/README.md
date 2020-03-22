# Terraform::Gitlab::Group

This resource allows you to create and manage GitLab groups.
Note your provider will need to be configured with admin-level access for this resource to work.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Gitlab::Group",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#lfsenabled" title="LfsEnabled">LfsEnabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#parentid" title="ParentId">ParentId</a>" : <i>Double</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
        "<a href="#requestaccessenabled" title="RequestAccessEnabled">RequestAccessEnabled</a>" : <i>Boolean</i>,
        "<a href="#visibilitylevel" title="VisibilityLevel">VisibilityLevel</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Gitlab::Group
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#lfsenabled" title="LfsEnabled">LfsEnabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#parentid" title="ParentId">ParentId</a>: <i>Double</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
    <a href="#requestaccessenabled" title="RequestAccessEnabled">RequestAccessEnabled</a>: <i>Boolean</i>
    <a href="#visibilitylevel" title="VisibilityLevel">VisibilityLevel</a>: <i>String</i>
</pre>

## Properties

#### Description

The description of the group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LfsEnabled

Boolean, defaults to true.  Whether to enable LFS
support for projects in this group.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of this group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParentId

Integer, id of the parent group (creates a nested group).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

The path of the group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestAccessEnabled

Boolean, defaults to false.  Whether to
enable users to request access to the group.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VisibilityLevel

Set to `public` to create a public group.
Valid values are `private`, `internal`, `public`.
Groups are created as private by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### FullName

Returns the <code>FullName</code> value.

#### FullPath

Returns the <code>FullPath</code> value.

#### Id

Returns the <code>Id</code> value.

#### RunnersToken

Returns the <code>RunnersToken</code> value.

#### WebUrl

Returns the <code>WebUrl</code> value.

