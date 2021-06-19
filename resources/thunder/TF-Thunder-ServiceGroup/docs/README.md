# TF::Thunder::ServiceGroup

`thunder_service_group` Provides details about thunder slb service group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::ServiceGroup",
    "Properties" : {
        "<a href="#backupservereventlog" title="BackupServerEventLog">BackupServerEventLog</a>" : <i>Double</i>,
        "<a href="#connrate" title="ConnRate">ConnRate</a>" : <i>Double</i>,
        "<a href="#connrateduration" title="ConnRateDuration">ConnRateDuration</a>" : <i>Double</i>,
        "<a href="#connrategraceperiod" title="ConnRateGracePeriod">ConnRateGracePeriod</a>" : <i>Double</i>,
        "<a href="#connratelog" title="ConnRateLog">ConnRateLog</a>" : <i>Double</i>,
        "<a href="#connraterevertduration" title="ConnRateRevertDuration">ConnRateRevertDuration</a>" : <i>Double</i>,
        "<a href="#connrevertrate" title="ConnRevertRate">ConnRevertRate</a>" : <i>Double</i>,
        "<a href="#extendedstats" title="ExtendedStats">ExtendedStats</a>" : <i>Double</i>,
        "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>String</i>,
        "<a href="#healthcheckdisable" title="HealthCheckDisable">HealthCheckDisable</a>" : <i>Double</i>,
        "<a href="#l4sessionrevertduration" title="L4SessionRevertDuration">L4SessionRevertDuration</a>" : <i>Double</i>,
        "<a href="#l4sessionusage" title="L4SessionUsage">L4SessionUsage</a>" : <i>Double</i>,
        "<a href="#l4sessionusageduration" title="L4SessionUsageDuration">L4SessionUsageDuration</a>" : <i>Double</i>,
        "<a href="#l4sessionusagegraceperiod" title="L4SessionUsageGracePeriod">L4SessionUsageGracePeriod</a>" : <i>Double</i>,
        "<a href="#l4sessionusagelog" title="L4SessionUsageLog">L4SessionUsageLog</a>" : <i>Double</i>,
        "<a href="#l4sessionusagerevertrate" title="L4SessionUsageRevertRate">L4SessionUsageRevertRate</a>" : <i>Double</i>,
        "<a href="#lbmethod" title="LbMethod">LbMethod</a>" : <i>String</i>,
        "<a href="#lcmethod" title="LcMethod">LcMethod</a>" : <i>String</i>,
        "<a href="#minactivemember" title="MinActiveMember">MinActiveMember</a>" : <i>Double</i>,
        "<a href="#minactivememberaction" title="MinActiveMemberAction">MinActiveMemberAction</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#priorityaffinity" title="PriorityAffinity">PriorityAffinity</a>" : <i>Double</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#pseudoroundrobin" title="PseudoRoundRobin">PseudoRoundRobin</a>" : <i>Double</i>,
        "<a href="#reportdelay" title="ReportDelay">ReportDelay</a>" : <i>Double</i>,
        "<a href="#resetonserverselectionfail" title="ResetOnServerSelectionFail">ResetOnServerSelectionFail</a>" : <i>Double</i>,
        "<a href="#resetpriorityaffinity" title="ResetPriorityAffinity">ResetPriorityAffinity</a>" : <i>Double</i>,
        "<a href="#rptextserver" title="RptExtServer">RptExtServer</a>" : <i>Double</i>,
        "<a href="#samplersptime" title="SampleRspTime">SampleRspTime</a>" : <i>Double</i>,
        "<a href="#sharedpartitionpolicytemplate" title="SharedPartitionPolicyTemplate">SharedPartitionPolicyTemplate</a>" : <i>Double</i>,
        "<a href="#sharedpartitionsvcgrphealthcheck" title="SharedPartitionSvcgrpHealthCheck">SharedPartitionSvcgrpHealthCheck</a>" : <i>Double</i>,
        "<a href="#statelessautoswitch" title="StatelessAutoSwitch">StatelessAutoSwitch</a>" : <i>Double</i>,
        "<a href="#statelesslbmethod" title="StatelessLbMethod">StatelessLbMethod</a>" : <i>String</i>,
        "<a href="#statelesslbmethod2" title="StatelessLbMethod2">StatelessLbMethod2</a>" : <i>String</i>,
        "<a href="#statsdataaction" title="StatsDataAction">StatsDataAction</a>" : <i>String</i>,
        "<a href="#strictselect" title="StrictSelect">StrictSelect</a>" : <i>Double</i>,
        "<a href="#svcgrphealthcheckshared" title="SvcgrpHealthCheckShared">SvcgrpHealthCheckShared</a>" : <i>String</i>,
        "<a href="#templatepolicy" title="TemplatePolicy">TemplatePolicy</a>" : <i>String</i>,
        "<a href="#templatepolicyshared" title="TemplatePolicyShared">TemplatePolicyShared</a>" : <i>String</i>,
        "<a href="#templateport" title="TemplatePort">TemplatePort</a>" : <i>String</i>,
        "<a href="#templateserver" title="TemplateServer">TemplateServer</a>" : <i>String</i>,
        "<a href="#topfastest" title="TopFastest">TopFastest</a>" : <i>Double</i>,
        "<a href="#topslowest" title="TopSlowest">TopSlowest</a>" : <i>Double</i>,
        "<a href="#trafficreplicationmirror" title="TrafficReplicationMirror">TrafficReplicationMirror</a>" : <i>Double</i>,
        "<a href="#trafficreplicationmirrordarepl" title="TrafficReplicationMirrorDaRepl">TrafficReplicationMirrorDaRepl</a>" : <i>Double</i>,
        "<a href="#trafficreplicationmirroriprepl" title="TrafficReplicationMirrorIpRepl">TrafficReplicationMirrorIpRepl</a>" : <i>Double</i>,
        "<a href="#trafficreplicationmirrorsadarepl" title="TrafficReplicationMirrorSaDaRepl">TrafficReplicationMirrorSaDaRepl</a>" : <i>Double</i>,
        "<a href="#trafficreplicationmirrorsarepl" title="TrafficReplicationMirrorSaRepl">TrafficReplicationMirrorSaRepl</a>" : <i>Double</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#memberlist" title="MemberList">MemberList</a>" : <i>[ <a href="memberlistdefinition.md">MemberListDefinition</a>, ... ]</i>,
        "<a href="#priorities" title="Priorities">Priorities</a>" : <i>[ <a href="prioritiesdefinition.md">PrioritiesDefinition</a>, ... ]</i>,
        "<a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>" : <i>[ <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::ServiceGroup
Properties:
    <a href="#backupservereventlog" title="BackupServerEventLog">BackupServerEventLog</a>: <i>Double</i>
    <a href="#connrate" title="ConnRate">ConnRate</a>: <i>Double</i>
    <a href="#connrateduration" title="ConnRateDuration">ConnRateDuration</a>: <i>Double</i>
    <a href="#connrategraceperiod" title="ConnRateGracePeriod">ConnRateGracePeriod</a>: <i>Double</i>
    <a href="#connratelog" title="ConnRateLog">ConnRateLog</a>: <i>Double</i>
    <a href="#connraterevertduration" title="ConnRateRevertDuration">ConnRateRevertDuration</a>: <i>Double</i>
    <a href="#connrevertrate" title="ConnRevertRate">ConnRevertRate</a>: <i>Double</i>
    <a href="#extendedstats" title="ExtendedStats">ExtendedStats</a>: <i>Double</i>
    <a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>String</i>
    <a href="#healthcheckdisable" title="HealthCheckDisable">HealthCheckDisable</a>: <i>Double</i>
    <a href="#l4sessionrevertduration" title="L4SessionRevertDuration">L4SessionRevertDuration</a>: <i>Double</i>
    <a href="#l4sessionusage" title="L4SessionUsage">L4SessionUsage</a>: <i>Double</i>
    <a href="#l4sessionusageduration" title="L4SessionUsageDuration">L4SessionUsageDuration</a>: <i>Double</i>
    <a href="#l4sessionusagegraceperiod" title="L4SessionUsageGracePeriod">L4SessionUsageGracePeriod</a>: <i>Double</i>
    <a href="#l4sessionusagelog" title="L4SessionUsageLog">L4SessionUsageLog</a>: <i>Double</i>
    <a href="#l4sessionusagerevertrate" title="L4SessionUsageRevertRate">L4SessionUsageRevertRate</a>: <i>Double</i>
    <a href="#lbmethod" title="LbMethod">LbMethod</a>: <i>String</i>
    <a href="#lcmethod" title="LcMethod">LcMethod</a>: <i>String</i>
    <a href="#minactivemember" title="MinActiveMember">MinActiveMember</a>: <i>Double</i>
    <a href="#minactivememberaction" title="MinActiveMemberAction">MinActiveMemberAction</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#priorityaffinity" title="PriorityAffinity">PriorityAffinity</a>: <i>Double</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#pseudoroundrobin" title="PseudoRoundRobin">PseudoRoundRobin</a>: <i>Double</i>
    <a href="#reportdelay" title="ReportDelay">ReportDelay</a>: <i>Double</i>
    <a href="#resetonserverselectionfail" title="ResetOnServerSelectionFail">ResetOnServerSelectionFail</a>: <i>Double</i>
    <a href="#resetpriorityaffinity" title="ResetPriorityAffinity">ResetPriorityAffinity</a>: <i>Double</i>
    <a href="#rptextserver" title="RptExtServer">RptExtServer</a>: <i>Double</i>
    <a href="#samplersptime" title="SampleRspTime">SampleRspTime</a>: <i>Double</i>
    <a href="#sharedpartitionpolicytemplate" title="SharedPartitionPolicyTemplate">SharedPartitionPolicyTemplate</a>: <i>Double</i>
    <a href="#sharedpartitionsvcgrphealthcheck" title="SharedPartitionSvcgrpHealthCheck">SharedPartitionSvcgrpHealthCheck</a>: <i>Double</i>
    <a href="#statelessautoswitch" title="StatelessAutoSwitch">StatelessAutoSwitch</a>: <i>Double</i>
    <a href="#statelesslbmethod" title="StatelessLbMethod">StatelessLbMethod</a>: <i>String</i>
    <a href="#statelesslbmethod2" title="StatelessLbMethod2">StatelessLbMethod2</a>: <i>String</i>
    <a href="#statsdataaction" title="StatsDataAction">StatsDataAction</a>: <i>String</i>
    <a href="#strictselect" title="StrictSelect">StrictSelect</a>: <i>Double</i>
    <a href="#svcgrphealthcheckshared" title="SvcgrpHealthCheckShared">SvcgrpHealthCheckShared</a>: <i>String</i>
    <a href="#templatepolicy" title="TemplatePolicy">TemplatePolicy</a>: <i>String</i>
    <a href="#templatepolicyshared" title="TemplatePolicyShared">TemplatePolicyShared</a>: <i>String</i>
    <a href="#templateport" title="TemplatePort">TemplatePort</a>: <i>String</i>
    <a href="#templateserver" title="TemplateServer">TemplateServer</a>: <i>String</i>
    <a href="#topfastest" title="TopFastest">TopFastest</a>: <i>Double</i>
    <a href="#topslowest" title="TopSlowest">TopSlowest</a>: <i>Double</i>
    <a href="#trafficreplicationmirror" title="TrafficReplicationMirror">TrafficReplicationMirror</a>: <i>Double</i>
    <a href="#trafficreplicationmirrordarepl" title="TrafficReplicationMirrorDaRepl">TrafficReplicationMirrorDaRepl</a>: <i>Double</i>
    <a href="#trafficreplicationmirroriprepl" title="TrafficReplicationMirrorIpRepl">TrafficReplicationMirrorIpRepl</a>: <i>Double</i>
    <a href="#trafficreplicationmirrorsadarepl" title="TrafficReplicationMirrorSaDaRepl">TrafficReplicationMirrorSaDaRepl</a>: <i>Double</i>
    <a href="#trafficreplicationmirrorsarepl" title="TrafficReplicationMirrorSaRepl">TrafficReplicationMirrorSaRepl</a>: <i>Double</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#memberlist" title="MemberList">MemberList</a>: <i>
      - <a href="memberlistdefinition.md">MemberListDefinition</a></i>
    <a href="#priorities" title="Priorities">Priorities</a>: <i>
      - <a href="prioritiesdefinition.md">PrioritiesDefinition</a></i>
    <a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>: <i>
      - <a href="samplingenabledefinition.md">SamplingEnableDefinition</a></i>
</pre>

## Properties

#### BackupServerEventLog

Send log info on back up server events.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnRate

Dynamically enable stateless method by conn-rate (Rate to trigger stateless method(conn/sec)).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnRateDuration

Period that trigger condition consistently happens(seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnRateGracePeriod

Define the grace period during transition (Define the grace period during transition(seconds)).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnRateLog

Send log if transition happens.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnRateRevertDuration

Period that revert condition consistently happens(seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnRevertRate

Rate to revert to statelful method (conn/sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedStats

Enable extended statistics on service group.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheck

Health Check (Monitor Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckDisable

Disable health check.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L4SessionRevertDuration

Period that revert condition consistently happens(seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L4SessionUsage

Dynamically enable stateless method by session usage (Usage to trigger stateless method).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L4SessionUsageDuration

Period that trigger condition consistently happens(seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L4SessionUsageGracePeriod

Define the grace period during transition (Define the grace period during transition(seconds)).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L4SessionUsageLog

Send log if transition happens.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L4SessionUsageRevertRate

Usage to revert to statelful method.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbMethod

‘dst-ip-hash’: Load-balancing based on only Dst IP and Port hash; ‘dst-ip-only-hash’: Load-balancing based on only Dst IP hash; ‘fastest-response’: Fastest response time on service port level; ‘least-request’: Least request on service port level; ‘src-ip-hash’: Load-balancing based on only Src IP and Port hash; ‘src-ip-only-hash’: Load-balancing based on only Src IP hash; ‘weighted-rr’: Weighted round robin on server level; ‘round-robin’: Round robin on server level; ‘round-robin-strict’: Strict mode round robin on server level; ‘odd-even-hash’: odd/even hash based of client src-ip;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LcMethod

‘least-connection’: Least connection on server level; ‘service-least-connection’: Least connection on service port level; ‘weighted-least-connection’: Weighted least connection on server level; ‘service-weighted-least-connection’: Weighted least connection on service port level;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinActiveMember

Minimum Active Member Per Priority (Minimum Active Member before Action).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinActiveMemberAction

‘dynamic-priority’: dynamic change member priority to met the min-active-member requirement; ‘skip-pri-set’: Skip Current Priority Set If Min not met;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Member name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PriorityAffinity

Priority affinity. Persist to the same priority if possible.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

‘tcp’: TCP LB service; ‘udp’: UDP LB service;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PseudoRoundRobin

PRR, select the oldest node for sub-select.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReportDelay

Reporting frequency (in minutes).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResetOnServerSelectionFail

Send reset to client if server selection fails.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResetPriorityAffinity

Reset.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RptExtServer

Report top 10 fastest/slowest servers.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SampleRspTime

sample server response time.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionPolicyTemplate

Reference a policy template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionSvcgrpHealthCheck

Reference a health-check from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatelessAutoSwitch

Enable auto stateless method.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatelessLbMethod

‘stateless-dst-ip-hash’: Stateless load-balancing based on Dst IP and Dst port hash; ‘stateless-per-pkt-round-robin’: Stateless load-balancing using per-packet round-robin; ‘stateless-src-dst-ip-hash’: Stateless load-balancing based on IP and port hash for both Src and Dst; ‘stateless-src-dst-ip-only-hash’: Stateless load-balancing based on only IP hash for both Src and Dst; ‘stateless-src-ip-hash’: Stateless load-balancing based on Src IP and Src port hash; ‘stateless-src-ip-only-hash’: Stateless load-balancing based on only Src IP hash;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatelessLbMethod2

‘stateless-dst-ip-hash’: Stateless load-balancing based on Dst IP and Dst port hash; ‘stateless-per-pkt-round-robin’: Stateless load-balancing using per-packet round-robin; ‘stateless-src-dst-ip-hash’: Stateless load-balancing based on IP and port hash for both Src and Dst; ‘stateless-src-dst-ip-only-hash’: Stateless load-balancing based on only IP hash for both Src and Dst; ‘stateless-src-ip-hash’: Stateless load-balancing based on Src IP and Src port hash; ‘stateless-src-ip-only-hash’: Stateless load-balancing based on only Src IP hash;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatsDataAction

‘stats-data-enable’: Enable statistical data collection for service group; ‘stats-data-disable’: Disable statistical data collection for service group;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StrictSelect

strict selection.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SvcgrpHealthCheckShared

Health Check (Monitor Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePolicy

Policy template (Policy template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePolicyShared

Policy template.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplatePort

Port template (Port template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateServer

Server template (Server template name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopFastest

Report top 10 fastest servers.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopSlowest

Report top 10 slowest servers.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficReplicationMirror

Mirror Bi-directional Packet.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficReplicationMirrorDaRepl

Replace Destination MAC.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficReplicationMirrorIpRepl

Replaces IP with server-IP.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficReplicationMirrorSaDaRepl

Replace Source MAC and Destination MAC.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficReplicationMirrorSaRepl

Replace Source MAC.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemberList

_Required_: No

_Type_: List of <a href="memberlistdefinition.md">MemberListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priorities

_Required_: No

_Type_: List of <a href="prioritiesdefinition.md">PrioritiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SamplingEnable

_Required_: No

_Type_: List of <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

