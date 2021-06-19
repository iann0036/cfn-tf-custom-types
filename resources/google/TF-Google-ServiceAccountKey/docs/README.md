# TF::Google::ServiceAccountKey

Creates and manages service account keys, which allow the use of a service account outside of Google Cloud. 

* [API documentation](https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::ServiceAccountKey",
    "Properties" : {
        "<a href="#keepers" title="Keepers">Keepers</a>" : <i>[ <a href="keepersdefinition.md">KeepersDefinition</a>, ... ]</i>,
        "<a href="#keyalgorithm" title="KeyAlgorithm">KeyAlgorithm</a>" : <i>String</i>,
        "<a href="#privatekeytype" title="PrivateKeyType">PrivateKeyType</a>" : <i>String</i>,
        "<a href="#publickeydata" title="PublicKeyData">PublicKeyData</a>" : <i>String</i>,
        "<a href="#publickeytype" title="PublicKeyType">PublicKeyType</a>" : <i>String</i>,
        "<a href="#serviceaccountid" title="ServiceAccountId">ServiceAccountId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::ServiceAccountKey
Properties:
    <a href="#keepers" title="Keepers">Keepers</a>: <i>
      - <a href="keepersdefinition.md">KeepersDefinition</a></i>
    <a href="#keyalgorithm" title="KeyAlgorithm">KeyAlgorithm</a>: <i>String</i>
    <a href="#privatekeytype" title="PrivateKeyType">PrivateKeyType</a>: <i>String</i>
    <a href="#publickeydata" title="PublicKeyData">PublicKeyData</a>: <i>String</i>
    <a href="#publickeytype" title="PublicKeyType">PublicKeyType</a>: <i>String</i>
    <a href="#serviceaccountid" title="ServiceAccountId">ServiceAccountId</a>: <i>String</i>
</pre>

## Properties

#### Keepers

_Required_: No

_Type_: List of <a href="keepersdefinition.md">KeepersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyAlgorithm

The algorithm used to generate the key. KEY_ALG_RSA_2048 is the default algorithm.
Valid values are listed at
[ServiceAccountPrivateKeyType](https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKeyAlgorithm)
(only used on create).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKeyType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicKeyData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicKeyType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccountId

The Service account id of the Key. This can be a string in the format
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

#### Id

Returns the <code>Id</code> value.

#### Name

Returns the <code>Name</code> value.

#### PrivateKey

Returns the <code>PrivateKey</code> value.

#### PublicKey

Returns the <code>PublicKey</code> value.

#### ValidAfter

Returns the <code>ValidAfter</code> value.

#### ValidBefore

Returns the <code>ValidBefore</code> value.

