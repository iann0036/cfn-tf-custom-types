# Terraform::Alicloud::KmsKey

A kms key can help user to protect data security in the transmission process.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::KmsKey",
    "Properties" : {
        "<a href="#deletionwindowindays" title="DeletionWindowInDays">DeletionWindowInDays</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
        "<a href="#keyusage" title="KeyUsage">KeyUsage</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::KmsKey
Properties:
    <a href="#deletionwindowindays" title="DeletionWindowInDays">DeletionWindowInDays</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
    <a href="#keyusage" title="KeyUsage">KeyUsage</a>: <i>String</i>
</pre>

## Properties

#### DeletionWindowInDays

Duration in days after which the key is deleted
after destruction of the resource, must be between 7 and 30 days. Defaults to 30 days.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the key as viewed in Alicloud console. Default to "From Terraform".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEnabled

Specifies whether the key is enabled. Defaults to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyUsage

Specifies the usage of CMK. Currently, default to 'ENCRYPT/DECRYPT', indicating that CMK is used for encryption and decryption.

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

#### Arn

Returns the <code>Arn</code> value.

