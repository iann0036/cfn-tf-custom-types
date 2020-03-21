# Terraform::FlexibleEngine::NetworkingSubnetV2

Manages a V2 Neutron subnet resource within FlexibleEngine.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::FlexibleEngine::NetworkingSubnetV2",
    "Properties" : {
        "<a href="#cidr" title="Cidr">Cidr</a>" : <i>String</i>,
        "<a href="#dnsnameservers" title="DnsNameservers">DnsNameservers</a>" : <i>[ String, ... ]</i>,
        "<a href="#enabledhcp" title="EnableDhcp">EnableDhcp</a>" : <i>Boolean</i>,
        "<a href="#gatewayip" title="GatewayIp">GatewayIp</a>" : <i>String</i>,
        "<a href="#ipversion" title="IpVersion">IpVersion</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>String</i>,
        "<a href="#nogateway" title="NoGateway">NoGateway</a>" : <i>Boolean</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
        "<a href="#valuespecs" title="ValueSpecs">ValueSpecs</a>" : <i>[ <a href="valuespecs.md">ValueSpecs</a>, ... ]</i>,
        "<a href="#allocationpools" title="AllocationPools">AllocationPools</a>" : <i>[ <a href="allocationpools.md">AllocationPools</a>, ... ]</i>,
        "<a href="#hostroutes" title="HostRoutes">HostRoutes</a>" : <i>[ <a href="hostroutes.md">HostRoutes</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::FlexibleEngine::NetworkingSubnetV2
Properties:
    <a href="#cidr" title="Cidr">Cidr</a>: <i>String</i>
    <a href="#dnsnameservers" title="DnsNameservers">DnsNameservers</a>: <i>
      - String</i>
    <a href="#enabledhcp" title="EnableDhcp">EnableDhcp</a>: <i>Boolean</i>
    <a href="#gatewayip" title="GatewayIp">GatewayIp</a>: <i>String</i>
    <a href="#ipversion" title="IpVersion">IpVersion</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkid" title="NetworkId">NetworkId</a>: <i>String</i>
    <a href="#nogateway" title="NoGateway">NoGateway</a>: <i>Boolean</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
    <a href="#valuespecs" title="ValueSpecs">ValueSpecs</a>: <i>
      - <a href="valuespecs.md">ValueSpecs</a></i>
    <a href="#allocationpools" title="AllocationPools">AllocationPools</a>: <i>
      - <a href="allocationpools.md">AllocationPools</a></i>
    <a href="#hostroutes" title="HostRoutes">HostRoutes</a>: <i>
      - <a href="hostroutes.md">HostRoutes</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Cidr

CIDR representing IP range for this subnet, based on IP
version. Changing this creates a new subnet.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsNameservers

An array of DNS name server names used by hosts
in this subnet. Changing this updates the DNS name servers for the existing
subnet.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDhcp

The administrative state of the network.
Acceptable values are "true" and "false". Changing this value enables or
disables the DHCP capabilities of the existing subnet. Defaults to true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayIp

Default gateway used by devices in this subnet.
Leaving this blank and not setting `no_gateway` will cause a default
gateway of `.1` to be used. Changing this updates the gateway IP of the
existing subnet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpVersion

IP version, either 4 (default) or 6. Changing this creates a
new subnet.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the subnet. Changing this updates the name of
the existing subnet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

The UUID of the parent network. Changing this
creates a new subnet.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoGateway

Do not set a gateway IP on this subnet. Changing
this removes or adds a default gateway IP of the existing subnet.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnet. If omitted, the
`region` argument of the provider is used. Changing this creates a new
subnet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

The owner of the subnet. Required if admin wants to
create a subnet for another tenant. Changing this creates a new subnet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueSpecs

Map of additional options.

_Required_: No

_Type_: List of <a href="valuespecs.md">ValueSpecs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllocationPools

_Required_: No

_Type_: List of <a href="allocationpools.md">AllocationPools</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostRoutes

_Required_: No

_Type_: List of <a href="hostroutes.md">HostRoutes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

