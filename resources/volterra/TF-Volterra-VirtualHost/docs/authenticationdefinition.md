# TF::Volterra::VirtualHost AuthenticationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#redirectdynamic" title="RedirectDynamic">RedirectDynamic</a>" : <i>Boolean</i>,
    "<a href="#redirecturl" title="RedirectUrl">RedirectUrl</a>" : <i>String</i>,
    "<a href="#useauthobjectconfig" title="UseAuthObjectConfig">UseAuthObjectConfig</a>" : <i>Boolean</i>,
    "<a href="#authconfig" title="AuthConfig">AuthConfig</a>" : <i>[ <a href="authconfigdefinition.md">AuthConfigDefinition</a>, ... ]</i>,
    "<a href="#cookieparams" title="CookieParams">CookieParams</a>" : <i>[ <a href="cookieparamsdefinition.md">CookieParamsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#redirectdynamic" title="RedirectDynamic">RedirectDynamic</a>: <i>Boolean</i>
<a href="#redirecturl" title="RedirectUrl">RedirectUrl</a>: <i>String</i>
<a href="#useauthobjectconfig" title="UseAuthObjectConfig">UseAuthObjectConfig</a>: <i>Boolean</i>
<a href="#authconfig" title="AuthConfig">AuthConfig</a>: <i>
      - <a href="authconfigdefinition.md">AuthConfigDefinition</a></i>
<a href="#cookieparams" title="CookieParams">CookieParams</a>: <i>
      - <a href="cookieparamsdefinition.md">CookieParamsDefinition</a></i>
</pre>

## Properties

#### RedirectDynamic

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseAuthObjectConfig

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthConfig

_Required_: No

_Type_: List of <a href="authconfigdefinition.md">AuthConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookieParams

_Required_: No

_Type_: List of <a href="cookieparamsdefinition.md">CookieParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

