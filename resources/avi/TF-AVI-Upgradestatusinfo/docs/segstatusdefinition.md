# TF::AVI::Upgradestatusinfo SegStatusDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#controllerversion" title="ControllerVersion">ControllerVersion</a>" : <i>String</i>,
    "<a href="#disruptedvsref" title="DisruptedVsRef">DisruptedVsRef</a>" : <i>[ String, ... ]</i>,
    "<a href="#duration" title="Duration">Duration</a>" : <i>String</i>,
    "<a href="#endtime" title="EndTime">EndTime</a>" : <i>String</i>,
    "<a href="#enqueuetime" title="EnqueueTime">EnqueueTime</a>" : <i>String</i>,
    "<a href="#hamode" title="HaMode">HaMode</a>" : <i>String</i>,
    "<a href="#inprogress" title="InProgress">InProgress</a>" : <i>Boolean</i>,
    "<a href="#notes" title="Notes">Notes</a>" : <i>[ String, ... ]</i>,
    "<a href="#numse" title="NumSe">NumSe</a>" : <i>Double</i>,
    "<a href="#numsewithnovs" title="NumSeWithNoVs">NumSeWithNoVs</a>" : <i>Double</i>,
    "<a href="#numsewithvsnotscaledout" title="NumSeWithVsNotScaledout">NumSeWithVsNotScaledout</a>" : <i>Double</i>,
    "<a href="#numsewithvsscaledout" title="NumSeWithVsScaledout">NumSeWithVsScaledout</a>" : <i>Double</i>,
    "<a href="#numvs" title="NumVs">NumVs</a>" : <i>Double</i>,
    "<a href="#numvsdisrupted" title="NumVsDisrupted">NumVsDisrupted</a>" : <i>Double</i>,
    "<a href="#progress" title="Progress">Progress</a>" : <i>Double</i>,
    "<a href="#reason" title="Reason">Reason</a>" : <i>[ String, ... ]</i>,
    "<a href="#requesttime" title="RequestTime">RequestTime</a>" : <i>String</i>,
    "<a href="#sealreadyupgradedatstart" title="SeAlreadyUpgradedAtStart">SeAlreadyUpgradedAtStart</a>" : <i>[ String, ... ]</i>,
    "<a href="#sedisconnectedatstart" title="SeDisconnectedAtStart">SeDisconnectedAtStart</a>" : <i>[ String, ... ]</i>,
    "<a href="#segroupname" title="SeGroupName">SeGroupName</a>" : <i>String</i>,
    "<a href="#segroupuuid" title="SeGroupUuid">SeGroupUuid</a>" : <i>String</i>,
    "<a href="#seipmissingatstart" title="SeIpMissingAtStart">SeIpMissingAtStart</a>" : <i>[ String, ... ]</i>,
    "<a href="#sepoweredoffatstart" title="SePoweredoffAtStart">SePoweredoffAtStart</a>" : <i>[ String, ... ]</i>,
    "<a href="#serebootinprogressref" title="SeRebootInProgressRef">SeRebootInProgressRef</a>" : <i>String</i>,
    "<a href="#seupgradecompleted" title="SeUpgradeCompleted">SeUpgradeCompleted</a>" : <i>[ String, ... ]</i>,
    "<a href="#seupgradefailed" title="SeUpgradeFailed">SeUpgradeFailed</a>" : <i>[ String, ... ]</i>,
    "<a href="#seupgradeinprogress" title="SeUpgradeInProgress">SeUpgradeInProgress</a>" : <i>[ String, ... ]</i>,
    "<a href="#seupgradenotstarted" title="SeUpgradeNotStarted">SeUpgradeNotStarted</a>" : <i>[ String, ... ]</i>,
    "<a href="#seupgradeskipsuspended" title="SeUpgradeSkipSuspended">SeUpgradeSkipSuspended</a>" : <i>[ String, ... ]</i>,
    "<a href="#seupgradesuspended" title="SeUpgradeSuspended">SeUpgradeSuspended</a>" : <i>[ String, ... ]</i>,
    "<a href="#sewithnovs" title="SeWithNoVs">SeWithNoVs</a>" : <i>[ String, ... ]</i>,
    "<a href="#sewithvsnotscaledout" title="SeWithVsNotScaledout">SeWithVsNotScaledout</a>" : <i>[ String, ... ]</i>,
    "<a href="#sewithvsscaledout" title="SeWithVsScaledout">SeWithVsScaledout</a>" : <i>[ String, ... ]</i>,
    "<a href="#starttime" title="StartTime">StartTime</a>" : <i>String</i>,
    "<a href="#state" title="State">State</a>" : <i>String</i>,
    "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
    "<a href="#thread" title="Thread">Thread</a>" : <i>String</i>,
    "<a href="#trafficstatus" title="TrafficStatus">TrafficStatus</a>" : <i>String</i>,
    "<a href="#vsmigrateinprogressref" title="VsMigrateInProgressRef">VsMigrateInProgressRef</a>" : <i>[ String, ... ]</i>,
    "<a href="#vsscaleininprogressref" title="VsScaleinInProgressRef">VsScaleinInProgressRef</a>" : <i>[ String, ... ]</i>,
    "<a href="#vsscaleoutinprogressref" title="VsScaleoutInProgressRef">VsScaleoutInProgressRef</a>" : <i>[ String, ... ]</i>,
    "<a href="#worker" title="Worker">Worker</a>" : <i>String</i>,
    "<a href="#seupgradeerrors" title="SeUpgradeErrors">SeUpgradeErrors</a>" : <i>[ <a href="seupgradeerrorsdefinition.md">SeUpgradeErrorsDefinition</a>, ... ]</i>,
    "<a href="#vserrors" title="VsErrors">VsErrors</a>" : <i>[ <a href="vserrorsdefinition.md">VsErrorsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#controllerversion" title="ControllerVersion">ControllerVersion</a>: <i>String</i>
