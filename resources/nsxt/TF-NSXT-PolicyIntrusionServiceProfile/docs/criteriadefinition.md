# TF::NSXT::PolicyIntrusionServiceProfile CriteriaDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#attacktargets" title="AttackTargets">AttackTargets</a>" : <i>[ String, ... ]</i>,
    "<a href="#attacktypes" title="AttackTypes">AttackTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#cvss" title="Cvss">Cvss</a>" : <i>[ String, ... ]</i>,
    "<a href="#productsaffected" title="ProductsAffected">ProductsAffected</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#attacktargets" title="AttackTargets">AttackTargets</a>: <i>
      - String</i>
<a href="#attacktypes" title="AttackTypes">AttackTypes</a>: <i>
      - String</i>
<a href="#cvss" title="Cvss">Cvss</a>: <i>
      - String</i>
<a href="#productsaffected" title="ProductsAffected">ProductsAffected</a>: <i>
      - String</i>
</pre>

## Properties

#### AttackTargets

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttackTypes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cvss

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProductsAffected

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

