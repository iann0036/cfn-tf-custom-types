# TF::Fastly::ServiceCompute S3loggingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#acl" title="Acl">Acl</a>" : <i>String</i>,
    "<a href="#bucketname" title="BucketName">BucketName</a>" : <i>String</i>,
    "<a href="#compressioncodec" title="CompressionCodec">CompressionCodec</a>" : <i>String</i>,
    "<a href="#domain" title="Domain">Domain</a>" : <i>[ <a href="domaindefinition.md">DomainDefinition</a>, ... ]</i>,
    "<a href="#gziplevel" title="GzipLevel">GzipLevel</a>" : <i>Double</i>,
    "<a href="#messagetype" title="MessageType">MessageType</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
    "<a href="#publickey" title="PublicKey">PublicKey</a>" : <i>String</i>,
    "<a href="#redundancy" title="Redundancy">Redundancy</a>" : <i>String</i>,
    "<a href="#s3accesskey" title="S3AccessKey">S3AccessKey</a>" : <i>String</i>,
    "<a href="#s3iamrole" title="S3IamRole">S3IamRole</a>" : <i>String</i>,
    "<a href="#s3secretkey" title="S3SecretKey">S3SecretKey</a>" : <i>String</i>,
    "<a href="#serversideencryption" title="ServerSideEncryption">ServerSideEncryption</a>" : <i>String</i>,
    "<a href="#serversideencryptionkmskeyid" title="ServerSideEncryptionKmsKeyId">ServerSideEncryptionKmsKeyId</a>" : <i>String</i>,
    "<a href="#timestampformat" title="TimestampFormat">TimestampFormat</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#acl" title="Acl">Acl</a>: <i>String</i>
<a href="#bucketname" title="BucketName">BucketName</a>: <i>String</i>
<a href="#compressioncodec" title="CompressionCodec">CompressionCodec</a>: <i>String</i>
<a href="#domain" title="Domain">Domain</a>: <i>
      - <a href="domaindefinition.md">DomainDefinition</a></i>
<a href="#gziplevel" title="GzipLevel">GzipLevel</a>: <i>Double</i>
<a href="#messagetype" title="MessageType">MessageType</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#period" title="Period">Period</a>: <i>Double</i>
<a href="#publickey" title="PublicKey">PublicKey</a>: <i>String</i>
<a href="#redundancy" title="Redundancy">Redundancy</a>: <i>String</i>
<a href="#s3accesskey" title="S3AccessKey">S3AccessKey</a>: <i>String</i>
<a href="#s3iamrole" title="S3IamRole">S3IamRole</a>: <i>String</i>
<a href="#s3secretkey" title="S3SecretKey">S3SecretKey</a>: <i>String</i>
<a href="#serversideencryption" title="ServerSideEncryption">ServerSideEncryption</a>: <i>String</i>
<a href="#serversideencryptionkmskeyid" title="ServerSideEncryptionKmsKeyId">ServerSideEncryptionKmsKeyId</a>: <i>String</i>
<a href="#timestampformat" title="TimestampFormat">TimestampFormat</a>: <i>String</i>
</pre>

## Properties

#### Acl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BucketName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompressionCodec

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

_Required_: No

_Type_: List of <a href="domaindefinition.md">DomainDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GzipLevel

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MessageType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redundancy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3AccessKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3IamRole

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3SecretKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSideEncryption

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSideEncryptionKmsKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimestampFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

