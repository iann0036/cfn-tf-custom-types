# TF::AWS::NetworkfirewallRuleGroup MatchAttributesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#protocols" title="Protocols">Protocols</a>" : <i>[ Double, ... ]</i>,
    "<a href="#destination" title="Destination">Destination</a>" : <i>[ <a href="destinationdefinition.md">DestinationDefinition</a>, ... ]</i>,
    "<a href="#destinationport" title="DestinationPort">DestinationPort</a>" : <i>[ <a href="destinationportdefinition.md">DestinationPortDefinition</a>, ... ]</i>,
    "<a href="#source" title="Source">Source</a>" : <i>[ <a href="sourcedefinition.md">SourceDefinition</a>, ... ]</i>,
    "<a href="#sourceport" title="SourcePort">SourcePort</a>" : <i>[ <a href="sourceportdefinition.md">SourcePortDefinition</a>, ... ]</i>,
    "<a href="#tcpflag" title="TcpFlag">TcpFlag</a>" : <i>[ <a href="tcpflagdefinition.md">TcpFlagDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#protocols" title="Protocols">Protocols</a>: <i>
      - Double</i>
<a href="#destination" title="Destination">Destination</a>: <i>
      - <a href="destinationdefinition.md">DestinationDefinition</a></i>
<a href="#destinationport" title="DestinationPort">DestinationPort</a>: <i>
      - <a href="destinationportdefinition.md">DestinationPortDefinition</a></i>
<a href="#source" title="Source">Source</a>: <i>
      - <a href="sourcedefinition.md">SourceDefinition</a></i>
<a href="#sourceport" title="SourcePort">SourcePort</a>: <i>
      - <a href="sourceportdefinition.md">SourcePortDefinition</a></i>
<a href="#tcpflag" title="TcpFlag">TcpFlag</a>: <i>
      - <a href="tcpflagdefinition.md">TcpFlagDefinition</a></i>
</pre>

## Properties

#### Protocols

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No

_Type_: List of <a href="destinationdefinition.md">DestinationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationPort

_Required_: No

_Type_: List of <a href="destinationportdefinition.md">DestinationPortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: List of <a href="sourcedefinition.md">SourceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcePort

_Required_: No

_Type_: List of <a href="sourceportdefinition.md">SourcePortDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpFlag

_Required_: No

_Type_: List of <a href="tcpflagdefinition.md">TcpFlagDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

