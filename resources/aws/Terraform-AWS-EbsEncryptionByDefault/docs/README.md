# Terraform::AWS::EbsEncryptionByDefault

Provides a resource to manage whether default EBS encryption is enabled for your AWS account in the current AWS region. To manage the default KMS key for the region, see the [`aws_ebs_default_kms_key` resource](/docs/providers/aws/r/ebs_default_kms_key.html).

~> **NOTE:** Removing this Terraform resource disables default EBS encryption.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::EbsEncryptionByDefault",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::EbsEncryptionByDefault
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
</pre>

## Properties

#### Enabled

Whether or not default EBS encryption is enabled. Valid values are `true` or `false`. Defaults to `true`.

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

