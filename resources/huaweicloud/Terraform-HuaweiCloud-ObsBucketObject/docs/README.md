# Terraform::HuaweiCloud::ObsBucketObject

Provides an OBS bucket object resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::ObsBucketObject",
    "Properties" : {
        "<a href="#acl" title="Acl">Acl</a>" : <i>String</i>,
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#content" title="Content">Content</a>" : <i>String</i>,
        "<a href="#contenttype" title="ContentType">ContentType</a>" : <i>String</i>,
        "<a href="#encryption" title="Encryption">Encryption</a>" : <i>Boolean</i>,
        "<a href="#etag" title="Etag">Etag</a>" : <i>String</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#storageclass" title="StorageClass">StorageClass</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::ObsBucketObject
Properties:
    <a href="#acl" title="Acl">Acl</a>: <i>String</i>
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#content" title="Content">Content</a>: <i>String</i>
    <a href="#contenttype" title="ContentType">ContentType</a>: <i>String</i>
    <a href="#encryption" title="Encryption">Encryption</a>: <i>Boolean</i>
    <a href="#etag" title="Etag">Etag</a>: <i>String</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#storageclass" title="StorageClass">StorageClass</a>: <i>String</i>
</pre>

## Properties

#### Acl

The ACL policy to apply. Defaults to `private`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bucket

The name of the bucket to put the file in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Content

The literal content being uploaded to the bucket.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentType

A standard MIME type describing the format of the object data, e.g. application/octet-stream.
All Valid MIME Types are valid for this input.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encryption

Whether enable server-side encryption of the object in SSE-KMS mode.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Etag

Specifies the unique identifier of the object content. It can be used to trigger updates.
The only meaningful value is `md5(file("path_to_file"))`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

The name of the object once it is in the bucket.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

The path to the source file being uploaded to the bucket.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageClass

Specifies the storage class of the object. Defaults to `STANDARD`.

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

#### Id

Returns the <code>Id</code> value.

#### Size

Returns the <code>Size</code> value.

#### VersionId

Returns the <code>VersionId</code> value.

