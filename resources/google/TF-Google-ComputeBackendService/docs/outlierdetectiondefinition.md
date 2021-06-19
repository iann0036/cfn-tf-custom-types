# TF::Google::ComputeBackendService OutlierDetectionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#consecutiveerrors" title="ConsecutiveErrors">ConsecutiveErrors</a>" : <i>Double</i>,
    "<a href="#consecutivegatewayfailure" title="ConsecutiveGatewayFailure">ConsecutiveGatewayFailure</a>" : <i>Double</i>,
    "<a href="#enforcingconsecutiveerrors" title="EnforcingConsecutiveErrors">EnforcingConsecutiveErrors</a>" : <i>Double</i>,
    "<a href="#enforcingconsecutivegatewayfailure" title="EnforcingConsecutiveGatewayFailure">EnforcingConsecutiveGatewayFailure</a>" : <i>Double</i>,
    "<a href="#enforcingsuccessrate" title="EnforcingSuccessRate">EnforcingSuccessRate</a>" : <i>Double</i>,
    "<a href="#maxejectionpercent" title="MaxEjectionPercent">MaxEjectionPercent</a>" : <i>Double</i>,
    "<a href="#successrateminimumhosts" title="SuccessRateMinimumHosts">SuccessRateMinimumHosts</a>" : <i>Double</i>,
    "<a href="#successraterequestvolume" title="SuccessRateRequestVolume">SuccessRateRequestVolume</a>" : <i>Double</i>,
    "<a href="#successratestdevfactor" title="SuccessRateStdevFactor">SuccessRateStdevFactor</a>" : <i>Double</i>,
    "<a href="#baseejectiontime" title="BaseEjectionTime">BaseEjectionTime</a>" : <i>[ <a href="baseejectiontimedefinition.md">BaseEjectionTimeDefinition</a>, ... ]</i>,
    "<a href="#interval" title="Interval">Interval</a>" : <i>[ <a href="intervaldefinition.md">IntervalDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#consecutiveerrors" title="ConsecutiveErrors">ConsecutiveErrors</a>: <i>Double</i>
<a href="#consecutivegatewayfailure" title="ConsecutiveGatewayFailure">ConsecutiveGatewayFailure</a>: <i>Double</i>
<a href="#enforcingconsecutiveerrors" title="EnforcingConsecutiveErrors">EnforcingConsecutiveErrors</a>: <i>Double</i>
<a href="#enforcingconsecutivegatewayfailure" title="EnforcingConsecutiveGatewayFailure">EnforcingConsecutiveGatewayFailure</a>: <i>Double</i>
<a href="#enforcingsuccessrate" title="EnforcingSuccessRate">EnforcingSuccessRate</a>: <i>Double</i>
<a href="#maxejectionpercent" title="MaxEjectionPercent">MaxEjectionPercent</a>: <i>Double</i>
<a href="#successrateminimumhosts" title="SuccessRateMinimumHosts">SuccessRateMinimumHosts</a>: <i>Double</i>
<a href="#successraterequestvolume" title="SuccessRateRequestVolume">SuccessRateRequestVolume</a>: <i>Double</i>
<a href="#successratestdevfactor" title="SuccessRateStdevFactor">SuccessRateStdevFactor</a>: <i>Double</i>
<a href="#baseejectiontime" title="BaseEjectionTime">BaseEjectionTime</a>: <i>
      - <a href="baseejectiontimedefinition.md">BaseEjectionTimeDefinition</a></i>
<a href="#interval" title="Interval">Interval</a>: <i>
      - <a href="intervaldefinition.md">IntervalDefinition</a></i>
</pre>

## Properties

#### ConsecutiveErrors

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsecutiveGatewayFailure

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnforcingConsecutiveErrors

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnforcingConsecutiveGatewayFailure

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnforcingSuccessRate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxEjectionPercent

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuccessRateMinimumHosts

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuccessRateRequestVolume

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuccessRateStdevFactor

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BaseEjectionTime

_Required_: No

_Type_: List of <a href="baseejectiontimedefinition.md">BaseEjectionTimeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

_Required_: No

_Type_: List of <a href="intervaldefinition.md">IntervalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

