# TF::AWS::IamAccessKey

Provides an IAM access key. This is a set of credentials that allow API requests to be made as an IAM user.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::IamAccessKey",
    "Properties" : {
        "<a href="#pgpkey" title="PgpKey">PgpKey</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#user" title="User">User</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::IamAccessKey
Properties:
    <a href="#pgpkey" title="PgpKey">PgpKey</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#user" title="User">User</a>: <i>String</i>
</pre>

## Properties

#### PgpKey

Either a base-64 encoded PGP public key, or a
keybase username in the form `keybase:some_person_that_exists`, for use
in the `encrypted_secret` output attribute.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

The access key status to apply. Defaults to `Active`.
Valid values are `Active` and `Inactive`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

The IAM user to associate with this access key.

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

#### CreateDate

Returns the <code>CreateDate</code> value.

#### EncryptedSecret

Returns the <code>EncryptedSecret</code> value.

#### Id

Returns the <code>Id</code> value.

#### KeyFingerprint

Returns the <code>KeyFingerprint</code> value.

#### Secret

Returns the <code>Secret</code> value.

#### SesSmtpPasswordV4

Returns the <code>SesSmtpPasswordV4</code> value.

