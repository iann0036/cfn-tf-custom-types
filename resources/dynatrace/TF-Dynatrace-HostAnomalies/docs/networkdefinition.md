# TF::Dynatrace::HostAnomalies NetworkDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#connectivity" title="Connectivity">Connectivity</a>" : <i>[ <a href="connectivitydefinition.md">ConnectivityDefinition</a>, ... ]</i>,
    "<a href="#droppedpackets" title="DroppedPackets">DroppedPackets</a>" : <i>[ <a href="droppedpacketsdefinition.md">DroppedPacketsDefinition</a>, ... ]</i>,
    "<a href="#errors" title="Errors">Errors</a>" : <i>[ <a href="errorsdefinition.md">ErrorsDefinition</a>, ... ]</i>,
    "<a href="#retransmission" title="Retransmission">Retransmission</a>" : <i>[ <a href="retransmissiondefinition.md">RetransmissionDefinition</a>, ... ]</i>,
    "<a href="#utilization" title="Utilization">Utilization</a>" : <i>[ <a href="utilizationdefinition.md">UtilizationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#connectivity" title="Connectivity">Connectivity</a>: <i>
      - <a href="connectivitydefinition.md">ConnectivityDefinition</a></i>
<a href="#droppedpackets" title="DroppedPackets">DroppedPackets</a>: <i>
      - <a href="droppedpacketsdefinition.md">DroppedPacketsDefinition</a></i>
<a href="#errors" title="Errors">Errors</a>: <i>
      - <a href="errorsdefinition.md">ErrorsDefinition</a></i>
<a href="#retransmission" title="Retransmission">Retransmission</a>: <i>
      - <a href="retransmissiondefinition.md">RetransmissionDefinition</a></i>
<a href="#utilization" title="Utilization">Utilization</a>: <i>
      - <a href="utilizationdefinition.md">UtilizationDefinition</a></i>
</pre>

## Properties

#### Connectivity

_Required_: No

_Type_: List of <a href="connectivitydefinition.md">ConnectivityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DroppedPackets

_Required_: No

_Type_: List of <a href="droppedpacketsdefinition.md">DroppedPacketsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Errors

_Required_: No

_Type_: List of <a href="errorsdefinition.md">ErrorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Retransmission

_Required_: No

_Type_: List of <a href="retransmissiondefinition.md">RetransmissionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Utilization

_Required_: No

_Type_: List of <a href="utilizationdefinition.md">UtilizationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

