# Terraform::Rundeck::Job Option

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowmultiplevalues" title="AllowMultipleValues">AllowMultipleValues</a>" : <i>Boolean</i>,
    "<a href="#defaultvalue" title="DefaultValue">DefaultValue</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#exposedtoscripts" title="ExposedToScripts">ExposedToScripts</a>" : <i>Boolean</i>,
    "<a href="#multivaluedelimiter" title="MultiValueDelimiter">MultiValueDelimiter</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#obscureinput" title="ObscureInput">ObscureInput</a>" : <i>Boolean</i>,
    "<a href="#requirepredefinedchoice" title="RequirePredefinedChoice">RequirePredefinedChoice</a>" : <i>Boolean</i>,
    "<a href="#required" title="Required">Required</a>" : <i>Boolean</i>,
    "<a href="#validationregex" title="ValidationRegex">ValidationRegex</a>" : <i>String</i>,
    "<a href="#valuechoices" title="ValueChoices">ValueChoices</a>" : <i>[ String, ... ]</i>,
    "<a href="#valuechoicesurl" title="ValueChoicesUrl">ValueChoicesUrl</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#allowmultiplevalues" title="AllowMultipleValues">AllowMultipleValues</a>: <i>Boolean</i>
<a href="#defaultvalue" title="DefaultValue">DefaultValue</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#exposedtoscripts" title="ExposedToScripts">ExposedToScripts</a>: <i>Boolean</i>
<a href="#multivaluedelimiter" title="MultiValueDelimiter">MultiValueDelimiter</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#obscureinput" title="ObscureInput">ObscureInput</a>: <i>Boolean</i>
<a href="#requirepredefinedchoice" title="RequirePredefinedChoice">RequirePredefinedChoice</a>: <i>Boolean</i>
<a href="#required" title="Required">Required</a>: <i>Boolean</i>
<a href="#validationregex" title="ValidationRegex">ValidationRegex</a>: <i>String</i>
<a href="#valuechoices" title="ValueChoices">ValueChoices</a>: <i>
      - String</i>
<a href="#valuechoicesurl" title="ValueChoicesUrl">ValueChoicesUrl</a>: <i>String</i>
</pre>

## Properties

#### AllowMultipleValues

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultValue

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExposedToScripts

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultiValueDelimiter

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObscureInput

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequirePredefinedChoice

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Required

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidationRegex

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueChoices

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueChoicesUrl

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

