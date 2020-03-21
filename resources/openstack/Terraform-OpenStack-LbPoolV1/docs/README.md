# Terraform::OpenStack::LbPoolV1

Manages a V1 load balancer pool resource within OpenStack.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::LbPoolV1",
    "Properties" : {
        "<a href="#lbmethod" title="LbMethod">LbMethod</a>" : <i>String</i>,
        "<a href="#lbprovider" title="LbProvider">LbProvider</a>" : <i>String</i>,
        "<a href="#member" title="Member">Member</a>" : <i>[ String, ... ]</i>,
        "<a href="#monitorids" title="MonitorIds">MonitorIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::LbPoolV1
Properties:
    <a href="#lbmethod" title="LbMethod">LbMethod</a>: <i>String</i>
    <a href="#lbprovider" title="LbProvider">LbProvider</a>: <i>String</i>
    <a href="#member" title="Member">Member</a>: <i>
      - String</i>
    <a href="#monitorids" title="MonitorIds">MonitorIds</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### LbMethod

The algorithm used to distribute load between the
members of the pool. The current specification supports 'ROUND_ROBIN' and
'LEAST_CONNECTIONS' as valid values for this attribute.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbProvider

The backend load balancing provider. For example:
`haproxy`, `F5`, etc.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Member

An existing node to add to the pool. Changing this
updates the members of the pool. The member object structure is documented
below. Please note that the `member` block is deprecated in favor of the
`openstack_lb_member_v1` resource.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonitorIds

A list of IDs of monitors to associate with the
pool.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the pool. Changing this updates the name of
the existing pool.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The protocol used by the pool members, you can use
either 'TCP, 'HTTP', or 'HTTPS'. Changing this creates a new pool.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 Networking client.
A Networking client is needed to create an LB pool. If omitted, the
`region` argument of the provider is used. Changing this creates a new
LB pool.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The network on which the members of the pool will be
located. Only members that are on this network can be added to the pool.
Changing this creates a new pool.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

The owner of the pool. Required if admin wants to
create a pool member for another tenant. Changing this creates a new pool.

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

