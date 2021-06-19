# TF::OPC::ComputeVpnEndpointV2

The ``opc_compute_vpn_endpoint_v2`` resource creates and manages an VPN Endpoint V2 in an Oracle Cloud Infrastructure Compute Classic identity domain.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OPC::ComputeVpnEndpointV2",
    "Properties" : {
        "<a href="#customervpngateway" title="CustomerVpnGateway">CustomerVpnGateway</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#ikeidentifier" title="IkeIdentifier">IkeIdentifier</a>" : <i>String</i>,
        "<a href="#ipnetwork" title="IpNetwork">IpNetwork</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#presharedkey" title="PreSharedKey">PreSharedKey</a>" : <i>String</i>,
        "<a href="#reachableroutes" title="ReachableRoutes">ReachableRoutes</a>" : <i>[ String, ... ]</i>,
        "<a href="#requireperfectforwardsecrecy" title="RequirePerfectForwardSecrecy">RequirePerfectForwardSecrecy</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#vnicsets" title="VnicSets">VnicSets</a>" : <i>[ String, ... ]</i>,
        "<a href="#phaseonesettings" title="PhaseOneSettings">PhaseOneSettings</a>" : <i>[ <a href="phaseonesettingsdefinition.md">PhaseOneSettingsDefinition</a>, ... ]</i>,
        "<a href="#phasetwosettings" title="PhaseTwoSettings">PhaseTwoSettings</a>" : <i>[ <a href="phasetwosettingsdefinition.md">PhaseTwoSettingsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OPC::ComputeVpnEndpointV2
Properties:
    <a href="#customervpngateway" title="CustomerVpnGateway">CustomerVpnGateway</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#ikeidentifier" title="IkeIdentifier">IkeIdentifier</a>: <i>String</i>
    <a href="#ipnetwork" title="IpNetwork">IpNetwork</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#presharedkey" title="PreSharedKey">PreSharedKey</a>: <i>String</i>
    <a href="#reachableroutes" title="ReachableRoutes">ReachableRoutes</a>: <i>
      - String</i>
    <a href="#requireperfectforwardsecrecy" title="RequirePerfectForwardSecrecy">RequirePerfectForwardSecrecy</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#vnicsets" title="VnicSets">VnicSets</a>: <i>
      - String</i>
    <a href="#phaseonesettings" title="PhaseOneSettings">PhaseOneSettings</a>: <i>
      - <a href="phaseonesettingsdefinition.md">PhaseOneSettingsDefinition</a></i>
    <a href="#phasetwosettings" title="PhaseTwoSettings">PhaseTwoSettings</a>: <i>
      - <a href="phasetwosettingsdefinition.md">PhaseTwoSettingsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CustomerVpnGateway

The ip address of the VPN gateway in your data center through which you want to connect to the Oracle Cloud VPN gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description of the VPN Endpoint V2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Enables or disables the VPN Endpoint V2. Set to true by default.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeIdentifier

The Internet Key Exchange (IKE) ID. If you don't specify a value, the default value is the public IP address of the cloud gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpNetwork

The name of the IP network on which the cloud gateway is created by VPNaaS.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the VPN Endpoint V2.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreSharedKey

The pre-shared VPN key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReachableRoutes

A list of routes (CIDR prefixes) that are reachable through this VPN tunnel.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequirePerfectForwardSecrecy

Boolean specifying whether Perfect Forward Secrecy is enabled. Set to true by default.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

List of tags that may be applied to the VPN Endpoint V2.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnicSets

A list of vnic sets that traffics is allowed to and from.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhaseOneSettings

_Required_: No

_Type_: List of <a href="phaseonesettingsdefinition.md">PhaseOneSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhaseTwoSettings

_Required_: No

_Type_: List of <a href="phasetwosettingsdefinition.md">PhaseTwoSettingsDefinition</a>

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

#### LocalGatewayIpAddress

Public IP Address of the Local Gateway.

#### LocalGatewayPrivateIpAddress

Private IP Address of the Local Gateway.

#### TunnelStatus

Returns the <code>TunnelStatus</code> value.

#### Uri

The Uniform Resource Identifier for the VPN Endpoint V2.

