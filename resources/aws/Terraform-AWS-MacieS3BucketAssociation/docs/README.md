# Terraform::AWS::MacieS3BucketAssociation

Associates an S3 resource with Amazon Macie for monitoring and data classification.

~> **NOTE:** Before using Amazon Macie for the first time it must be enabled manually. Instructions are [here](https://docs.aws.amazon.com/macie/latest/userguide/macie-setting-up.html#macie-setting-up-enable).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::MacieS3BucketAssociation",
    "Properties" : {
        "<a href="#bucketname" title="BucketName">BucketName</a>" : <i>String</i>,
        "<a href="#memberaccountid" title="MemberAccountId">MemberAccountId</a>" : <i>String</i>,
        "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>,
        "<a href="#classificationtype" title="ClassificationType">ClassificationType</a>" : <i>[ <a href="classificationtype.md">ClassificationType</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::MacieS3BucketAssociation
Properties:
    <a href="#bucketname" title="BucketName">BucketName</a>: <i>String</i>
    <a href="#memberaccountid" title="MemberAccountId">MemberAccountId</a>: <i>String</i>
    <a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
    <a href="#classificationtype" title="ClassificationType">ClassificationType</a>: <i>
      - <a href="classificationtype.md">ClassificationType</a></i>
</pre>

## Properties

#### BucketName

The name of the S3 bucket that you want to associate with Amazon Macie.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemberAccountId

The ID of the Amazon Macie member account whose S3 resources you want to associate with Macie. If `member_account_id` isn't specified, the action associates specified S3 resources with Macie for the current master account.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

Object key prefix identifying one or more S3 objects to which the association applies.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassificationType

_Required_: No

_Type_: List of <a href="classificationtype.md">ClassificationType</a>

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

