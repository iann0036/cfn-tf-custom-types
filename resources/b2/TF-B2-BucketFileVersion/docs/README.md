# TF::B2::BucketFileVersion

CloudFormation equivalent of b2_bucket_file_version

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::B2::BucketFileVersion",
    "Properties" : {
        "<a href="#bucketid" title="BucketId">BucketId</a>" : <i>String</i>,
        "<a href="#contenttype" title="ContentType">ContentType</a>" : <i>String</i>,
        "<a href="#fileinfo" title="FileInfo">FileInfo</a>" : <i>[ <a href="fileinfodefinition.md">FileInfoDefinition</a>, ... ]</i>,
        "<a href="#filename" title="FileName">FileName</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#serversideencryption" title="ServerSideEncryption">ServerSideEncryption</a>" : <i>[ <a href="serversideencryptiondefinition.md">ServerSideEncryptionDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::B2::BucketFileVersion
Properties:
    <a href="#bucketid" title="BucketId">BucketId</a>: <i>String</i>
    <a href="#contenttype" title="ContentType">ContentType</a>: <i>String</i>
    <a href="#fileinfo" title="FileInfo">FileInfo</a>: <i>
      - <a href="fileinfodefinition.md">FileInfoDefinition</a></i>
    <a href="#filename" title="FileName">FileName</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#serversideencryption" title="ServerSideEncryption">ServerSideEncryption</a>: <i>
      - <a href="serversideencryptiondefinition.md">ServerSideEncryptionDefinition</a></i>
</pre>

## Properties

#### BucketId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileInfo

_Required_: No

_Type_: List of <a href="fileinfodefinition.md">FileInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSideEncryption

_Required_: No

_Type_: List of <a href="serversideencryptiondefinition.md">ServerSideEncryptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Action

Returns the <code>Action</code> value.

#### ContentMd5

Returns the <code>ContentMd5</code> value.

#### ContentSha1

Returns the <code>ContentSha1</code> value.

#### FileId

Returns the <code>FileId</code> value.

#### Id

Returns the <code>Id</code> value.

#### Size

Returns the <code>Size</code> value.

#### UploadTimestamp

Returns the <code>UploadTimestamp</code> value.