<a href="#disruptedvsref" title="DisruptedVsRef">DisruptedVsRef</a>: <i>
      - String</i>
<a href="#duration" title="Duration">Duration</a>: <i>String</i>
<a href="#endtime" title="EndTime">EndTime</a>: <i>String</i>
<a href="#enqueuetime" title="EnqueueTime">EnqueueTime</a>: <i>String</i>
<a href="#hamode" title="HaMode">HaMode</a>: <i>String</i>
<a href="#inprogress" title="InProgress">InProgress</a>: <i>Boolean</i>
<a href="#notes" title="Notes">Notes</a>: <i>
      - String</i>
<a href="#numse" title="NumSe">NumSe</a>: <i>Double</i>
<a href="#numsewithnovs" title="NumSeWithNoVs">NumSeWithNoVs</a>: <i>Double</i>
<a href="#numsewithvsnotscaledout" title="NumSeWithVsNotScaledout">NumSeWithVsNotScaledout</a>: <i>Double</i>
<a href="#numsewithvsscaledout" title="NumSeWithVsScaledout">NumSeWithVsScaledout</a>: <i>Double</i>
<a href="#numvs" title="NumVs">NumVs</a>: <i>Double</i>
<a href="#numvsdisrupted" title="NumVsDisrupted">NumVsDisrupted</a>: <i>Double</i>
<a href="#progress" title="Progress">Progress</a>: <i>Double</i>
<a href="#reason" title="Reason">Reason</a>: <i>
      - String</i>
<a href="#requesttime" title="RequestTime">RequestTime</a>: <i>String</i>
<a href="#sealreadyupgradedatstart" title="SeAlreadyUpgradedAtStart">SeAlreadyUpgradedAtStart</a>: <i>
      - String</i>
<a href="#sedisconnectedatstart" title="SeDisconnectedAtStart">SeDisconnectedAtStart</a>: <i>
      - String</i>
<a href="#segroupname" title="SeGroupName">SeGroupName</a>: <i>String</i>
<a href="#segroupuuid" title="SeGroupUuid">SeGroupUuid</a>: <i>String</i>
<a href="#seipmissingatstart" title="SeIpMissingAtStart">SeIpMissingAtStart</a>: <i>
      - String</i>
