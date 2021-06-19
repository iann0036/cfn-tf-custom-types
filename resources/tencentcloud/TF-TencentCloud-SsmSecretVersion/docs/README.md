# TF::TencentCloud::SsmSecretVersion

Provide a resource to create a SSM secret version.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::SsmSecretVersion",
    "Properties" : {
        "<a href="#secretbinary" title="SecretBinary">SecretBinary</a>" : <i>String</i>,
        "<a href="#secretname" title="SecretName">SecretName</a>" : <i>String</i>,
        "<a href="#secretstring" title="SecretString">SecretString</a>" : <i>String</i>,
        "<a href="#versionid" title="VersionId">VersionId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::SsmSecretVersion
Properties:
    <a href="#secretbinary" title="SecretBinary">SecretBinary</a>: <i>String</i>
    <a href="#secretname" title="SecretName">SecretName</a>: <i>String</i>
    <a href="#secretstring" title="SecretString">SecretString</a>: <i>String</i>
    <a href="#versionid" title="VersionId">VersionId</a>: <i>String</i>
</pre>

## Properties

#### SecretBinary

The base64-encoded binary secret. secret_binary and secret_string must be set only one, and the maximum support is 4096 bytes. When secret status is `Disabled`, this field will not update anymore.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretName

Name of secret which cannot be repeated in the same region. The maximum length is 128 bytes. The name can only contain English letters, numbers, underscore and hyphen '-'. The first character must be a letter or number.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretString

The string text of secret. secret_binary and secret_string must be set only one, and the maximum support is 4096 bytes. When secret status is `Disabled`, this field will not update anymore.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionId

Version of secret. The maximum length is 64 bytes. The version_id can only contain English letters, numbers, underscore and hyphen '-'. The first character must be a letter or number.

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

