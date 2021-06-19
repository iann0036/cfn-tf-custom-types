# TF::ECL::NetworkGatewayInterfaceV2

Manages a V2 gateway interface resource within Enterprise Cloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ECL::NetworkGatewayInterfaceV2",
    "Properties" : {
        "<a href="#awsgwid" title="AwsGwId">AwsGwId</a>" : <i>String</i>,
        "<a href="#azuregwid" title="AzureGwId">AzureGwId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#ficgwid" title="FicGwId">FicGwId</a>" : <i>String</i>,
        "<a href="#gcpgwid" title="GcpGwId">GcpGwId</a>" : <i>String</i>,
        "<a href="#gwvipv4" title="GwVipv4">GwVipv4</a>" : <i>String</i>,
        "<a href="#interdcgwid" title="InterdcGwId">InterdcGwId</a>" : <i>String</i>,
        "<a href="#internetgwid" title="InternetGwId">InternetGwId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#netmask" title="Netmask">Netmask</a>" : <i>Double</i>,
        "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>String</i>,
        "<a href="#primaryipv4" title="PrimaryIpv4">PrimaryIpv4</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#secondaryipv4" title="SecondaryIpv4">SecondaryIpv4</a>" : <i>String</i>,
        "<a href="#servicetype" title="ServiceType">ServiceType</a>" : <i>String</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
        "<a href="#vpngwid" title="VpnGwId">VpnGwId</a>" : <i>String</i>,
        "<a href="#vrid" title="Vrid">Vrid</a>" : <i>Double</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ECL::NetworkGatewayInterfaceV2
Properties:
    <a href="#awsgwid" title="AwsGwId">AwsGwId</a>: <i>String</i>
    <a href="#azuregwid" title="AzureGwId">AzureGwId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#ficgwid" title="FicGwId">FicGwId</a>: <i>String</i>
    <a href="#gcpgwid" title="GcpGwId">GcpGwId</a>: <i>String</i>
    <a href="#gwvipv4" title="GwVipv4">GwVipv4</a>: <i>String</i>
    <a href="#interdcgwid" title="InterdcGwId">InterdcGwId</a>: <i>String</i>
    <a href="#internetgwid" title="InternetGwId">InternetGwId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#netmask" title="Netmask">Netmask</a>: <i>Double</i>
    <a href="#networkid" title="NetworkId">NetworkId</a>: <i>String</i>
    <a href="#primaryipv4" title="PrimaryIpv4">PrimaryIpv4</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#secondaryipv4" title="SecondaryIpv4">SecondaryIpv4</a>: <i>String</i>
    <a href="#servicetype" title="ServiceType">ServiceType</a>: <i>String</i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
    <a href="#vpngwid" title="VpnGwId">VpnGwId</a>: <i>String</i>
    <a href="#vrid" title="Vrid">Vrid</a>: <i>Double</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AwsGwId

AWS Gateway to which this port is connected.
Conflicts with "azure_gw_id", "fic_gw_id", "gcp_gw_id", "interdc_gw_id", "internet_gw_id" and "vpn_gw_id".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureGwId

Azure Gateway to which this port is connected.
Conflicts with "aws_gw_id", "fic_gw_id", "gcp_gw_id", "interdc_gw_id", "internet_gw_id" and "vpn_gw_id".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the Gateway Interface resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FicGwId

FIC Gateway to which this port is connected.
Conflicts with "aws_gw_id", "azure_gw_id", "gcp_gw_id", "interdc_gw_id", "internet_gw_id" and "vpn_gw_id".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpGwId

GCP Gateway to which this port is connected.
Conflicts with "aws_gw_id", "azure_gw_id", "fic_gw_id", "interdc_gw_id", "internet_gw_id" and "vpn_gw_id".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GwVipv4

IP version 4 address to be assigned virtual router on VRRP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterdcGwId

Inter DC Gateway to which this port is connected.
Conflicts with "aws_gw_id", "azure_gw_id", "fic_gw_id", "gcp_gw_id", "internet_gw_id" and "vpn_gw_id".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetGwId

Internet GW to which this port is connected.
Conflicts with "aws_gw_id", "azure_gw_id", "fic_gw_id", "gcp_gw_id", "interdc_gw_id" and "vpn_gw_id".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the Gateway Interface resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Netmask

Netmask for IPv4 addresses.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

Network connected to this interface.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryIpv4

IP version 4 address to be assigned to primary device on VRRP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 Network client.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryIpv4

IP version 4 address to be assigned to secondary device on VRRP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceType

Service type for this interface.
Must be one of "aws", "azure", "fic", "gcp", "interdc", "internet" and "vpn".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

Tenant ID of the owner (UUID).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnGwId

VPN Gateway to which this port is connected.
Conflicts with "aws_gw_id", "azure_gw_id", "fic_gw_id", "gcp_gw_id", "interdc_gw_id" and "internet_gw_id".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vrid

VRRP Group ID for this GW Interface.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### GwVipv6

Returns the <code>GwVipv6</code> value.

#### Id

Returns the <code>Id</code> value.

#### PrimaryIpv6

Returns the <code>PrimaryIpv6</code> value.

#### SecondaryIpv6

Returns the <code>SecondaryIpv6</code> value.

