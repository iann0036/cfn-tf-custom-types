# TF::GoogleBeta::GoogleAppEngineFlexibleAppVersion HandlersDefinition

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
    "<a href="#script" title="Script">Script</a>" : <i>[ <a href="scriptdefinition.md">ScriptDefinition</a>, ... ]</i>,
    "<a href="#staticfiles" title="StaticFiles">StaticFiles</a>" : <i>[ <a href="staticfilesdefinition.md">StaticFilesDefinition</a>, ... ]</i>
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
      - <a href="scriptdefinition.md">ScriptDefinition</a></i>
<a href="#staticfiles" title="StaticFiles">StaticFiles</a>: <i>
      - <a href="staticfilesdefinition.md">StaticFilesDefinition</a></i>
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

_Type_: List of <a href="scriptdefinition.md">ScriptDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticFiles

_Required_: No

_Type_: List of <a href="staticfilesdefinition.md">StaticFilesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

