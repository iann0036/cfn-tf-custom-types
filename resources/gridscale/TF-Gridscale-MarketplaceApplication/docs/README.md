# TF::Gridscale::MarketplaceApplication

Provides a marketplace application resource. This can be used to create, modify, and delete marketplace applications.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Gridscale::MarketplaceApplication",
    "Properties" : {
        "<a href="#category" title="Category">Category</a>" : <i>String</i>,
        "<a href="#metaadvices" title="MetaAdvices">MetaAdvices</a>" : <i>String</i>,
        "<a href="#metaauthor" title="MetaAuthor">MetaAuthor</a>" : <i>String</i>,
        "<a href="#metacomponents" title="MetaComponents">MetaComponents</a>" : <i>[ String, ... ]</i>,
        "<a href="#metafeatures" title="MetaFeatures">MetaFeatures</a>" : <i>String</i>,
        "<a href="#metahints" title="MetaHints">MetaHints</a>" : <i>String</i>,
        "<a href="#metaicon" title="MetaIcon">MetaIcon</a>" : <i>String</i>,
        "<a href="#metalicense" title="MetaLicense">MetaLicense</a>" : <i>String</i>,
        "<a href="#metaos" title="MetaOs">MetaOs</a>" : <i>String</i>,
        "<a href="#metaoverview" title="MetaOverview">MetaOverview</a>" : <i>String</i>,
        "<a href="#metatermsofuse" title="MetaTermsOfUse">MetaTermsOfUse</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#objectstoragepath" title="ObjectStoragePath">ObjectStoragePath</a>" : <i>String</i>,
        "<a href="#publish" title="Publish">Publish</a>" : <i>Boolean</i>,
        "<a href="#setupcores" title="SetupCores">SetupCores</a>" : <i>Double</i>,
        "<a href="#setupmemory" title="SetupMemory">SetupMemory</a>" : <i>Double</i>,
        "<a href="#setupstoragecapacity" title="SetupStorageCapacity">SetupStorageCapacity</a>" : <i>Double</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Gridscale::MarketplaceApplication
Properties:
    <a href="#category" title="Category">Category</a>: <i>String</i>
    <a href="#metaadvices" title="MetaAdvices">MetaAdvices</a>: <i>String</i>
    <a href="#metaauthor" title="MetaAuthor">MetaAuthor</a>: <i>String</i>
    <a href="#metacomponents" title="MetaComponents">MetaComponents</a>: <i>
      - String</i>
    <a href="#metafeatures" title="MetaFeatures">MetaFeatures</a>: <i>String</i>
    <a href="#metahints" title="MetaHints">MetaHints</a>: <i>String</i>
    <a href="#metaicon" title="MetaIcon">MetaIcon</a>: <i>String</i>
    <a href="#metalicense" title="MetaLicense">MetaLicense</a>: <i>String</i>
    <a href="#metaos" title="MetaOs">MetaOs</a>: <i>String</i>
    <a href="#metaoverview" title="MetaOverview">MetaOverview</a>: <i>String</i>
    <a href="#metatermsofuse" title="MetaTermsOfUse">MetaTermsOfUse</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#objectstoragepath" title="ObjectStoragePath">ObjectStoragePath</a>: <i>String</i>
    <a href="#publish" title="Publish">Publish</a>: <i>Boolean</i>
    <a href="#setupcores" title="SetupCores">SetupCores</a>: <i>Double</i>
    <a href="#setupmemory" title="SetupMemory">SetupMemory</a>: <i>Double</i>
    <a href="#setupstoragecapacity" title="SetupStorageCapacity">SetupStorageCapacity</a>: <i>Double</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Category

Category of marketplace application. Accepted values: "CMS", "project management", "Adminpanel", "Collaboration", "Cloud Storage", "Archiving".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetaAdvices

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetaAuthor

Author.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetaComponents

Components (e.g: MySql, Apache, etc.).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetaFeatures

List of functions.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetaHints

Hints.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetaIcon

base64 encoded image of the icon.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetaLicense

License number.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetaOs

Operating system.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetaOverview

Describes the main function of the application.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetaTermsOfUse

Terms of use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The human-readable name of the object. It supports the full UTF-8 character set, with a maximum of 64 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectStoragePath

Path to the images for the application, must be in .gz format and started with s3//.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Publish

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetupCores

Number of server's cores.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetupMemory

The capacity of server's memory in GB.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetupStorageCapacity

The capacity of server's storage in GB.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ChangeTime

Returns the <code>ChangeTime</code> value.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### IsApplicationOwner

Returns the <code>IsApplicationOwner</code> value.

#### IsPublishGlobal

Returns the <code>IsPublishGlobal</code> value.

#### IsPublishGlobalRequested

Returns the <code>IsPublishGlobalRequested</code> value.

#### IsPublishRequested

Returns the <code>IsPublishRequested</code> value.

#### IsPublished

Returns the <code>IsPublished</code> value.

#### PublishGlobalRequestedDate

Returns the <code>PublishGlobalRequestedDate</code> value.

#### PublishRequestedDate

Returns the <code>PublishRequestedDate</code> value.

#### PublishedDate

Returns the <code>PublishedDate</code> value.

#### PublishedGlobalDate

Returns the <code>PublishedGlobalDate</code> value.

#### Status

Returns the <code>Status</code> value.

#### Type

Returns the <code>Type</code> value.

#### UniqueHash

Returns the <code>UniqueHash</code> value.

