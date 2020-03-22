# Terraform::NSXT::LbPool

Provides a resource to configure lb pool on NSX-T manager

~> **NOTE:** This resource requires NSX version 2.3 or higher.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NSXT::LbPool",
    "Properties" : {
        "<a href="#activemonitorid" title="ActiveMonitorId">ActiveMonitorId</a>" : <i>String</i>,
        "<a href="#algorithm" title="Algorithm">Algorithm</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#minactivemembers" title="MinActiveMembers">MinActiveMembers</a>" : <i>Double</i>,
        "<a href="#passivemonitorid" title="PassiveMonitorId">PassiveMonitorId</a>" : <i>String</i>,
        "<a href="#tcpmultiplexingenabled" title="TcpMultiplexingEnabled">TcpMultiplexingEnabled</a>" : <i>Boolean</i>,
        "<a href="#tcpmultiplexingnumber" title="TcpMultiplexingNumber">TcpMultiplexingNumber</a>" : <i>Double</i>,
        "<a href="#member" title="Member">Member</a>" : <i>[ <a href="member.md">Member</a>, ... ]</i>,
        "<a href="#membergroup" title="MemberGroup">MemberGroup</a>" : <i>[ <a href="membergroup.md">MemberGroup</a>, ... ]</i>,
        "<a href="#snattranslation" title="SnatTranslation">SnatTranslation</a>" : <i>[ <a href="snattranslation.md">SnatTranslation</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tag.md">Tag</a>, ... ]</i>,
        "<a href="#groupingobject" title="GroupingObject">GroupingObject</a>" : <i>[ <a href="groupingobject.md">GroupingObject</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NSXT::LbPool
Properties:
    <a href="#activemonitorid" title="ActiveMonitorId">ActiveMonitorId</a>: <i>String</i>
    <a href="#algorithm" title="Algorithm">Algorithm</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#minactivemembers" title="MinActiveMembers">MinActiveMembers</a>: <i>Double</i>
    <a href="#passivemonitorid" title="PassiveMonitorId">PassiveMonitorId</a>: <i>String</i>
    <a href="#tcpmultiplexingenabled" title="TcpMultiplexingEnabled">TcpMultiplexingEnabled</a>: <i>Boolean</i>
    <a href="#tcpmultiplexingnumber" title="TcpMultiplexingNumber">TcpMultiplexingNumber</a>: <i>Double</i>
    <a href="#member" title="Member">Member</a>: <i>
      - <a href="member.md">Member</a></i>
    <a href="#membergroup" title="MemberGroup">MemberGroup</a>: <i>
      - <a href="membergroup.md">MemberGroup</a></i>
    <a href="#snattranslation" title="SnatTranslation">SnatTranslation</a>: <i>
      - <a href="snattranslation.md">SnatTranslation</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tag.md">Tag</a></i>
    <a href="#groupingobject" title="GroupingObject">GroupingObject</a>: <i>
      - <a href="groupingobject.md">GroupingObject</a></i>
</pre>

## Properties

#### ActiveMonitorId

Active health monitor Id. If one is not set, the active healthchecks will be disabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Algorithm

Load balancing algorithm controls how the incoming connections are distributed among the members. Supported algorithms are: ROUND_ROBIN, WEIGHTED_ROUND_ROBIN, LEAST_CONNECTION, WEIGHTED_LEAST_CONNECTION, IP_HASH.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of this resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The display name of this resource. pool member name.
* `ip_address` - (Required) Pool member IP address.
* `max_concurrent_connections` - (Optional) To ensure members are not overloaded, connections to a member can be capped by the load balancer. When a member reaches this limit, it is skipped during server selection. If it is not specified, it means that connections are unlimited.
* `port` - (Optional) If port is specified, all connections will be sent to this port. Only single port is supported. If unset, the same port the client connected to will be used, it could be overrode by default_pool_member_port setting in virtual server. The port should not specified for port range case.
* `weight` - (Optional) Pool member weight is used for WEIGHTED_ROUND_ROBIN balancing algorithm. The weight value would be ignored in other algorithms.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinActiveMembers

The minimum number of members for the pool to be considered active. This value is 1 by default.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PassiveMonitorId

Passive health monitor Id. If one is not set, the passive healthchecks will be disabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpMultiplexingEnabled

TCP multiplexing allows the same TCP connection between load balancer and the backend server to be used for sending multiple client requests from different client TCP connections. Disabled by default.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpMultiplexingNumber

The maximum number of TCP connections per pool that are idly kept alive for sending future client requests. The default value for this is 6.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Member

_Required_: No

_Type_: List of <a href="member.md">Member</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemberGroup

_Required_: No

_Type_: List of <a href="membergroup.md">MemberGroup</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnatTranslation

_Required_: No

_Type_: List of <a href="snattranslation.md">SnatTranslation</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tag.md">Tag</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupingObject

_Required_: No

_Type_: List of <a href="groupingobject.md">GroupingObject</a>

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

#### Revision

Returns the <code>Revision</code> value.

