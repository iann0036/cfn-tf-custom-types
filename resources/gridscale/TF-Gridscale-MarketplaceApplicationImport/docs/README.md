# TF::Gridscale::MarketplaceApplicationImport

Provides an imported marketplace application resource. This can be used to import marketplace applications, and delete imported marketplace applications.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Gridscale::MarketplaceApplicationImport",
    "Properties" : {
        "<a href="#importuniquehash" title="ImportUniqueHash">ImportUniqueHash</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Gridscale::MarketplaceApplicationImport
Properties:
    <a href="#importuniquehash" title="ImportUniqueHash">ImportUniqueHash</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ImportUniqueHash

Hash of a specific marketplace application that you want to import. A change of this argument necessitates the re-creation of the resource.

_Required_: Yes

_Type_: String

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

#### Category

Returns the <code>Category</code> value.

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

#### MetaAdvices

Returns the <code>MetaAdvices</code> value.

#### MetaAuthor

Returns the <code>MetaAuthor</code> value.

#### MetaComponents

Returns the <code>MetaComponents</code> value.

#### MetaFeatures

Returns the <code>MetaFeatures</code> value.

#### MetaHints

Returns the <code>MetaHints</code> value.

#### MetaIcon

Returns the <code>MetaIcon</code> value.

#### MetaLicense

Returns the <code>MetaLicense</code> value.

#### MetaOs

Returns the <code>MetaOs</code> value.

#### MetaOverview

Returns the <code>MetaOverview</code> value.

#### MetaTermsOfUse

Returns the <code>MetaTermsOfUse</code> value.

#### Name

Returns the <code>Name</code> value.

#### ObjectStoragePath

Returns the <code>ObjectStoragePath</code> value.

#### PublishGlobalRequestedDate

Returns the <code>PublishGlobalRequestedDate</code> value.

#### PublishRequestedDate

Returns the <code>PublishRequestedDate</code> value.

#### PublishedDate

Returns the <code>PublishedDate</code> value.

#### PublishedGlobalDate

Returns the <code>PublishedGlobalDate</code> value.

#### SetupCores

Returns the <code>SetupCores</code> value.

#### SetupMemory

Returns the <code>SetupMemory</code> value.

#### SetupStorageCapacity

Returns the <code>SetupStorageCapacity</code> value.

#### Status

Returns the <code>Status</code> value.

#### Type

Returns the <code>Type</code> value.

#### UniqueHash

Returns the <code>UniqueHash</code> value.

