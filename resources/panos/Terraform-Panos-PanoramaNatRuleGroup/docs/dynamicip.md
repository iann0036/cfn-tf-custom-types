# Terraform::Panos::PanoramaNatRuleGroup DynamicIp

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#translatedaddresses" title="TranslatedAddresses">TranslatedAddresses</a>" : <i>[ String, ... ]</i>,
    "<a href="#fallback" title="Fallback">Fallback</a>" : <i>[ <a href="dynamicip-fallback.md">Fallback</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#translatedaddresses" title="TranslatedAddresses">TranslatedAddresses</a>: <i>
      - String</i>
<a href="#fallback" title="Fallback">Fallback</a>: <i>
      - <a href="dynamicip-fallback.md">Fallback</a></i>
</pre>

## Properties

#### TranslatedAddresses

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fallback

_Required_: No

_Type_: List of <a href="dynamicip-fallback.md">Fallback</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

