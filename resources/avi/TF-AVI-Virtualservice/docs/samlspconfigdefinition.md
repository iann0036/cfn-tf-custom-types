# TF::AVI::Virtualservice SamlSpConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cookiename" title="CookieName">CookieName</a>" : <i>String</i>,
    "<a href="#cookietimeout" title="CookieTimeout">CookieTimeout</a>" : <i>Double</i>,
    "<a href="#entityid" title="EntityId">EntityId</a>" : <i>String</i>,
    "<a href="#signingsslkeyandcertificateref" title="SigningSslKeyAndCertificateRef">SigningSslKeyAndCertificateRef</a>" : <i>String</i>,
    "<a href="#singlesignonurl" title="SingleSignonUrl">SingleSignonUrl</a>" : <i>String</i>,
    "<a href="#useidpsessiontimeout" title="UseIdpSessionTimeout">UseIdpSessionTimeout</a>" : <i>Boolean</i>,
    "<a href="#key" title="Key">Key</a>" : <i>[ <a href="keydefinition.md">KeyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cookiename" title="CookieName">CookieName</a>: <i>String</i>
<a href="#cookietimeout" title="CookieTimeout">CookieTimeout</a>: <i>Double</i>
<a href="#entityid" title="EntityId">EntityId</a>: <i>String</i>
<a href="#signingsslkeyandcertificateref" title="SigningSslKeyAndCertificateRef">SigningSslKeyAndCertificateRef</a>: <i>String</i>
<a href="#singlesignonurl" title="SingleSignonUrl">SingleSignonUrl</a>: <i>String</i>
<a href="#useidpsessiontimeout" title="UseIdpSessionTimeout">UseIdpSessionTimeout</a>: <i>Boolean</i>
<a href="#key" title="Key">Key</a>: <i>
      - <a href="keydefinition.md">KeyDefinition</a></i>
</pre>

## Properties

#### CookieName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookieTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EntityId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SigningSslKeyAndCertificateRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SingleSignonUrl

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseIdpSessionTimeout

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

_Required_: No

_Type_: List of <a href="keydefinition.md">KeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

