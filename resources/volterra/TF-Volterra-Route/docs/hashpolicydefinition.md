# TF::Volterra::Route HashPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#headername" title="HeaderName">HeaderName</a>" : <i>String</i>,
    "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>Boolean</i>,
    "<a href="#terminal" title="Terminal">Terminal</a>" : <i>Boolean</i>,
    "<a href="#cookie" title="Cookie">Cookie</a>" : <i>[ <a href="cookiedefinition.md">CookieDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#headername" title="HeaderName">HeaderName</a>: <i>String</i>
<a href="#sourceip" title="SourceIp">SourceIp</a>: <i>Boolean</i>
<a href="#terminal" title="Terminal">Terminal</a>: <i>Boolean</i>
<a href="#cookie" title="Cookie">Cookie</a>: <i>
      - <a href="cookiedefinition.md">CookieDefinition</a></i>
</pre>

## Properties

#### HeaderName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Terminal

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cookie

_Required_: No

_Type_: List of <a href="cookiedefinition.md">CookieDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

