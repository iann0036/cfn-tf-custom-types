# Terraform::FlexibleEngine::VpcSubnetV1

Provides an VPC subnet resource.

# Example Usage

 ```hcl
resource "flexibleengine_vpc_v1" "vpc_v1" {
  name = "${var.vpc_name}"
  cidr = "${var.vpc_cidr}"
}


resource "flexibleengine_vpc_subnet_v1" "subnet_v1" {
  name = "${var.subnet_name}"
  cidr = "${var.subnet_cidr}"
  gateway_ip = "${var.subnet_gateway_ip}"
  vpc_id = "${flexibleengine_vpc_v1.vpc_v1.id}"
}
 ```

# Argument Reference

The following arguments are supported:

* `name` (Required) - The subnet name. The value is a string of 1 to 64 characters that can contain letters, digits, underscores (_), and hyphens (-).

* `cidr` (Required) - Specifies the network segment on which the subnet resides. The value must be in CIDR format. The value must be within the CIDR block of the VPC. The subnet mask cannot be greater than 28. Changing this creates a new Subnet.

* `gateway_ip` (Required) - Specifies the gateway of the subnet. The value must be a valid IP address. The value must be an IP address in the subnet segment. Changing this creates a new Subnet.

* `vpc_id` (Required) - Specifies the ID of the VPC to which the subnet belongs. Changing this creates a new Subnet.

* `dhcp_enable` (Optional) - Specifies whether the DHCP function is enabled for the subnet. The value can be true or false. If this parameter is left blank, it is set to true by default.

* `primary_dns` (Optional) - Specifies the IP address of DNS server 1 on the subnet. The value must be a valid IP address.

* `secondary_dns` (Optional) - Specifies the IP address of DNS server 2 on the subnet. The value must be a valid IP address.

* `dns_list` (Optional) - Specifies the DNS server address list of a subnet. This field is required if you need to use more than two DNS servers. This parameter value is the superset of both DNS server address 1 and DNS server address 2.

* `availability_zone` (Optional) - Identifies the availability zone (AZ) to which the subnet belongs. The value must be an existing AZ in the system. Changing this creates a new Subnet.


# Attributes Reference

All of the argument attributes are also exported as
result attributes:

* `id` - Specifies a resource ID in UUID format.
 
* `status` - Specifies the status of the subnet. The value can be ACTIVE, DOWN, UNKNOWN, or ERROR.

* `subnet_id` - Specifies the subnet (Native OpenStack API) ID.

# Import

Subnets can be imported using the `subnet id`, e.g.

```
 $ terraform import flexibleengine_vpc_subnet_v1 4779ab1c-7c1a-44b1-a02e-93dfc361b32d
```

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::FlexibleEngine::VpcSubnetV1",
    "Properties" : {
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#cidr" title="Cidr">Cidr</a>" : <i>String</i>,
        "<a href="#dhcpenable" title="DhcpEnable">DhcpEnable</a>" : <i>Boolean</i>,
        "<a href="#dnslist" title="DnsList">DnsList</a>" : <i>[ String, ... ]</i>,
        "<a href="#gatewayip" title="GatewayIp">GatewayIp</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#primarydns" title="PrimaryDns">PrimaryDns</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#secondarydns" title="SecondaryDns">SecondaryDns</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::FlexibleEngine::VpcSubnetV1
Properties:
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#cidr" title="Cidr">Cidr</a>: <i>String</i>
    <a href="#dhcpenable" title="DhcpEnable">DhcpEnable</a>: <i>Boolean</i>
    <a href="#dnslist" title="DnsList">DnsList</a>: <i>
      - String</i>
    <a href="#gatewayip" title="GatewayIp">GatewayIp</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#primarydns" title="PrimaryDns">PrimaryDns</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#secondarydns" title="SecondaryDns">SecondaryDns</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AvailabilityZone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cidr

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpEnable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayIp

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryDns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryDns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### SubnetId

Returns the <code>SubnetId</code> value.

