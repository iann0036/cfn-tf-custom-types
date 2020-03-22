# Terraform::BIGIP::NetSelfip

`bigip_net_selfip` Manages a selfip configuration

Resource should be named with their "full path". The full path is the combination of the partition + name of the resource, for example /Common/my-selfip.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::BIGIP::NetSelfip",
    "Properties" : {
        "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#trafficgroup" title="TrafficGroup">TrafficGroup</a>" : <i>String</i>,
        "<a href="#vlan" title="Vlan">Vlan</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::BIGIP::NetSelfip
Properties:
    <a href="#ip" title="Ip">Ip</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#trafficgroup" title="TrafficGroup">TrafficGroup</a>: <i>String</i>
    <a href="#vlan" title="Vlan">Vlan</a>: <i>String</i>
</pre>

## Properties

#### Ip

The Self IP's address and netmask.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the selfip.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficGroup

Specifies the traffic group, defaults to `traffic-group-local-only` if not specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vlan

Specifies the VLAN for which you are setting a self IP address. This setting must be provided when a self IP is created.

_Required_: Yes

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

