# Terraform::BIGIP::LtmPersistenceProfileCookie

Configures a cookie persistence profile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::BIGIP::LtmPersistenceProfileCookie",
    "Properties" : {
        "<a href="#alwayssend" title="AlwaysSend">AlwaysSend</a>" : <i>String</i>,
        "<a href="#appservice" title="AppService">AppService</a>" : <i>String</i>,
        "<a href="#cookieencryption" title="CookieEncryption">CookieEncryption</a>" : <i>String</i>,
        "<a href="#cookieencryptionpassphrase" title="CookieEncryptionPassphrase">CookieEncryptionPassphrase</a>" : <i>String</i>,
        "<a href="#cookiename" title="CookieName">CookieName</a>" : <i>String</i>,
        "<a href="#defaultsfrom" title="DefaultsFrom">DefaultsFrom</a>" : <i>String</i>,
        "<a href="#expiration" title="Expiration">Expiration</a>" : <i>String</i>,
        "<a href="#hashlength" title="HashLength">HashLength</a>" : <i>Double</i>,
        "<a href="#hashoffset" title="HashOffset">HashOffset</a>" : <i>Double</i>,
        "<a href="#httponly" title="Httponly">Httponly</a>" : <i>String</i>,
        "<a href="#matchacrosspools" title="MatchAcrossPools">MatchAcrossPools</a>" : <i>String</i>,
        "<a href="#matchacrossservices" title="MatchAcrossServices">MatchAcrossServices</a>" : <i>String</i>,
        "<a href="#matchacrossvirtuals" title="MatchAcrossVirtuals">MatchAcrossVirtuals</a>" : <i>String</i>,
        "<a href="#mirror" title="Mirror">Mirror</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#overrideconnlimit" title="OverrideConnLimit">OverrideConnLimit</a>" : <i>String</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::BIGIP::LtmPersistenceProfileCookie
Properties:
    <a href="#alwayssend" title="AlwaysSend">AlwaysSend</a>: <i>String</i>
    <a href="#appservice" title="AppService">AppService</a>: <i>String</i>
    <a href="#cookieencryption" title="CookieEncryption">CookieEncryption</a>: <i>String</i>
    <a href="#cookieencryptionpassphrase" title="CookieEncryptionPassphrase">CookieEncryptionPassphrase</a>: <i>String</i>
    <a href="#cookiename" title="CookieName">CookieName</a>: <i>String</i>
    <a href="#defaultsfrom" title="DefaultsFrom">DefaultsFrom</a>: <i>String</i>
    <a href="#expiration" title="Expiration">Expiration</a>: <i>String</i>
    <a href="#hashlength" title="HashLength">HashLength</a>: <i>Double</i>
    <a href="#hashoffset" title="HashOffset">HashOffset</a>: <i>Double</i>
    <a href="#httponly" title="Httponly">Httponly</a>: <i>String</i>
    <a href="#matchacrosspools" title="MatchAcrossPools">MatchAcrossPools</a>: <i>String</i>
    <a href="#matchacrossservices" title="MatchAcrossServices">MatchAcrossServices</a>: <i>String</i>
    <a href="#matchacrossvirtuals" title="MatchAcrossVirtuals">MatchAcrossVirtuals</a>: <i>String</i>
    <a href="#mirror" title="Mirror">Mirror</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#overrideconnlimit" title="OverrideConnLimit">OverrideConnLimit</a>: <i>String</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
</pre>

## Properties

#### AlwaysSend

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppService

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookieEncryption

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookieEncryptionPassphrase

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookieName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultsFrom

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expiration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HashLength

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HashOffset

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Httponly

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchAcrossPools

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchAcrossServices

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchAcrossVirtuals

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mirror

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideConnLimit

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

