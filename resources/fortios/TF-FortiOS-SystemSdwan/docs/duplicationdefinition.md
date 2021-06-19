# TF::FortiOS::SystemSdwan DuplicationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#packetdeduplication" title="PacketDeDuplication">PacketDeDuplication</a>" : <i>String</i>,
    "<a href="#packetduplication" title="PacketDuplication">PacketDuplication</a>" : <i>String</i>,
    "<a href="#dstaddr" title="Dstaddr">Dstaddr</a>" : <i>[ <a href="dstaddrdefinition.md">DstaddrDefinition</a>, ... ]</i>,
    "<a href="#dstaddr6" title="Dstaddr6">Dstaddr6</a>" : <i>[ <a href="dstaddr6definition.md">Dstaddr6Definition</a>, ... ]</i>,
    "<a href="#dstintf" title="Dstintf">Dstintf</a>" : <i>[ <a href="dstintfdefinition.md">DstintfDefinition</a>, ... ]</i>,
    "<a href="#service" title="Service">Service</a>" : <i>[ <a href="servicedefinition.md">ServiceDefinition</a>, ... ]</i>,
    "<a href="#serviceid" title="ServiceId">ServiceId</a>" : <i>[ <a href="serviceiddefinition.md">ServiceIdDefinition</a>, ... ]</i>,
    "<a href="#srcaddr" title="Srcaddr">Srcaddr</a>" : <i>[ <a href="srcaddrdefinition.md">SrcaddrDefinition</a>, ... ]</i>,
    "<a href="#srcaddr6" title="Srcaddr6">Srcaddr6</a>" : <i>[ <a href="srcaddr6definition.md">Srcaddr6Definition</a>, ... ]</i>,
    "<a href="#srcintf" title="Srcintf">Srcintf</a>" : <i>[ <a href="srcintfdefinition.md">SrcintfDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#packetdeduplication" title="PacketDeDuplication">PacketDeDuplication</a>: <i>String</i>
<a href="#packetduplication" title="PacketDuplication">PacketDuplication</a>: <i>String</i>
<a href="#dstaddr" title="Dstaddr">Dstaddr</a>: <i>
      - <a href="dstaddrdefinition.md">DstaddrDefinition</a></i>
<a href="#dstaddr6" title="Dstaddr6">Dstaddr6</a>: <i>
      - <a href="dstaddr6definition.md">Dstaddr6Definition</a></i>
<a href="#dstintf" title="Dstintf">Dstintf</a>: <i>
      - <a href="dstintfdefinition.md">DstintfDefinition</a></i>
<a href="#service" title="Service">Service</a>: <i>
      - <a href="servicedefinition.md">ServiceDefinition</a></i>
<a href="#serviceid" title="ServiceId">ServiceId</a>: <i>
      - <a href="serviceiddefinition.md">ServiceIdDefinition</a></i>
<a href="#srcaddr" title="Srcaddr">Srcaddr</a>: <i>
      - <a href="srcaddrdefinition.md">SrcaddrDefinition</a></i>
<a href="#srcaddr6" title="Srcaddr6">Srcaddr6</a>: <i>
      - <a href="srcaddr6definition.md">Srcaddr6Definition</a></i>
<a href="#srcintf" title="Srcintf">Srcintf</a>: <i>
      - <a href="srcintfdefinition.md">SrcintfDefinition</a></i>
</pre>

## Properties

#### Id

Duplication rule ID (1 - 255).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacketDeDuplication

Enable/disable discarding of packets that have been duplicated. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacketDuplication

Configure packet duplication method. Valid values: `disable`, `force`, `on-demand`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstaddr

_Required_: No

_Type_: List of <a href="dstaddrdefinition.md">DstaddrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstaddr6

_Required_: No

_Type_: List of <a href="dstaddr6definition.md">Dstaddr6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstintf

_Required_: No

_Type_: List of <a href="dstintfdefinition.md">DstintfDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No

_Type_: List of <a href="servicedefinition.md">ServiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceId

_Required_: No

_Type_: List of <a href="serviceiddefinition.md">ServiceIdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcaddr

_Required_: No

_Type_: List of <a href="srcaddrdefinition.md">SrcaddrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcaddr6

_Required_: No

_Type_: List of <a href="srcaddr6definition.md">Srcaddr6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcintf

_Required_: No

_Type_: List of <a href="srcintfdefinition.md">SrcintfDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

