# TF::AzureRM::Frontdoor ForwardingConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#backendpoolname" title="BackendPoolName">BackendPoolName</a>" : <i>String</i>,
    "<a href="#cacheenabled" title="CacheEnabled">CacheEnabled</a>" : <i>Boolean</i>,
    "<a href="#cachequeryparameterstripdirective" title="CacheQueryParameterStripDirective">CacheQueryParameterStripDirective</a>" : <i>String</i>,
    "<a href="#cacheusedynamiccompression" title="CacheUseDynamicCompression">CacheUseDynamicCompression</a>" : <i>Boolean</i>,
    "<a href="#customforwardingpath" title="CustomForwardingPath">CustomForwardingPath</a>" : <i>String</i>,
    "<a href="#forwardingprotocol" title="ForwardingProtocol">ForwardingProtocol</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#backendpoolname" title="BackendPoolName">BackendPoolName</a>: <i>String</i>
<a href="#cacheenabled" title="CacheEnabled">CacheEnabled</a>: <i>Boolean</i>
<a href="#cachequeryparameterstripdirective" title="CacheQueryParameterStripDirective">CacheQueryParameterStripDirective</a>: <i>String</i>
<a href="#cacheusedynamiccompression" title="CacheUseDynamicCompression">CacheUseDynamicCompression</a>: <i>Boolean</i>
<a href="#customforwardingpath" title="CustomForwardingPath">CustomForwardingPath</a>: <i>String</i>
<a href="#forwardingprotocol" title="ForwardingProtocol">ForwardingProtocol</a>: <i>String</i>
</pre>

## Properties

#### BackendPoolName

Specifies the name of the Backend Pool to forward the incoming traffic to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheEnabled

Specifies whether to Enable caching or not. Valid options are `true` or `false`. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheQueryParameterStripDirective

Defines cache behaviour in relation to query string parameters. Valid options are `StripAll` or `StripNone`. Defaults to `StripAll`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheUseDynamicCompression

Whether to use dynamic compression when caching. Valid options are `true` or `false`. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomForwardingPath

Path to use when constructing the request to forward to the backend. This functions as a URL Rewrite. Default behaviour preserves the URL path.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardingProtocol

Protocol to use when redirecting. Valid options are `HttpOnly`, `HttpsOnly`, or `MatchRequest`. Defaults to `HttpsOnly`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

