# Terraform::Panos::PanoramaPbfRuleGroup Destination

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#addresses" title="Addresses">Addresses</a>" : <i>[ String, ... ]</i>,
    "<a href="#applications" title="Applications">Applications</a>" : <i>[ String, ... ]</i>,
    "<a href="#negate" title="Negate">Negate</a>" : <i>Boolean</i>,
    "<a href="#services" title="Services">Services</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#addresses" title="Addresses">Addresses</a>: <i>
      - String</i>
<a href="#applications" title="Applications">Applications</a>: <i>
      - String</i>
<a href="#negate" title="Negate">Negate</a>: <i>Boolean</i>
<a href="#services" title="Services">Services</a>: <i>
      - String</i>
</pre>

## Properties

#### Addresses

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Applications

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Negate

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Services

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

