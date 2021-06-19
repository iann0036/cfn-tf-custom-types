# TF::Thunder::SlbTemplatePersistCookie

`thunder_slb_template_persist_cookie` Provides details about thunder slb template persist cookie

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplatePersistCookie",
    "Properties" : {
        "<a href="#cookiename" title="CookieName">CookieName</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#donthonorconnrules" title="DontHonorConnRules">DontHonorConnRules</a>" : <i>Double</i>,
        "<a href="#encryptlevel" title="EncryptLevel">EncryptLevel</a>" : <i>Double</i>,
        "<a href="#encrypted" title="Encrypted">Encrypted</a>" : <i>String</i>,
        "<a href="#expire" title="Expire">Expire</a>" : <i>Double</i>,
        "<a href="#httponly" title="Httponly">Httponly</a>" : <i>Double</i>,
        "<a href="#insertalways" title="InsertAlways">InsertAlways</a>" : <i>Double</i>,
        "<a href="#matchtype" title="MatchType">MatchType</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#passphrase" title="PassPhrase">PassPhrase</a>" : <i>String</i>,
        "<a href="#passthru" title="PassThru">PassThru</a>" : <i>Double</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
        "<a href="#scanallmembers" title="ScanAllMembers">ScanAllMembers</a>" : <i>Double</i>,
        "<a href="#secure" title="Secure">Secure</a>" : <i>Double</i>,
        "<a href="#server" title="Server">Server</a>" : <i>Double</i>,
        "<a href="#serverservicegroup" title="ServerServiceGroup">ServerServiceGroup</a>" : <i>Double</i>,
        "<a href="#servicegroup" title="ServiceGroup">ServiceGroup</a>" : <i>Double</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbTemplatePersistCookie
Properties:
    <a href="#cookiename" title="CookieName">CookieName</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#donthonorconnrules" title="DontHonorConnRules">DontHonorConnRules</a>: <i>Double</i>
    <a href="#encryptlevel" title="EncryptLevel">EncryptLevel</a>: <i>Double</i>
    <a href="#encrypted" title="Encrypted">Encrypted</a>: <i>String</i>
    <a href="#expire" title="Expire">Expire</a>: <i>Double</i>
    <a href="#httponly" title="Httponly">Httponly</a>: <i>Double</i>
    <a href="#insertalways" title="InsertAlways">InsertAlways</a>: <i>Double</i>
    <a href="#matchtype" title="MatchType">MatchType</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#passphrase" title="PassPhrase">PassPhrase</a>: <i>String</i>
    <a href="#passthru" title="PassThru">PassThru</a>: <i>Double</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
    <a href="#scanallmembers" title="ScanAllMembers">ScanAllMembers</a>: <i>Double</i>
    <a href="#secure" title="Secure">Secure</a>: <i>Double</i>
    <a href="#server" title="Server">Server</a>: <i>Double</i>
    <a href="#serverservicegroup" title="ServerServiceGroup">ServerServiceGroup</a>: <i>Double</i>
    <a href="#servicegroup" title="ServiceGroup">ServiceGroup</a>: <i>Double</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
</pre>

## Properties

#### CookieName

Set cookie name (Cookie name, default “sto-id”).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

Set cookie domain.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DontHonorConnRules

Do not observe connection rate rules.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptLevel

Encryption level for cookie name / value.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encrypted

Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expire

Set cookie expiration time (Expiration in seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Httponly

Enable HttpOnly attribute.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsertAlways

Insert persist cookie to every reponse.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchType

Persist for server, default is port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Cookie persistence (Cookie persistence template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PassPhrase

Set passphrase for encryption.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PassThru

Pass thru mode - Server sends the persist cookie.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

Set cookie path (Cookie path, default is “/”).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScanAllMembers

Persist within the same server SCAN.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secure

Enable secure attribute.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

Persist to the same server, default is port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerServiceGroup

Persist to the same server and within the same service group.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceGroup

Persist within the same service group.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

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

