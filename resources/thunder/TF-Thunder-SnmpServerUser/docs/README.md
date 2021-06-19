# TF::Thunder::SnmpServerUser

`thunder_snmp_server_user` Provides details about thunder snmp server user

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SnmpServerUser",
    "Properties" : {
        "<a href="#authval" title="AuthVal">AuthVal</a>" : <i>String</i>,
        "<a href="#encpasswd" title="Encpasswd">Encpasswd</a>" : <i>String</i>,
        "<a href="#group" title="Group">Group</a>" : <i>String</i>,
        "<a href="#passwd" title="Passwd">Passwd</a>" : <i>String</i>,
        "<a href="#priv" title="Priv">Priv</a>" : <i>String</i>,
        "<a href="#privpwencrypted" title="PrivPwEncrypted">PrivPwEncrypted</a>" : <i>String</i>,
        "<a href="#pwencrypted" title="PwEncrypted">PwEncrypted</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#v3" title="V3">V3</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SnmpServerUser
Properties:
    <a href="#authval" title="AuthVal">AuthVal</a>: <i>String</i>
    <a href="#encpasswd" title="Encpasswd">Encpasswd</a>: <i>String</i>
    <a href="#group" title="Group">Group</a>: <i>String</i>
    <a href="#passwd" title="Passwd">Passwd</a>: <i>String</i>
    <a href="#priv" title="Priv">Priv</a>: <i>String</i>
    <a href="#privpwencrypted" title="PrivPwEncrypted">PrivPwEncrypted</a>: <i>String</i>
    <a href="#pwencrypted" title="PwEncrypted">PwEncrypted</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#v3" title="V3">V3</a>: <i>String</i>
</pre>

## Properties

#### AuthVal

‘md5’: Use HMAC MD5 algorithm for authentication; ‘sha’: Use HMAC SHA algorithm for authentication;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encpasswd

Passphrase for encryption.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

Group to which the user belongs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Passwd

Password of this user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priv

‘des’: DES encryption alogrithm; ‘aes’: AES encryption alogrithm;  (Encryption type).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivPwEncrypted

Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED passphrase string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PwEncrypted

Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED passphrase string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

Name of the user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### V3

‘auth’: Using the authNoPriv Security Level; ‘noauth’: Using the noAuthNoPriv Security Level;.

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

