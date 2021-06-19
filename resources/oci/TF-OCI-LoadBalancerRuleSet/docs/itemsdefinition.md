# TF::OCI::LoadBalancerRuleSet ItemsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#allowedmethods" title="AllowedMethods">AllowedMethods</a>" : <i>[ String, ... ]</i>,
    "<a href="#areinvalidcharactersallowed" title="AreInvalidCharactersAllowed">AreInvalidCharactersAllowed</a>" : <i>Boolean</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#header" title="Header">Header</a>" : <i>String</i>,
    "<a href="#httplargeheadersizeinkb" title="HttpLargeHeaderSizeInKb">HttpLargeHeaderSizeInKb</a>" : <i>Double</i>,
    "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>,
    "<a href="#responsecode" title="ResponseCode">ResponseCode</a>" : <i>Double</i>,
    "<a href="#statuscode" title="StatusCode">StatusCode</a>" : <i>Double</i>,
    "<a href="#suffix" title="Suffix">Suffix</a>" : <i>String</i>,
    "<a href="#value" title="Value">Value</a>" : <i>String</i>,
    "<a href="#conditions" title="Conditions">Conditions</a>" : <i>[ <a href="conditionsdefinition.md">ConditionsDefinition</a>, ... ]</i>,
    "<a href="#redirecturi" title="RedirectUri">RedirectUri</a>" : <i>[ <a href="redirecturidefinition.md">RedirectUriDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#allowedmethods" title="AllowedMethods">AllowedMethods</a>: <i>
      - String</i>
<a href="#areinvalidcharactersallowed" title="AreInvalidCharactersAllowed">AreInvalidCharactersAllowed</a>: <i>Boolean</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#header" title="Header">Header</a>: <i>String</i>
<a href="#httplargeheadersizeinkb" title="HttpLargeHeaderSizeInKb">HttpLargeHeaderSizeInKb</a>: <i>Double</i>
<a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
<a href="#responsecode" title="ResponseCode">ResponseCode</a>: <i>Double</i>
<a href="#statuscode" title="StatusCode">StatusCode</a>: <i>Double</i>
<a href="#suffix" title="Suffix">Suffix</a>: <i>String</i>
<a href="#value" title="Value">Value</a>: <i>String</i>
<a href="#conditions" title="Conditions">Conditions</a>: <i>
      - <a href="conditionsdefinition.md">ConditionsDefinition</a></i>
<a href="#redirecturi" title="RedirectUri">RedirectUri</a>: <i>
      - <a href="redirecturidefinition.md">RedirectUriDefinition</a></i>
</pre>

## Properties

#### Action

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedMethods

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AreInvalidCharactersAllowed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Header

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpLargeHeaderSizeInKb

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseCode

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatusCode

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Suffix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Conditions

_Required_: No

_Type_: List of <a href="conditionsdefinition.md">ConditionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectUri

_Required_: No

_Type_: List of <a href="redirecturidefinition.md">RedirectUriDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

