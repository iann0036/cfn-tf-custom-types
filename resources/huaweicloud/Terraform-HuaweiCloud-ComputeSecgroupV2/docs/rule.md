# Terraform::HuaweiCloud::ComputeSecgroupV2 Rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cidr" title="Cidr">Cidr</a>" : <i>String</i>,
    "<a href="#fromgroupid" title="FromGroupId">FromGroupId</a>" : <i>String</i>,
    "<a href="#fromport" title="FromPort">FromPort</a>" : <i>Double</i>,
    "<a href="#ipprotocol" title="IpProtocol">IpProtocol</a>" : <i>String</i>,
    "<a href="#self" title="Self">Self</a>" : <i>Boolean</i>,
    "<a href="#toport" title="ToPort">ToPort</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#cidr" title="Cidr">Cidr</a>: <i>String</i>
<a href="#fromgroupid" title="FromGroupId">FromGroupId</a>: <i>String</i>
<a href="#fromport" title="FromPort">FromPort</a>: <i>Double</i>
<a href="#ipprotocol" title="IpProtocol">IpProtocol</a>: <i>String</i>
<a href="#self" title="Self">Self</a>: <i>Boolean</i>
<a href="#toport" title="ToPort">ToPort</a>: <i>Double</i>
</pre>

## Properties

#### Cidr

Required if `from_group_id` or `self` is empty. The IP range
that will be the source of network traffic to the security group. Use 0.0.0.0/0
to allow all IP addresses. Changing this creates a new security group rule. Cannot
be combined with `from_group_id` or `self`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FromGroupId

Required if `cidr` or `self` is empty. The ID of a
group from which to forward traffic to the parent group. Changing this creates a
new security group rule. Cannot be combined with `cidr` or `self`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FromPort

An integer representing the lower bound of the port
range to open. Changing this creates a new security group rule.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpProtocol

The protocol type that will be allowed. Changing
this creates a new security group rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Self

Required if `cidr` and `from_group_id` is empty. If true,
the security group itself will be added as a source to this ingress rule. Cannot
be combined with `cidr` or `from_group_id`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ToPort

An integer representing the upper bound of the port
range to open. Changing this creates a new security group rule.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

