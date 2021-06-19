# TF::Alicloud::OssBucket

Provides a resource to create a oss bucket and set its attribution.

-> **NOTE:** The bucket namespace is shared by all users of the OSS system. Please set bucket name as unique as possible.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::OssBucket",
    "Properties" : {
        "<a href="#acl" title="Acl">Acl</a>" : <i>String</i>,
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>" : <i>Boolean</i>,
        "<a href="#loggingisenable" title="LoggingIsenable">LoggingIsenable</a>" : <i>Boolean</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#redundancytype" title="RedundancyType">RedundancyType</a>" : <i>String</i>,
        "<a href="#storageclass" title="StorageClass">StorageClass</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#corsrule" title="CorsRule">CorsRule</a>" : <i>[ <a href="corsruledefinition.md">CorsRuleDefinition</a>, ... ]</i>,
        "<a href="#lifecyclerule" title="LifecycleRule">LifecycleRule</a>" : <i>[ <a href="lifecycleruledefinition.md">LifecycleRuleDefinition</a>, ... ]</i>,
        "<a href="#logging" title="Logging">Logging</a>" : <i>[ <a href="loggingdefinition.md">LoggingDefinition</a>, ... ]</i>,
        "<a href="#refererconfig" title="RefererConfig">RefererConfig</a>" : <i>[ <a href="refererconfigdefinition.md">RefererConfigDefinition</a>, ... ]</i>,
        "<a href="#serversideencryptionrule" title="ServerSideEncryptionRule">ServerSideEncryptionRule</a>" : <i>[ <a href="serversideencryptionruledefinition.md">ServerSideEncryptionRuleDefinition</a>, ... ]</i>,
        "<a href="#transferacceleration" title="TransferAcceleration">TransferAcceleration</a>" : <i>[ <a href="transferaccelerationdefinition.md">TransferAccelerationDefinition</a>, ... ]</i>,
        "<a href="#versioning" title="Versioning">Versioning</a>" : <i>[ <a href="versioningdefinition.md">VersioningDefinition</a>, ... ]</i>,
        "<a href="#website" title="Website">Website</a>" : <i>[ <a href="websitedefinition.md">WebsiteDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::OssBucket
Properties:
    <a href="#acl" title="Acl">Acl</a>: <i>String</i>
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>: <i>Boolean</i>
    <a href="#loggingisenable" title="LoggingIsenable">LoggingIsenable</a>: <i>Boolean</i>
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#redundancytype" title="RedundancyType">RedundancyType</a>: <i>String</i>
    <a href="#storageclass" title="StorageClass">StorageClass</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#corsrule" title="CorsRule">CorsRule</a>: <i>
      - <a href="corsruledefinition.md">CorsRuleDefinition</a></i>
    <a href="#lifecyclerule" title="LifecycleRule">LifecycleRule</a>: <i>
      - <a href="lifecycleruledefinition.md">LifecycleRuleDefinition</a></i>
    <a href="#logging" title="Logging">Logging</a>: <i>
      - <a href="loggingdefinition.md">LoggingDefinition</a></i>
    <a href="#refererconfig" title="RefererConfig">RefererConfig</a>: <i>
      - <a href="refererconfigdefinition.md">RefererConfigDefinition</a></i>
    <a href="#serversideencryptionrule" title="ServerSideEncryptionRule">ServerSideEncryptionRule</a>: <i>
      - <a href="serversideencryptionruledefinition.md">ServerSideEncryptionRuleDefinition</a></i>
    <a href="#transferacceleration" title="TransferAcceleration">TransferAcceleration</a>: <i>
      - <a href="transferaccelerationdefinition.md">TransferAccelerationDefinition</a></i>
    <a href="#versioning" title="Versioning">Versioning</a>: <i>
      - <a href="versioningdefinition.md">VersioningDefinition</a></i>
    <a href="#website" title="Website">Website</a>: <i>
      - <a href="websitedefinition.md">WebsiteDefinition</a></i>
</pre>

## Properties

#### Acl

The [canned ACL](https://www.alibabacloud.com/help/doc-detail/31898.htm) to apply. Can be "private", "public-read" and "public-read-write". Defaults to "private".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bucket

The name of the bucket. If omitted, Terraform will assign a random and unique name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDestroy

A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. These objects are not recoverable. Defaults to "false".

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingIsenable

The flag of using logging enable container. Defaults true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

Json format text of bucket policy [bucket policy management](https://www.alibabacloud.com/help/doc-detail/100680.htm).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedundancyType

The [redundancy type](https://www.alibabacloud.com/help/doc-detail/90589.htm) to enable. Can be "LRS", and "ZRS". Defaults to "LRS".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageClass

The [storage class](https://www.alibabacloud.com/help/doc-detail/51374.htm) to apply. Can be "Standard", "IA" and "Archive". Defaults to "Standard".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the bucket. The items are no more than 10 for a bucket.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorsRule

_Required_: No

_Type_: List of <a href="corsruledefinition.md">CorsRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifecycleRule

_Required_: No

_Type_: List of <a href="lifecycleruledefinition.md">LifecycleRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logging

_Required_: No

_Type_: List of <a href="loggingdefinition.md">LoggingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RefererConfig

_Required_: No

_Type_: List of <a href="refererconfigdefinition.md">RefererConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSideEncryptionRule

_Required_: No

_Type_: List of <a href="serversideencryptionruledefinition.md">ServerSideEncryptionRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransferAcceleration

_Required_: No

_Type_: List of <a href="transferaccelerationdefinition.md">TransferAccelerationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Versioning

_Required_: No

_Type_: List of <a href="versioningdefinition.md">VersioningDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Website

_Required_: No

_Type_: List of <a href="websitedefinition.md">WebsiteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreationDate

Returns the <code>CreationDate</code> value.

#### ExtranetEndpoint

Returns the <code>ExtranetEndpoint</code> value.

#### Id

Returns the <code>Id</code> value.

#### IntranetEndpoint

Returns the <code>IntranetEndpoint</code> value.

#### Location

Returns the <code>Location</code> value.

#### Owner

Returns the <code>Owner</code> value.

