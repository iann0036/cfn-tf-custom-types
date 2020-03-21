# Terraform::OpenTelekomCloud::LbPoolV2 Persistence

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cookiename" title="CookieName">CookieName</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#cookiename" title="CookieName">CookieName</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### CookieName

The name of the cookie if persistence mode is set
appropriately. Required if `type = APP_COOKIE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of persistence mode. The current specification
supports SOURCE_IP, HTTP_COOKIE, and APP_COOKIE.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

