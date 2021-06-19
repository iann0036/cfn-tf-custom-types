# TF::OnePassword::Item FieldDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#label" title="Label">Label</a>" : <i>String</i>,
    "<a href="#purpose" title="Purpose">Purpose</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#value" title="Value">Value</a>" : <i>String</i>,
    "<a href="#passwordrecipe" title="PasswordRecipe">PasswordRecipe</a>" : <i>[ <a href="passwordrecipedefinition.md">PasswordRecipeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#label" title="Label">Label</a>: <i>String</i>
<a href="#purpose" title="Purpose">Purpose</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#value" title="Value">Value</a>: <i>String</i>
<a href="#passwordrecipe" title="PasswordRecipe">PasswordRecipe</a>: <i>
      - <a href="passwordrecipedefinition.md">PasswordRecipeDefinition</a></i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Purpose

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordRecipe

_Required_: No

_Type_: List of <a href="passwordrecipedefinition.md">PasswordRecipeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

