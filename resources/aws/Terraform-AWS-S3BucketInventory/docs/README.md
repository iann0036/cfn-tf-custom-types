# Terraform::AWS::S3BucketInventory

Provides a S3 bucket [inventory configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-inventory.html) resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::S3BucketInventory",
    "Properties" : {
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>[ <a href="bucket.md">Bucket</a>, ... ]</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#includedobjectversions" title="IncludedObjectVersions">IncludedObjectVersions</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#optionalfields" title="OptionalFields">OptionalFields</a>" : <i>[ String, ... ]</i>,
        "<a href="#destination" title="Destination">Destination</a>" : <i>[ <a href="destination.md">Destination</a>, ... ]</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>[ <a href="filter.md">Filter</a>, ... ]</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>[ <a href="schedule.md">Schedule</a>, ... ]</i>,
        "<a href="#encryption" title="Encryption">Encryption</a>" : <i>[ <a href="encryption.md">Encryption</a>, ... ]</i>,
        "<a href="#ssekms" title="SseKms">SseKms</a>" : <i>[ <a href="ssekms.md">SseKms</a>, ... ]</i>,
        "<a href="#sses3" title="SseS3">SseS3</a>" : <i>[ <a href="sses3.md">SseS3</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::S3BucketInventory
Properties:
    <a href="#bucket" title="Bucket">Bucket</a>: <i>
      - <a href="bucket.md">Bucket</a></i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#includedobjectversions" title="IncludedObjectVersions">IncludedObjectVersions</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#optionalfields" title="OptionalFields">OptionalFields</a>: <i>
      - String</i>
    <a href="#destination" title="Destination">Destination</a>: <i>
      - <a href="destination.md">Destination</a></i>
    <a href="#filter" title="Filter">Filter</a>: <i>
      - <a href="filter.md">Filter</a></i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>
      - <a href="schedule.md">Schedule</a></i>
    <a href="#encryption" title="Encryption">Encryption</a>: <i>
      - <a href="encryption.md">Encryption</a></i>
    <a href="#ssekms" title="SseKms">SseKms</a>: <i>
      - <a href="ssekms.md">SseKms</a></i>
    <a href="#sses3" title="SseS3">SseS3</a>: <i>
      - <a href="sses3.md">SseS3</a></i>
</pre>

## Properties

#### Bucket

_Required_: Yes

_Type_: List of <a href="bucket.md">Bucket</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Specifies whether the inventory is enabled or disabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludedObjectVersions

Object versions to include in the inventory list. Valid values: `All`, `Current`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Unique identifier of the inventory configuration for the bucket.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptionalFields

List of optional fields that are included in the inventory results.
Valid values: `Size`, `LastModifiedDate`, `StorageClass`, `ETag`, `IsMultipartUploaded`, `ReplicationStatus`, `EncryptionStatus`, `ObjectLockRetainUntilDate`, `ObjectLockMode`, `ObjectLockLegalHoldStatus`, `IntelligentTieringAccessTier`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No

_Type_: List of <a href="destination.md">Destination</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: List of <a href="filter.md">Filter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No

_Type_: List of <a href="schedule.md">Schedule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encryption

_Required_: No

_Type_: List of <a href="encryption.md">Encryption</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SseKms

_Required_: No

_Type_: List of <a href="ssekms.md">SseKms</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SseS3

_Required_: No

_Type_: List of <a href="sses3.md">SseS3</a>

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

