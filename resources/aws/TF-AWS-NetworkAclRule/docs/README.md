# TF::AWS::NetworkAclRule

Creates an entry (a rule) in a network ACL with the specified rule number.

~> **NOTE on Network ACLs and Network ACL Rules:** Terraform currently
provides both a standalone Network ACL Rule resource and a [Network ACL](network_acl.html) resource with rules
defined in-line. At this time you cannot use a Network ACL with in-line rules
in conjunction with any Network ACL Rule resources. Doing so will cause
a conflict of rule settings and will overwrite rules.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::NetworkAclRule",
    "Properties" : {
        "<a href="#cidrblock" title="CidrBlock">CidrBlock</a>" : <i>String</i>,
        "<a href="#egress" title="Egress">Egress</a>" : <i>Boolean</i>,
        "<a href="#fromport" title="FromPort">FromPort</a>" : <i>Double</i>,
        "<a href="#icmpcode" title="IcmpCode">IcmpCode</a>" : <i>String</i>,
        "<a href="#icmptype" title="IcmpType">IcmpType</a>" : <i>String</i>,
        "<a href="#ipv6cidrblock" title="Ipv6CidrBlock">Ipv6CidrBlock</a>" : <i>String</i>,
        "<a href="#networkaclid" title="NetworkAclId">NetworkAclId</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#ruleaction" title="RuleAction">RuleAction</a>" : <i>String</i>,
        "<a href="#rulenumber" title="RuleNumber">RuleNumber</a>" : <i>Double</i>,
        "<a href="#toport" title="ToPort">ToPort</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::NetworkAclRule
Properties:
    <a href="#cidrblock" title="CidrBlock">CidrBlock</a>: <i>String</i>
    <a href="#egress" title="Egress">Egress</a>: <i>Boolean</i>
    <a href="#fromport" title="FromPort">FromPort</a>: <i>Double</i>
    <a href="#icmpcode" title="IcmpCode">IcmpCode</a>: <i>String</i>
    <a href="#icmptype" title="IcmpType">IcmpType</a>: <i>String</i>
    <a href="#ipv6cidrblock" title="Ipv6CidrBlock">Ipv6CidrBlock</a>: <i>String</i>
    <a href="#networkaclid" title="NetworkAclId">NetworkAclId</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#ruleaction" title="RuleAction">RuleAction</a>: <i>String</i>
    <a href="#rulenumber" title="RuleNumber">RuleNumber</a>: <i>Double</i>
    <a href="#toport" title="ToPort">ToPort</a>: <i>Double</i>
</pre>

## Properties

#### CidrBlock

The network range to allow or deny, in CIDR notation (for example 172.16.0.0/24 ).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Egress

Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet). Default `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FromPort

The from port to match.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpCode

ICMP protocol: The ICMP code. Required if specifying ICMP for the protocol. e.g. -1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpType

ICMP protocol: The ICMP type. Required if specifying ICMP for the protocol. e.g. -1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6CidrBlock

The IPv6 CIDR block to allow or deny.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkAclId

The ID of the network ACL.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The protocol. A value of -1 means all protocols.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleAction

Indicates whether to allow or deny the traffic that matches the rule. Accepted values: `allow` | `deny`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleNumber

The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ToPort

The to port to match.

_Required_: No

_Type_: Double

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