<a href="#sepoweredoffatstart" title="SePoweredoffAtStart">SePoweredoffAtStart</a>: <i>
      - String</i>
<a href="#serebootinprogressref" title="SeRebootInProgressRef">SeRebootInProgressRef</a>: <i>String</i>
<a href="#seupgradecompleted" title="SeUpgradeCompleted">SeUpgradeCompleted</a>: <i>
      - String</i>
<a href="#seupgradefailed" title="SeUpgradeFailed">SeUpgradeFailed</a>: <i>
      - String</i>
<a href="#seupgradeinprogress" title="SeUpgradeInProgress">SeUpgradeInProgress</a>: <i>
      - String</i>
<a href="#seupgradenotstarted" title="SeUpgradeNotStarted">SeUpgradeNotStarted</a>: <i>
      - String</i>
<a href="#seupgradeskipsuspended" title="SeUpgradeSkipSuspended">SeUpgradeSkipSuspended</a>: <i>
      - String</i>
<a href="#seupgradesuspended" title="SeUpgradeSuspended">SeUpgradeSuspended</a>: <i>
      - String</i>
<a href="#sewithnovs" title="SeWithNoVs">SeWithNoVs</a>: <i>
      - String</i>
<a href="#sewithvsnotscaledout" title="SeWithVsNotScaledout">SeWithVsNotScaledout</a>: <i>
      - String</i>
<a href="#sewithvsscaledout" title="SeWithVsScaledout">SeWithVsScaledout</a>: <i>
      - String</i>
<a href="#starttime" title="StartTime">StartTime</a>: <i>String</i>
<a href="#state" title="State">State</a>: <i>String</i>
<a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
<a href="#thread" title="Thread">Thread</a>: <i>String</i>
<a href="#trafficstatus" title="TrafficStatus">TrafficStatus</a>: <i>String</i>
<a href="#vsmigrateinprogressref" title="VsMigrateInProgressRef">VsMigrateInProgressRef</a>: <i>
      - String</i>
<a href="#vsscaleininprogressref" title="VsScaleinInProgressRef">VsScaleinInProgressRef</a>: <i>
      - String</i>
<a href="#vsscaleoutinprogressref" title="VsScaleoutInProgressRef">VsScaleoutInProgressRef</a>: <i>
      - String</i>
<a href="#worker" title="Worker">Worker</a>: <i>String</i>
<a href="#seupgradeerrors" title="SeUpgradeErrors">SeUpgradeErrors</a>: <i>
      - <a href="seupgradeerrorsdefinition.md">SeUpgradeErrorsDefinition</a></i>
<a href="#vserrors" title="VsErrors">VsErrors</a>: <i>
      - <a href="vserrorsdefinition.md">VsErrorsDefinition</a></i>
</pre>

## Properties

#### ControllerVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisruptedVsRef

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnqueueTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InProgress

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumSe

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumSeWithNoVs

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumSeWithVsNotScaledout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumSeWithVsScaledout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumVs

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumVsDisrupted

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Progress

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reason

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeAlreadyUpgradedAtStart

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeDisconnectedAtStart

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeGroupName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeGroupUuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeIpMissingAtStart

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SePoweredoffAtStart

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeRebootInProgressRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeUpgradeCompleted

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeUpgradeFailed

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeUpgradeInProgress

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeUpgradeNotStarted

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeUpgradeSkipSuspended

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeUpgradeSuspended

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeWithNoVs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeWithVsNotScaledout

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeWithVsScaledout

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Thread

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsMigrateInProgressRef

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsScaleinInProgressRef

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsScaleoutInProgressRef

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Worker

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeUpgradeErrors

_Required_: No

_Type_: List of <a href="seupgradeerrorsdefinition.md">SeUpgradeErrorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsErrors

_Required_: No

_Type_: List of <a href="vserrorsdefinition.md">VsErrorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

