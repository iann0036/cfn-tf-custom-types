# TF::AWS::SecretsmanagerSecretVersion

Provides a resource to manage AWS Secrets Manager secret version including its secret value. To manage secret metadata, see the [`aws_secretsmanager_secret` resource](/docs/providers/aws/r/secretsmanager_secret.html).

~> **NOTE:** If the `AWSCURRENT` staging label is present on this version during resource deletion, that label cannot be removed and will be skipped to prevent errors when fully deleting the secret. That label will leave this secret version active even after the resource is deleted from Terraform unless the secret itself is deleted. Move the `AWSCURRENT` staging label before or after deleting this resource from Terraform to fully trigger version deprecation if necessary.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::SecretsmanagerSecretVersion",
    "Properties" : {
        "<a href="#secretbinary" title="SecretBinary">SecretBinary</a>" : <i>String</i>,
        "<a href="#secretid" title="SecretId">SecretId</a>" : <i>String</i>,
        "<a href="#secretstring" title="SecretString">SecretString</a>" : <i>String</i>,
        "<a href="#versionstages" title="VersionStages">VersionStages</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::SecretsmanagerSecretVersion
Properties:
    <a href="#secretbinary" title="SecretBinary">SecretBinary</a>: <i>String</i>
    <a href="#secretid" title="SecretId">SecretId</a>: <i>String</i>
    <a href="#secretstring" title="SecretString">SecretString</a>: <i>String</i>
    <a href="#versionstages" title="VersionStages">VersionStages</a>: <i>
      - String</i>
</pre>

## Properties

#### SecretBinary

Specifies binary data that you want to encrypt and store in this version of the secret. This is required if secret_string is not set. Needs to be encoded to base64.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretId

Specifies the secret to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret. The secret must already exist.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretString

Specifies text data that you want to encrypt and store in this version of the secret. This is required if secret_binary is not set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionStages

Specifies a list of staging labels that are attached to this version of the secret. A staging label must be unique to a single version of the secret. If you specify a staging label that's already associated with a different version of the same secret then that staging label is automatically removed from the other version and attached to this version. If you do not specify a value, then AWS Secrets Manager automatically moves the staging label `AWSCURRENT` to this new version on creation.

_Required_: No

_Type_: List of String

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

#### Id

Returns the <code>Id</code> value.

#### VersionId

Returns the <code>VersionId</code> value.

