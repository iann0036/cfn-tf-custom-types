# TF::ECL::NetworkStaticRouteV2

Manages a V2 static route resource within Enterprise Cloud.
~> **Notice** We only support Static Route with service_type "internet" for now.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ECL::NetworkStaticRouteV2",
    "Properties" : {
        "<a href="#awsgwid" title="AwsGwId">AwsGwId</a>" : <i>String</i>,
        "<a href="#azuregwid" title="AzureGwId">AzureGwId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#destination" title="Destination">Destination</a>" : <i>String</i>,
        "<a href="#ficgwid" title="FicGwId">FicGwId</a>" : <i>String</i>,
        "<a href="#gcpgwid" title="GcpGwId">GcpGwId</a>" : <i>String</i>,
        "<a href="#interdcgwid" title="InterdcGwId">InterdcGwId</a>" : <i>String</i>,
        "<a href="#internetgwid" title="InternetGwId">InternetGwId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nexthop" title="Nexthop">Nexthop</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#servicetype" title="ServiceType">ServiceType</a>" : <i>String</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
        "<a href="#vpngwid" title="VpnGwId">VpnGwId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ECL::NetworkStaticRouteV2
Properties:
    <a href="#awsgwid" title="AwsGwId">AwsGwId</a>: <i>String</i>
    <a href="#azuregwid" title="AzureGwId">AzureGwId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#destination" title="Destination">Destination</a>: <i>String</i>
    <a href="#ficgwid" title="FicGwId">FicGwId</a>: <i>String</i>
    <a href="#gcpgwid" title="GcpGwId">GcpGwId</a>: <i>String</i>
    <a href="#interdcgwid" title="InterdcGwId">InterdcGwId</a>: <i>String</i>
    <a href="#internetgwid" title="InternetGwId">InternetGwId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nexthop" title="Nexthop">Nexthop</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#servicetype" title="ServiceType">ServiceType</a>: <i>String</i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
    <a href="#vpngwid" title="VpnGwId">VpnGwId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AwsGwId

AWS Gateway on which this static route will be set. Conflicts with "azure_gw_id", "fic_gw_id", "gcp_gw_id", "interdc_gw_id", "internet_gw_id" and "vpn_gw_id".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureGwId

Azure Gateway on which this static route will be set. Conflicts with "aws_gw_id", "fic_gw_id", "gcp_gw_id", "interdc_gw_id", "internet_gw_id" and "vpn_gw_id".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the Static Route resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

CIDR this static route points to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FicGwId

FIC Gateway on which this static route will be set. Conflicts with "aws_gw_id", "azure_gw_id", "gcp_gw_id", "interdc_gw_id", "internet_gw_id" and "vpn_gw_id".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpGwId

GCP Gateway on which this static route will be set. Conflicts with "aws_gw_id", "azure_gw_id", "fic_gw_id", "interdc_gw_id", "internet_gw_id" and "vpn_gw_id".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterdcGwId

Inter DC Gateway on which this static route will be set. Conflicts with "aws_gw_id", "azure_gw_id", "fic_gw_id", "gcp_gw_id", "internet_gw_id" and "vpn_gw_id".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetGwId

Internet Gateway on which this static route will be set. Conflicts with "aws_gw_id", "azure_gw_id", "fic_gw_id", "gcp_gw_id", "interdc_gw_id" and "vpn_gw_id".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the Static Route resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nexthop

Next Hop address for specified CIDR.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 Network client.
Public ips are associated with accounts, but a Network client is needed to
create one. If omitted, the `region` argument of the provider is used.
Changing this creates a new public ip.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceType

Service type for this route. Must be one of "aws", "azure", "gcp", "interdc", "internet" and "vpn".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

Tenant ID of the owner (UUID).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnGwId

VPN Gateway on which this static route will be set. Conflicts with "aws_gw_id", "azure_gw_id", "fic_gw_id", "gcp_gw_id", "interdc_gw_id" and "internet_gw_id".

_Required_: No

_Type_: String

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

#### Id

Returns the <code>Id</code> value.

