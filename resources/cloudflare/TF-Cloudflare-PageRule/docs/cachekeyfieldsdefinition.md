# TF::Cloudflare::PageRule CacheKeyFieldsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cookie" title="Cookie">Cookie</a>" : <i>[ <a href="cookiedefinition.md">CookieDefinition</a>, ... ]</i>,
    "<a href="#header" title="Header">Header</a>" : <i>[ <a href="headerdefinition.md">HeaderDefinition</a>, ... ]</i>,
    "<a href="#host" title="Host">Host</a>" : <i>[ <a href="hostdefinition.md">HostDefinition</a>, ... ]</i>,
    "<a href="#querystring" title="QueryString">QueryString</a>" : <i>[ <a href="querystringdefinition.md">QueryStringDefinition</a>, ... ]</i>,
    "<a href="#user" title="User">User</a>" : <i>[ <a href="userdefinition.md">UserDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cookie" title="Cookie">Cookie</a>: <i>
      - <a href="cookiedefinition.md">CookieDefinition</a></i>
<a href="#header" title="Header">Header</a>: <i>
      - <a href="headerdefinition.md">HeaderDefinition</a></i>
<a href="#host" title="Host">Host</a>: <i>
      - <a href="hostdefinition.md">HostDefinition</a></i>
<a href="#querystring" title="QueryString">QueryString</a>: <i>
      - <a href="querystringdefinition.md">QueryStringDefinition</a></i>
<a href="#user" title="User">User</a>: <i>
      - <a href="userdefinition.md">UserDefinition</a></i>
</pre>

## Properties

#### Cookie

_Required_: No

_Type_: List of <a href="cookiedefinition.md">CookieDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Header

_Required_: No

_Type_: List of <a href="headerdefinition.md">HeaderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host

_Required_: No

_Type_: List of <a href="hostdefinition.md">HostDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryString

_Required_: No

_Type_: List of <a href="querystringdefinition.md">QueryStringDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

_Required_: No

_Type_: List of <a href="userdefinition.md">UserDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

