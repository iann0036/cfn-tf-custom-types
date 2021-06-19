# TF::AVI::Natpolicy MatchDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#destinationip" title="DestinationIp">DestinationIp</a>" : <i>[ <a href="destinationipdefinition.md">DestinationIpDefinition</a>, ... ]</i>,
    "<a href="#services" title="Services">Services</a>" : <i>[ <a href="servicesdefinition.md">ServicesDefinition</a>, ... ]</i>,
    "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>[ <a href="sourceipdefinition.md">SourceIpDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#destinationip" title="DestinationIp">DestinationIp</a>: <i>
      - <a href="destinationipdefinition.md">DestinationIpDefinition</a></i>
<a href="#services" title="Services">Services</a>: <i>
      - <a href="servicesdefinition.md">ServicesDefinition</a></i>
<a href="#sourceip" title="SourceIp">SourceIp</a>: <i>
      - <a href="sourceipdefinition.md">SourceIpDefinition</a></i>
</pre>

## Properties

#### DestinationIp

_Required_: No

_Type_: List of <a href="destinationipdefinition.md">DestinationIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Services

_Required_: No

_Type_: List of <a href="servicesdefinition.md">ServicesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

_Required_: No

_Type_: List of <a href="sourceipdefinition.md">SourceIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

