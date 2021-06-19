# TF::ECL::BaremetalServerV2 RaidArraysDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#diskhardwareids" title="DiskHardwareIds">DiskHardwareIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#primarystorage" title="PrimaryStorage">PrimaryStorage</a>" : <i>Boolean</i>,
    "<a href="#raidcardhardwareid" title="RaidCardHardwareId">RaidCardHardwareId</a>" : <i>String</i>,
    "<a href="#raidlevel" title="RaidLevel">RaidLevel</a>" : <i>Double</i>,
    "<a href="#partitions" title="Partitions">Partitions</a>" : <i>[ <a href="partitionsdefinition.md">PartitionsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#diskhardwareids" title="DiskHardwareIds">DiskHardwareIds</a>: <i>
      - String</i>
<a href="#primarystorage" title="PrimaryStorage">PrimaryStorage</a>: <i>Boolean</i>
<a href="#raidcardhardwareid" title="RaidCardHardwareId">RaidCardHardwareId</a>: <i>String</i>
<a href="#raidlevel" title="RaidLevel">RaidLevel</a>: <i>Double</i>
<a href="#partitions" title="Partitions">Partitions</a>: <i>
      - <a href="partitionsdefinition.md">PartitionsDefinition</a></i>
</pre>

## Properties

#### DiskHardwareIds

List of disk hardware ID. Changing
this creates a new server.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryStorage

Primary storage flag. At least one storage
shoul be primary. Changing this creates a new server.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RaidCardHardwareId

Raid card hardware ID. Changing
this creates a new server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RaidLevel

Raid level. Changing this creates a new server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Partitions

_Required_: No

_Type_: List of <a href="partitionsdefinition.md">PartitionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

