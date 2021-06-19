# TF::Nutanix::User

Provides a resource to create a user based on the input parameters.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Nutanix::User",
    "Properties" : {
        "<a href="#ownerreference" title="OwnerReference">OwnerReference</a>" : <i>[ <a href="ownerreferencedefinition.md">OwnerReferenceDefinition</a>, ... ]</i>,
        "<a href="#projectreference" title="ProjectReference">ProjectReference</a>" : <i>[ <a href="projectreferencedefinition.md">ProjectReferenceDefinition</a>, ... ]</i>,
        "<a href="#categories" title="Categories">Categories</a>" : <i>[ <a href="categoriesdefinition.md">CategoriesDefinition</a>, ... ]</i>,
        "<a href="#directoryserviceuser" title="DirectoryServiceUser">DirectoryServiceUser</a>" : <i>[ <a href="directoryserviceuserdefinition.md">DirectoryServiceUserDefinition</a>, ... ]</i>,
        "<a href="#identityprovideruser" title="IdentityProviderUser">IdentityProviderUser</a>" : <i>[ <a href="identityprovideruserdefinition.md">IdentityProviderUserDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Nutanix::User
Properties:
    <a href="#ownerreference" title="OwnerReference">OwnerReference</a>: <i>
      - <a href="ownerreferencedefinition.md">OwnerReferenceDefinition</a></i>
    <a href="#projectreference" title="ProjectReference">ProjectReference</a>: <i>
      - <a href="projectreferencedefinition.md">ProjectReferenceDefinition</a></i>
    <a href="#categories" title="Categories">Categories</a>: <i>
      - <a href="categoriesdefinition.md">CategoriesDefinition</a></i>
    <a href="#directoryserviceuser" title="DirectoryServiceUser">DirectoryServiceUser</a>: <i>
      - <a href="directoryserviceuserdefinition.md">DirectoryServiceUserDefinition</a></i>
    <a href="#identityprovideruser" title="IdentityProviderUser">IdentityProviderUser</a>: <i>
      - <a href="identityprovideruserdefinition.md">IdentityProviderUserDefinition</a></i>
</pre>

## Properties

#### OwnerReference

_Required_: No

_Type_: List of <a href="ownerreferencedefinition.md">OwnerReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectReference

_Required_: No

_Type_: List of <a href="projectreferencedefinition.md">ProjectReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Categories

_Required_: No

_Type_: List of <a href="categoriesdefinition.md">CategoriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectoryServiceUser

_Required_: No

_Type_: List of <a href="directoryserviceuserdefinition.md">DirectoryServiceUserDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdentityProviderUser

_Required_: No

_Type_: List of <a href="identityprovideruserdefinition.md">IdentityProviderUserDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AccessControlPolicyReferenceList

Returns the <code>AccessControlPolicyReferenceList</code> value.

#### ApiVersion

Returns the <code>ApiVersion</code> value.

#### DisplayName

Returns the <code>DisplayName</code> value.

#### Id

Returns the <code>Id</code> value.

#### Metadata

Returns the <code>Metadata</code> value.

#### Name

Returns the <code>Name</code> value.

#### ProjectReferenceList

Returns the <code>ProjectReferenceList</code> value.

#### State

Returns the <code>State</code> value.

#### UserType

Returns the <code>UserType</code> value.

