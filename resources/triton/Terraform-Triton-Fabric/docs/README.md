# Terraform::Triton::Fabric

The `triton_fabric` resource represents an fabric for a Triton account. The fabric is a logical set of interconnected switches.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Triton::Fabric",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>,
        "<a href="#internetnat" title="InternetNat">InternetNat</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#provisionendip" title="ProvisionEndIp">ProvisionEndIp</a>" : <i>String</i>,
        "<a href="#provisionstartip" title="ProvisionStartIp">ProvisionStartIp</a>" : <i>String</i>,
        "<a href="#resolvers" title="Resolvers">Resolvers</a>" : <i>[ String, ... ]</i>,
        "<a href="#routes" title="Routes">Routes</a>" : <i>[ <a href="routes.md">Routes</a>, ... ]</i>,
        "<a href="#subnet" title="Subnet">Subnet</a>" : <i>String</i>,
        "<a href="#vlanid" title="VlanId">VlanId</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Triton::Fabric
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
    <a href="#internetnat" title="InternetNat">InternetNat</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#provisionendip" title="ProvisionEndIp">ProvisionEndIp</a>: <i>String</i>
    <a href="#provisionstartip" title="ProvisionStartIp">ProvisionStartIp</a>: <i>String</i>
    <a href="#resolvers" title="Resolvers">Resolvers</a>: <i>
      - String</i>
    <a href="#routes" title="Routes">Routes</a>: <i>
      - <a href="routes.md">Routes</a></i>
    <a href="#subnet" title="Subnet">Subnet</a>: <i>String</i>
    <a href="#vlanid" title="VlanId">VlanId</a>: <i>Double</i>
</pre>

## Properties

#### Description

Optional description of network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

Optional gateway IP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetNat

If a NAT zone is provisioned at Gateway IP address. Default is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Network name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProvisionEndIp

Last assignable IP on the network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProvisionStartIp

First IP on the network that can be assigned.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resolvers

Array of IP addresses for resolvers.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Routes

Map of CIDR block to Gateway IP address.

_Required_: No

_Type_: List of <a href="routes.md">Routes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

CIDR formatted string describing network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanId

VLAN id the network is on. Number between 0-4095 indicating VLAN ID.

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

#### Fabric

Returns the <code>Fabric</code> value.

#### Id

Returns the <code>Id</code> value.

#### Public

Returns the <code>Public</code> value.

