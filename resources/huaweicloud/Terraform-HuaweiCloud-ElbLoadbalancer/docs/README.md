# Terraform::HuaweiCloud::ElbLoadbalancer

Manages an elastic loadbalancer resource within huawei cloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::ElbLoadbalancer",
    "Properties" : {
        "<a href="#adminstateup" title="AdminStateUp">AdminStateUp</a>" : <i>Double</i>,
        "<a href="#az" title="Az">Az</a>" : <i>String</i>,
        "<a href="#bandwidth" title="Bandwidth">Bandwidth</a>" : <i>Double</i>,
        "<a href="#chargemode" title="ChargeMode">ChargeMode</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#eiptype" title="EipType">EipType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>" : <i>String</i>,
        "<a href="#tenantid" title="Tenantid">Tenantid</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#vipaddress" title="VipAddress">VipAddress</a>" : <i>String</i>,
        "<a href="#vipsubnetid" title="VipSubnetId">VipSubnetId</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::ElbLoadbalancer
Properties:
    <a href="#adminstateup" title="AdminStateUp">AdminStateUp</a>: <i>Double</i>
    <a href="#az" title="Az">Az</a>: <i>String</i>
    <a href="#bandwidth" title="Bandwidth">Bandwidth</a>: <i>Double</i>
    <a href="#chargemode" title="ChargeMode">ChargeMode</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#eiptype" title="EipType">EipType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>: <i>String</i>
    <a href="#tenantid" title="Tenantid">Tenantid</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#vipaddress" title="VipAddress">VipAddress</a>: <i>String</i>
    <a href="#vipsubnetid" title="VipSubnetId">VipSubnetId</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AdminStateUp

Specifies the status of the load balancer.
Value range: 0 or false: indicates that the load balancer is stopped. Only
tenants are allowed to enter these two values. 1 or true: indicates that
the load balancer is running properly. 2 or false: indicates that the load
balancer is frozen. Only tenants are allowed to enter these two values.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Az

Specifies the ID of the availability zone (AZ). This
parameter is mandatory when type is set to Internal, and it is invalid
when type is set to External.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bandwidth

Specifies the bandwidth (Mbit/s). This parameter
is mandatory when type is set to External, and it is invalid when type
is set to Internal. The value ranges from 1 to 300.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChargeMode

This is a reserved field. If the system supports
charging by traffic and this field is specified, then you are charged by
traffic for elastic IP addresses. The value is traffic.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Provides supplementary information about the
listener. The value is a string of 0 to 128 characters and cannot be <>.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EipType

This parameter is reserved.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the load balancer name. The name is a string
of 1 to 64 characters that consist of letters, digits, underscores (_),
and hyphens (-).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupId

Specifies the security group ID. The
value is a string of 1 to 200 characters that consists of uppercase and
lowercase letters, digits, and hyphens (-). This parameter is mandatory
only when type is set to Internal.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tenantid

Specifies the tenant ID. This parameter is mandatory
only when type is set to Internal.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Specifies the load balancer type. The value can be
Internal or External.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipAddress

Specifies the IP address provided by ELB.
When typeis set to External, the value of this parameter is the elastic
IP address. When type is set to Internal, the value of this parameter is
the private network IP address. You can select an existing elastic IP address
and create a public network load balancer. When this parameter is configured,
parameters bandwidth, charge_mode, and eip_type are invalid.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipSubnetId

Specifies the ID of the private network
to be added. This parameter is mandatory when type is set to Internal,
and it is invalid when type is set to External.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

Specifies the VPC ID.

_Required_: Yes

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

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Status

Returns the <code>Status</code> value.

#### UpdateTime

Returns the <code>UpdateTime</code> value.

