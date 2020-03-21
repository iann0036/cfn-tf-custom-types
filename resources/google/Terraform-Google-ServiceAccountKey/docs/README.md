# Terraform::Google::ServiceAccountKey

Creates and manages service account key-pairs, which allow the user to establish identity of a service account outside of GCP. For more information, see [the official documentation](https://cloud.google.com/iam/docs/creating-managing-service-account-keys) and [API](https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ServiceAccountKey",
    "Properties" : {
        "<a href="#keyalgorithm" title="KeyAlgorithm">KeyAlgorithm</a>" : <i>String</i>,
        "<a href="#pgpkey" title="PgpKey">PgpKey</a>" : <i>String</i>,
        "<a href="#privatekeytype" title="PrivateKeyType">PrivateKeyType</a>" : <i>String</i>,
        "<a href="#publickeytype" title="PublicKeyType">PublicKeyType</a>" : <i>String</i>,
        "<a href="#serviceaccountid" title="ServiceAccountId">ServiceAccountId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ServiceAccountKey
Properties:
    <a href="#keyalgorithm" title="KeyAlgorithm">KeyAlgorithm</a>: <i>String</i>
    <a href="#pgpkey" title="PgpKey">PgpKey</a>: <i>String</i>
    <a href="#privatekeytype" title="PrivateKeyType">PrivateKeyType</a>: <i>String</i>
    <a href="#publickeytype" title="PublicKeyType">PublicKeyType</a>: <i>String</i>
    <a href="#serviceaccountid" title="ServiceAccountId">ServiceAccountId</a>: <i>String</i>
</pre>

## Properties

#### KeyAlgorithm

The algorithm used to generate the key. KEY_ALG_RSA_2048 is the default algorithm.
Valid values are listed at
[ServiceAccountPrivateKeyType](https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKeyAlgorithm)
(only used on create).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PgpKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKeyType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicKeyType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccountId

The Service account id of the Key Pair. This can be a string in the format
`{ACCOUNT}` or `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}`, where `{ACCOUNT}` is the email address or
unique id of the service account. If the `{ACCOUNT}` syntax is used, the project will be inferred from the account.

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

#### Name

Returns the <code>Name</code> value.

#### PrivateKey

Returns the <code>PrivateKey</code> value.

#### PrivateKeyEncrypted

Returns the <code>PrivateKeyEncrypted</code> value.

#### PrivateKeyFingerprint

Returns the <code>PrivateKeyFingerprint</code> value.

#### PublicKey

Returns the <code>PublicKey</code> value.

#### ValidAfter

Returns the <code>ValidAfter</code> value.

#### ValidBefore

Returns the <code>ValidBefore</code> value.

