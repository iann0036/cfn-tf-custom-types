# TF::SignalFx::Dashboard VariableDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#alias" title="Alias">Alias</a>" : <i>String</i>,
    "<a href="#applyifexist" title="ApplyIfExist">ApplyIfExist</a>" : <i>Boolean</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#property" title="Property">Property</a>" : <i>String</i>,
    "<a href="#replaceonly" title="ReplaceOnly">ReplaceOnly</a>" : <i>Boolean</i>,
    "<a href="#restrictedsuggestions" title="RestrictedSuggestions">RestrictedSuggestions</a>" : <i>Boolean</i>,
    "<a href="#valuerequired" title="ValueRequired">ValueRequired</a>" : <i>Boolean</i>,
    "<a href="#values" title="Values">Values</a>" : <i>[ String, ... ]</i>,
    "<a href="#valuessuggested" title="ValuesSuggested">ValuesSuggested</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#alias" title="Alias">Alias</a>: <i>String</i>
<a href="#applyifexist" title="ApplyIfExist">ApplyIfExist</a>: <i>Boolean</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#property" title="Property">Property</a>: <i>String</i>
<a href="#replaceonly" title="ReplaceOnly">ReplaceOnly</a>: <i>Boolean</i>
<a href="#restrictedsuggestions" title="RestrictedSuggestions">RestrictedSuggestions</a>: <i>Boolean</i>
<a href="#valuerequired" title="ValueRequired">ValueRequired</a>: <i>Boolean</i>
<a href="#values" title="Values">Values</a>: <i>
      - String</i>
<a href="#valuessuggested" title="ValuesSuggested">ValuesSuggested</a>: <i>
      - String</i>
</pre>

## Properties

#### Alias

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplyIfExist

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Property

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplaceOnly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestrictedSuggestions

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueRequired

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Values

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValuesSuggested

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

