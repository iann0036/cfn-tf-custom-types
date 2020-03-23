# Terraform::AWS::S3Bucket Destination

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
    "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
    "<a href="#replicakmskeyid" title="ReplicaKmsKeyId">ReplicaKmsKeyId</a>" : <i>String</i>,
    "<a href="#storageclass" title="StorageClass">StorageClass</a>" : <i>String</i>,
    "<a href="#accesscontroltranslation" title="AccessControlTranslation">AccessControlTranslation</a>" : <i>[ <a href="destination-accesscontroltranslation.md">AccessControlTranslation</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
<a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
<a href="#replicakmskeyid" title="ReplicaKmsKeyId">ReplicaKmsKeyId</a>: <i>String</i>
<a href="#storageclass" title="StorageClass">StorageClass</a>: <i>String</i>
<a href="#accesscontroltranslation" title="AccessControlTranslation">AccessControlTranslation</a>: <i>
      - <a href="destination-accesscontroltranslation.md">AccessControlTranslation</a></i>
</pre>

## Properties

#### AccountId

The Account ID to use for overriding the object owner on replication. Must be used in conjunction with `access_control_translation` override configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bucket

The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicaKmsKeyId

Destination KMS encryption key ARN for SSE-KMS replication. Must be used in conjunction with
`sse_kms_encrypted_objects` source selection criteria.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageClass

The class of storage used to store the object. Can be `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `GLACIER`, or `DEEP_ARCHIVE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessControlTranslation

_Required_: No

_Type_: List of <a href="destination-accesscontroltranslation.md">AccessControlTranslation</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

