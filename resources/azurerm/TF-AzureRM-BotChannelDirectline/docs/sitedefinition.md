# TF::AzureRM::BotChannelDirectline SiteDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#enhancedauthenticationenabled" title="EnhancedAuthenticationEnabled">EnhancedAuthenticationEnabled</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#trustedorigins" title="TrustedOrigins">TrustedOrigins</a>" : <i>[ String, ... ]</i>,
    "<a href="#v1allowed" title="V1Allowed">V1Allowed</a>" : <i>Boolean</i>,
    "<a href="#v3allowed" title="V3Allowed">V3Allowed</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#enhancedauthenticationenabled" title="EnhancedAuthenticationEnabled">EnhancedAuthenticationEnabled</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#trustedorigins" title="TrustedOrigins">TrustedOrigins</a>: <i>
      - String</i>
<a href="#v1allowed" title="V1Allowed">V1Allowed</a>: <i>Boolean</i>
<a href="#v3allowed" title="V3Allowed">V3Allowed</a>: <i>Boolean</i>
</pre>

## Properties

#### Enabled

Enables/Disables this site. Enabled by default.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnhancedAuthenticationEnabled

Enables additional security measures for this site, see [Enhanced Directline Authentication Features](https://blog.botframework.com/2018/09/25/enhanced-direct-line-authentication-features). Disabled by default.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the site.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustedOrigins

This field is required when `is_secure_site_enabled` is enabled. Determines which origins can establish a Directline conversation for this site.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### V1Allowed

Enables v1 of the Directline protocol for this site. Enabled by default.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### V3Allowed

Enables v3 of the Directline protocol for this site. Enabled by default.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

