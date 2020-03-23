# Terraform::AWS::EbsDefaultKmsKey

Provides a resource to manage the default customer master key (CMK) that your AWS account uses to encrypt EBS volumes.

Your AWS account has an AWS-managed default CMK that is used for encrypting an EBS volume when no CMK is specified in the API call that creates the volume.
By using the `aws_ebs_default_kms_key` resource, you can specify a customer-managed CMK to use in place of the AWS-managed default CMK.

~> **NOTE:** Creating an `aws_ebs_default_kms_key` resource does not enable default EBS encryption. Use the [`aws_ebs_encryption_by_default`](ebs_encryption_by_default.html) to enable default EBS encryption.

~> **NOTE:** Destroying this resource will reset the default CMK to the account's AWS-managed default CMK for EBS.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::EbsDefaultKmsKey",
    "Properties" : {
        "<a href="#keyarn" title="KeyArn">KeyArn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::EbsDefaultKmsKey
Properties:
    <a href="#keyarn" title="KeyArn">KeyArn</a>: <i>String</i>
</pre>

## Properties

#### KeyArn

The ARN of the AWS Key Management Service (AWS KMS) customer master key (CMK) to use to encrypt the EBS volume.

_Required_: Yes

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

#### Id

Returns the <code>Id</code> value.

