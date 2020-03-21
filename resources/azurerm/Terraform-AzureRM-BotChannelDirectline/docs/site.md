# Terraform::AzureRM::BotChannelDirectline Site

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

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnhancedAuthenticationEnabled

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustedOrigins

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### V1Allowed

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### V3Allowed

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

