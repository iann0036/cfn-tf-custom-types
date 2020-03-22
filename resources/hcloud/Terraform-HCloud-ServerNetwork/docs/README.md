# Terraform::HCloud::ServerNetwork

Provides a Hetzner Cloud Server Network to represent a private network on a server in the Hetzner Cloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HCloud::ServerNetwork",
    "Properties" : {
        "<a href="#aliasips" title="AliasIps">AliasIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
        "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>Double</i>,
        "<a href="#serverid" title="ServerId">ServerId</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HCloud::ServerNetwork
Properties:
    <a href="#aliasips" title="AliasIps">AliasIps</a>: <i>
      - String</i>
    <a href="#ip" title="Ip">Ip</a>: <i>String</i>
    <a href="#networkid" title="NetworkId">NetworkId</a>: <i>Double</i>
    <a href="#serverid" title="ServerId">ServerId</a>: <i>Double</i>
</pre>

## Properties

#### AliasIps

Additional IPs to be assigned to this server.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

IP to request to be assigned to this server. If you do not provide this then you will be auto assigned an IP address.
- `alias_ips` - (Required, list[string]) Additional IPs to be assigned to this server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

ID of the network which should be added to the server.
- `server_id` - (Required, int) ID of the server.
- `ip` - (Optional, string) IP to request to be assigned to this server. If you do not provide this then you will be auto assigned an IP address.
- `alias_ips` - (Required, list[string]) Additional IPs to be assigned to this server.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerId

ID of the server.
- `ip` - (Optional, string) IP to request to be assigned to this server. If you do not provide this then you will be auto assigned an IP address.
- `alias_ips` - (Required, list[string]) Additional IPs to be assigned to this server.

_Required_: Yes

_Type_: Double

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

