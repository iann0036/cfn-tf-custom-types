# TF::HCloud::ServerNetwork

Provides a Hetzner Cloud Server Network to represent a private network on a server in the Hetzner Cloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::HCloud::ServerNetwork",
    "Properties" : {
        "<a href="#aliasips" title="AliasIps">AliasIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
        "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>Double</i>,
        "<a href="#serverid" title="ServerId">ServerId</a>" : <i>Double</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::HCloud::ServerNetwork
Properties:
    <a href="#aliasips" title="AliasIps">AliasIps</a>: <i>
      - String</i>
    <a href="#ip" title="Ip">Ip</a>: <i>String</i>
    <a href="#networkid" title="NetworkId">NetworkId</a>: <i>Double</i>
    <a href="#serverid" title="ServerId">ServerId</a>: <i>Double</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
</pre>

## Properties

#### AliasIps

Additional IPs to be assigned
to this server.
- `network_id` - (Optional, int) ID of the network which should be added
to the server. Required if `subnet_id` is not set. Successful creation
of the resource depends on the existence of a subnet in the Hetzner
Cloud Backend. Using `network_id` will not create an explicit
dependency between server and subnet. Therefore `depends_on` may need
to be used. Alternatively the `subnet_id` property can be used, which
will create an explicit dependency between `hcloud_server_network` and
the existence of a subnet.
- `subnet_id` - (Optional, string) ID of the sub-network which should be
added to the Server. Required if `network_id` is not set.
*Note*: if the `ip` property is missing, the Server is currently added
to the last created subnet.
- `ip` - (Optional, string) IP to request to be assigned to this server.
If you do not provide this then you will be auto assigned an IP
address.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

IP to request to be assigned to this server.
If you do not provide this then you will be auto assigned an IP
address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

ID of the network which should be added
to the server. Required if `subnet_id` is not set. Successful creation
of the resource depends on the existence of a subnet in the Hetzner
Cloud Backend. Using `network_id` will not create an explicit
dependency between server and subnet. Therefore `depends_on` may need
to be used. Alternatively the `subnet_id` property can be used, which
will create an explicit dependency between `hcloud_server_network` and
the existence of a subnet.
- `subnet_id` - (Optional, string) ID of the sub-network which should be
added to the Server. Required if `network_id` is not set.
*Note*: if the `ip` property is missing, the Server is currently added
to the last created subnet.
- `ip` - (Optional, string) IP to request to be assigned to this server.
If you do not provide this then you will be auto assigned an IP
address.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerId

ID of the server.
- `alias_ips` - (Required, list[string]) Additional IPs to be assigned
to this server.
- `network_id` - (Optional, int) ID of the network which should be added
to the server. Required if `subnet_id` is not set. Successful creation
of the resource depends on the existence of a subnet in the Hetzner
Cloud Backend. Using `network_id` will not create an explicit
dependency between server and subnet. Therefore `depends_on` may need
to be used. Alternatively the `subnet_id` property can be used, which
will create an explicit dependency between `hcloud_server_network` and
the existence of a subnet.
- `subnet_id` - (Optional, string) ID of the sub-network which should be
added to the Server. Required if `network_id` is not set.
*Note*: if the `ip` property is missing, the Server is currently added
to the last created subnet.
- `ip` - (Optional, string) IP to request to be assigned to this server.
If you do not provide this then you will be auto assigned an IP
address.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

ID of the sub-network which should be
added to the Server. Required if `network_id` is not set.
*Note*: if the `ip` property is missing, the Server is currently added
to the last created subnet.
- `ip` - (Optional, string) IP to request to be assigned to this server.
If you do not provide this then you will be auto assigned an IP
address.

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

#### MacAddress

Returns the <code>MacAddress</code> value.

