# TF::AVI::Upgradestatusinfo HistoryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#duration" title="Duration">Duration</a>" : <i>Double</i>,
    "<a href="#endtime" title="EndTime">EndTime</a>" : <i>String</i>,
    "<a href="#ops" title="Ops">Ops</a>" : <i>String</i>,
    "<a href="#patchversion" title="PatchVersion">PatchVersion</a>" : <i>String</i>,
    "<a href="#starttime" title="StartTime">StartTime</a>" : <i>String</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>,
    "<a href="#seupgradeevents" title="SeUpgradeEvents">SeUpgradeEvents</a>" : <i>[ <a href="seupgradeeventsdefinition.md">SeUpgradeEventsDefinition</a>, ... ]</i>,
    "<a href="#segstatus" title="SegStatus">SegStatus</a>" : <i>[ <a href="segstatusdefinition.md">SegStatusDefinition</a>, ... ]</i>,
    "<a href="#state" title="State">State</a>" : <i>[ <a href="statedefinition.md">StateDefinition</a>, ... ]</i>,
    "<a href="#upgradeevents" title="UpgradeEvents">UpgradeEvents</a>" : <i>[ <a href="upgradeeventsdefinition.md">UpgradeEventsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#duration" title="Duration">Duration</a>: <i>Double</i>
<a href="#endtime" title="EndTime">EndTime</a>: <i>String</i>
<a href="#ops" title="Ops">Ops</a>: <i>String</i>
<a href="#patchversion" title="PatchVersion">PatchVersion</a>: <i>String</i>
<a href="#starttime" title="StartTime">StartTime</a>: <i>String</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
<a href="#seupgradeevents" title="SeUpgradeEvents">SeUpgradeEvents</a>: <i>
      - <a href="seupgradeeventsdefinition.md">SeUpgradeEventsDefinition</a></i>
<a href="#segstatus" title="SegStatus">SegStatus</a>: <i>
      - <a href="segstatusdefinition.md">SegStatusDefinition</a></i>
<a href="#state" title="State">State</a>: <i>
      - <a href="statedefinition.md">StateDefinition</a></i>
<a href="#upgradeevents" title="UpgradeEvents">UpgradeEvents</a>: <i>
      - <a href="upgradeeventsdefinition.md">UpgradeEventsDefinition</a></i>
</pre>

## Properties

#### Duration

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ops

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PatchVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeUpgradeEvents

_Required_: No

_Type_: List of <a href="seupgradeeventsdefinition.md">SeUpgradeEventsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SegStatus

_Required_: No

_Type_: List of <a href="segstatusdefinition.md">SegStatusDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: List of <a href="statedefinition.md">StateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeEvents

_Required_: No

_Type_: List of <a href="upgradeeventsdefinition.md">UpgradeEventsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

