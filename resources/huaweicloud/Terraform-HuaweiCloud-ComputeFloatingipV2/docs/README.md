# Terraform::HuaweiCloud::ComputeFloatingipV2

Manages a V2 floating IP resource within HuaweiCloud Nova (compute)
that can be used for compute instances.

Please note that managing floating IPs through the HuaweiCloud Compute API has
been deprecated. Unless you are using an older HuaweiCloud environment, it is
recommended to use the [`huaweicloud_networking_floatingip_v2`](networking_floatingip_v2.html)
resource instead, which uses the HuaweiCloud Networking API.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::ComputeFloatingipV2",
    "Properties" : {
        "<a href="#pool" title="Pool">Pool</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::ComputeFloatingipV2
Properties:
    <a href="#pool" title="Pool">Pool</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
</pre>

## Properties

#### Pool

The name of the pool from which to obtain the floating
IP. Only admin_external_net is valid. Changing this creates a new floating IP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 Compute client.
A Compute client is needed to create a floating IP that can be used with
a compute instance. If omitted, the `region` argument of the provider
is used. Changing this creates a new floating IP (which may or may not
have a different address).

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

#### Address

Returns the <code>Address</code> value.

#### FixedIp

Returns the <code>FixedIp</code> value.

#### InstanceId

Returns the <code>InstanceId</code> value.

