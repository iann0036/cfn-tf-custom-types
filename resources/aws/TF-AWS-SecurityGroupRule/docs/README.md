# TF::AWS::SecurityGroupRule

Provides a security group rule resource. Represents a single `ingress` or
`egress` group rule, which can be added to external Security Groups.

~> **NOTE on Security Groups and Security Group Rules:** Terraform currently
provides both a standalone Security Group Rule resource (a single `ingress` or
`egress` rule), and a [Security Group resource](security_group.html) with `ingress` and `egress` rules
defined in-line. At this time you cannot use a Security Group with in-line rules
in conjunction with any Security Group Rule resources. Doing so will cause
a conflict of rule settings and will overwrite rules.

~> **NOTE:** Setting `protocol = "all"` or `protocol = -1` with `from_port` and `to_port` will result in the EC2 API creating a security group rule with all ports open. This API behavior cannot be controlled by Terraform and may generate warnings in the future.

~> **NOTE:** Referencing Security Groups across VPC peering has certain restrictions. More information is available in the [VPC Peering User Gu...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::SecurityGroupRule",
    "Properties" : {
        "<a href="#cidrblocks" title="CidrBlocks">CidrBlocks</a>" : <i>[ String, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#fromport" title="FromPort">FromPort</a>" : <i>Double</i>,
        "<a href="#ipv6cidrblocks" title="Ipv6CidrBlocks">Ipv6CidrBlocks</a>" : <i>[ String, ... ]</i>,
        "<a href="#prefixlistids" title="PrefixListIds">PrefixListIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>" : <i>String</i>,
        "<a href="#self" title="Self">Self</a>" : <i>Boolean</i>,
        "<a href="#sourcesecuritygroupid" title="SourceSecurityGroupId">SourceSecurityGroupId</a>" : <i>String</i>,
        "<a href="#toport" title="ToPort">ToPort</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::SecurityGroupRule
Properties:
    <a href="#cidrblocks" title="CidrBlocks">CidrBlocks</a>: <i>
      - String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#fromport" title="FromPort">FromPort</a>: <i>Double</i>
    <a href="#ipv6cidrblocks" title="Ipv6CidrBlocks">Ipv6CidrBlocks</a>: <i>
      - String</i>
    <a href="#prefixlistids" title="PrefixListIds">PrefixListIds</a>: <i>
      - String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>: <i>String</i>
    <a href="#self" title="Self">Self</a>: <i>Boolean</i>
    <a href="#sourcesecuritygroupid" title="SourceSecurityGroupId">SourceSecurityGroupId</a>: <i>String</i>
    <a href="#toport" title="ToPort">ToPort</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### CidrBlocks

List of CIDR blocks. Cannot be specified with `source_security_group_id` or `self`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FromPort

Start port (or ICMP type number if protocol is "icmp" or "icmpv6").

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6CidrBlocks

List of IPv6 CIDR blocks. Cannot be specified with `source_security_group_id` or `self`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixListIds

List of Prefix List IDs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Protocol. If not icmp, icmpv6, tcp, udp, or all use the [protocol number](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupId

Security group to apply this rule to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Self

Whether the security group itself will be added as a source to this ingress rule. Cannot be specified with `cidr_blocks`, `ipv6_cidr_blocks`, or `source_security_group_id`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceSecurityGroupId

Security group id to allow access to/from, depending on the `type`. Cannot be specified with `cidr_blocks`, `ipv6_cidr_blocks`, or `self`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ToPort

End port (or ICMP code if protocol is "icmp").

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Type of rule being created. Valid options are `ingress` (inbound)
or `egress` (outbound).

_Required_: Yes

_Type_: String

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

