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

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultBackendHttpSettingsName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRedirectConfigurationName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRewriteRuleSetName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathRule

_Required_: No

_Type_: List of <a href="urlpathmap-pathrule.md">PathRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

