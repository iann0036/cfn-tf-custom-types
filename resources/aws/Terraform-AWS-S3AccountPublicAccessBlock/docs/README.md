# Terraform::AWS::S3AccountPublicAccessBlock

CloudFormation equivalent of aws_s3_account_public_access_block

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::S3AccountPublicAccessBlock",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
        "<a href="#blockpublicacls" title="BlockPublicAcls">BlockPublicAcls</a>" : <i>Boolean</i>,
        "<a href="#blockpublicpolicy" title="BlockPublicPolicy">BlockPublicPolicy</a>" : <i>Boolean</i>,
        "<a href="#ignorepublicacls" title="IgnorePublicAcls">IgnorePublicAcls</a>" : <i>Boolean</i>,
        "<a href="#restrictpublicbuckets" title="RestrictPublicBuckets">RestrictPublicBuckets</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::S3AccountPublicAccessBlock
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
    <a href="#blockpublicacls" title="BlockPublicAcls">BlockPublicAcls</a>: <i>Boolean</i>
    <a href="#blockpublicpolicy" title="BlockPublicPolicy">BlockPublicPolicy</a>: <i>Boolean</i>
    <a href="#ignorepublicacls" title="IgnorePublicAcls">IgnorePublicAcls</a>: <i>Boolean</i>
    <a href="#restrictpublicbuckets" title="RestrictPublicBuckets">RestrictPublicBuckets</a>: <i>Boolean</i>
</pre>

## Properties

#### AccountId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockPublicAcls

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockPublicPolicy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnorePublicAcls

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestrictPublicBuckets

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

