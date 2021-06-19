# TF::Akamai::GtmProperty

Use the `akamai_gtm_property` resource provides the resource for creating, configuring and importing a GTM property, a set of IP addresses or CNAMEs that GTM provides in response to DNS queries based on a set of rules. 

~> **Note** Import requires an ID with this format: `existing_domain_name`:`existing_property_name`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Akamai::GtmProperty",
    "Properties" : {
        "<a href="#backupcname" title="BackupCname">BackupCname</a>" : <i>String</i>,
        "<a href="#backupip" title="BackupIp">BackupIp</a>" : <i>String</i>,
        "<a href="#balancebydownloadscore" title="BalanceByDownloadScore">BalanceByDownloadScore</a>" : <i>Boolean</i>,
        "<a href="#cname" title="Cname">Cname</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#dynamicttl" title="DynamicTtl">DynamicTtl</a>" : <i>Double</i>,
        "<a href="#failbackdelay" title="FailbackDelay">FailbackDelay</a>" : <i>Double</i>,
        "<a href="#failoverdelay" title="FailoverDelay">FailoverDelay</a>" : <i>Double</i>,
        "<a href="#ghostdemandreporting" title="GhostDemandReporting">GhostDemandReporting</a>" : <i>Boolean</i>,
        "<a href="#handoutlimit" title="HandoutLimit">HandoutLimit</a>" : <i>Double</i>,
        "<a href="#handoutmode" title="HandoutMode">HandoutMode</a>" : <i>String</i>,
        "<a href="#healthmax" title="HealthMax">HealthMax</a>" : <i>Double</i>,
        "<a href="#healthmultiplier" title="HealthMultiplier">HealthMultiplier</a>" : <i>Double</i>,
        "<a href="#healththreshold" title="HealthThreshold">HealthThreshold</a>" : <i>Double</i>,
        "<a href="#ipv6" title="Ipv6">Ipv6</a>" : <i>Boolean</i>,
        "<a href="#loadimbalancepercentage" title="LoadImbalancePercentage">LoadImbalancePercentage</a>" : <i>Double</i>,
        "<a href="#mapname" title="MapName">MapName</a>" : <i>String</i>,
        "<a href="#maxunreachablepenalty" title="MaxUnreachablePenalty">MaxUnreachablePenalty</a>" : <i>Double</i>,
        "<a href="#minlivefraction" title="MinLiveFraction">MinLiveFraction</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#scoreaggregationtype" title="ScoreAggregationType">ScoreAggregationType</a>" : <i>String</i>,
        "<a href="#staticttl" title="StaticTtl">StaticTtl</a>" : <i>Double</i>,
        "<a href="#stickinessbonusconstant" title="StickinessBonusConstant">StickinessBonusConstant</a>" : <i>Double</i>,
        "<a href="#stickinessbonuspercentage" title="StickinessBonusPercentage">StickinessBonusPercentage</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#unreachablethreshold" title="UnreachableThreshold">UnreachableThreshold</a>" : <i>Double</i>,
        "<a href="#usecomputedtargets" title="UseComputedTargets">UseComputedTargets</a>" : <i>Boolean</i>,
        "<a href="#waitoncomplete" title="WaitOnComplete">WaitOnComplete</a>" : <i>Boolean</i>,
        "<a href="#livenesstest" title="LivenessTest">LivenessTest</a>" : <i>[ <a href="livenesstestdefinition.md">LivenessTestDefinition</a>, ... ]</i>,
        "<a href="#staticrrset" title="StaticRrSet">StaticRrSet</a>" : <i>[ <a href="staticrrsetdefinition.md">StaticRrSetDefinition</a>, ... ]</i>,
        "<a href="#traffictarget" title="TrafficTarget">TrafficTarget</a>" : <i>[ <a href="traffictargetdefinition.md">TrafficTargetDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Akamai::GtmProperty
Properties:
    <a href="#backupcname" title="BackupCname">BackupCname</a>: <i>String</i>
    <a href="#backupip" title="BackupIp">BackupIp</a>: <i>String</i>
    <a href="#balancebydownloadscore" title="BalanceByDownloadScore">BalanceByDownloadScore</a>: <i>Boolean</i>
    <a href="#cname" title="Cname">Cname</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#dynamicttl" title="DynamicTtl">DynamicTtl</a>: <i>Double</i>
    <a href="#failbackdelay" title="FailbackDelay">FailbackDelay</a>: <i>Double</i>
    <a href="#failoverdelay" title="FailoverDelay">FailoverDelay</a>: <i>Double</i>
    <a href="#ghostdemandreporting" title="GhostDemandReporting">GhostDemandReporting</a>: <i>Boolean</i>
    <a href="#handoutlimit" title="HandoutLimit">HandoutLimit</a>: <i>Double</i>
    <a href="#handoutmode" title="HandoutMode">HandoutMode</a>: <i>String</i>
    <a href="#healthmax" title="HealthMax">HealthMax</a>: <i>Double</i>
    <a href="#healthmultiplier" title="HealthMultiplier">HealthMultiplier</a>: <i>Double</i>
    <a href="#healththreshold" title="HealthThreshold">HealthThreshold</a>: <i>Double</i>
    <a href="#ipv6" title="Ipv6">Ipv6</a>: <i>Boolean</i>
    <a href="#loadimbalancepercentage" title="LoadImbalancePercentage">LoadImbalancePercentage</a>: <i>Double</i>
    <a href="#mapname" title="MapName">MapName</a>: <i>String</i>
    <a href="#maxunreachablepenalty" title="MaxUnreachablePenalty">MaxUnreachablePenalty</a>: <i>Double</i>
    <a href="#minlivefraction" title="MinLiveFraction">MinLiveFraction</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#scoreaggregationtype" title="ScoreAggregationType">ScoreAggregationType</a>: <i>String</i>
    <a href="#staticttl" title="StaticTtl">StaticTtl</a>: <i>Double</i>
    <a href="#stickinessbonusconstant" title="StickinessBonusConstant">StickinessBonusConstant</a>: <i>Double</i>
    <a href="#stickinessbonuspercentage" title="StickinessBonusPercentage">StickinessBonusPercentage</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#unreachablethreshold" title="UnreachableThreshold">UnreachableThreshold</a>: <i>Double</i>
    <a href="#usecomputedtargets" title="UseComputedTargets">UseComputedTargets</a>: <i>Boolean</i>
    <a href="#waitoncomplete" title="WaitOnComplete">WaitOnComplete</a>: <i>Boolean</i>
    <a href="#livenesstest" title="LivenessTest">LivenessTest</a>: <i>
      - <a href="livenesstestdefinition.md">LivenessTestDefinition</a></i>
    <a href="#staticrrset" title="StaticRrSet">StaticRrSet</a>: <i>
      - <a href="staticrrsetdefinition.md">StaticRrSetDefinition</a></i>
    <a href="#traffictarget" title="TrafficTarget">TrafficTarget</a>: <i>
      - <a href="traffictargetdefinition.md">TrafficTargetDefinition</a></i>
</pre>

## Properties

#### BackupCname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BalanceByDownloadScore

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailbackDelay

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailoverDelay

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GhostDemandReporting

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HandoutLimit

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HandoutMode

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthMax

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthMultiplier

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadImbalancePercentage

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MapName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUnreachablePenalty

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinLiveFraction

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScoreAggregationType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StickinessBonusConstant

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StickinessBonusPercentage

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnreachableThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseComputedTargets

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitOnComplete

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LivenessTest

_Required_: No

_Type_: List of <a href="livenesstestdefinition.md">LivenessTestDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticRrSet

_Required_: No

_Type_: List of <a href="staticrrsetdefinition.md">StaticRrSetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficTarget

_Required_: No

_Type_: List of <a href="traffictargetdefinition.md">TrafficTargetDefinition</a>

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

#### WeightedHashBitsForIpv4

Returns the <code>WeightedHashBitsForIpv4</code> value.

#### WeightedHashBitsForIpv6

Returns the <code>WeightedHashBitsForIpv6</code> value.

