# TF::AVI::Applicationpersistenceprofile HttpCookiePersistenceProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#alwayssendcookie" title="AlwaysSendCookie">AlwaysSendCookie</a>" : <i>Boolean</i>,
    "<a href="#cookiename" title="CookieName">CookieName</a>" : <i>String</i>,
    "<a href="#encryptionkey" title="EncryptionKey">EncryptionKey</a>" : <i>String</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
    "<a href="#key" title="Key">Key</a>" : <i>[ <a href="keydefinition.md">KeyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#alwayssendcookie" title="AlwaysSendCookie">AlwaysSendCookie</a>: <i>Boolean</i>
<a href="#cookiename" title="CookieName">CookieName</a>: <i>String</i>
<a href="#encryptionkey" title="EncryptionKey">EncryptionKey</a>: <i>String</i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
<a href="#key" title="Key">Key</a>: <i>
      - <a href="keydefinition.md">KeyDefinition</a></i>
</pre>

## Properties

#### AlwaysSendCookie

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookieName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

_Required_: No

_Type_: List of <a href="keydefinition.md">KeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

