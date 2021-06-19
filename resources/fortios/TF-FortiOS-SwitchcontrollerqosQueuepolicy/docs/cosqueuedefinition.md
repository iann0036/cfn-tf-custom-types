# TF::FortiOS::SwitchcontrollerqosQueuepolicy CosQueueDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#droppolicy" title="DropPolicy">DropPolicy</a>" : <i>String</i>,
    "<a href="#ecn" title="Ecn">Ecn</a>" : <i>String</i>,
    "<a href="#maxrate" title="MaxRate">MaxRate</a>" : <i>Double</i>,
    "<a href="#maxratepercent" title="MaxRatePercent">MaxRatePercent</a>" : <i>Double</i>,
    "<a href="#minrate" title="MinRate">MinRate</a>" : <i>Double</i>,
    "<a href="#minratepercent" title="MinRatePercent">MinRatePercent</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#droppolicy" title="DropPolicy">DropPolicy</a>: <i>String</i>
<a href="#ecn" title="Ecn">Ecn</a>: <i>String</i>
<a href="#maxrate" title="MaxRate">MaxRate</a>: <i>Double</i>
<a href="#maxratepercent" title="MaxRatePercent">MaxRatePercent</a>: <i>Double</i>
<a href="#minrate" title="MinRate">MinRate</a>: <i>Double</i>
<a href="#minratepercent" title="MinRatePercent">MinRatePercent</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#weight" title="Weight">Weight</a>: <i>Double</i>
</pre>

## Properties

#### Description

Description of the COS queue.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DropPolicy

COS queue drop policy. Valid values: `taildrop`, `weighted-random-early-detection`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ecn

Enable/disable ECN packet marking to drop eligible packets. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRate

Maximum rate (0 - 4294967295 kbps, 0 to disable).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRatePercent

Maximum rate (% of link speed).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinRate

Minimum rate (0 - 4294967295 kbps, 0 to disable).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinRatePercent

Minimum rate (% of link speed).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Cos queue ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

Weight of weighted round robin scheduling.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

