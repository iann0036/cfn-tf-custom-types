# Terraform::Brightbox::OrbitContainer

Provides a Brightbox Orbit Container resource. This can be used to create,
modify, and delete Containers in Orbit.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Brightbox::OrbitContainer",
    "Properties" : {
        "<a href="#containerread" title="ContainerRead">ContainerRead</a>" : <i>[ String, ... ]</i>,
        "<a href="#containersynckey" title="ContainerSyncKey">ContainerSyncKey</a>" : <i>String</i>,
        "<a href="#containersyncto" title="ContainerSyncTo">ContainerSyncTo</a>" : <i>String</i>,
        "<a href="#containerwrite" title="ContainerWrite">ContainerWrite</a>" : <i>[ String, ... ]</i>,
        "<a href="#historylocation" title="HistoryLocation">HistoryLocation</a>" : <i>String</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadata.md">Metadata</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#versionslocation" title="VersionsLocation">VersionsLocation</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Brightbox::OrbitContainer
Properties:
    <a href="#containerread" title="ContainerRead">ContainerRead</a>: <i>
      - String</i>
    <a href="#containersynckey" title="ContainerSyncKey">ContainerSyncKey</a>: <i>String</i>
    <a href="#containersyncto" title="ContainerSyncTo">ContainerSyncTo</a>: <i>String</i>
    <a href="#containerwrite" title="ContainerWrite">ContainerWrite</a>: <i>
      - String</i>
    <a href="#historylocation" title="HistoryLocation">HistoryLocation</a>: <i>String</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadata.md">Metadata</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#versionslocation" title="VersionsLocation">VersionsLocation</a>: <i>String</i>
</pre>

## Properties

#### ContainerRead

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerSyncKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerSyncTo

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerWrite

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HistoryLocation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

A dictionary of metadata key/value items. The key must be in lower case with no underscores or spaces.

_Required_: No

_Type_: List of <a href="metadata.md">Metadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A label assigned to the Orbit container.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionsLocation

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

#### BytesUsed

Returns the <code>BytesUsed</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Id

Returns the <code>Id</code> value.

#### ObjectCount

Returns the <code>ObjectCount</code> value.

#### StoragePolicy

Returns the <code>StoragePolicy</code> value.

