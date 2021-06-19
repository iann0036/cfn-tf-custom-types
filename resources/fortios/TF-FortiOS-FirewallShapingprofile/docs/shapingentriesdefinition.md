# TF::FortiOS::FirewallShapingprofile ShapingEntriesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#burstinmsec" title="BurstInMsec">BurstInMsec</a>" : <i>Double</i>,
    "<a href="#cburstinmsec" title="CburstInMsec">CburstInMsec</a>" : <i>Double</i>,
    "<a href="#classid" title="ClassId">ClassId</a>" : <i>Double</i>,
    "<a href="#guaranteedbandwidthpercentage" title="GuaranteedBandwidthPercentage">GuaranteedBandwidthPercentage</a>" : <i>Double</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#limit" title="Limit">Limit</a>" : <i>Double</i>,
    "<a href="#max" title="Max">Max</a>" : <i>Double</i>,
    "<a href="#maximumbandwidthpercentage" title="MaximumBandwidthPercentage">MaximumBandwidthPercentage</a>" : <i>Double</i>,
    "<a href="#min" title="Min">Min</a>" : <i>Double</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>String</i>,
    "<a href="#redprobability" title="RedProbability">RedProbability</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#burstinmsec" title="BurstInMsec">BurstInMsec</a>: <i>Double</i>
<a href="#cburstinmsec" title="CburstInMsec">CburstInMsec</a>: <i>Double</i>
<a href="#classid" title="ClassId">ClassId</a>: <i>Double</i>
<a href="#guaranteedbandwidthpercentage" title="GuaranteedBandwidthPercentage">GuaranteedBandwidthPercentage</a>: <i>Double</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#limit" title="Limit">Limit</a>: <i>Double</i>
<a href="#max" title="Max">Max</a>: <i>Double</i>
<a href="#maximumbandwidthpercentage" title="MaximumBandwidthPercentage">MaximumBandwidthPercentage</a>: <i>Double</i>
<a href="#min" title="Min">Min</a>: <i>Double</i>
<a href="#priority" title="Priority">Priority</a>: <i>String</i>
<a href="#redprobability" title="RedProbability">RedProbability</a>: <i>Double</i>
</pre>

## Properties

#### BurstInMsec

Number of bytes that can be burst at maximum-bandwidth speed. Formula: burst = maximum-bandwidth*burst-in-msec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CburstInMsec

Number of bytes that can be burst as fast as the interface can transmit. Formula: cburst = maximum-bandwidth*cburst-in-msec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassId

Class ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuaranteedBandwidthPercentage

Guaranteed bandwith in percentage.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

ID number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Limit

Hard limit on the real queue size in packets.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Max

Average queue size in packets at which RED drop probability is maximal.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumBandwidthPercentage

Maximum bandwith in percentage.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Min

Average queue size in packets at which RED drop becomes a possibility.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

Priority.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedProbability

Maximum probability (in percentage) for RED marking.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

