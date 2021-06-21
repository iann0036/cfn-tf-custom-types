# TF::Panos::NatRuleGroup StaticIpDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bidirectional" title="BiDirectional">BiDirectional</a>" : <i>Boolean</i>,
    "<a href="#translatedaddress" title="TranslatedAddress">TranslatedAddress</a>" : <i>[ <a href="translatedaddressdefinition.md">TranslatedAddressDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bidirectional" title="BiDirectional">BiDirectional</a>: <i>Boolean</i>
<a href="#translatedaddress" title="TranslatedAddress">TranslatedAddress</a>: <i>
      - <a href="translatedaddressdefinition.md">TranslatedAddressDefinition</a></i>
</pre>

## Properties

#### BiDirectional

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TranslatedAddress

_Required_: Yes

_Type_: List of <a href="translatedaddressdefinition.md">TranslatedAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
