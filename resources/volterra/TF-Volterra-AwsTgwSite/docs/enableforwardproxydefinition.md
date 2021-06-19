# TF::Volterra::AwsTgwSite EnableForwardProxyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#connectiontimeout" title="ConnectionTimeout">ConnectionTimeout</a>" : <i>Double</i>,
    "<a href="#maxconnectattempts" title="MaxConnectAttempts">MaxConnectAttempts</a>" : <i>Double</i>,
    "<a href="#nointerception" title="NoInterception">NoInterception</a>" : <i>Boolean</i>,
    "<a href="#whitelistedports" title="WhiteListedPorts">WhiteListedPorts</a>" : <i>[ Double, ... ]</i>,
    "<a href="#whitelistedprefixes" title="WhiteListedPrefixes">WhiteListedPrefixes</a>" : <i>[ String, ... ]</i>,
    "<a href="#tlsintercept" title="TlsIntercept">TlsIntercept</a>" : <i>[ <a href="tlsinterceptdefinition.md">TlsInterceptDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#connectiontimeout" title="ConnectionTimeout">ConnectionTimeout</a>: <i>Double</i>
<a href="#maxconnectattempts" title="MaxConnectAttempts">MaxConnectAttempts</a>: <i>Double</i>
<a href="#nointerception" title="NoInterception">NoInterception</a>: <i>Boolean</i>
<a href="#whitelistedports" title="WhiteListedPorts">WhiteListedPorts</a>: <i>
      - Double</i>
<a href="#whitelistedprefixes" title="WhiteListedPrefixes">WhiteListedPrefixes</a>: <i>
      - String</i>
<a href="#tlsintercept" title="TlsIntercept">TlsIntercept</a>: <i>
      - <a href="tlsinterceptdefinition.md">TlsInterceptDefinition</a></i>
</pre>

## Properties

#### ConnectionTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConnectAttempts

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoInterception

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WhiteListedPorts

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WhiteListedPrefixes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsIntercept

_Required_: No

_Type_: List of <a href="tlsinterceptdefinition.md">TlsInterceptDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

