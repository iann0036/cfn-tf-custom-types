# Terraform::Alicloud::Slb

Provides an Application Load Balancer resource.

-> **NOTE:** At present, to avoid some unnecessary regulation confusion, SLB can not support alicloud international account to create "paybybandwidth" instance.

-> **NOTE:** The supported specifications vary by region. Currently not all regions support guaranteed-performance instances.
For more details about guaranteed-performance instance, see [Guaranteed-performance instances](https://www.alibabacloud.com/help/doc-detail/27657.htm).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::Slb",
    "Properties" : {
        "<a href="#address" title="Address">Address</a>" : <i>String</i>,
        "<a href="#addressipversion" title="AddressIpVersion">AddressIpVersion</a>" : <i>String</i>,
        "<a href="#addresstype" title="AddressType">AddressType</a>" : <i>String</i>,
        "<a href="#bandwidth" title="Bandwidth">Bandwidth</a>" : <i>Double</i>,
        "<a href="#deleteprotection" title="DeleteProtection">DeleteProtection</a>" : <i>String</i>,
        "<a href="#instancechargetype" title="InstanceChargeType">InstanceChargeType</a>" : <i>String</i>,
        "<a href="#internet" title="Internet">Internet</a>" : <i>Boolean</i>,
        "<a href="#internetchargetype" title="InternetChargeType">InternetChargeType</a>" : <i>String</i>,
        "<a href="#masterzoneid" title="MasterZoneId">MasterZoneId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
        "<a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>" : <i>String</i>,
        "<a href="#slavezoneid" title="SlaveZoneId">SlaveZoneId</a>" : <i>String</i>,
        "<a href="#specification" title="Specification">Specification</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#vswitchid" title="VswitchId">VswitchId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::Slb
Properties:
    <a href="#address" title="Address">Address</a>: <i>String</i>
    <a href="#addressipversion" title="AddressIpVersion">AddressIpVersion</a>: <i>String</i>
    <a href="#addresstype" title="AddressType">AddressType</a>: <i>String</i>
    <a href="#bandwidth" title="Bandwidth">Bandwidth</a>: <i>Double</i>
    <a href="#deleteprotection" title="DeleteProtection">DeleteProtection</a>: <i>String</i>
    <a href="#instancechargetype" title="InstanceChargeType">InstanceChargeType</a>: <i>String</i>
    <a href="#internet" title="Internet">Internet</a>: <i>Boolean</i>
    <a href="#internetchargetype" title="InternetChargeType">InternetChargeType</a>: <i>String</i>
    <a href="#masterzoneid" title="MasterZoneId">MasterZoneId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#period" title="Period">Period</a>: <i>Double</i>
    <a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>: <i>String</i>
    <a href="#slavezoneid" title="SlaveZoneId">SlaveZoneId</a>: <i>String</i>
    <a href="#specification" title="Specification">Specification</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#vswitchid" title="VswitchId">VswitchId</a>: <i>String</i>
</pre>

## Properties

#### Address

Specify the IP address of the private network for the SLB instance, which must be in the destination CIDR block of the correspond ing switch.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddressIpVersion

The IP version of the SLB instance to be created, which can be set to ipv4 or ipv6 . Default to "ipv4". Now, only internet instance support ipv6 address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddressType

The network type of the SLB instance. Valid values: ["internet", "intranet"]. If load balancer launched in VPC, this value must be "intranet".
- internet: After an Internet SLB instance is created, the system allocates a public IP address so that the instance can forward requests from the Internet.
- intranet: After an intranet SLB instance is created, the system allocates an intranet IP address so that the instance can only forward intranet requests.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bandwidth

Valid
value is between 1 and 1000, If argument "internet_charge_type" is "paybytraffic", then this value will be ignore.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteProtection

Whether enable the deletion protection or not. on: Enable deletion protection. off: Disable deletion protection. Default to off. Only postpaid instance support this function.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceChargeType

The billing method of the load balancer. Valid values are "PrePaid" and "PostPaid". Default to "PostPaid".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Internet

Field 'internet' has been deprecated from provider version 1.55.3. Use 'address_type' replaces it.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetChargeType

Valid
values are `PayByBandwidth`, `PayByTraffic`. If this value is "PayByBandwidth", then argument "internet" must be "true". Default is "PayByTraffic". If load balancer launched in VPC, this value must be "PayByTraffic".
Before version 1.10.1, the valid values are "paybybandwidth" and "paybytraffic".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterZoneId

The primary zone ID of the SLB instance. If not specified, the system will be randomly assigned. You can query the primary and standby zones in a region by calling the DescribeZone API.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the SLB. This name must be unique within your AliCloud account, can have a maximum of 80 characters,
must contain only alphanumeric characters or hyphens, such as "-","/",".","_", and must not begin or end with a hyphen. If not specified,
Terraform will autogenerate a name beginning with `tf-lb`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

The duration that you will buy the resource, in month. It is valid when `instance_charge_type` is `PrePaid`. Default to 1. Valid values: [1-9, 12, 24, 36].

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupId

The Id of resource group which the SLB belongs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlaveZoneId

The standby zone ID of the SLB instance. If not specified, the system will be randomly assigned. You can query the primary and standby zones in a region by calling the DescribeZone API.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Specification

The specification of the Server Load Balancer instance. Default to empty string indicating it is "Shared-Performance" instance.
Launching "[Performance-guaranteed](https://www.alibabacloud.com/help/doc-detail/27657.htm)" instance, it is must be specified and it valid values are: "slb.s1.small", "slb.s2.small", "slb.s2.medium",
"slb.s3.small", "slb.s3.medium", "slb.s3.large" and "slb.s4.large".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource. The `tags` can have a maximum of 10 tag for every load balancer instance.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VswitchId

The VSwitch ID to launch in. If `address_type` is internet, it will be ignore.

_Required_: No

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

