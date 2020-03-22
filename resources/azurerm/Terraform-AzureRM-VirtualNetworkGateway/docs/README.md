# Terraform::AzureRM::VirtualNetworkGateway

Manages a Virtual Network Gateway to establish secure, cross-premises connectivity.

-> **Note:** Please be aware that provisioning a Virtual Network Gateway takes a long time (between 30 minutes and 1 hour)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::VirtualNetworkGateway",
    "Properties" : {
        "<a href="#activeactive" title="ActiveActive">ActiveActive</a>" : <i>Boolean</i>,
        "<a href="#defaultlocalnetworkgatewayid" title="DefaultLocalNetworkGatewayId">DefaultLocalNetworkGatewayId</a>" : <i>String</i>,
        "<a href="#enablebgp" title="EnableBgp">EnableBgp</a>" : <i>Boolean</i>,
        "<a href="#generation" title="Generation">Generation</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#sku" title="Sku">Sku</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#vpntype" title="VpnType">VpnType</a>" : <i>String</i>,
        "<a href="#bgpsettings" title="BgpSettings">BgpSettings</a>" : <i>[ <a href="bgpsettings.md">BgpSettings</a>, ... ]</i>,
        "<a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>" : <i>[ <a href="ipconfiguration.md">IpConfiguration</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#vpnclientconfiguration" title="VpnClientConfiguration">VpnClientConfiguration</a>" : <i>[ <a href="vpnclientconfiguration.md">VpnClientConfiguration</a>, ... ]</i>,
        "<a href="#revokedcertificate" title="RevokedCertificate">RevokedCertificate</a>" : <i>[ <a href="revokedcertificate.md">RevokedCertificate</a>, ... ]</i>,
        "<a href="#rootcertificate" title="RootCertificate">RootCertificate</a>" : <i>[ <a href="rootcertificate.md">RootCertificate</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::VirtualNetworkGateway
Properties:
    <a href="#activeactive" title="ActiveActive">ActiveActive</a>: <i>Boolean</i>
    <a href="#defaultlocalnetworkgatewayid" title="DefaultLocalNetworkGatewayId">DefaultLocalNetworkGatewayId</a>: <i>String</i>
    <a href="#enablebgp" title="EnableBgp">EnableBgp</a>: <i>Boolean</i>
    <a href="#generation" title="Generation">Generation</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#sku" title="Sku">Sku</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#vpntype" title="VpnType">VpnType</a>: <i>String</i>
    <a href="#bgpsettings" title="BgpSettings">BgpSettings</a>: <i>
      - <a href="bgpsettings.md">BgpSettings</a></i>
    <a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>: <i>
      - <a href="ipconfiguration.md">IpConfiguration</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#vpnclientconfiguration" title="VpnClientConfiguration">VpnClientConfiguration</a>: <i>
      - <a href="vpnclientconfiguration.md">VpnClientConfiguration</a></i>
    <a href="#revokedcertificate" title="RevokedCertificate">RevokedCertificate</a>: <i>
      - <a href="revokedcertificate.md">RevokedCertificate</a></i>
    <a href="#rootcertificate" title="RootCertificate">RootCertificate</a>: <i>
      - <a href="rootcertificate.md">RootCertificate</a></i>
</pre>

## Properties

#### ActiveActive

If `true`, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a `HighPerformance` or an
`UltraPerformance` sku. If `false`, an active-standby gateway will be created.
Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultLocalNetworkGatewayId

The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (*forced tunneling*). Refer to the
[Azure documentation on forced tunneling](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm).
If not specified, forced tunneling is disabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBgp

If `true`, BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Generation

The Generation of the Virtual Network gateway. Possible values include `Generation1`, `Generation2` or `None`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Virtual Network Gateway. Changing the name
forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sku

Configuration of the size and capacity of the virtual network
gateway. Valid options are `Basic`, `Standard`, `HighPerformance`, `UltraPerformance`,
`ErGw1AZ`, `ErGw2AZ`, `ErGw3AZ`, `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw4`,`VpnGw5`, `VpnGw1AZ`,
`VpnGw2AZ`, `VpnGw3AZ`,`VpnGw4AZ` and `VpnGw5AZ` and depend on the `type`, `vpn_type` and
`generation` arguments.
A `PolicyBased` gateway only supports the `Basic` sku. Further, the `UltraPerformance`
sku is only supported by an `ExpressRoute` gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of the Virtual Network Gateway. Valid options are
`Vpn` or `ExpressRoute`. Changing the type forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnType

The routing type of the Virtual Network Gateway. Valid
options are `RouteBased` or `PolicyBased`. Defaults to `RouteBased`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BgpSettings

_Required_: No

_Type_: List of <a href="bgpsettings.md">BgpSettings</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpConfiguration

_Required_: No

_Type_: List of <a href="ipconfiguration.md">IpConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnClientConfiguration

_Required_: No

_Type_: List of <a href="vpnclientconfiguration.md">VpnClientConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RevokedCertificate

_Required_: No

_Type_: List of <a href="revokedcertificate.md">RevokedCertificate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootCertificate

_Required_: No

_Type_: List of <a href="rootcertificate.md">RootCertificate</a>

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

