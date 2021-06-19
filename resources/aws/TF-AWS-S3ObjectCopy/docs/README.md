# TF::AWS::S3ObjectCopy

Provides a resource for copying an S3 object.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::S3ObjectCopy",
    "Properties" : {
        "<a href="#acl" title="Acl">Acl</a>" : <i>String</i>,
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#bucketkeyenabled" title="BucketKeyEnabled">BucketKeyEnabled</a>" : <i>Boolean</i>,
        "<a href="#cachecontrol" title="CacheControl">CacheControl</a>" : <i>String</i>,
        "<a href="#contentdisposition" title="ContentDisposition">ContentDisposition</a>" : <i>String</i>,
        "<a href="#contentencoding" title="ContentEncoding">ContentEncoding</a>" : <i>String</i>,
        "<a href="#contentlanguage" title="ContentLanguage">ContentLanguage</a>" : <i>String</i>,
        "<a href="#contenttype" title="ContentType">ContentType</a>" : <i>String</i>,
        "<a href="#copyifmatch" title="CopyIfMatch">CopyIfMatch</a>" : <i>String</i>,
        "<a href="#copyifmodifiedsince" title="CopyIfModifiedSince">CopyIfModifiedSince</a>" : <i>String</i>,
        "<a href="#copyifnonematch" title="CopyIfNoneMatch">CopyIfNoneMatch</a>" : <i>String</i>,
        "<a href="#copyifunmodifiedsince" title="CopyIfUnmodifiedSince">CopyIfUnmodifiedSince</a>" : <i>String</i>,
        "<a href="#customeralgorithm" title="CustomerAlgorithm">CustomerAlgorithm</a>" : <i>String</i>,
        "<a href="#customerkey" title="CustomerKey">CustomerKey</a>" : <i>String</i>,
        "<a href="#customerkeymd5" title="CustomerKeyMd5">CustomerKeyMd5</a>" : <i>String</i>,
        "<a href="#expectedbucketowner" title="ExpectedBucketOwner">ExpectedBucketOwner</a>" : <i>String</i>,
        "<a href="#expectedsourcebucketowner" title="ExpectedSourceBucketOwner">ExpectedSourceBucketOwner</a>" : <i>String</i>,
        "<a href="#expires" title="Expires">Expires</a>" : <i>String</i>,
        "<a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>" : <i>Boolean</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#kmsencryptioncontext" title="KmsEncryptionContext">KmsEncryptionContext</a>" : <i>String</i>,
        "<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>" : <i>String</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>,
        "<a href="#metadatadirective" title="MetadataDirective">MetadataDirective</a>" : <i>String</i>,
        "<a href="#objectlocklegalholdstatus" title="ObjectLockLegalHoldStatus">ObjectLockLegalHoldStatus</a>" : <i>String</i>,
        "<a href="#objectlockmode" title="ObjectLockMode">ObjectLockMode</a>" : <i>String</i>,
        "<a href="#objectlockretainuntildate" title="ObjectLockRetainUntilDate">ObjectLockRetainUntilDate</a>" : <i>String</i>,
        "<a href="#requestpayer" title="RequestPayer">RequestPayer</a>" : <i>String</i>,
        "<a href="#serversideencryption" title="ServerSideEncryption">ServerSideEncryption</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#sourcecustomeralgorithm" title="SourceCustomerAlgorithm">SourceCustomerAlgorithm</a>" : <i>String</i>,
        "<a href="#sourcecustomerkey" title="SourceCustomerKey">SourceCustomerKey</a>" : <i>String</i>,
        "<a href="#sourcecustomerkeymd5" title="SourceCustomerKeyMd5">SourceCustomerKeyMd5</a>" : <i>String</i>,
        "<a href="#storageclass" title="StorageClass">StorageClass</a>" : <i>String</i>,
        "<a href="#taggingdirective" title="TaggingDirective">TaggingDirective</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#websiteredirect" title="WebsiteRedirect">WebsiteRedirect</a>" : <i>String</i>,
        "<a href="#grant" title="Grant">Grant</a>" : <i>[ <a href="grantdefinition.md">GrantDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::S3ObjectCopy
Properties:
    <a href="#acl" title="Acl">Acl</a>: <i>String</i>
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#bucketkeyenabled" title="BucketKeyEnabled">BucketKeyEnabled</a>: <i>Boolean</i>
    <a href="#cachecontrol" title="CacheControl">CacheControl</a>: <i>String</i>
    <a href="#contentdisposition" title="ContentDisposition">ContentDisposition</a>: <i>String</i>
    <a href="#contentencoding" title="ContentEncoding">ContentEncoding</a>: <i>String</i>
    <a href="#contentlanguage" title="ContentLanguage">ContentLanguage</a>: <i>String</i>
    <a href="#contenttype" title="ContentType">ContentType</a>: <i>String</i>
    <a href="#copyifmatch" title="CopyIfMatch">CopyIfMatch</a>: <i>String</i>
    <a href="#copyifmodifiedsince" title="CopyIfModifiedSince">CopyIfModifiedSince</a>: <i>String</i>
    <a href="#copyifnonematch" title="CopyIfNoneMatch">CopyIfNoneMatch</a>: <i>String</i>
    <a href="#copyifunmodifiedsince" title="CopyIfUnmodifiedSince">CopyIfUnmodifiedSince</a>: <i>String</i>
    <a href="#customeralgorithm" title="CustomerAlgorithm">CustomerAlgorithm</a>: <i>String</i>
    <a href="#customerkey" title="CustomerKey">CustomerKey</a>: <i>String</i>
    <a href="#customerkeymd5" title="CustomerKeyMd5">CustomerKeyMd5</a>: <i>String</i>
    <a href="#expectedbucketowner" title="ExpectedBucketOwner">ExpectedBucketOwner</a>: <i>String</i>
    <a href="#expectedsourcebucketowner" title="ExpectedSourceBucketOwner">ExpectedSourceBucketOwner</a>: <i>String</i>
    <a href="#expires" title="Expires">Expires</a>: <i>String</i>
    <a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>: <i>Boolean</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#kmsencryptioncontext" title="KmsEncryptionContext">KmsEncryptionContext</a>: <i>String</i>
    <a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>: <i>String</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
    <a href="#metadatadirective" title="MetadataDirective">MetadataDirective</a>: <i>String</i>
    <a href="#objectlocklegalholdstatus" title="ObjectLockLegalHoldStatus">ObjectLockLegalHoldStatus</a>: <i>String</i>
    <a href="#objectlockmode" title="ObjectLockMode">ObjectLockMode</a>: <i>String</i>
    <a href="#objectlockretainuntildate" title="ObjectLockRetainUntilDate">ObjectLockRetainUntilDate</a>: <i>String</i>
    <a href="#requestpayer" title="RequestPayer">RequestPayer</a>: <i>String</i>
    <a href="#serversideencryption" title="ServerSideEncryption">ServerSideEncryption</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#sourcecustomeralgorithm" title="SourceCustomerAlgorithm">SourceCustomerAlgorithm</a>: <i>String</i>
    <a href="#sourcecustomerkey" title="SourceCustomerKey">SourceCustomerKey</a>: <i>String</i>
    <a href="#sourcecustomerkeymd5" title="SourceCustomerKeyMd5">SourceCustomerKeyMd5</a>: <i>String</i>
    <a href="#storageclass" title="StorageClass">StorageClass</a>: <i>String</i>
    <a href="#taggingdirective" title="TaggingDirective">TaggingDirective</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#websiteredirect" title="WebsiteRedirect">WebsiteRedirect</a>: <i>String</i>
    <a href="#grant" title="Grant">Grant</a>: <i>
      - <a href="grantdefinition.md">GrantDefinition</a></i>
</pre>

## Properties

#### Acl

[Canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Defaults to `private`. Valid values are `private`, `public-read`, `public-read-write`, `authenticated-read`, `aws-exec-read`, `bucket-owner-read`, and `bucket-owner-full-control`. Conflicts with `grant`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bucket

Name of the bucket to put the file in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BucketKeyEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheControl

Specifies caching behavior along the request/reply chain Read [w3c cache_control](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9) for further details.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentDisposition

Specifies presentational information for the object. Read [w3c content_disposition](http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1) for further information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentEncoding

Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [w3c content encoding](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11) for further information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentLanguage

Language the content is in e.g. en-US or en-GB.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentType

Standard MIME type describing the format of the object data, e.g. `application/octet-stream`. All Valid MIME Types are valid for this input.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CopyIfMatch

Copies the object if its entity tag (ETag) matches the specified tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CopyIfModifiedSince

Copies the object if it has been modified since the specified time, in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CopyIfNoneMatch

Copies the object if its entity tag (ETag) is different than the specified ETag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CopyIfUnmodifiedSince

Copies the object if it hasn't been modified since the specified time, in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerAlgorithm

Specifies the algorithm to use to when encrypting the object (for example, AES256).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerKey

Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon S3 does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side-encryption-customer-algorithm header.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerKeyMd5

Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpectedBucketOwner

Account id of the expected destination bucket owner. If the destination bucket is owned by a different account, the request will fail with an HTTP 403 (Access Denied) error.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpectedSourceBucketOwner

Account id of the expected source bucket owner. If the source bucket is owned by a different account, the request will fail with an HTTP 403 (Access Denied) error.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expires

Date and time at which the object is no longer cacheable, in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDestroy

Allow the object to be deleted by removing any legal hold on any object version. Default is `false`. This value should be set to `true` only if the bucket has S3 object lock enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

Name of the object once it is in the bucket.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsEncryptionContext

Specifies the AWS KMS Encryption Context to use for object encryption. The value is a base64-encoded UTF-8 string holding JSON with the encryption context key-value pairs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyId

Specifies the AWS KMS Key ARN to use for object encryption. This value is a fully qualified **ARN** of the KMS Key. If using `aws_kms_key`, use the exported `arn` attribute: `kms_key_id = aws_kms_key.foo.arn`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

A map of keys/values to provision metadata (will be automatically prefixed by `x-amz-meta-`, note that only lowercase label are currently supported by the AWS Go API).

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetadataDirective

Specifies whether the metadata is copied from the source object or replaced with metadata provided in the request. Valid values are `COPY` and `REPLACE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectLockLegalHoldStatus

The [legal hold](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html#object-lock-legal-holds) status that you want to apply to the specified object. Valid values are `ON` and `OFF`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectLockMode

The object lock [retention mode](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html#object-lock-retention-modes) that you want to apply to this object. Valid values are `GOVERNANCE` and `COMPLIANCE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectLockRetainUntilDate

The date and time, in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8), when this object's object lock will [expire](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html#object-lock-retention-periods).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestPayer

Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. For information about downloading objects from requester pays buckets, see Downloading Objects in Requestor Pays Buckets (https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html) in the Amazon S3 Developer Guide. If included, the only valid value is `requester`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSideEncryption

Specifies server-side encryption of the object in S3. Valid values are `AES256` and `aws:kms`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

Specifies the source object for the copy operation. You specify the value in one of two formats. For objects not accessed through an access point, specify the name of the source bucket and the key of the source object, separated by a slash (`/`). For example, `testbucket/test1.json`. For objects accessed through access points, specify the Amazon Resource Name (ARN) of the object as accessed through the access point, in the format `arn:aws:s3:<Region>:<account-id>:accesspoint/<access-point-name>/object/<key>`. For example, `arn:aws:s3:us-west-2:9999912999:accesspoint/my-access-point/object/testbucket/test1.json`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceCustomerAlgorithm

Specifies the algorithm to use when decrypting the source object (for example, AES256).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceCustomerKey

Specifies the customer-provided encryption key for Amazon S3 to use to decrypt the source object. The encryption key provided in this header must be one that was used when the source object was created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceCustomerKeyMd5

Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageClass

Specifies the desired [Storage Class](http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html)
for the object. Can be either `STANDARD`, `REDUCED_REDUNDANCY`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `GLACIER`, `DEEP_ARCHIVE`, or `STANDARD_IA`. Defaults to `STANDARD`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaggingDirective

Specifies whether the object tag-set are copied from the source object or replaced with tag-set provided in the request. Valid values are `COPY` and `REPLACE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the object. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebsiteRedirect

Specifies a target URL for [website redirect](http://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Grant

_Required_: No

_Type_: List of <a href="grantdefinition.md">GrantDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Etag

Returns the <code>Etag</code> value.

#### Expiration

Returns the <code>Expiration</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastModified

Returns the <code>LastModified</code> value.

#### RequestCharged

Returns the <code>RequestCharged</code> value.

#### SourceVersionId

Returns the <code>SourceVersionId</code> value.

#### VersionId

Returns the <code>VersionId</code> value.

