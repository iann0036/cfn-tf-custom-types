# Terraform::AWS::S3Bucket ReplicationConfiguration Rules Destination

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
    "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
    "<a href="#replicakmskeyid" title="ReplicaKmsKeyId">ReplicaKmsKeyId</a>" : <i>String</i>,
    "<a href="#storageclass" title="StorageClass">StorageClass</a>" : <i>String</i>,
    "<a href="#accesscontroltranslation" title="AccessControlTranslation">AccessControlTranslation</a>" : <i>[ <a href="replicationconfiguration-rules-destination-accesscontroltranslation.md">AccessControlTranslation</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
<a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
<a href="#replicakmskeyid" title="ReplicaKmsKeyId">ReplicaKmsKeyId</a>: <i>String</i>
<a href="#storageclass" title="StorageClass">StorageClass</a>: <i>String</i>
<a href="#accesscontroltranslation" title="AccessControlTranslation">AccessControlTranslation</a>: <i>
      - <a href="replicationconfiguration-rules-destination-accesscontroltranslation.md">AccessControlTranslation</a></i>
</pre>

## Properties

#### AccountId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bucket

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicaKmsKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageClass

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessControlTranslation

_Required_: No

_Type_: List of <a href="replicationconfiguration-rules-destination-accesscontroltranslation.md">AccessControlTranslation</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

