# Terraform::AzureRM::ApplicationGateway UrlPathMap

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultbackendaddresspoolname" title="DefaultBackendAddressPoolName">DefaultBackendAddressPoolName</a>" : <i>String</i>,
    "<a href="#defaultbackendhttpsettingsname" title="DefaultBackendHttpSettingsName">DefaultBackendHttpSettingsName</a>" : <i>String</i>,
    "<a href="#defaultredirectconfigurationname" title="DefaultRedirectConfigurationName">DefaultRedirectConfigurationName</a>" : <i>String</i>,
    "<a href="#defaultrewriterulesetname" title="DefaultRewriteRuleSetName">DefaultRewriteRuleSetName</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#pathrule" title="PathRule">PathRule</a>" : <i>[ <a href="urlpathmap-pathrule.md">PathRule</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultbackendaddresspoolname" title="DefaultBackendAddressPoolName">DefaultBackendAddressPoolName</a>: <i>String</i>
<a href="#defaultbackendhttpsettingsname" title="DefaultBackendHttpSettingsName">DefaultBackendHttpSettingsName</a>: <i>String</i>
<a href="#defaultredirectconfigurationname" title="DefaultRedirectConfigurationName">DefaultRedirectConfigurationName</a>: <i>String</i>
<a href="#defaultrewriterulesetname" title="DefaultRewriteRuleSetName">DefaultRewriteRuleSetName</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#pathrule" title="PathRule">PathRule</a>: <i>
      - <a href="urlpathmap-pathrule.md">PathRule</a></i>
</pre>

## Properties

#### DefaultBackendAddressPoolName

The Name of the Default Backend Address Pool which should be used for this URL Path Map. Cannot be set if `default_redirect_configuration_name` is set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultBackendHttpSettingsName

The Name of the Default Backend HTTP Settings Collection which should be used for this URL Path Map. Cannot be set if `default_redirect_configuration_name` is set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRedirectConfigurationName

The Name of the Default Redirect Configuration which should be used for this URL Path Map. Cannot be set if either `default_backend_address_pool_name` or `default_backend_http_settings_name` is set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRewriteRuleSetName

The Name of the Default Rewrite Rule Set which should be used for this URL Path Map. Only valid for v2 SKUs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Name of the URL Path Map.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathRule

_Required_: No

_Type_: List of <a href="urlpathmap-pathrule.md">PathRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

