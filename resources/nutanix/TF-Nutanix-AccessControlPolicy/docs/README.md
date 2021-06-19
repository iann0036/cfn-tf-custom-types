# TF::Nutanix::AccessControlPolicy

Provides a resource to create an access control policy based on the input parameters.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Nutanix::AccessControlPolicy",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#categories" title="Categories">Categories</a>" : <i>[ <a href="categoriesdefinition.md">CategoriesDefinition</a>, ... ]</i>,
        "<a href="#contextfilterlist" title="ContextFilterList">ContextFilterList</a>" : <i>[ <a href="contextfilterlistdefinition.md">ContextFilterListDefinition</a>, ... ]</i>,
        "<a href="#ownerreference" title="OwnerReference">OwnerReference</a>" : <i>[ <a href="ownerreferencedefinition.md">OwnerReferenceDefinition</a>, ... ]</i>,
        "<a href="#rolereference" title="RoleReference">RoleReference</a>" : <i>[ <a href="rolereferencedefinition.md">RoleReferenceDefinition</a>, ... ]</i>,
        "<a href="#usergroupreferencelist" title="UserGroupReferenceList">UserGroupReferenceList</a>" : <i>[ <a href="usergroupreferencelistdefinition.md">UserGroupReferenceListDefinition</a>, ... ]</i>,
        "<a href="#userreferencelist" title="UserReferenceList">UserReferenceList</a>" : <i>[ <a href="userreferencelistdefinition.md">UserReferenceListDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Nutanix::AccessControlPolicy
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#categories" title="Categories">Categories</a>: <i>
      - <a href="categoriesdefinition.md">CategoriesDefinition</a></i>
    <a href="#contextfilterlist" title="ContextFilterList">ContextFilterList</a>: <i>
      - <a href="contextfilterlistdefinition.md">ContextFilterListDefinition</a></i>
    <a href="#ownerreference" title="OwnerReference">OwnerReference</a>: <i>
      - <a href="ownerreferencedefinition.md">OwnerReferenceDefinition</a></i>
    <a href="#rolereference" title="RoleReference">RoleReference</a>: <i>
      - <a href="rolereferencedefinition.md">RoleReferenceDefinition</a></i>
    <a href="#usergroupreferencelist" title="UserGroupReferenceList">UserGroupReferenceList</a>: <i>
      - <a href="usergroupreferencelistdefinition.md">UserGroupReferenceListDefinition</a></i>
    <a href="#userreferencelist" title="UserReferenceList">UserReferenceList</a>: <i>
      - <a href="userreferencelistdefinition.md">UserReferenceListDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Categories

_Required_: No

_Type_: List of <a href="categoriesdefinition.md">CategoriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContextFilterList

_Required_: No

_Type_: List of <a href="contextfilterlistdefinition.md">ContextFilterListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OwnerReference

_Required_: No

_Type_: List of <a href="ownerreferencedefinition.md">OwnerReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleReference

_Required_: No

_Type_: List of <a href="rolereferencedefinition.md">RoleReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserGroupReferenceList

_Required_: No

_Type_: List of <a href="usergroupreferencelistdefinition.md">UserGroupReferenceListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserReferenceList

_Required_: No

_Type_: List of <a href="userreferencelistdefinition.md">UserReferenceListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ApiVersion

Returns the <code>ApiVersion</code> value.

#### Id

Returns the <code>Id</code> value.

#### Metadata

Returns the <code>Metadata</code> value.

#### State

Returns the <code>State</code> value.

