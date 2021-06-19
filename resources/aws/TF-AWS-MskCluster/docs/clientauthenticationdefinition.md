# TF::AWS::MskCluster ClientAuthenticationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#sasl" title="Sasl">Sasl</a>" : <i>[ <a href="sasldefinition.md">SaslDefinition</a>, ... ]</i>,
    "<a href="#tls" title="Tls">Tls</a>" : <i>[ <a href="tlsdefinition.md">TlsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#sasl" title="Sasl">Sasl</a>: <i>
      - <a href="sasldefinition.md">SaslDefinition</a></i>
<a href="#tls" title="Tls">Tls</a>: <i>
      - <a href="tlsdefinition.md">TlsDefinition</a></i>
</pre>

## Properties

#### Sasl

_Required_: No

_Type_: List of <a href="sasldefinition.md">SaslDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tls

_Required_: No

_Type_: List of <a href="tlsdefinition.md">TlsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

