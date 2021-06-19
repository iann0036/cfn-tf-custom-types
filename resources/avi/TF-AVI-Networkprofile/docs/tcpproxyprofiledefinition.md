# TF::AVI::Networkprofile TcpProxyProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#aggressivecongestionavoidance" title="AggressiveCongestionAvoidance">AggressiveCongestionAvoidance</a>" : <i>Boolean</i>,
    "<a href="#autowindowgrowth" title="AutoWindowGrowth">AutoWindowGrowth</a>" : <i>Boolean</i>,
    "<a href="#automatic" title="Automatic">Automatic</a>" : <i>Boolean</i>,
    "<a href="#ccalgo" title="CcAlgo">CcAlgo</a>" : <i>String</i>,
    "<a href="#congestionrecoveryscalingfactor" title="CongestionRecoveryScalingFactor">CongestionRecoveryScalingFactor</a>" : <i>Double</i>,
    "<a href="#idleconnectiontimeout" title="IdleConnectionTimeout">IdleConnectionTimeout</a>" : <i>Double</i>,
    "<a href="#idleconnectiontype" title="IdleConnectionType">IdleConnectionType</a>" : <i>String</i>,
    "<a href="#ignoretimewait" title="IgnoreTimeWait">IgnoreTimeWait</a>" : <i>Boolean</i>,
    "<a href="#ipdscp" title="IpDscp">IpDscp</a>" : <i>Double</i>,
    "<a href="#keepaliveinhalfclosestate" title="KeepaliveInHalfcloseState">KeepaliveInHalfcloseState</a>" : <i>Boolean</i>,
    "<a href="#maxretransmissions" title="MaxRetransmissions">MaxRetransmissions</a>" : <i>Double</i>,
    "<a href="#maxsegmentsize" title="MaxSegmentSize">MaxSegmentSize</a>" : <i>Double</i>,
    "<a href="#maxsynretransmissions" title="MaxSynRetransmissions">MaxSynRetransmissions</a>" : <i>Double</i>,
    "<a href="#minrexmttimeout" title="MinRexmtTimeout">MinRexmtTimeout</a>" : <i>Double</i>,
    "<a href="#naglesalgorithm" title="NaglesAlgorithm">NaglesAlgorithm</a>" : <i>Boolean</i>,
    "<a href="#reassemblyqueuesize" title="ReassemblyQueueSize">ReassemblyQueueSize</a>" : <i>Double</i>,
    "<a href="#receivewindow" title="ReceiveWindow">ReceiveWindow</a>" : <i>Double</i>,
    "<a href="#reorderthreshold" title="ReorderThreshold">ReorderThreshold</a>" : <i>Double</i>,
    "<a href="#slowstartscalingfactor" title="SlowStartScalingFactor">SlowStartScalingFactor</a>" : <i>Double</i>,
    "<a href="#timewaitdelay" title="TimeWaitDelay">TimeWaitDelay</a>" : <i>Double</i>,
    "<a href="#useinterfacemtu" title="UseInterfaceMtu">UseInterfaceMtu</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#aggressivecongestionavoidance" title="AggressiveCongestionAvoidance">AggressiveCongestionAvoidance</a>: <i>Boolean</i>
<a href="#autowindowgrowth" title="AutoWindowGrowth">AutoWindowGrowth</a>: <i>Boolean</i>
<a href="#automatic" title="Automatic">Automatic</a>: <i>Boolean</i>
<a href="#ccalgo" title="CcAlgo">CcAlgo</a>: <i>String</i>
<a href="#congestionrecoveryscalingfactor" title="CongestionRecoveryScalingFactor">CongestionRecoveryScalingFactor</a>: <i>Double</i>
<a href="#idleconnectiontimeout" title="IdleConnectionTimeout">IdleConnectionTimeout</a>: <i>Double</i>
<a href="#idleconnectiontype" title="IdleConnectionType">IdleConnectionType</a>: <i>String</i>
<a href="#ignoretimewait" title="IgnoreTimeWait">IgnoreTimeWait</a>: <i>Boolean</i>
<a href="#ipdscp" title="IpDscp">IpDscp</a>: <i>Double</i>
<a href="#keepaliveinhalfclosestate" title="KeepaliveInHalfcloseState">KeepaliveInHalfcloseState</a>: <i>Boolean</i>
<a href="#maxretransmissions" title="MaxRetransmissions">MaxRetransmissions</a>: <i>Double</i>
<a href="#maxsegmentsize" title="MaxSegmentSize">MaxSegmentSize</a>: <i>Double</i>
<a href="#maxsynretransmissions" title="MaxSynRetransmissions">MaxSynRetransmissions</a>: <i>Double</i>
<a href="#minrexmttimeout" title="MinRexmtTimeout">MinRexmtTimeout</a>: <i>Double</i>
<a href="#naglesalgorithm" title="NaglesAlgorithm">NaglesAlgorithm</a>: <i>Boolean</i>
<a href="#reassemblyqueuesize" title="ReassemblyQueueSize">ReassemblyQueueSize</a>: <i>Double</i>
<a href="#receivewindow" title="ReceiveWindow">ReceiveWindow</a>: <i>Double</i>
<a href="#reorderthreshold" title="ReorderThreshold">ReorderThreshold</a>: <i>Double</i>
<a href="#slowstartscalingfactor" title="SlowStartScalingFactor">SlowStartScalingFactor</a>: <i>Double</i>
<a href="#timewaitdelay" title="TimeWaitDelay">TimeWaitDelay</a>: <i>Double</i>
<a href="#useinterfacemtu" title="UseInterfaceMtu">UseInterfaceMtu</a>: <i>Boolean</i>
</pre>

## Properties

#### AggressiveCongestionAvoidance

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoWindowGrowth

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Automatic

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CcAlgo

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CongestionRecoveryScalingFactor

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleConnectionTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleConnectionType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreTimeWait

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpDscp

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepaliveInHalfcloseState

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRetransmissions

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSegmentSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSynRetransmissions

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinRexmtTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NaglesAlgorithm

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReassemblyQueueSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReceiveWindow

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReorderThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlowStartScalingFactor

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeWaitDelay

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseInterfaceMtu

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

