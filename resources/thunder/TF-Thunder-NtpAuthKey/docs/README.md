# TF::Thunder::NtpAuthKey

`thunder_ntp_auth_key` Provides details about thunder ntp auth key

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::NtpAuthKey",
    "Properties" : {
        "<a href="#algtype" title="AlgType">AlgType</a>" : <i>String</i>,
        "<a href="#asckey" title="AscKey">AscKey</a>" : <i>String</i>,
        "<a href="#encrypted" title="Encrypted">Encrypted</a>" : <i>String</i>,
        "<a href="#hexencrypted" title="HexEncrypted">HexEncrypted</a>" : <i>String</i>,
        "<a href="#hexkey" title="HexKey">HexKey</a>" : <i>String</i>,
        "<a href="#key" title="Key">Key</a>" : <i>Double</i>,
        "<a href="#keytype" title="KeyType">KeyType</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::NtpAuthKey
Properties:
    <a href="#algtype" title="AlgType">AlgType</a>: <i>String</i>
    <a href="#asckey" title="AscKey">AscKey</a>: <i>String</i>
    <a href="#encrypted" title="Encrypted">Encrypted</a>: <i>String</i>
    <a href="#hexencrypted" title="HexEncrypted">HexEncrypted</a>: <i>String</i>
    <a href="#hexkey" title="HexKey">HexKey</a>: <i>String</i>
    <a href="#key" title="Key">Key</a>: <i>Double</i>
    <a href="#keytype" title="KeyType">KeyType</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
</pre>

## Properties

#### AlgType

‘M’: encryption using MD5; ‘SHA’: encryption using SHA; ‘SHA1’: encryption using SHA1;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AscKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encrypted

Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HexEncrypted

Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HexKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

authentication key.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyType

‘ascii’: key string in ASCII form; ‘hex’: key string in hex form;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

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

#### Id

Returns the <code>Id</code> value.

