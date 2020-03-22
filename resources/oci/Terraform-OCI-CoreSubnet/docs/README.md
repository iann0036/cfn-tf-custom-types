# Terraform::OCI::CoreSubnet

This resource provides the Subnet resource in Oracle Cloud Infrastructure Core service.

Creates a new subnet in the specified VCN. You can't change the size of the subnet after creation,
so it's important to think about the size of subnets you need before creating them.
For more information, see [VCNs and Subnets](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm).
For information on the number of subnets you can have in a VCN, see
[Service Limits](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/servicelimits.htm).

For the purposes of access control, you must provide the OCID of the compartment where you want the subnet
to reside. Notice that the subnet doesn't have to be in the same compartment as the VCN, route tables, or
other Networking Service components. If you're not sure which compartment to use, put the subnet in
the same compartment as the VCN. For more information about compartments and access control, see
[Overview of the IAM Service](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs,
see [Resource Identifiers](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

You may optionally associate a route table with the subnet. If you don't, the subnet will use the
VCN's default route table. For more information about route tables, see
[Route Tables](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm).

You may optionally associate a security list with the subnet. If you don't, the subnet will use the
VCN's default security list. For more information about security lists, see
[Security Lists](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/securitylists.htm).

You may optionally associate a set of DHCP options with the subnet. If you don't, the subnet will use the
VCN's default set. For more information about DHCP options, see
[DHCP Options](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingDHCP.htm).

You may optionally specify a *display name* for the subnet, otherwise a default is provided.
It does not have to be unique, and you can change it. Avoid entering confidential information.

You can also add a DNS label for the subnet, which is required if you want the Internet and
VCN Resolver to resolve hostnames for instances in the subnet. For more information, see
[DNS in Your Virtual Cloud Network](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::CoreSubnet",
    "Properties" : {
        "<a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>" : <i>String</i>,
        "<a href="#cidrblock" title="CidrBlock">CidrBlock</a>" : <i>String</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtags.md">DefinedTags</a>, ... ]</i>,
        "<a href="#dhcpoptionsid" title="DhcpOptionsId">DhcpOptionsId</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#dnslabel" title="DnsLabel">DnsLabel</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtags.md">FreeformTags</a>, ... ]</i>,
        "<a href="#ipv6cidrblock" title="Ipv6cidrBlock">Ipv6cidrBlock</a>" : <i>String</i>,
        "<a href="#prohibitpubliciponvnic" title="ProhibitPublicIpOnVnic">ProhibitPublicIpOnVnic</a>" : <i>Boolean</i>,
        "<a href="#routetableid" title="RouteTableId">RouteTableId</a>" : <i>String</i>,
        "<a href="#securitylistids" title="SecurityListIds">SecurityListIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#vcnid" title="VcnId">VcnId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::CoreSubnet
Properties:
    <a href="#availabilitydomain" title="AvailabilityDomain">AvailabilityDomain</a>: <i>String</i>
    <a href="#cidrblock" title="CidrBlock">CidrBlock</a>: <i>String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtags.md">DefinedTags</a></i>
    <a href="#dhcpoptionsid" title="DhcpOptionsId">DhcpOptionsId</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#dnslabel" title="DnsLabel">DnsLabel</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtags.md">FreeformTags</a></i>
    <a href="#ipv6cidrblock" title="Ipv6cidrBlock">Ipv6cidrBlock</a>: <i>String</i>
    <a href="#prohibitpubliciponvnic" title="ProhibitPublicIpOnVnic">ProhibitPublicIpOnVnic</a>: <i>Boolean</i>
    <a href="#routetableid" title="RouteTableId">RouteTableId</a>: <i>String</i>
    <a href="#securitylistids" title="SecurityListIds">SecurityListIds</a>: <i>
      - String</i>
    <a href="#vcnid" title="VcnId">VcnId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AvailabilityDomain

Controls whether the subnet is regional or specific to an availability domain. Oracle recommends creating regional subnets because they're more flexible and make it easier to implement failover across availability domains. Originally, AD-specific subnets were the only kind available to use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CidrBlock

The CIDR IP address range of the subnet.  Example: `172.16.1.0/24`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

(Updatable) The OCID of the compartment to contain the subnet.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

_Required_: No

_Type_: List of <a href="definedtags.md">DefinedTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpOptionsId

(Updatable) The OCID of the set of DHCP options the subnet will use. If you don't provide a value, the subnet uses the VCN's default set of DHCP options.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsLabel

A DNS label for the subnet, used in conjunction with the VNIC's hostname and VCN's DNS label to form a fully qualified domain name (FQDN) for each VNIC within this subnet (for example, `bminstance-1.subnet123.vcn1.oraclevcn.com`). Must be an alphanumeric string that begins with a letter and is unique within the VCN. The value cannot be changed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtags.md">FreeformTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6cidrBlock

IPv6 is currently supported only in the Government Cloud. Use this to enable IPv6 addressing for this subnet. The VCN must be enabled for IPv6. You can't change this subnet characteristic later. All subnets are /64 in size. The subnet portion of the IPv6 address is the fourth hextet from the left (1111 in the following example).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProhibitPublicIpOnVnic

Whether VNICs within this subnet can have public IP addresses. Defaults to false, which means VNICs created in this subnet will automatically be assigned public IP addresses unless specified otherwise during instance launch or VNIC creation (with the `assignPublicIp` flag in [CreateVnicDetails](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/CreateVnicDetails/)). If `prohibitPublicIpOnVnic` is set to true, VNICs created in this subnet cannot have public IP addresses (that is, it's a private subnet).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteTableId

(Updatable) The OCID of the route table the subnet will use. If you don't provide a value, the subnet uses the VCN's default route table.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityListIds

(Updatable) The OCIDs of the security list or lists the subnet will use. If you don't provide a value, the subnet uses the VCN's default security list. Remember that security lists are associated *with the subnet*, but the rules are applied to the individual VNICs in the subnet.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcnId

The OCID of the VCN to contain the subnet.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

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

#### Ipv6publicCidrBlock

Returns the <code>Ipv6publicCidrBlock</code> value.

#### Ipv6virtualRouterIp

Returns the <code>Ipv6virtualRouterIp</code> value.

#### State

Returns the <code>State</code> value.

#### SubnetDomainName

Returns the <code>SubnetDomainName</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### VirtualRouterIp

Returns the <code>VirtualRouterIp</code> value.

#### VirtualRouterMac

Returns the <code>VirtualRouterMac</code> value.

