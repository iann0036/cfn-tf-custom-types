# TF::DigitalOcean::Loadbalancer StickySessionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cookiename" title="CookieName">CookieName</a>" : <i>String</i>,
    "<a href="#cookiettlseconds" title="CookieTtlSeconds">CookieTtlSeconds</a>" : <i>Double</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#cookiename" title="CookieName">CookieName</a>: <i>String</i>
<a href="#cookiettlseconds" title="CookieTtlSeconds">CookieTtlSeconds</a>: <i>Double</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### CookieName

The name to be used for the cookie sent to the client. This attribute is required when using `cookies` for the sticky sessions type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookieTtlSeconds

The number of seconds until the cookie set by the Load Balancer expires. This attribute is required when using `cookies` for the sticky sessions type.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

An attribute indicating how and if requests from a client will be persistently served by the same backend Droplet. The possible values are `cookies` or `none`. If not specified, the default value is `none`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

