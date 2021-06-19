# TF::NSXT::PolicyLbPool

This resource provides a method for the management of Load Balancer Pool.

This resource is applicable to NSX Policy Manager.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NSXT::PolicyLbPool",
    "Properties" : {
        "<a href="#activemonitorpath" title="ActiveMonitorPath">ActiveMonitorPath</a>" : <i>String</i>,
        "<a href="#algorithm" title="Algorithm">Algorithm</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#minactivemembers" title="MinActiveMembers">MinActiveMembers</a>" : <i>Double</i>,
        "<a href="#nsxid" title="NsxId">NsxId</a>" : <i>String</i>,
        "<a href="#passivemonitorpath" title="PassiveMonitorPath">PassiveMonitorPath</a>" : <i>String</i>,
        "<a href="#tcpmultiplexingenabled" title="TcpMultiplexingEnabled">TcpMultiplexingEnabled</a>" : <i>Boolean</i>,
        "<a href="#tcpmultiplexingnumber" title="TcpMultiplexingNumber">TcpMultiplexingNumber</a>" : <i>Double</i>,
        "<a href="#member" title="Member">Member</a>" : <i>[ <a href="memberdefinition.md">MemberDefinition</a>, ... ]</i>,
        "<a href="#membergroup" title="MemberGroup">MemberGroup</a>" : <i>[ <a href="membergroupdefinition.md">MemberGroupDefinition</a>, ... ]</i>,
        "<a href="#snat" title="Snat">Snat</a>" : <i>[ <a href="snatdefinition.md">SnatDefinition</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NSXT::PolicyLbPool
Properties:
    <a href="#activemonitorpath" title="ActiveMonitorPath">ActiveMonitorPath</a>: <i>String</i>
    <a href="#algorithm" title="Algorithm">Algorithm</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#minactivemembers" title="MinActiveMembers">MinActiveMembers</a>: <i>Double</i>
    <a href="#nsxid" title="NsxId">NsxId</a>: <i>String</i>
    <a href="#passivemonitorpath" title="PassiveMonitorPath">PassiveMonitorPath</a>: <i>String</i>
    <a href="#tcpmultiplexingenabled" title="TcpMultiplexingEnabled">TcpMultiplexingEnabled</a>: <i>Boolean</i>
    <a href="#tcpmultiplexingnumber" title="TcpMultiplexingNumber">TcpMultiplexingNumber</a>: <i>Double</i>
    <a href="#member" title="Member">Member</a>: <i>
      - <a href="memberdefinition.md">MemberDefinition</a></i>
    <a href="#membergroup" title="MemberGroup">MemberGroup</a>: <i>
      - <a href="membergroupdefinition.md">MemberGroupDefinition</a></i>
    <a href="#snat" title="Snat">Snat</a>: <i>
      - <a href="snatdefinition.md">SnatDefinition</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### ActiveMonitorPath

Active monitor to be associated with this pool.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Algorithm

Load balancing algorithm, one of `ROUND_ROBIN`, `WEIGHTED_ROUND_ROBIN`, `LEAST_CONNECTION`, `WEIGHTED_LEAST_CONNECTION`, `IP_HASH`. Default is `ROUND_ROBIN`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Display name of the member.
* `max_concurrent_connections` - (Optional) To ensure members are not overloaded, connections to a member can be capped by this setting.
* `port` - (Optional) If port is specified, all connections will be redirected to this port.
* `weight` - (Optional) Pool member weight is used for WEIGHTED algorithms.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinActiveMembers

A pool is considered active if there are at least certain minimum number of members.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxId

The NSX ID of this resource. If set, this ID will be used to create the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PassiveMonitorPath

Passive monitor to be associated with this pool.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpMultiplexingEnabled

Enable TCP multiplexing within the pool.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpMultiplexingNumber

The maximum number of TCP connections per pool that are idly kept alive for sending future client requests.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Member

_Required_: No

_Type_: List of <a href="memberdefinition.md">MemberDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemberGroup

_Required_: No

_Type_: List of <a href="membergroupdefinition.md">MemberGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Snat

_Required_: No

_Type_: List of <a href="snatdefinition.md">SnatDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

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

#### Path

Returns the <code>Path</code> value.

#### Revision

Returns the <code>Revision</code> value.

