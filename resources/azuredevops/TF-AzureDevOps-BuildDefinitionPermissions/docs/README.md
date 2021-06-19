# TF::AzureDevOps::BuildDefinitionPermissions

Manages permissions for a Build Definition

~> **Note** Permissions can be assigned to group principals and not to single user principals.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureDevOps::BuildDefinitionPermissions",
    "Properties" : {
        "<a href="#builddefinitionid" title="BuildDefinitionId">BuildDefinitionId</a>" : <i>String</i>,
        "<a href="#permissions" title="Permissions">Permissions</a>" : <i>[ <a href="permissionsdefinition.md">PermissionsDefinition</a>, ... ]</i>,
        "<a href="#principal" title="Principal">Principal</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#replace" title="Replace">Replace</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureDevOps::BuildDefinitionPermissions
Properties:
    <a href="#builddefinitionid" title="BuildDefinitionId">BuildDefinitionId</a>: <i>String</i>
    <a href="#permissions" title="Permissions">Permissions</a>: <i>
      - <a href="permissionsdefinition.md">PermissionsDefinition</a></i>
    <a href="#principal" title="Principal">Principal</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#replace" title="Replace">Replace</a>: <i>Boolean</i>
</pre>

## Properties

#### BuildDefinitionId

The id of the build definition to assign the permissions.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permissions

the permissions to assign. The following permissions are available.

_Required_: Yes

_Type_: List of <a href="permissionsdefinition.md">PermissionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Principal

The **group** principal to assign the permissions.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The ID of the project to assign the permissions.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Replace

Replace (`true`) or merge (`false`) the permissions. Default: `true`.

_Required_: No

_Type_: Boolean

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

