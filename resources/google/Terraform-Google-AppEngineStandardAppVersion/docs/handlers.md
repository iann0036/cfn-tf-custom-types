# Terraform::Google::AppEngineStandardAppVersion Handlers

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authfailaction" title="AuthFailAction">AuthFailAction</a>" : <i>String</i>,
    "<a href="#login" title="Login">Login</a>" : <i>String</i>,
    "<a href="#redirecthttpresponsecode" title="RedirectHttpResponseCode">RedirectHttpResponseCode</a>" : <i>String</i>,
    "<a href="#securitylevel" title="SecurityLevel">SecurityLevel</a>" : <i>String</i>,
    "<a href="#urlregex" title="UrlRegex">UrlRegex</a>" : <i>String</i>,
    "<a href="#script" title="Script">Script</a>" : <i>[ &lt;a href=&#34;handlers-script.md&#34;&gt;Script&lt;/a&gt;, ... ]</i>,
    "<a href="#staticfiles" title="StaticFiles">StaticFiles</a>" : <i>[ &lt;a href=&#34;handlers-staticfiles.md&#34;&gt;StaticFiles&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#authfailaction" title="AuthFailAction">AuthFailAction</a>: <i>String</i>
<a href="#login" title="Login">Login</a>: <i>String</i>
<a href="#redirecthttpresponsecode" title="RedirectHttpResponseCode">RedirectHttpResponseCode</a>: <i>String</i>
<a href="#securitylevel" title="SecurityLevel">SecurityLevel</a>: <i>String</i>
<a href="#urlregex" title="UrlRegex">UrlRegex</a>: <i>String</i>
<a href="#script" title="Script">Script</a>: <i>
      - &lt;a href=&#34;handlers-script.md&#34;&gt;Script&lt;/a&gt;</i>
<a href="#staticfiles" title="StaticFiles">StaticFiles</a>: <i>
      - &lt;a href=&#34;handlers-staticfiles.md&#34;&gt;StaticFiles&lt;/a&gt;</i>
</pre>

## Properties

#### AuthFailAction

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Login

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectHttpResponseCode

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityLevel

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlRegex

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Script

_Required_: No
_Type_: List of &lt;a href=&#34;handlers-script.md&#34;&gt;Script&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticFiles

_Required_: No
_Type_: List of &lt;a href=&#34;handlers-staticfiles.md&#34;&gt;StaticFiles&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

