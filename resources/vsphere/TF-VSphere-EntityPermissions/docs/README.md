# TF::VSphere::EntityPermissions

The `vsphere_entity_permissions` resource can be used to create and manage entity permissions. 
Permissions can be created on an entity for a given user or group with the specified role.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VSphere::EntityPermissions",
    "Properties" : {
        "<a href="#entityid" title="EntityId">EntityId</a>" : <i>String</i>,
        "<a href="#entitytype" title="EntityType">EntityType</a>" : <i>String</i>,
        "<a href="#permissions" title="Permissions">Permissions</a>" : <i>[ <a href="permissionsdefinition.md">PermissionsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VSphere::EntityPermissions
Properties:
    <a href="#entityid" title="EntityId">EntityId</a>: <i>String</i>
    <a href="#entitytype" title="EntityType">EntityType</a>: <i>String</i>
    <a href="#permissions" title="Permissions">Permissions</a>: <i>
      - <a href="permissionsdefinition.md">PermissionsDefinition</a></i>
</pre>

## Properties

#### EntityId

The managed object id (uuid for some entities) on which permissions are to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EntityType

The managed object type, types can be found in the managed object type section
[here](https://code.vmware.com/apis/968/vsphere).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permissions

_Required_: No

_Type_: List of <a href="permissionsdefinition.md">PermissionsDefinition</a>

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

