# TF::MongoDBAtlas::CustomDbRole

`mongodbatlas_custom_db_role` provides a Custom DB Role resource. The customDBRoles resource lets you retrieve, create and modify the custom MongoDB roles in your cluster. Use custom MongoDB roles to specify custom sets of actions which cannot be described by the built-in Atlas database user privileges.

-> **IMPORTANT** Custom roles cannot use actions unavailable to any cluster version in your project. Custom roles are defined at the project level, and must be compatible with each MongoDB version used by your project’s clusters. If you have a cluster in your project with MongoDB 3.4, you cannot create a custom role that uses actions introduced in MongoDB 3.6, such as useUUID.


-> **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MongoDBAtlas::CustomDbRole",
    "Properties" : {
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#rolename" title="RoleName">RoleName</a>" : <i>String</i>,
        "<a href="#actions" title="Actions">Actions</a>" : <i>[ <a href="actionsdefinition.md">ActionsDefinition</a>, ... ]</i>,
        "<a href="#inheritedroles" title="InheritedRoles">InheritedRoles</a>" : <i>[ <a href="inheritedrolesdefinition.md">InheritedRolesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MongoDBAtlas::CustomDbRole
Properties:
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#rolename" title="RoleName">RoleName</a>: <i>String</i>
    <a href="#actions" title="Actions">Actions</a>: <i>
      - <a href="actionsdefinition.md">ActionsDefinition</a></i>
    <a href="#inheritedroles" title="InheritedRoles">InheritedRoles</a>: <i>
      - <a href="inheritedrolesdefinition.md">InheritedRolesDefinition</a></i>
</pre>

## Properties

#### ProjectId

The unique ID for the project to create the database user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleName

Name of the custom role.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Actions

_Required_: No

_Type_: List of <a href="actionsdefinition.md">ActionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InheritedRoles

_Required_: No

_Type_: List of <a href="inheritedrolesdefinition.md">InheritedRolesDefinition</a>

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

