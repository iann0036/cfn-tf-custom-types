# TF::AVI::Natpolicy ServicesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#destinationport" title="DestinationPort">DestinationPort</a>" : <i>[ <a href="destinationportdefinition.md">DestinationPortDefinition</a>, ... ]</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>[ <a href="protocoldefinition.md">ProtocolDefinition</a>, ... ]</i>,
    "<a href="#sourceport" title="SourcePort">SourcePort</a>" : <i>[ <a href="sourceportdefinition.md">SourcePortDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#destinationport" title="DestinationPort">DestinationPort</a>: <i>
      - <a href="destinationportdefinition.md">DestinationPortDefinition</a></i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>
      - <a href="protocoldefinition.md">ProtocolDefinition</a></i>
<a href="#sourceport" title="SourcePort">SourcePort</a>: <i>
      - <a href="sourceportdefinition.md">SourcePortDefinition</a></i>
</pre>

## Properties

#### DestinationPort

_Required_: No

_Type_: List of <a href="destinationportdefinition.md">DestinationPortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: List of <a href="protocoldefinition.md">ProtocolDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcePort

_Required_: No

_Type_: List of <a href="sourceportdefinition.md">SourcePortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

