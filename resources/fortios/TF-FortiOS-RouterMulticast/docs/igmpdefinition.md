# TF::FortiOS::RouterMulticast IgmpDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accessgroup" title="AccessGroup">AccessGroup</a>" : <i>String</i>,
    "<a href="#immediateleavegroup" title="ImmediateLeaveGroup">ImmediateLeaveGroup</a>" : <i>String</i>,
    "<a href="#lastmemberquerycount" title="LastMemberQueryCount">LastMemberQueryCount</a>" : <i>Double</i>,
    "<a href="#lastmemberqueryinterval" title="LastMemberQueryInterval">LastMemberQueryInterval</a>" : <i>Double</i>,
    "<a href="#queryinterval" title="QueryInterval">QueryInterval</a>" : <i>Double</i>,
    "<a href="#querymaxresponsetime" title="QueryMaxResponseTime">QueryMaxResponseTime</a>" : <i>Double</i>,
    "<a href="#querytimeout" title="QueryTimeout">QueryTimeout</a>" : <i>Double</i>,
    "<a href="#routeralertcheck" title="RouterAlertCheck">RouterAlertCheck</a>" : <i>String</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#accessgroup" title="AccessGroup">AccessGroup</a>: <i>String</i>
<a href="#immediateleavegroup" title="ImmediateLeaveGroup">ImmediateLeaveGroup</a>: <i>String</i>
<a href="#lastmemberquerycount" title="LastMemberQueryCount">LastMemberQueryCount</a>: <i>Double</i>
<a href="#lastmemberqueryinterval" title="LastMemberQueryInterval">LastMemberQueryInterval</a>: <i>Double</i>
<a href="#queryinterval" title="QueryInterval">QueryInterval</a>: <i>Double</i>
<a href="#querymaxresponsetime" title="QueryMaxResponseTime">QueryMaxResponseTime</a>: <i>Double</i>
<a href="#querytimeout" title="QueryTimeout">QueryTimeout</a>: <i>Double</i>
<a href="#routeralertcheck" title="RouterAlertCheck">RouterAlertCheck</a>: <i>String</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
</pre>

## Properties

#### AccessGroup

Groups IGMP hosts are allowed to join.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImmediateLeaveGroup

Groups to drop membership for immediately after receiving IGMPv2 leave.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastMemberQueryCount

Number of group specific queries before removing group (2 - 7, default = 2).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastMemberQueryInterval

Timeout between IGMPv2 leave and removing group (1 - 65535 msec, default = 1000).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryInterval

Interval between queries to IGMP hosts (1 - 65535 sec, default = 125).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryMaxResponseTime

Maximum time to wait for a IGMP query response (1 - 25 sec, default = 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryTimeout

Timeout between queries before becoming querier for network (60 - 900, default = 255).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouterAlertCheck

Enable/disable require IGMP packets contain router alert option. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

Maximum version of IGMP to support. Valid values: `3`, `2`, `1`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

