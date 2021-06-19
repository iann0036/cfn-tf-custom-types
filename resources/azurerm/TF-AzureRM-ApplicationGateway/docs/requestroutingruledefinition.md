# TF::AzureRM::ApplicationGateway RequestRoutingRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#backendaddresspoolname" title="BackendAddressPoolName">BackendAddressPoolName</a>" : <i>String</i>,
    "<a href="#backendhttpsettingsname" title="BackendHttpSettingsName">BackendHttpSettingsName</a>" : <i>String</i>,
    "<a href="#httplistenername" title="HttpListenerName">HttpListenerName</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#redirectconfigurationname" title="RedirectConfigurationName">RedirectConfigurationName</a>" : <i>String</i>,
    "<a href="#rewriterulesetname" title="RewriteRuleSetName">RewriteRuleSetName</a>" : <i>String</i>,
    "<a href="#ruletype" title="RuleType">RuleType</a>" : <i>String</i>,
    "<a href="#urlpathmapname" title="UrlPathMapName">UrlPathMapName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#backendaddresspoolname" title="BackendAddressPoolName">BackendAddressPoolName</a>: <i>String</i>
<a href="#backendhttpsettingsname" title="BackendHttpSettingsName">BackendHttpSettingsName</a>: <i>String</i>
<a href="#httplistenername" title="HttpListenerName">HttpListenerName</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#redirectconfigurationname" title="RedirectConfigurationName">RedirectConfigurationName</a>: <i>String</i>
<a href="#rewriterulesetname" title="RewriteRuleSetName">RewriteRuleSetName</a>: <i>String</i>
<a href="#ruletype" title="RuleType">RuleType</a>: <i>String</i>
<a href="#urlpathmapname" title="UrlPathMapName">UrlPathMapName</a>: <i>String</i>
</pre>

## Properties

#### BackendAddressPoolName

The Name of the Backend Address Pool which should be used for this Routing Rule. Cannot be set if `redirect_configuration_name` is set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendHttpSettingsName

The Name of the Backend HTTP Settings Collection which should be used for this Routing Rule. Cannot be set if `redirect_configuration_name` is set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpListenerName

The Name of the HTTP Listener which should be used for this Routing Rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Name of this Request Routing Rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectConfigurationName

The Name of the Redirect Configuration which should be used for this Routing Rule. Cannot be set if either `backend_address_pool_name` or `backend_http_settings_name` is set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RewriteRuleSetName

The Name of the Rewrite Rule Set which should be used for this Routing Rule. Only valid for v2 SKUs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleType

The Type of Routing that should be used for this Rule. Possible values are `Basic` and `PathBasedRouting`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlPathMapName

The Name of the URL Path Map which should be associated with this Routing Rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

