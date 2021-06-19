# TF::HCloud::Server NetworkDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#aliasips" title="AliasIps">AliasIps</a>" : <i>[ String, ... ]</i>,
    "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
    "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#aliasips" title="AliasIps">AliasIps</a>: <i>
      - String</i>
<a href="#ip" title="Ip">Ip</a>: <i>String</i>
<a href="#networkid" title="NetworkId">NetworkId</a>: <i>Double</i>
</pre>

## Properties

#### AliasIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

