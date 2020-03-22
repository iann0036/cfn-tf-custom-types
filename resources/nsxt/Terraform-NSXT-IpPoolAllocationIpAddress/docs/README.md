# Terraform::NSXT::IpPoolAllocationIpAddress

Provides a resource to allocate an IP address from an IP pool on NSX-T manager

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NSXT::IpPoolAllocationIpAddress",
    "Properties" : {
        "<a href="#allocationid" title="AllocationId">AllocationId</a>" : <i>String</i>,
        "<a href="#ippoolid" title="IpPoolId">IpPoolId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NSXT::IpPoolAllocationIpAddress
Properties:
    <a href="#allocationid" title="AllocationId">AllocationId</a>: <i>String</i>
    <a href="#ippoolid" title="IpPoolId">IpPoolId</a>: <i>String</i>
</pre>

## Properties

#### AllocationId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpPoolId

Ip Pool ID from which the IP address will be allocated.

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

