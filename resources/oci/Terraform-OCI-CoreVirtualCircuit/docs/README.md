# Terraform::OCI::CoreVirtualCircuit

This resource provides the Virtual Circuit resource in Oracle Cloud Infrastructure Core service.

Creates a new virtual circuit to use with Oracle Cloud
Infrastructure FastConnect. For more information, see
[FastConnect Overview](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm).

For the purposes of access control, you must provide the OCID of the
compartment where you want the virtual circuit to reside. If you're
not sure which compartment to use, put the virtual circuit in the
same compartment with the DRG it's using. For more information about
compartments and access control, see
[Overview of the IAM Service](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm).
For information about OCIDs, see
[Resource Identifiers](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

You may optionally specify a *display name* for the virtual circuit.
It does not have to be unique, and you can change it. Avoid entering confidential information.

**Important:** When creating a virtual circuit, you specify a DRG for
the traffic to flow through. Make sure you attach the DRG to your
VCN and confirm the VCN's routing sends traffic to the DRG. Otherwise
traffic will not flow. For more information, see
[Route Tables](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::CoreVirtualCircuit",
    "Properties" : {
        "<a href="#bandwidthshapename" title="BandwidthShapeName">BandwidthShapeName</a>" : <i>String</i>,
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#customerasn" title="CustomerAsn">CustomerAsn</a>" : <i>String</i>,
        "<a href="#customerbgpasn" title="CustomerBgpAsn">CustomerBgpAsn</a>" : <i>Double</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtags.md">DefinedTags</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtags.md">FreeformTags</a>, ... ]</i>,
        "<a href="#gatewayid" title="GatewayId">GatewayId</a>" : <i>String</i>,
        "<a href="#providerserviceid" title="ProviderServiceId">ProviderServiceId</a>" : <i>String</i>,
        "<a href="#providerservicekeyname" title="ProviderServiceKeyName">ProviderServiceKeyName</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#crossconnectmappings" title="CrossConnectMappings">CrossConnectMappings</a>" : <i>[ <a href="crossconnectmappings.md">CrossConnectMappings</a>, ... ]</i>,
        "<a href="#publicprefixes" title="PublicPrefixes">PublicPrefixes</a>" : <i>[ <a href="publicprefixes.md">PublicPrefixes</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::CoreVirtualCircuit
Properties:
    <a href="#bandwidthshapename" title="BandwidthShapeName">BandwidthShapeName</a>: <i>String</i>
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#customerasn" title="CustomerAsn">CustomerAsn</a>: <i>String</i>
    <a href="#customerbgpasn" title="CustomerBgpAsn">CustomerBgpAsn</a>: <i>Double</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtags.md">DefinedTags</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtags.md">FreeformTags</a></i>
    <a href="#gatewayid" title="GatewayId">GatewayId</a>: <i>String</i>
    <a href="#providerserviceid" title="ProviderServiceId">ProviderServiceId</a>: <i>String</i>
    <a href="#providerservicekeyname" title="ProviderServiceKeyName">ProviderServiceKeyName</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#crossconnectmappings" title="CrossConnectMappings">CrossConnectMappings</a>: <i>
      - <a href="crossconnectmappings.md">CrossConnectMappings</a></i>
    <a href="#publicprefixes" title="PublicPrefixes">PublicPrefixes</a>: <i>
      - <a href="publicprefixes.md">PublicPrefixes</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### BandwidthShapeName

(Updatable) The provisioned data rate of the connection.  To get a list of the available bandwidth levels (that is, shapes), see [ListFastConnectProviderServiceVirtualCircuitBandwidthShapes](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/FastConnectProviderService/ListFastConnectProviderVirtualCircuitBandwidthShapes).  Example: `10 Gbps`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompartmentId

(Updatable) The OCID of the compartment to contain the virtual circuit.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerAsn

(Updatable) Your BGP ASN (either public or private). Provide this value only if there's a BGP session that goes from your edge router to Oracle. Otherwise, leave this empty or null. Can be a 2-byte or 4-byte ASN. Uses "asplain" format.  Example: `12345` (2-byte) or `1587232876` (4-byte).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerBgpAsn

(Updatable) Deprecated. Instead use `customerAsn`. If you specify values for both, the request will be rejected.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

_Required_: No

_Type_: List of <a href="definedtags.md">DefinedTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtags.md">FreeformTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayId

(Updatable) For private virtual circuits only. The OCID of the [dynamic routing gateway (DRG)](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/Drg) that this virtual circuit uses.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderServiceId

The OCID of the service offered by the provider (if you're connecting via a provider). To get a list of the available service offerings, see [ListFastConnectProviderServices](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/FastConnectProviderService/ListFastConnectProviderServices).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProviderServiceKeyName

(Updatable) The service key name offered by the provider (if the customer is connecting via a provider).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The Oracle Cloud Infrastructure region where this virtual circuit is located. Example: `phx`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of IP addresses used in this virtual circuit. PRIVATE means [RFC 1918](https://tools.ietf.org/html/rfc1918) addresses (10.0.0.0/8, 172.16/12, and 192.168/16).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrossConnectMappings

_Required_: No

_Type_: List of <a href="crossconnectmappings.md">CrossConnectMappings</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicPrefixes

_Required_: No

_Type_: List of <a href="publicprefixes.md">PublicPrefixes</a>

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

#### BgpManagement

Returns the <code>BgpManagement</code> value.

#### BgpSessionState

Returns the <code>BgpSessionState</code> value.

#### Id

Returns the <code>Id</code> value.

#### OracleBgpAsn

Returns the <code>OracleBgpAsn</code> value.

#### ProviderState

Returns the <code>ProviderState</code> value.

#### ReferenceComment

Returns the <code>ReferenceComment</code> value.

#### ServiceType

Returns the <code>ServiceType</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

