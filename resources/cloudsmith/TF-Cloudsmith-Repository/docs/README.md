# TF::Cloudsmith::Repository

CloudFormation equivalent of cloudsmith_repository

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Cloudsmith::Repository",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#indexfiles" title="IndexFiles">IndexFiles</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#repositorytype" title="RepositoryType">RepositoryType</a>" : <i>String</i>,
        "<a href="#slug" title="Slug">Slug</a>" : <i>String</i>,
        "<a href="#storageregion" title="StorageRegion">StorageRegion</a>" : <i>String</i>,
        "<a href="#waitfordeletion" title="WaitForDeletion">WaitForDeletion</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Cloudsmith::Repository
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#indexfiles" title="IndexFiles">IndexFiles</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#repositorytype" title="RepositoryType">RepositoryType</a>: <i>String</i>
    <a href="#slug" title="Slug">Slug</a>: <i>String</i>
    <a href="#storageregion" title="StorageRegion">StorageRegion</a>: <i>String</i>
    <a href="#waitfordeletion" title="WaitForDeletion">WaitForDeletion</a>: <i>Boolean</i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndexFiles

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepositoryType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slug

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageRegion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForDeletion

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

#### CdnUrl

Returns the <code>CdnUrl</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### DeletedAt

Returns the <code>DeletedAt</code> value.

#### Id

Returns the <code>Id</code> value.

#### NamespaceUrl

Returns the <code>NamespaceUrl</code> value.

#### SelfHtmlUrl

Returns the <code>SelfHtmlUrl</code> value.

#### SelfUrl

Returns the <code>SelfUrl</code> value.

#### SlugPerm

Returns the <code>SlugPerm</code> value.

