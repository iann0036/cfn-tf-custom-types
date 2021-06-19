# TF::HCloud::LoadBalancerNetwork

Provides a Hetzner Cloud Load Balancer Network to represent a private network on a Load Balancer in the Hetzner Cloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::HCloud::LoadBalancerNetwork",
    "Properties" : {
        "<a href="#enablepublicinterface" title="EnablePublicInterface">EnablePublicInterface</a>" : <i>Boolean</i>,
        "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
        "<a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>" : <i>Double</i>,
        "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>Double</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::HCloud::LoadBalancerNetwork
Properties:
    <a href="#enablepublicinterface" title="EnablePublicInterface">EnablePublicInterface</a>: <i>Boolean</i>
    <a href="#ip" title="Ip">Ip</a>: <i>String</i>
    <a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>: <i>Double</i>
    <a href="#networkid" title="NetworkId">NetworkId</a>: <i>Double</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
</pre>

## Properties

#### EnablePublicInterface

Enable or disable the
Load Balancers public interface. Default: `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

IP to request to be assigned to this Load
Balancer. If you do not provide this then you will be auto assigned an
IP address.
- `enable_public_interface` - (Optional, bool) Enable or disable the
Load Balancers public interface. Default: `true`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerId

ID of the Load Balancer.
- `network_id` - (Optional, int) ID of the network which should be added
to the Load Balancer. Required if `subnet_id` is not set. Successful
creation of the resource depends on the existence of a subnet in the
Hetzner Cloud Backend. Using `network_id` will not create an explicit
dependency between the Load Balancer and the subnet. Therefore
`depends_on` may need to be used. Alternatively the `subnet_id`
property can be used, which will create an explicit dependency between
`hcloud_load_balancer_network` and the existence of a subnet.
- `subnet_id` - (Optional, string) ID of the sub-network which should be
added to the Load Balancer. Required if `network_id` is not set.
*Note*: if the `ip` property is missing, the Load Balancer is
currently added to the last created subnet.
- `ip` - (Optional, string) IP to request to be assigned to this Load
Balancer. If you do not provide this then you will be auto assigned an
IP address.
- `enable_public_interface` - (Optional, bool) Enable or disable the
Load Balancers public interface. Default: `true`.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

ID of the network which should be added
to the Load Balancer. Required if `subnet_id` is not set. Successful
creation of the resource depends on the existence of a subnet in the
Hetzner Cloud Backend. Using `network_id` will not create an explicit
dependency between the Load Balancer and the subnet. Therefore
`depends_on` may need to be used. Alternatively the `subnet_id`
property can be used, which will create an explicit dependency between
`hcloud_load_balancer_network` and the existence of a subnet.
- `subnet_id` - (Optional, string) ID of the sub-network which should be
added to the Load Balancer. Required if `network_id` is not set.
*Note*: if the `ip` property is missing, the Load Balancer is
currently added to the last created subnet.
- `ip` - (Optional, string) IP to request to be assigned to this Load
Balancer. If you do not provide this then you will be auto assigned an
IP address.
- `enable_public_interface` - (Optional, bool) Enable or disable the
Load Balancers public interface. Default: `true`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

ID of the sub-network which should be
added to the Load Balancer. Required if `network_id` is not set.
*Note*: if the `ip` property is missing, the Load Balancer is
currently added to the last created subnet.
- `ip` - (Optional, string) IP to request to be assigned to this Load
Balancer. If you do not provide this then you will be auto assigned an
IP address.
- `enable_public_interface` - (Optional, bool) Enable or disable the
Load Balancers public interface. Default: `true`.

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

