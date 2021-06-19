# TF::AWS::EipAssociation

Provides an AWS EIP Association as a top level resource, to associate and
disassociate Elastic IPs from AWS Instances and Network Interfaces.

~> **NOTE:** Do not use this resource to associate an EIP to `aws_lb` or `aws_nat_gateway` resources. Instead use the `allocation_id` available in those resources to allow AWS to manage the association, otherwise you will see `AuthFailure` errors.

~> **NOTE:** `aws_eip_association` is useful in scenarios where EIPs are either
pre-existing or distributed to customers or users and therefore cannot be changed.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::EipAssociation",
    "Properties" : {
        "<a href="#allocationid" title="AllocationId">AllocationId</a>" : <i>String</i>,
        "<a href="#allowreassociation" title="AllowReassociation">AllowReassociation</a>" : <i>Boolean</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#networkinterfaceid" title="NetworkInterfaceId">NetworkInterfaceId</a>" : <i>String</i>,
        "<a href="#privateipaddress" title="PrivateIpAddress">PrivateIpAddress</a>" : <i>String</i>,
        "<a href="#publicip" title="PublicIp">PublicIp</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::EipAssociation
Properties:
    <a href="#allocationid" title="AllocationId">AllocationId</a>: <i>String</i>
    <a href="#allowreassociation" title="AllowReassociation">AllowReassociation</a>: <i>Boolean</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#networkinterfaceid" title="NetworkInterfaceId">NetworkInterfaceId</a>: <i>String</i>
    <a href="#privateipaddress" title="PrivateIpAddress">PrivateIpAddress</a>: <i>String</i>
    <a href="#publicip" title="PublicIp">PublicIp</a>: <i>String</i>
</pre>

## Properties

#### AllocationId

The allocation ID. This is required for EC2-VPC.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowReassociation

Whether to allow an Elastic IP to
be re-associated. Defaults to `true` in VPC.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

The ID of the instance. This is required for
EC2-Classic. For EC2-VPC, you can specify either the instance ID or the
network interface ID, but not both. The operation fails if you specify an
instance ID unless exactly one network interface is attached.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterfaceId

The ID of the network interface. If the
instance has more than one network interface, you must specify a network
interface ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIpAddress

The primary or secondary private IP address
to associate with the Elastic IP address. If no private IP address is
specified, the Elastic IP address is associated with the primary private IP
address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIp

The Elastic IP address. This is required for EC2-Classic.

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

#### Id

Returns the <code>Id</code> value.

