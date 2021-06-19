# TF::Thunder::SlbTemplatePolicy

`thunder_slb_template_policy` Provides details about thunder slb template policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplatePolicy",
    "Properties" : {
        "<a href="#bwlistname" title="BwListName">BwListName</a>" : <i>String</i>,
        "<a href="#fulldomaintree" title="FullDomainTree">FullDomainTree</a>" : <i>Double</i>,
        "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#overlimit" title="OverLimit">OverLimit</a>" : <i>Double</i>,
        "<a href="#overlimitlockup" title="OverLimitLockup">OverLimitLockup</a>" : <i>Double</i>,
        "<a href="#overlimitlogging" title="OverLimitLogging">OverLimitLogging</a>" : <i>Double</i>,
        "<a href="#overlimitreset" title="OverLimitReset">OverLimitReset</a>" : <i>Double</i>,
        "<a href="#overlap" title="Overlap">Overlap</a>" : <i>Double</i>,
        "<a href="#share" title="Share">Share</a>" : <i>Double</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#usedestinationip" title="UseDestinationIp">UseDestinationIp</a>" : <i>Double</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#bwlistid" title="BwListId">BwListId</a>" : <i>[ <a href="bwlistiddefinition.md">BwListIdDefinition</a>, ... ]</i>,
        "<a href="#classlist" title="ClassList">ClassList</a>" : <i>[ <a href="classlistdefinition.md">ClassListDefinition</a>, ... ]</i>,
        "<a href="#forwardpolicy" title="ForwardPolicy">ForwardPolicy</a>" : <i>[ <a href="forwardpolicydefinition.md">ForwardPolicyDefinition</a>, ... ]</i>,
        "<a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>" : <i>[ <a href="samplingenabledefinition.md">SamplingEnableDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbTemplatePolicy
Properties:
    <a href="#bwlistname" title="BwListName">BwListName</a>: <i>String</i>
    <a href="#fulldomaintree" title="FullDomainTree">FullDomainTree</a>: <i>Double</i>
    <a href="#interval" title="Interval">Interval</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#overlimit" title="OverLimit">OverLimit</a>: <i>Double</i>
    <a href="#overlimitlockup" title="OverLimitLockup">OverLimitLockup</a>: <i>Double</i>
    <a href="#overlimitlogging" title="OverLimitLogging">OverLimitLogging</a>: <i>Double</i>
    <a href="#overlimitreset" title="OverLimitReset">OverLimitReset</a>: <i>Double</i>
    <a href="#overlap" title="Overlap">Overlap</a>: <i>Double</i>
    <a href="#share" title="Share">Share</a>: <i>Double</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#usedestinationip" title="UseDestinationIp">UseDestinationIp</a>: <i>Double</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#bwlistid" title="BwListId">BwListId</a>: <i>
      - <a href="bwlistiddefinition.md">BwListIdDefinition</a></i>
    <a href="#classlist" title="ClassList">ClassList</a>: <i>
      - <a href="classlistdefinition.md">ClassListDefinition</a></i>
    <a href="#forwardpolicy" title="ForwardPolicy">ForwardPolicy</a>: <i>
      - <a href="forwardpolicydefinition.md">ForwardPolicyDefinition</a></i>
    <a href="#samplingenable" title="SamplingEnable">SamplingEnable</a>: <i>
      - <a href="samplingenabledefinition.md">SamplingEnableDefinition</a></i>
</pre>

## Properties

#### BwListName

Specify a blacklist/whitelist name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FullDomainTree

Share counters between geo-location and sub regions.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

Specify log interval in minutes, by default system will log every over limit instance.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Class list name or geo-location-class-list name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverLimit

Specify operation in case over limit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverLimitLockup

Don’t accept any new connection for certain time (Lockup duration (minute)).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverLimitLogging

Log a message.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverLimitReset

Reset the connection when it exceeds limit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Overlap

Use overlap mode for geo-location to do longest match.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Share

Share counters between virtual ports and virtual servers.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

Define timeout value of PBSLB dynamic entry (Timeout value (minute, default is 5)).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseDestinationIp

Use destination IP to match the policy.

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

#### BwListId

_Required_: No

_Type_: List of <a href="bwlistiddefinition.md">BwListIdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassList

_Required_: No

_Type_: List of <a href="classlistdefinition.md">ClassListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardPolicy

_Required_: No

_Type_: List of <a href="forwardpolicydefinition.md">ForwardPolicyDefinition</a>

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

Specify id that maps to service group (The id number).

