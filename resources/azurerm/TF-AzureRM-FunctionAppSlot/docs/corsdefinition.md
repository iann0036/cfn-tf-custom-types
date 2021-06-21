# TF::AzureRM::FunctionAppSlot CorsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowedorigins" title="AllowedOrigins">AllowedOrigins</a>" : <i>[ String, ... ]</i>,
    "<a href="#supportcredentials" title="SupportCredentials">SupportCredentials</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#allowedorigins" title="AllowedOrigins">AllowedOrigins</a>: <i>
      - String</i>
<a href="#supportcredentials" title="SupportCredentials">SupportCredentials</a>: <i>Boolean</i>
</pre>

## Properties

#### AllowedOrigins

A list of origins which should be able to make cross-origin calls. `*` can be used to allow all calls.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupportCredentials

Are credentials supported?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
