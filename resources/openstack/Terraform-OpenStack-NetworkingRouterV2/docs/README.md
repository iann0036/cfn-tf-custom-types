# Terraform::OpenStack::NetworkingRouterV2

Manages a V2 router resource within OpenStack.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::NetworkingRouterV2",
    "Properties" : {
        "<a href="#adminstateup" title="AdminStateUp">AdminStateUp</a>" : <i>Boolean</i>,
        "<a href="#availabilityzonehints" title="AvailabilityZoneHints">AvailabilityZoneHints</a>" : <i>[ String, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#distributed" title="Distributed">Distributed</a>" : <i>Boolean</i>,
        "<a href="#enablesnat" title="EnableSnat">EnableSnat</a>" : <i>Boolean</i>,
        "<a href="#externalgateway" title="ExternalGateway">ExternalGateway</a>" : <i>String</i>,
        "<a href="#externalnetworkid" title="ExternalNetworkId">ExternalNetworkId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
        "<a href="#valuespecs" title="ValueSpecs">ValueSpecs</a>" : <i>[ <a href="valuespecs.md">ValueSpecs</a>, ... ]</i>,
        "<a href="#externalfixedip" title="ExternalFixedIp">ExternalFixedIp</a>" : <i>[ <a href="externalfixedip.md">ExternalFixedIp</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#vendoroptions" title="VendorOptions">VendorOptions</a>" : <i>[ <a href="vendoroptions.md">VendorOptions</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::NetworkingRouterV2
Properties:
    <a href="#adminstateup" title="AdminStateUp">AdminStateUp</a>: <i>Boolean</i>
    <a href="#availabilityzonehints" title="AvailabilityZoneHints">AvailabilityZoneHints</a>: <i>
      - String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#distributed" title="Distributed">Distributed</a>: <i>Boolean</i>
    <a href="#enablesnat" title="EnableSnat">EnableSnat</a>: <i>Boolean</i>
    <a href="#externalgateway" title="ExternalGateway">ExternalGateway</a>: <i>String</i>
    <a href="#externalnetworkid" title="ExternalNetworkId">ExternalNetworkId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
    <a href="#valuespecs" title="ValueSpecs">ValueSpecs</a>: <i>
      - <a href="valuespecs.md">ValueSpecs</a></i>
    <a href="#externalfixedip" title="ExternalFixedIp">ExternalFixedIp</a>: <i>
      - <a href="externalfixedip.md">ExternalFixedIp</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#vendoroptions" title="VendorOptions">VendorOptions</a>: <i>
      - <a href="vendoroptions.md">VendorOptions</a></i>
</pre>

## Properties

#### AdminStateUp

Administrative up/down status for the router
(must be "true" or "false" if provided). Changing this updates the
`admin_state_up` of an existing router.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZoneHints

An availability zone is used to make
network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
this creates a new router.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Human-readable description for the router.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Distributed

Indicates whether or not to create a
distributed router. The default policy setting in Neutron restricts
usage of this property to administrative users only.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSnat

Enable Source NAT for the router. Valid values are
"true" or "false". An `external_network_id` has to be set in order to
set this property. Changing this updates the `enable_snat` of the router.
Setting this value **requires** an **ext-gw-mode** extension to be enabled
in OpenStack Neutron.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalGateway

The
network UUID of an external gateway for the router. A router with an
external gateway is required if any compute instances or load balancers
will be using floating IPs. Changing this updates the external gateway
of an existing router.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalNetworkId

The network UUID of an external gateway
for the router. A router with an external gateway is required if any
compute instances or load balancers will be using floating IPs. Changing
this updates the external gateway of the router.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name for the router. Changing this
updates the `name` of an existing router.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
`region` argument of the provider is used. Changing this creates a new
router.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A set of string tags for the router.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

The owner of the floating IP. Required if admin wants
to create a router for another tenant. Changing this creates a new router.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueSpecs

Map of additional driver-specific options.

_Required_: No

_Type_: List of <a href="valuespecs.md">ValueSpecs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalFixedIp

_Required_: No

_Type_: List of <a href="externalfixedip.md">ExternalFixedIp</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VendorOptions

_Required_: No

_Type_: List of <a href="vendoroptions.md">VendorOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AllTags

Returns the <code>AllTags</code> value.

