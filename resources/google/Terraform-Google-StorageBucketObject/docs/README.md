# Terraform::Google::StorageBucketObject

Creates a new object inside an existing bucket in Google cloud storage service (GCS). 
[ACLs](https://cloud.google.com/storage/docs/access-control/lists) can be applied using the `google_storage_object_acl` resource.
 For more information see 
[the official documentation](https://cloud.google.com/storage/docs/key-terms#objects) 
and 
[API](https://cloud.google.com/storage/docs/json_api/v1/objects).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::StorageBucketObject",
    "Properties" : {
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#cachecontrol" title="CacheControl">CacheControl</a>" : <i>String</i>,
        "<a href="#content" title="Content">Content</a>" : <i>String</i>,
        "<a href="#contentdisposition" title="ContentDisposition">ContentDisposition</a>" : <i>String</i>,
        "<a href="#contentencoding" title="ContentEncoding">ContentEncoding</a>" : <i>String</i>,
        "<a href="#contentlanguage" title="ContentLanguage">ContentLanguage</a>" : <i>String</i>,
        "<a href="#contenttype" title="ContentType">ContentType</a>" : <i>String</i>,
        "<a href="#detectmd5hash" title="DetectMd5hash">DetectMd5hash</a>" : <i>String</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadata.md">Metadata</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#storageclass" title="StorageClass">StorageClass</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::StorageBucketObject
Properties:
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#cachecontrol" title="CacheControl">CacheControl</a>: <i>String</i>
    <a href="#content" title="Content">Content</a>: <i>String</i>
    <a href="#contentdisposition" title="ContentDisposition">ContentDisposition</a>: <i>String</i>
    <a href="#contentencoding" title="ContentEncoding">ContentEncoding</a>: <i>String</i>
    <a href="#contentlanguage" title="ContentLanguage">ContentLanguage</a>: <i>String</i>
    <a href="#contenttype" title="ContentType">ContentType</a>: <i>String</i>
    <a href="#detectmd5hash" title="DetectMd5hash">DetectMd5hash</a>: <i>String</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadata.md">Metadata</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#storageclass" title="StorageClass">StorageClass</a>: <i>String</i>
</pre>

## Properties

#### Bucket

The name of the containing bucket.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheControl

[Cache-Control](https://tools.ietf.org/html/rfc7234#section-5.2)
directive to specify caching behavior of object data. If omitted and object is accessible to all anonymous users, the default will be public, max-age=3600.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Content

Data as `string` to be uploaded. Must be defined if `source` is not. **Note**: The `content` field is marked as sensitive. To view the raw contents of the object, please define an [output](/docs/configuration/outputs.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentDisposition

[Content-Disposition](https://tools.ietf.org/html/rfc6266) of the object data.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentEncoding

[Content-Encoding](https://tools.ietf.org/html/rfc7231#section-3.1.2.2) of the object data.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentLanguage

[Content-Language](https://tools.ietf.org/html/rfc7231#section-3.1.3.2) of the object data.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentType

[Content-Type](https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the object data. Defaults to "application/octet-stream" or "text/plain; charset=utf-8".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DetectMd5hash

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

User-provided metadata, in key/value pairs.

_Required_: No

_Type_: List of <a href="metadata.md">Metadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the object. If you're interpolating the name of this object, see `output_name` instead.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

A path to the data you want to upload. Must be defined
if `content` is not.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageClass

The [StorageClass](https://cloud.google.com/storage/docs/storage-classes) of the new bucket object.
Supported values include: `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`. If not provided, this defaults to the bucket's default
storage class or to a [standard](https://cloud.google.com/storage/docs/storage-classes#standard) class.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Crc32c

Returns the <code>Crc32c</code> value.

#### Md5hash

Returns the <code>Md5hash</code> value.

#### OutputName

Returns the <code>OutputName</code> value.

#### SelfLink

Returns the <code>SelfLink</code> value.

