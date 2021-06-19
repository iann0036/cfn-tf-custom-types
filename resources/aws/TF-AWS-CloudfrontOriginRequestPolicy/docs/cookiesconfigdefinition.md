# TF::AWS::CloudfrontOriginRequestPolicy CookiesConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cookiebehavior" title="CookieBehavior">CookieBehavior</a>" : <i>String</i>,
    "<a href="#cookies" title="Cookies">Cookies</a>" : <i>[ <a href="cookiesdefinition.md">CookiesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cookiebehavior" title="CookieBehavior">CookieBehavior</a>: <i>String</i>
<a href="#cookies" title="Cookies">Cookies</a>: <i>
      - <a href="cookiesdefinition.md">CookiesDefinition</a></i>
</pre>

## Properties

#### CookieBehavior

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cookies

_Required_: No

_Type_: List of <a href="cookiesdefinition.md">CookiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

