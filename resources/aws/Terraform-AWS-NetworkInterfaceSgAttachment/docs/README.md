# Terraform::AWS::NetworkInterfaceSgAttachment

This resource attaches a security group to an Elastic Network Interface (ENI).
It can be used to attach a security group to any existing ENI, be it a
secondary ENI or one attached as the primary interface on an instance.

~> **NOTE on instances, interfaces, and security groups:** Terraform currently
provides the capability to assign security groups via the [`aws_instance`][1]
and the [`aws_network_interface`][2] resources. Using this resource in
conjunction with security groups provided in-line in those resources will cause
conflicts, and will lead to spurious diffs and undefined behavior - please use
one or the other.

[1]: /docs/providers/aws/d/instance.html
[2]: /docs/providers/aws/r/network_interface.html

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::NetworkInterfaceSgAttachment",
    "Properties" : {
        "<a href="#networkinterfaceid" title="NetworkInterfaceId">NetworkInterfaceId</a>" : <i>String</i>,
        "<a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::NetworkInterfaceSgAttachment
Properties:
    <a href="#networkinterfaceid" title="NetworkInterfaceId">NetworkInterfaceId</a>: <i>String</i>
    <a href="#securitygroupid" title="SecurityGroupId">SecurityGroupId</a>: <i>String</i>
</pre>

## Properties

#### NetworkInterfaceId

The ID of the network interface to attach to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupId

The ID of the security group.
* `network_interface_id` - (Required) The ID of the network interface to attach to.

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

