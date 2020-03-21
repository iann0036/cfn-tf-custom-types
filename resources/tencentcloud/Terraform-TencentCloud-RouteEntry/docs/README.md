# Terraform::TencentCloud::RouteEntry

Provides a resource to create a routing entry in a VPC routing table.

~> **NOTE:** It has been deprecated and replaced by tencentcloud_route_table_entry.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::RouteEntry",
    "Properties" : {
        "<a href="#cidrblock" title="CidrBlock">CidrBlock</a>" : <i>String</i>,
        "<a href="#nexthub" title="NextHub">NextHub</a>" : <i>String</i>,
        "<a href="#nexttype" title="NextType">NextType</a>" : <i>String</i>,
        "<a href="#routetableid" title="RouteTableId">RouteTableId</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::RouteEntry
Properties:
    <a href="#cidrblock" title="CidrBlock">CidrBlock</a>: <i>String</i>
    <a href="#nexthub" title="NextHub">NextHub</a>: <i>String</i>
    <a href="#nexttype" title="NextType">NextType</a>: <i>String</i>
    <a href="#routetableid" title="RouteTableId">RouteTableId</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
</pre>

## Properties

#### CidrBlock

The RouteEntry's target network segment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHub

The route entry's next hub. CVM instance ID or VPC router interface ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextType

The next hop type. Available value is `public_gateway`,`vpn_gateway`,`sslvpn_gateway`,`dc_gateway`,`peering_connection`,`nat_gateway` and `instance`. `instance` points to CVM Instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteTableId

The ID of the route table.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

The VPC ID.

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

