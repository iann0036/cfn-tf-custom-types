# Terraform::AWS::CloudfrontOriginAccessIdentity

Creates an Amazon CloudFront origin access identity.

For information about CloudFront distributions, see the
[Amazon CloudFront Developer Guide][1]. For more information on generating
origin access identities, see
[Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content][2].

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::CloudfrontOriginAccessIdentity",
    "Properties" : {
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::CloudfrontOriginAccessIdentity
Properties:
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
</pre>

## Properties

#### Comment

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

Returns the <code>CallerReference</code> value.

#### CloudfrontAccessIdentityPath

Returns the <code>CloudfrontAccessIdentityPath</code> value.

#### Etag

Returns the <code>Etag</code> value.

#### IamArn

Returns the <code>IamArn</code> value.

#### Id

Returns the <code>Id</code> value.

#### S3CanonicalUserId

Returns the <code>S3CanonicalUserId</code> value.

