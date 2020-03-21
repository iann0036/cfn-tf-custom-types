# Terraform::NSXT::LbPool

CloudFormation equivalent of nsxt_lb_pool

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
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
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
    <a href="#id" title="Id">Id</a>: <i>String</i>
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

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Algorithm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinActiveMembers

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PassiveMonitorId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpMultiplexingEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpMultiplexingNumber

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

#### Revision

Returns the <code>Revision</code> value.

