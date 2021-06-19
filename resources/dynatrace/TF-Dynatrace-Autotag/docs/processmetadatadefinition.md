# TF::Dynatrace::Autotag ProcessMetadataDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#attribute" title="Attribute">Attribute</a>" : <i>String</i>,
    "<a href="#dynamickey" title="DynamicKey">DynamicKey</a>" : <i>[ <a href="dynamickeydefinition.md">DynamicKeyDefinition</a>, ... ]</i>,
    "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#attribute" title="Attribute">Attribute</a>: <i>String</i>
<a href="#dynamickey" title="DynamicKey">DynamicKey</a>: <i>
      - <a href="dynamickeydefinition.md">DynamicKeyDefinition</a></i>
<a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
</pre>

## Properties

#### Attribute

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicKey

_Required_: Yes

_Type_: List of <a href="dynamickeydefinition.md">DynamicKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

