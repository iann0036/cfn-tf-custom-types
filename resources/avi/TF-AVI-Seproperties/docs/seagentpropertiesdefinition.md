# TF::AVI::Seproperties SeAgentPropertiesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#controllerechomissaggressivelimit" title="ControllerEchoMissAggressiveLimit">ControllerEchoMissAggressiveLimit</a>" : <i>Double</i>,
    "<a href="#controllerechomisslimit" title="ControllerEchoMissLimit">ControllerEchoMissLimit</a>" : <i>Double</i>,
    "<a href="#controllerechorpcaggressivetimeout" title="ControllerEchoRpcAggressiveTimeout">ControllerEchoRpcAggressiveTimeout</a>" : <i>Double</i>,
    "<a href="#controllerechorpctimeout" title="ControllerEchoRpcTimeout">ControllerEchoRpcTimeout</a>" : <i>Double</i>,
    "<a href="#controllerheartbeatmisslimit" title="ControllerHeartbeatMissLimit">ControllerHeartbeatMissLimit</a>" : <i>Double</i>,
    "<a href="#controllerheartbeattimeoutsec" title="ControllerHeartbeatTimeoutSec">ControllerHeartbeatTimeoutSec</a>" : <i>Double</i>,
    "<a href="#controllerregistrationtimeoutsec" title="ControllerRegistrationTimeoutSec">ControllerRegistrationTimeoutSec</a>" : <i>Double</i>,
    "<a href="#controllerrpctimeout" title="ControllerRpcTimeout">ControllerRpcTimeout</a>" : <i>Double</i>,
    "<a href="#cpustatsinterval" title="CpustatsInterval">CpustatsInterval</a>" : <i>Double</i>,
    "<a href="#ctrlregpendingmaxwaittime" title="CtrlRegPendingMaxWaitTime">CtrlRegPendingMaxWaitTime</a>" : <i>Double</i>,
    "<a href="#debugmode" title="DebugMode">DebugMode</a>" : <i>Boolean</i>,
    "<a href="#dpaggressivedeqintervalmsec" title="DpAggressiveDeqIntervalMsec">DpAggressiveDeqIntervalMsec</a>" : <i>Double</i>,
    "<a href="#dpaggressiveenqintervalmsec" title="DpAggressiveEnqIntervalMsec">DpAggressiveEnqIntervalMsec</a>" : <i>Double</i>,
    "<a href="#dpbatchsize" title="DpBatchSize">DpBatchSize</a>" : <i>Double</i>,
    "<a href="#dpdeqintervalmsec" title="DpDeqIntervalMsec">DpDeqIntervalMsec</a>" : <i>Double</i>,
    "<a href="#dpenqintervalmsec" title="DpEnqIntervalMsec">DpEnqIntervalMsec</a>" : <i>Double</i>,
    "<a href="#dpmaxwaitrsptimesec" title="DpMaxWaitRspTimeSec">DpMaxWaitRspTimeSec</a>" : <i>Double</i>,
    "<a href="#dpregpendingmaxwaittime" title="DpRegPendingMaxWaitTime">DpRegPendingMaxWaitTime</a>" : <i>Double</i>,
    "<a href="#headlesstimeoutsec" title="HeadlessTimeoutSec">HeadlessTimeoutSec</a>" : <i>Double</i>,
    "<a href="#ignoredockermacchange" title="IgnoreDockerMacChange">IgnoreDockerMacChange</a>" : <i>Boolean</i>,
    "<a href="#nshelperdeqintervalmsec" title="NsHelperDeqIntervalMsec">NsHelperDeqIntervalMsec</a>" : <i>Double</i>,
    "<a href="#sdbflushinterval" title="SdbFlushInterval">SdbFlushInterval</a>" : <i>Double</i>,
    "<a href="#sdbpipelinesize" title="SdbPipelineSize">SdbPipelineSize</a>" : <i>Double</i>,
    "<a href="#sdbscancount" title="SdbScanCount">SdbScanCount</a>" : <i>Double</i>,
    "<a href="#segrpchangedisruptive" title="SeGrpChangeDisruptive">SeGrpChangeDisruptive</a>" : <i>Boolean</i>,
    "<a href="#sendsereadytimeout" title="SendSeReadyTimeout">SendSeReadyTimeout</a>" : <i>Double</i>,
    "<a href="#statesflushinterval" title="StatesFlushInterval">StatesFlushInterval</a>" : <i>Double</i>,
    "<a href="#vnicdhcpipcheckinterval" title="VnicDhcpIpCheckInterval">VnicDhcpIpCheckInterval</a>" : <i>Double</i>,
    "<a href="#vnicdhcpipmaxretries" title="VnicDhcpIpMaxRetries">VnicDhcpIpMaxRetries</a>" : <i>Double</i>,
    "<a href="#vnicipdeleteinterval" title="VnicIpDeleteInterval">VnicIpDeleteInterval</a>" : <i>Double</i>,
    "<a href="#vnicprobeinterval" title="VnicProbeInterval">VnicProbeInterval</a>" : <i>Double</i>,
    "<a href="#vnicrpcretryinterval" title="VnicRpcRetryInterval">VnicRpcRetryInterval</a>" : <i>Double</i>,
    "<a href="#vnicdbcmdhistorysize" title="VnicdbCmdHistorySize">VnicdbCmdHistorySize</a>" : <i>Double</i>,
    "<a href="#seagentstatecacheproperties" title="SeagentStatecacheProperties">SeagentStatecacheProperties</a>" : <i>[ <a href="seagentstatecachepropertiesdefinition.md">SeagentStatecachePropertiesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#controllerechomissaggressivelimit" title="ControllerEchoMissAggressiveLimit">ControllerEchoMissAggressiveLimit</a>: <i>Double</i>
