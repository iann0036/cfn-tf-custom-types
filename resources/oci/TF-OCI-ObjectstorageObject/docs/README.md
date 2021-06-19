# TF::OCI::ObjectstorageObject

This resource provides the Object resource in Oracle Cloud Infrastructure Object Storage service.

Creates a new object or overwrites an existing object with the same name. The maximum object size allowed by
PutObject is 50 GiB.

See [Object Names](https://docs.cloud.oracle.com/iaas/Content/Object/Tasks/managingobjects.htm#namerequirements)
for object naming requirements. 

See [Special Instructions for Object Storage PUT](https://docs.cloud.oracle.com/iaas/Content/API/Concepts/signingrequests.htm#ObjectStoragePut)
for request signature requirements.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::ObjectstorageObject",
    "Properties" : {
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#cachecontrol" title="CacheControl">CacheControl</a>" : <i>String</i>,
        "<a href="#content" title="Content">Content</a>" : <i>String</i>,
        "<a href="#contentdisposition" title="ContentDisposition">ContentDisposition</a>" : <i>String</i>,
        "<a href="#contentencoding" title="ContentEncoding">ContentEncoding</a>" : <i>String</i>,
        "<a href="#contentlanguage" title="ContentLanguage">ContentLanguage</a>" : <i>String</i>,
        "<a href="#contentmd5" title="ContentMd5">ContentMd5</a>" : <i>String</i>,
        "<a href="#contenttype" title="ContentType">ContentType</a>" : <i>String</i>,
        "<a href="#deleteallobjectversions" title="DeleteAllObjectVersions">DeleteAllObjectVersions</a>" : <i>Boolean</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#object" title="Object">Object</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#storagetier" title="StorageTier">StorageTier</a>" : <i>String</i>,
        "<a href="#sourceuridetails" title="SourceUriDetails">SourceUriDetails</a>" : <i>[ <a href="sourceuridetailsdefinition.md">SourceUriDetailsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::ObjectstorageObject
Properties:
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#cachecontrol" title="CacheControl">CacheControl</a>: <i>String</i>
    <a href="#content" title="Content">Content</a>: <i>String</i>
    <a href="#contentdisposition" title="ContentDisposition">ContentDisposition</a>: <i>String</i>
    <a href="#contentencoding" title="ContentEncoding">ContentEncoding</a>: <i>String</i>
    <a href="#contentlanguage" title="ContentLanguage">ContentLanguage</a>: <i>String</i>
    <a href="#contentmd5" title="ContentMd5">ContentMd5</a>: <i>String</i>
    <a href="#contenttype" title="ContentType">ContentType</a>: <i>String</i>
    <a href="#deleteallobjectversions" title="DeleteAllObjectVersions">DeleteAllObjectVersions</a>: <i>Boolean</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#object" title="Object">Object</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#storagetier" title="StorageTier">StorageTier</a>: <i>String</i>
    <a href="#sourceuridetails" title="SourceUriDetails">SourceUriDetails</a>: <i>
      - <a href="sourceuridetailsdefinition.md">SourceUriDetailsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Bucket

The name of the bucket. Avoid entering confidential information. Example: `my-new-bucket1`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheControl

The optional Cache-Control header that defines the caching behavior value to be returned in GetObject and HeadObject responses. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to identify objects that require caching restrictions.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Content

The object to upload to the object store. Cannot be defined if `source` or `source_uri_details` is defined.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentDisposition

The optional Content-Disposition header that defines presentational information for the object to be returned in GetObject and HeadObject responses. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to let users download objects with custom filenames in a browser.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentEncoding

The optional Content-Encoding header that defines the content encodings that were applied to the object to upload. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to determine what decoding mechanisms need to be applied to obtain the media-type specified by the Content-Type header of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentLanguage

The optional Content-Language header that defines the content language of the object to upload. Specifying values for this header has no effect on Object Storage behavior. Programs that read the object determine what to do based on the value provided. For example, you could use this header to identify and differentiate objects based on a particular language.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentMd5

(Updatable) The optional base-64 header that defines the encoded MD5 hash of the body. If the optional Content-MD5 header is present, Object Storage performs an integrity check on the body of the HTTP request by computing the MD5 hash for the body and comparing it to the MD5 hash supplied in the header. If the two hashes do not match, the object is rejected and an HTTP-400 Unmatched Content MD5 error is returned with the message:.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteAllObjectVersions

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Object

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageTier

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceUriDetails

_Required_: No

_Type_: List of <a href="sourceuridetailsdefinition.md">SourceUriDetailsDefinition</a>

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

#### ContentLength

(Updatable) The content length of the body.

#### Id

Returns the <code>Id</code> value.

#### State

Returns the <code>State</code> value.

#### VersionId

Returns the <code>VersionId</code> value.

#### WorkRequestId

Returns the <code>WorkRequestId</code> value.

