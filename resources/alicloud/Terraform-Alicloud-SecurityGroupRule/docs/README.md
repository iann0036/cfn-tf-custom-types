# Terraform::Alicloud::SecurityGroupRule

Provides a security group rule resource.
Represents a single `ingress` or `egress` group rule, which can be added to external Security Groups.

-> **NOTE:**  `nic_type` should set to `intranet` when security group type is `vpc` or specifying the `source_security_group_id`. In this situation it does not distinguish between intranet and internet, the rule is effective on them both.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::SecurityGroupRule",
    "Properties" : {
        "<a href="#cidrip" title="CidrIp">CidrIp</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#ipprotocol" title="IpProtocol">IpProtocol</a>" : <i>String</i>,
        "<a href="#nictype" title="NicType">NicType</a>" : <i>String</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#portrange" title="PortRange">PortRange</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>" : <i>String</i>,
        "<a href="#sourcegroupowneraccount" title="SourceGroupOwnerAccount">SourceGroupOwnerAccount</a>" : <i>String</i>,
        "<a href="#sourcesecuritygroupid" title="SourceSecurityGroupId">SourceSecurityGroupId</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::SecurityGroupRule
Properties:
    <a href="#cidrip" title="CidrIp">CidrIp</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#ipprotocol" title="IpProtocol">IpProtocol</a>: <i>String</i>
    <a href="#nictype" title="NicType">NicType</a>: <i>String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#portrange" title="PortRange">PortRange</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>: <i>String</i>
    <a href="#sourcegroupowneraccount" title="SourceGroupOwnerAccount">SourceGroupOwnerAccount</a>: <i>String</i>
    <a href="#sourcesecuritygroupid" title="SourceSecurityGroupId">SourceSecurityGroupId</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### CidrIp

The target IP address range. The default value is 0.0.0.0/0 (which means no restriction will be applied). Other supported formats include 10.159.6.18/12. Only IPv4 is supported.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the security group rule. The description can be up to 1 to 512 characters in length. Defaults to null.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpProtocol

The protocol. Can be `tcp`, `udp`, `icmp`, `gre` or `all`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NicType

Network type, can be either `internet` or `intranet`, the default value is `internet`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

Authorization policy, can be either `accept` or `drop`, the default value is `accept`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortRange

The range of port numbers relevant to the IP protocol. Default to "-1/-1". When the protocol is tcp or udp, each side port number range from 1 to 65535 and '-1/-1' will be invalid.
For example, `1/200` means that the range of the port numbers is 1-200. Other protocols' 'port_range' can only be "-1/-1", and other values will be invalid.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

Authorization policy priority, with parameter values: `1-100`, default value: 1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupId

The security group to apply this rule to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceGroupOwnerAccount

The Alibaba Cloud user account Id of the target security group when security groups are authorized across accounts.  This parameter is invalid if `cidr_ip` has already been set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceSecurityGroupId

The target security group ID within the same region. If this field is specified, the `nic_type` can only select `intranet`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of rule being created. Valid options are `ingress` (inbound) or `egress` (outbound).

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

