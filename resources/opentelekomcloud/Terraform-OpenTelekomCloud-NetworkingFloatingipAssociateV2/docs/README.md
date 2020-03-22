# Terraform::OpenTelekomCloud::NetworkingFloatingipAssociateV2

Associates a floating IP to a port. This is useful for situations
where you have a pre-allocated floating IP or are unable to use the
`opentelekomcloud_networking_floatingip_v2` resource to create a floating IP.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::NetworkingFloatingipAssociateV2",
    "Properties" : {
        "<a href="#floatingip" title="FloatingIp">FloatingIp</a>" : <i>String</i>,
        "<a href="#portid" title="PortId">PortId</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::NetworkingFloatingipAssociateV2
Properties:
    <a href="#floatingip" title="FloatingIp">FloatingIp</a>: <i>String</i>
    <a href="#portid" title="PortId">PortId</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
</pre>

## Properties

#### FloatingIp

IP Address of an existing floating IP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortId

ID of an existing port with at least one IP address to
associate with this floating IP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

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

