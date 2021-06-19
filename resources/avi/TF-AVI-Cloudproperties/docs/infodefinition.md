# TF::AVI::Cloudproperties InfoDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#flavorregexfilter" title="FlavorRegexFilter">FlavorRegexFilter</a>" : <i>String</i>,
    "<a href="#htypes" title="Htypes">Htypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#vtype" title="Vtype">Vtype</a>" : <i>String</i>,
    "<a href="#ccaprops" title="CcaProps">CcaProps</a>" : <i>[ <a href="ccapropsdefinition.md">CcaPropsDefinition</a>, ... ]</i>,
    "<a href="#controllerprops" title="ControllerProps">ControllerProps</a>" : <i>[ <a href="controllerpropsdefinition.md">ControllerPropsDefinition</a>, ... ]</i>,
    "<a href="#flavorprops" title="FlavorProps">FlavorProps</a>" : <i>[ <a href="flavorpropsdefinition.md">FlavorPropsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#flavorregexfilter" title="FlavorRegexFilter">FlavorRegexFilter</a>: <i>String</i>
<a href="#htypes" title="Htypes">Htypes</a>: <i>
      - String</i>
<a href="#vtype" title="Vtype">Vtype</a>: <i>String</i>
<a href="#ccaprops" title="CcaProps">CcaProps</a>: <i>
      - <a href="ccapropsdefinition.md">CcaPropsDefinition</a></i>
<a href="#controllerprops" title="ControllerProps">ControllerProps</a>: <i>
      - <a href="controllerpropsdefinition.md">ControllerPropsDefinition</a></i>
<a href="#flavorprops" title="FlavorProps">FlavorProps</a>: <i>
      - <a href="flavorpropsdefinition.md">FlavorPropsDefinition</a></i>
</pre>

## Properties

#### FlavorRegexFilter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Htypes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vtype

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CcaProps

_Required_: No

_Type_: List of <a href="ccapropsdefinition.md">CcaPropsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerProps

_Required_: No

_Type_: List of <a href="controllerpropsdefinition.md">ControllerPropsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlavorProps

_Required_: No

_Type_: List of <a href="flavorpropsdefinition.md">FlavorPropsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

