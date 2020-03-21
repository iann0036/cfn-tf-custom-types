# Terraform::HuaweiCloud::NetworkingSecgroupRuleV2

Manages a V2 neutron security group rule resource within HuaweiCloud.
Unlike Nova security groups, neutron separates the group from the rules
and also allows an admin to target a specific tenant_id.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::NetworkingSecgroupRuleV2",
    "Properties" : {
        "<a href="#direction" title="Direction">Direction</a>" : <i>String</i>,
        "<a href="#ethertype" title="Ethertype">Ethertype</a>" : <i>String</i>,
        "<a href="#portrangemax" title="PortRangeMax">PortRangeMax</a>" : <i>Double</i>,
        "<a href="#portrangemin" title="PortRangeMin">PortRangeMin</a>" : <i>Double</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#remotegroupid" title="RemoteGroupId">RemoteGroupId</a>" : <i>String</i>,
        "<a href="#remoteipprefix" title="RemoteIpPrefix">RemoteIpPrefix</a>" : <i>String</i>,
        "<a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>" : <i>String</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::NetworkingSecgroupRuleV2
Properties:
    <a href="#direction" title="Direction">Direction</a>: <i>String</i>
    <a href="#ethertype" title="Ethertype">Ethertype</a>: <i>String</i>
    <a href="#portrangemax" title="PortRangeMax">PortRangeMax</a>: <i>Double</i>
    <a href="#portrangemin" title="PortRangeMin">PortRangeMin</a>: <i>Double</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#remotegroupid" title="RemoteGroupId">RemoteGroupId</a>: <i>String</i>
    <a href="#remoteipprefix" title="RemoteIpPrefix">RemoteIpPrefix</a>: <i>String</i>
    <a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>: <i>String</i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Direction

The direction of the rule, valid values are __ingress__
or __egress__. Changing this creates a new security group rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ethertype

The layer 3 protocol type, valid values are __IPv4__
or __IPv6__. Changing this creates a new security group rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortRangeMax

The higher part of the allowed port range, valid
integer value needs to be between 1 and 65535. Changing this creates a new
security group rule.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortRangeMin

The lower part of the allowed port range, valid
integer value needs to be between 1 and 65535. Changing this creates a new
security group rule.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The layer 4 protocol type, valid values are following. Changing this creates a new security group rule. This is required if you want to specify a port range.
* __tcp__
* __udp__
* __icmp__
* __ah__
* __dccp__
* __egp__
* __esp__
* __gre__
* __igmp__
* __ipv6-encap__
* __ipv6-frag__
* __ipv6-icmp__
* __ipv6-nonxt__
* __ipv6-opts__
* __ipv6-route__
* __ospf__
* __pgm__
* __rsvp__
* __sctp__
* __udplite__
* __vrrp__.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
`region` argument of the provider is used. Changing this creates a new
security group rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteGroupId

The remote group id, the value needs to be an
Openstack ID of a security group in the same tenant. Changing this creates
a new security group rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteIpPrefix

The remote CIDR, the value needs to be a valid
CIDR (i.e. 192.168.0.0/16). Changing this creates a new security group rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupId

The security group id the rule should belong
to, the value needs to be an Openstack ID of a security group in the same
tenant. Changing this creates a new security group rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

The owner of the security group. Required if admin
wants to create a port for another tenant. Changing this creates a new
security group rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

