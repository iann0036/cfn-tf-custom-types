# TF::AWS::S3BucketPublicAccessBlock

Manages S3 bucket-level Public Access Block configuration. For more information about these settings, see the [AWS S3 Block Public Access documentation](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::S3BucketPublicAccessBlock",
    "Properties" : {
        "<a href="#blockpublicacls" title="BlockPublicAcls">BlockPublicAcls</a>" : <i>Boolean</i>,
        "<a href="#blockpublicpolicy" title="BlockPublicPolicy">BlockPublicPolicy</a>" : <i>Boolean</i>,
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#ignorepublicacls" title="IgnorePublicAcls">IgnorePublicAcls</a>" : <i>Boolean</i>,
        "<a href="#restrictpublicbuckets" title="RestrictPublicBuckets">RestrictPublicBuckets</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::S3BucketPublicAccessBlock
Properties:
    <a href="#blockpublicacls" title="BlockPublicAcls">BlockPublicAcls</a>: <i>Boolean</i>
    <a href="#blockpublicpolicy" title="BlockPublicPolicy">BlockPublicPolicy</a>: <i>Boolean</i>
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#ignorepublicacls" title="IgnorePublicAcls">IgnorePublicAcls</a>: <i>Boolean</i>
    <a href="#restrictpublicbuckets" title="RestrictPublicBuckets">RestrictPublicBuckets</a>: <i>Boolean</i>
</pre>

## Properties

#### BlockPublicAcls

Whether Amazon S3 should block public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
* PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
* PUT Object calls will fail if the request includes an object ACL.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockPublicPolicy

Whether Amazon S3 should block public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the existing bucket policy. When set to `true` causes Amazon S3 to:
* Reject calls to PUT Bucket policy if the specified bucket policy allows public access.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bucket

S3 Bucket to which this Public Access Block configuration should be applied.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnorePublicAcls

Whether Amazon S3 should ignore public ACLs for this bucket. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
* Ignore public ACLs on this bucket and any objects that it contains.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestrictPublicBuckets

Whether Amazon S3 should restrict public bucket policies for this bucket. Defaults to `false`. Enabling this setting does not affect the previously stored bucket policy, except that public and cross-account access within the public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
* Only the bucket owner and AWS Services can access this buckets if it has a public policy.

_Required_: No

_Type_: Boolean

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

