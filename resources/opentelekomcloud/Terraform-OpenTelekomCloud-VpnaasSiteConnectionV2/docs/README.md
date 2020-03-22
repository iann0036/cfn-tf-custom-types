# Terraform::OpenTelekomCloud::VpnaasSiteConnectionV2

Manages a V2 IPSec site connection resource within OpenTelekomCloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::VpnaasSiteConnectionV2",
    "Properties" : {
        "<a href="#adminstateup" title="AdminStateUp">AdminStateUp</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#ikepolicyid" title="IkepolicyId">IkepolicyId</a>" : <i>String</i>,
        "<a href="#initiator" title="Initiator">Initiator</a>" : <i>String</i>,
        "<a href="#ipsecpolicyid" title="IpsecpolicyId">IpsecpolicyId</a>" : <i>String</i>,
        "<a href="#localepgroupid" title="LocalEpGroupId">LocalEpGroupId</a>" : <i>String</i>,
        "<a href="#localid" title="LocalId">LocalId</a>" : <i>String</i>,
        "<a href="#mtu" title="Mtu">Mtu</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#peeraddress" title="PeerAddress">PeerAddress</a>" : <i>String</i>,
        "<a href="#peercidrs" title="PeerCidrs">PeerCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#peerepgroupid" title="PeerEpGroupId">PeerEpGroupId</a>" : <i>String</i>,
        "<a href="#peerid" title="PeerId">PeerId</a>" : <i>String</i>,
        "<a href="#psk" title="Psk">Psk</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
        "<a href="#valuespecs" title="ValueSpecs">ValueSpecs</a>" : <i>[ <a href="valuespecs.md">ValueSpecs</a>, ... ]</i>,
        "<a href="#vpnserviceid" title="VpnserviceId">VpnserviceId</a>" : <i>String</i>,
        "<a href="#dpd" title="Dpd">Dpd</a>" : <i>[ <a href="dpd.md">Dpd</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::VpnaasSiteConnectionV2
Properties:
    <a href="#adminstateup" title="AdminStateUp">AdminStateUp</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#ikepolicyid" title="IkepolicyId">IkepolicyId</a>: <i>String</i>
    <a href="#initiator" title="Initiator">Initiator</a>: <i>String</i>
    <a href="#ipsecpolicyid" title="IpsecpolicyId">IpsecpolicyId</a>: <i>String</i>
    <a href="#localepgroupid" title="LocalEpGroupId">LocalEpGroupId</a>: <i>String</i>
    <a href="#localid" title="LocalId">LocalId</a>: <i>String</i>
    <a href="#mtu" title="Mtu">Mtu</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#peeraddress" title="PeerAddress">PeerAddress</a>: <i>String</i>
    <a href="#peercidrs" title="PeerCidrs">PeerCidrs</a>: <i>
      - String</i>
    <a href="#peerepgroupid" title="PeerEpGroupId">PeerEpGroupId</a>: <i>String</i>
    <a href="#peerid" title="PeerId">PeerId</a>: <i>String</i>
    <a href="#psk" title="Psk">Psk</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
    <a href="#valuespecs" title="ValueSpecs">ValueSpecs</a>: <i>
      - <a href="valuespecs.md">ValueSpecs</a></i>
    <a href="#vpnserviceid" title="VpnserviceId">VpnserviceId</a>: <i>String</i>
    <a href="#dpd" title="Dpd">Dpd</a>: <i>
      - <a href="dpd.md">Dpd</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AdminStateUp

The administrative state of the resource. Can either be up(true) or down(false).
Changing this updates the administrative state of the existing connection.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The human-readable description for the connection.
Changing this updates the description of the existing connection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkepolicyId

The ID of the IKE policy. Changing this creates a new connection.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Initiator

A valid value is response-only or bi-directional. Default is bi-directional.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecpolicyId

The ID of the IPsec policy. Changing this creates a new connection.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalEpGroupId

The ID for the endpoint group that contains private subnets for the local side of the connection.
You must specify this parameter with the peer_ep_group_id parameter unless
in backward- compatible mode where peer_cidrs is provided with a subnet_id for the VPN service.
Changing this updates the existing connection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalId

An ID to be used instead of the external IP address for a virtual router used in traffic between instances on different networks in east-west traffic.
Most often, local ID would be domain name, email address, etc.
If this is not configured then the external IP address will be used as the ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mtu

The maximum transmission unit (MTU) value to address fragmentation.
Minimum value is 68 for IPv4, and 1280 for IPv6.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the connection. Changing this updates the name of
the existing connection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerAddress

The peer gateway public IPv4 or IPv6 address or FQDN.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerCidrs

Unique list of valid peer private CIDRs in the form < net_address > / < prefix > .

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerEpGroupId

The ID for the endpoint group that contains private CIDRs in the form < net_address > / < prefix > for the peer side of the connection.
You must specify this parameter with the local_ep_group_id parameter unless in backward-compatible mode
where peer_cidrs is provided with a subnet_id for the VPN service.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerId

The peer router identity for authentication. A valid value is an IPv4 address, IPv6 address, e-mail address, key ID, or FQDN.
Typically, this value matches the peer_address value.
Changing this updates the existing policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Psk

The pre-shared key. A valid value is any string.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 Networking client.
A Networking client is needed to create an IPSec site connection. If omitted, the
`region` argument of the provider is used. Changing this creates a new
site connection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

The owner of the connection. Required if admin wants to
create a connection for another project. Changing this creates a new connection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueSpecs

Map of additional options.

_Required_: No

_Type_: List of <a href="valuespecs.md">ValueSpecs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnserviceId

The ID of the VPN service. Changing this creates a new connection.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dpd

_Required_: No

_Type_: List of <a href="dpd.md">Dpd</a>

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

#### Id

Returns the <code>Id</code> value.

