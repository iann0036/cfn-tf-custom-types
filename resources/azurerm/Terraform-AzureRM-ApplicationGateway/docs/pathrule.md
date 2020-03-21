# Terraform::AzureRM::ApplicationGateway PathRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#backendaddresspoolname" title="BackendAddressPoolName">BackendAddressPoolName</a>" : <i>String</i>,
    "<a href="#backendhttpsettingsname" title="BackendHttpSettingsName">BackendHttpSettingsName</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#paths" title="Paths">Paths</a>" : <i>[ String, ... ]</i>,
    "<a href="#redirectconfigurationname" title="RedirectConfigurationName">RedirectConfigurationName</a>" : <i>String</i>,
    "<a href="#rewriterulesetname" title="RewriteRuleSetName">RewriteRuleSetName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#backendaddresspoolname" title="BackendAddressPoolName">BackendAddressPoolName</a>: <i>String</i>
<a href="#backendhttpsettingsname" title="BackendHttpSettingsName">BackendHttpSettingsName</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#paths" title="Paths">Paths</a>: <i>
      - String</i>
<a href="#redirectconfigurationname" title="RedirectConfigurationName">RedirectConfigurationName</a>: <i>String</i>
<a href="#rewriterulesetname" title="RewriteRuleSetName">RewriteRuleSetName</a>: <i>String</i>
</pre>

## Properties

#### BackendAddressPoolName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendHttpSettingsName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Paths

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectConfigurationName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RewriteRuleSetName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