<a href="#controllerechomisslimit" title="ControllerEchoMissLimit">ControllerEchoMissLimit</a>: <i>Double</i>
<a href="#controllerechorpcaggressivetimeout" title="ControllerEchoRpcAggressiveTimeout">ControllerEchoRpcAggressiveTimeout</a>: <i>Double</i>
<a href="#controllerechorpctimeout" title="ControllerEchoRpcTimeout">ControllerEchoRpcTimeout</a>: <i>Double</i>
<a href="#controllerheartbeatmisslimit" title="ControllerHeartbeatMissLimit">ControllerHeartbeatMissLimit</a>: <i>Double</i>
<a href="#controllerheartbeattimeoutsec" title="ControllerHeartbeatTimeoutSec">ControllerHeartbeatTimeoutSec</a>: <i>Double</i>
<a href="#controllerregistrationtimeoutsec" title="ControllerRegistrationTimeoutSec">ControllerRegistrationTimeoutSec</a>: <i>Double</i>
<a href="#controllerrpctimeout" title="ControllerRpcTimeout">ControllerRpcTimeout</a>: <i>Double</i>
<a href="#cpustatsinterval" title="CpustatsInterval">CpustatsInterval</a>: <i>Double</i>
<a href="#ctrlregpendingmaxwaittime" title="CtrlRegPendingMaxWaitTime">CtrlRegPendingMaxWaitTime</a>: <i>Double</i>
<a href="#debugmode" title="DebugMode">DebugMode</a>: <i>Boolean</i>
<a href="#dpaggressivedeqintervalmsec" title="DpAggressiveDeqIntervalMsec">DpAggressiveDeqIntervalMsec</a>: <i>Double</i>
<a href="#dpaggressiveenqintervalmsec" title="DpAggressiveEnqIntervalMsec">DpAggressiveEnqIntervalMsec</a>: <i>Double</i>
<a href="#dpbatchsize" title="DpBatchSize">DpBatchSize</a>: <i>Double</i>
<a href="#dpdeqintervalmsec" title="DpDeqIntervalMsec">DpDeqIntervalMsec</a>: <i>Double</i>
<a href="#dpenqintervalmsec" title="DpEnqIntervalMsec">DpEnqIntervalMsec</a>: <i>Double</i>
<a href="#dpmaxwaitrsptimesec" title="DpMaxWaitRspTimeSec">DpMaxWaitRspTimeSec</a>: <i>Double</i>
<a href="#dpregpendingmaxwaittime" title="DpRegPendingMaxWaitTime">DpRegPendingMaxWaitTime</a>: <i>Double</i>
<a href="#headlesstimeoutsec" title="HeadlessTimeoutSec">HeadlessTimeoutSec</a>: <i>Double</i>
<a href="#ignoredockermacchange" title="IgnoreDockerMacChange">IgnoreDockerMacChange</a>: <i>Boolean</i>
<a href="#nshelperdeqintervalmsec" title="NsHelperDeqIntervalMsec">NsHelperDeqIntervalMsec</a>: <i>Double</i>
<a href="#sdbflushinterval" title="SdbFlushInterval">SdbFlushInterval</a>: <i>Double</i>
<a href="#sdbpipelinesize" title="SdbPipelineSize">SdbPipelineSize</a>: <i>Double</i>
<a href="#sdbscancount" title="SdbScanCount">SdbScanCount</a>: <i>Double</i>
<a href="#segrpchangedisruptive" title="SeGrpChangeDisruptive">SeGrpChangeDisruptive</a>: <i>Boolean</i>
<a href="#sendsereadytimeout" title="SendSeReadyTimeout">SendSeReadyTimeout</a>: <i>Double</i>
<a href="#statesflushinterval" title="StatesFlushInterval">StatesFlushInterval</a>: <i>Double</i>
<a href="#vnicdhcpipcheckinterval" title="VnicDhcpIpCheckInterval">VnicDhcpIpCheckInterval</a>: <i>Double</i>
<a href="#vnicdhcpipmaxretries" title="VnicDhcpIpMaxRetries">VnicDhcpIpMaxRetries</a>: <i>Double</i>
<a href="#vnicipdeleteinterval" title="VnicIpDeleteInterval">VnicIpDeleteInterval</a>: <i>Double</i>
<a href="#vnicprobeinterval" title="VnicProbeInterval">VnicProbeInterval</a>: <i>Double</i>
<a href="#vnicrpcretryinterval" title="VnicRpcRetryInterval">VnicRpcRetryInterval</a>: <i>Double</i>
<a href="#vnicdbcmdhistorysize" title="VnicdbCmdHistorySize">VnicdbCmdHistorySize</a>: <i>Double</i>
<a href="#seagentstatecacheproperties" title="SeagentStatecacheProperties">SeagentStatecacheProperties</a>: <i>
      - <a href="seagentstatecachepropertiesdefinition.md">SeagentStatecachePropertiesDefinition</a></i>
</pre>

## Properties

#### ControllerEchoMissAggressiveLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerEchoMissLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerEchoRpcAggressiveTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerEchoRpcTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerHeartbeatMissLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerHeartbeatTimeoutSec

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerRegistrationTimeoutSec

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerRpcTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpustatsInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CtrlRegPendingMaxWaitTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DebugMode

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpAggressiveDeqIntervalMsec

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpAggressiveEnqIntervalMsec

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpBatchSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpDeqIntervalMsec

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpEnqIntervalMsec

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpMaxWaitRspTimeSec

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpRegPendingMaxWaitTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeadlessTimeoutSec

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreDockerMacChange

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsHelperDeqIntervalMsec

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdbFlushInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdbPipelineSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdbScanCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeGrpChangeDisruptive

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendSeReadyTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatesFlushInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnicDhcpIpCheckInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnicDhcpIpMaxRetries

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnicIpDeleteInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnicProbeInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnicRpcRetryInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnicdbCmdHistorySize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeagentStatecacheProperties

_Required_: No

_Type_: List of <a href="seagentstatecachepropertiesdefinition.md">SeagentStatecachePropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

