# Terraform::AWS::CloudfrontOriginAccessIdentity

CloudFormation equivalent of aws_cloudfront_origin_access_identity

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::CloudfrontOriginAccessIdentity",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#callerreference" title="CallerReference">CallerReference</a>" : <i>String</i>,
        "<a href="#cloudfrontaccessidentitypath" title="CloudfrontAccessIdentityPath">CloudfrontAccessIdentityPath</a>" : <i>String</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#etag" title="Etag">Etag</a>" : <i>String</i>,
        "<a href="#iamarn" title="IamArn">IamArn</a>" : <i>String</i>,
        "<a href="#s3canonicaluserid" title="S3CanonicalUserId">S3CanonicalUserId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::CloudfrontOriginAccessIdentity
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#callerreference" title="CallerReference">CallerReference</a>: <i>String</i>
    <a href="#cloudfrontaccessidentitypath" title="CloudfrontAccessIdentityPath">CloudfrontAccessIdentityPath</a>: <i>String</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#etag" title="Etag">Etag</a>: <i>String</i>
    <a href="#iamarn" title="IamArn">IamArn</a>: <i>String</i>
    <a href="#s3canonicaluserid" title="S3CanonicalUserId">S3CanonicalUserId</a>: <i>String</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CallerReference

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudfrontAccessIdentityPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Etag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3CanonicalUserId

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

#### CallerReference

Returns the &lt;code&gt;CallerReference&lt;/code&gt; value.

#### CloudfrontAccessIdentityPath

Returns the &lt;code&gt;CloudfrontAccessIdentityPath&lt;/code&gt; value.

#### Etag

Returns the &lt;code&gt;Etag&lt;/code&gt; value.

#### IamArn

Returns the &lt;code&gt;IamArn&lt;/code&gt; value.

#### S3CanonicalUserId

Returns the &lt;code&gt;S3CanonicalUserId&lt;/code&gt; value.

