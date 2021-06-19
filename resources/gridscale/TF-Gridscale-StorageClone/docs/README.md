# TF::Gridscale::StorageClone

Clone a storage instance. This can be used to create, modify, and delete the storage clones.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Gridscale::StorageClone",
    "Properties" : {
        "<a href="#capacity" title="Capacity">Capacity</a>" : <i>Double</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#sourcestorageid" title="SourceStorageId">SourceStorageId</a>" : <i>String</i>,
        "<a href="#storagetype" title="StorageType">StorageType</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Gridscale::StorageClone
Properties:
    <a href="#capacity" title="Capacity">Capacity</a>: <i>Double</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#sourcestorageid" title="SourceStorageId">SourceStorageId</a>: <i>String</i>
    <a href="#storagetype" title="StorageType">StorageType</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Capacity

The default value is inherited from the source storage instance. A desired capacity is possible. Required (integer - minimum: 1 - maximum: 4096).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

List of labels in the format [ "label1", "label2" ].

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The default value is inherited from the source storage instance. A desired name is possible. The human-readable name of the object. It supports the full UTF-8 character set, with a maximum of 64 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceStorageId

The ID of a storage instance which will be cloned.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageType

The default value is inherited from the source storage instance. A desired storage type is possible. (one of storage, storage_high, storage_insane).

_Required_: No

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

#### ChangeTime

Returns the <code>ChangeTime</code> value.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### CurrentPrice

Returns the <code>CurrentPrice</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastUsedTemplate

Returns the <code>LastUsedTemplate</code> value.

#### LicenseProductNo

Returns the <code>LicenseProductNo</code> value.

#### LocationCountry

Returns the <code>LocationCountry</code> value.

#### LocationIata

Returns the <code>LocationIata</code> value.

#### LocationName

Returns the <code>LocationName</code> value.

#### LocationUuid

Returns the <code>LocationUuid</code> value.

#### ParentUuid

Returns the <code>ParentUuid</code> value.

#### Status

Returns the <code>Status</code> value.

#### UsageInMinutes

Returns the <code>UsageInMinutes</code> value.

