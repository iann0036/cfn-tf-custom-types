# TF::AWS::VpnConnection

Manages an EC2 VPN connection. These objects can be connected to customer gateways, and allow you to establish tunnels between your network and Amazon.

~> **Note:** All arguments including `tunnel1_preshared_key` and `tunnel2_preshared_key` will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

~> **Note:** The CIDR blocks in the arguments `tunnel1_inside_cidr` and `tunnel2_inside_cidr` must have a prefix of /30 and be a part of a specific range.
[Read more about this in the AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpnTunnelOptionsSpecification.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::VpnConnection",
    "Properties" : {
        "<a href="#customergatewayid" title="CustomerGatewayId">CustomerGatewayId</a>" : <i>String</i>,
        "<a href="#enableacceleration" title="EnableAcceleration">EnableAcceleration</a>" : <i>Boolean</i>,
        "<a href="#localipv4networkcidr" title="LocalIpv4NetworkCidr">LocalIpv4NetworkCidr</a>" : <i>String</i>,
        "<a href="#localipv6networkcidr" title="LocalIpv6NetworkCidr">LocalIpv6NetworkCidr</a>" : <i>String</i>,
        "<a href="#remoteipv4networkcidr" title="RemoteIpv4NetworkCidr">RemoteIpv4NetworkCidr</a>" : <i>String</i>,
        "<a href="#remoteipv6networkcidr" title="RemoteIpv6NetworkCidr">RemoteIpv6NetworkCidr</a>" : <i>String</i>,
        "<a href="#staticroutesonly" title="StaticRoutesOnly">StaticRoutesOnly</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#transitgatewayid" title="TransitGatewayId">TransitGatewayId</a>" : <i>String</i>,
        "<a href="#tunnel1dpdtimeoutaction" title="Tunnel1DpdTimeoutAction">Tunnel1DpdTimeoutAction</a>" : <i>String</i>,
        "<a href="#tunnel1dpdtimeoutseconds" title="Tunnel1DpdTimeoutSeconds">Tunnel1DpdTimeoutSeconds</a>" : <i>Double</i>,
        "<a href="#tunnel1ikeversions" title="Tunnel1IkeVersions">Tunnel1IkeVersions</a>" : <i>[ String, ... ]</i>,
        "<a href="#tunnel1insidecidr" title="Tunnel1InsideCidr">Tunnel1InsideCidr</a>" : <i>String</i>,
        "<a href="#tunnel1insideipv6cidr" title="Tunnel1InsideIpv6Cidr">Tunnel1InsideIpv6Cidr</a>" : <i>String</i>,
        "<a href="#tunnel1phase1dhgroupnumbers" title="Tunnel1Phase1DhGroupNumbers">Tunnel1Phase1DhGroupNumbers</a>" : <i>[ Double, ... ]</i>,
        "<a href="#tunnel1phase1encryptionalgorithms" title="Tunnel1Phase1EncryptionAlgorithms">Tunnel1Phase1EncryptionAlgorithms</a>" : <i>[ String, ... ]</i>,
        "<a href="#tunnel1phase1integrityalgorithms" title="Tunnel1Phase1IntegrityAlgorithms">Tunnel1Phase1IntegrityAlgorithms</a>" : <i>[ String, ... ]</i>,
        "<a href="#tunnel1phase1lifetimeseconds" title="Tunnel1Phase1LifetimeSeconds">Tunnel1Phase1LifetimeSeconds</a>" : <i>Double</i>,
        "<a href="#tunnel1phase2dhgroupnumbers" title="Tunnel1Phase2DhGroupNumbers">Tunnel1Phase2DhGroupNumbers</a>" : <i>[ Double, ... ]</i>,
        "<a href="#tunnel1phase2encryptionalgorithms" title="Tunnel1Phase2EncryptionAlgorithms">Tunnel1Phase2EncryptionAlgorithms</a>" : <i>[ String, ... ]</i>,
        "<a href="#tunnel1phase2integrityalgorithms" title="Tunnel1Phase2IntegrityAlgorithms">Tunnel1Phase2IntegrityAlgorithms</a>" : <i>[ String, ... ]</i>,
        "<a href="#tunnel1phase2lifetimeseconds" title="Tunnel1Phase2LifetimeSeconds">Tunnel1Phase2LifetimeSeconds</a>" : <i>Double</i>,
        "<a href="#tunnel1presharedkey" title="Tunnel1PresharedKey">Tunnel1PresharedKey</a>" : <i>String</i>,
        "<a href="#tunnel1rekeyfuzzpercentage" title="Tunnel1RekeyFuzzPercentage">Tunnel1RekeyFuzzPercentage</a>" : <i>Double</i>,
        "<a href="#tunnel1rekeymargintimeseconds" title="Tunnel1RekeyMarginTimeSeconds">Tunnel1RekeyMarginTimeSeconds</a>" : <i>Double</i>,
        "<a href="#tunnel1replaywindowsize" title="Tunnel1ReplayWindowSize">Tunnel1ReplayWindowSize</a>" : <i>Double</i>,
        "<a href="#tunnel1startupaction" title="Tunnel1StartupAction">Tunnel1StartupAction</a>" : <i>String</i>,
        "<a href="#tunnel2dpdtimeoutaction" title="Tunnel2DpdTimeoutAction">Tunnel2DpdTimeoutAction</a>" : <i>String</i>,
        "<a href="#tunnel2dpdtimeoutseconds" title="Tunnel2DpdTimeoutSeconds">Tunnel2DpdTimeoutSeconds</a>" : <i>Double</i>,
        "<a href="#tunnel2ikeversions" title="Tunnel2IkeVersions">Tunnel2IkeVersions</a>" : <i>[ String, ... ]</i>,
        "<a href="#tunnel2insidecidr" title="Tunnel2InsideCidr">Tunnel2InsideCidr</a>" : <i>String</i>,
        "<a href="#tunnel2insideipv6cidr" title="Tunnel2InsideIpv6Cidr">Tunnel2InsideIpv6Cidr</a>" : <i>String</i>,
        "<a href="#tunnel2phase1dhgroupnumbers" title="Tunnel2Phase1DhGroupNumbers">Tunnel2Phase1DhGroupNumbers</a>" : <i>[ Double, ... ]</i>,
        "<a href="#tunnel2phase1encryptionalgorithms" title="Tunnel2Phase1EncryptionAlgorithms">Tunnel2Phase1EncryptionAlgorithms</a>" : <i>[ String, ... ]</i>,
        "<a href="#tunnel2phase1integrityalgorithms" title="Tunnel2Phase1IntegrityAlgorithms">Tunnel2Phase1IntegrityAlgorithms</a>" : <i>[ String, ... ]</i>,
        "<a href="#tunnel2phase1lifetimeseconds" title="Tunnel2Phase1LifetimeSeconds">Tunnel2Phase1LifetimeSeconds</a>" : <i>Double</i>,
        "<a href="#tunnel2phase2dhgroupnumbers" title="Tunnel2Phase2DhGroupNumbers">Tunnel2Phase2DhGroupNumbers</a>" : <i>[ Double, ... ]</i>,
        "<a href="#tunnel2phase2encryptionalgorithms" title="Tunnel2Phase2EncryptionAlgorithms">Tunnel2Phase2EncryptionAlgorithms</a>" : <i>[ String, ... ]</i>,
        "<a href="#tunnel2phase2integrityalgorithms" title="Tunnel2Phase2IntegrityAlgorithms">Tunnel2Phase2IntegrityAlgorithms</a>" : <i>[ String, ... ]</i>,
        "<a href="#tunnel2phase2lifetimeseconds" title="Tunnel2Phase2LifetimeSeconds">Tunnel2Phase2LifetimeSeconds</a>" : <i>Double</i>,
        "<a href="#tunnel2presharedkey" title="Tunnel2PresharedKey">Tunnel2PresharedKey</a>" : <i>String</i>,
        "<a href="#tunnel2rekeyfuzzpercentage" title="Tunnel2RekeyFuzzPercentage">Tunnel2RekeyFuzzPercentage</a>" : <i>Double</i>,
        "<a href="#tunnel2rekeymargintimeseconds" title="Tunnel2RekeyMarginTimeSeconds">Tunnel2RekeyMarginTimeSeconds</a>" : <i>Double</i>,
        "<a href="#tunnel2replaywindowsize" title="Tunnel2ReplayWindowSize">Tunnel2ReplayWindowSize</a>" : <i>Double</i>,
        "<a href="#tunnel2startupaction" title="Tunnel2StartupAction">Tunnel2StartupAction</a>" : <i>String</i>,
        "<a href="#tunnelinsideipversion" title="TunnelInsideIpVersion">TunnelInsideIpVersion</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::VpnConnection
Properties:
    <a href="#customergatewayid" title="CustomerGatewayId">CustomerGatewayId</a>: <i>String</i>
    <a href="#enableacceleration" title="EnableAcceleration">EnableAcceleration</a>: <i>Boolean</i>
    <a href="#localipv4networkcidr" title="LocalIpv4NetworkCidr">LocalIpv4NetworkCidr</a>: <i>String</i>
    <a href="#localipv6networkcidr" title="LocalIpv6NetworkCidr">LocalIpv6NetworkCidr</a>: <i>String</i>
    <a href="#remoteipv4networkcidr" title="RemoteIpv4NetworkCidr">RemoteIpv4NetworkCidr</a>: <i>String</i>
    <a href="#remoteipv6networkcidr" title="RemoteIpv6NetworkCidr">RemoteIpv6NetworkCidr</a>: <i>String</i>
    <a href="#staticroutesonly" title="StaticRoutesOnly">StaticRoutesOnly</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#transitgatewayid" title="TransitGatewayId">TransitGatewayId</a>: <i>String</i>
    <a href="#tunnel1dpdtimeoutaction" title="Tunnel1DpdTimeoutAction">Tunnel1DpdTimeoutAction</a>: <i>String</i>
    <a href="#tunnel1dpdtimeoutseconds" title="Tunnel1DpdTimeoutSeconds">Tunnel1DpdTimeoutSeconds</a>: <i>Double</i>
    <a href="#tunnel1ikeversions" title="Tunnel1IkeVersions">Tunnel1IkeVersions</a>: <i>
      - String</i>
    <a href="#tunnel1insidecidr" title="Tunnel1InsideCidr">Tunnel1InsideCidr</a>: <i>String</i>
    <a href="#tunnel1insideipv6cidr" title="Tunnel1InsideIpv6Cidr">Tunnel1InsideIpv6Cidr</a>: <i>String</i>
    <a href="#tunnel1phase1dhgroupnumbers" title="Tunnel1Phase1DhGroupNumbers">Tunnel1Phase1DhGroupNumbers</a>: <i>
      - Double</i>
    <a href="#tunnel1phase1encryptionalgorithms" title="Tunnel1Phase1EncryptionAlgorithms">Tunnel1Phase1EncryptionAlgorithms</a>: <i>
      - String</i>
    <a href="#tunnel1phase1integrityalgorithms" title="Tunnel1Phase1IntegrityAlgorithms">Tunnel1Phase1IntegrityAlgorithms</a>: <i>
      - String</i>
    <a href="#tunnel1phase1lifetimeseconds" title="Tunnel1Phase1LifetimeSeconds">Tunnel1Phase1LifetimeSeconds</a>: <i>Double</i>
    <a href="#tunnel1phase2dhgroupnumbers" title="Tunnel1Phase2DhGroupNumbers">Tunnel1Phase2DhGroupNumbers</a>: <i>
      - Double</i>
    <a href="#tunnel1phase2encryptionalgorithms" title="Tunnel1Phase2EncryptionAlgorithms">Tunnel1Phase2EncryptionAlgorithms</a>: <i>
      - String</i>
    <a href="#tunnel1phase2integrityalgorithms" title="Tunnel1Phase2IntegrityAlgorithms">Tunnel1Phase2IntegrityAlgorithms</a>: <i>
      - String</i>
    <a href="#tunnel1phase2lifetimeseconds" title="Tunnel1Phase2LifetimeSeconds">Tunnel1Phase2LifetimeSeconds</a>: <i>Double</i>
    <a href="#tunnel1presharedkey" title="Tunnel1PresharedKey">Tunnel1PresharedKey</a>: <i>String</i>
    <a href="#tunnel1rekeyfuzzpercentage" title="Tunnel1RekeyFuzzPercentage">Tunnel1RekeyFuzzPercentage</a>: <i>Double</i>
    <a href="#tunnel1rekeymargintimeseconds" title="Tunnel1RekeyMarginTimeSeconds">Tunnel1RekeyMarginTimeSeconds</a>: <i>Double</i>
    <a href="#tunnel1replaywindowsize" title="Tunnel1ReplayWindowSize">Tunnel1ReplayWindowSize</a>: <i>Double</i>
    <a href="#tunnel1startupaction" title="Tunnel1StartupAction">Tunnel1StartupAction</a>: <i>String</i>
    <a href="#tunnel2dpdtimeoutaction" title="Tunnel2DpdTimeoutAction">Tunnel2DpdTimeoutAction</a>: <i>String</i>
    <a href="#tunnel2dpdtimeoutseconds" title="Tunnel2DpdTimeoutSeconds">Tunnel2DpdTimeoutSeconds</a>: <i>Double</i>
    <a href="#tunnel2ikeversions" title="Tunnel2IkeVersions">Tunnel2IkeVersions</a>: <i>
      - String</i>
    <a href="#tunnel2insidecidr" title="Tunnel2InsideCidr">Tunnel2InsideCidr</a>: <i>String</i>
    <a href="#tunnel2insideipv6cidr" title="Tunnel2InsideIpv6Cidr">Tunnel2InsideIpv6Cidr</a>: <i>String</i>
    <a href="#tunnel2phase1dhgroupnumbers" title="Tunnel2Phase1DhGroupNumbers">Tunnel2Phase1DhGroupNumbers</a>: <i>
      - Double</i>
    <a href="#tunnel2phase1encryptionalgorithms" title="Tunnel2Phase1EncryptionAlgorithms">Tunnel2Phase1EncryptionAlgorithms</a>: <i>
      - String</i>
    <a href="#tunnel2phase1integrityalgorithms" title="Tunnel2Phase1IntegrityAlgorithms">Tunnel2Phase1IntegrityAlgorithms</a>: <i>
      - String</i>
    <a href="#tunnel2phase1lifetimeseconds" title="Tunnel2Phase1LifetimeSeconds">Tunnel2Phase1LifetimeSeconds</a>: <i>Double</i>
    <a href="#tunnel2phase2dhgroupnumbers" title="Tunnel2Phase2DhGroupNumbers">Tunnel2Phase2DhGroupNumbers</a>: <i>
      - Double</i>
    <a href="#tunnel2phase2encryptionalgorithms" title="Tunnel2Phase2EncryptionAlgorithms">Tunnel2Phase2EncryptionAlgorithms</a>: <i>
      - String</i>
    <a href="#tunnel2phase2integrityalgorithms" title="Tunnel2Phase2IntegrityAlgorithms">Tunnel2Phase2IntegrityAlgorithms</a>: <i>
      - String</i>
    <a href="#tunnel2phase2lifetimeseconds" title="Tunnel2Phase2LifetimeSeconds">Tunnel2Phase2LifetimeSeconds</a>: <i>Double</i>
    <a href="#tunnel2presharedkey" title="Tunnel2PresharedKey">Tunnel2PresharedKey</a>: <i>String</i>
    <a href="#tunnel2rekeyfuzzpercentage" title="Tunnel2RekeyFuzzPercentage">Tunnel2RekeyFuzzPercentage</a>: <i>Double</i>
    <a href="#tunnel2rekeymargintimeseconds" title="Tunnel2RekeyMarginTimeSeconds">Tunnel2RekeyMarginTimeSeconds</a>: <i>Double</i>
    <a href="#tunnel2replaywindowsize" title="Tunnel2ReplayWindowSize">Tunnel2ReplayWindowSize</a>: <i>Double</i>
    <a href="#tunnel2startupaction" title="Tunnel2StartupAction">Tunnel2StartupAction</a>: <i>String</i>
    <a href="#tunnelinsideipversion" title="TunnelInsideIpVersion">TunnelInsideIpVersion</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#vpngatewayid" title="VpnGatewayId">VpnGatewayId</a>: <i>String</i>
</pre>

## Properties

#### CustomerGatewayId

The ID of the customer gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableAcceleration

Indicate whether to enable acceleration for the VPN connection. Supports only EC2 Transit Gateway.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalIpv4NetworkCidr

The IPv4 CIDR on the customer gateway (on-premises) side of the VPN connection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalIpv6NetworkCidr

The IPv6 CIDR on the customer gateway (on-premises) side of the VPN connection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteIpv4NetworkCidr

The IPv4 CIDR on the AWS side of the VPN connection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteIpv6NetworkCidr

The IPv6 CIDR on the customer gateway (on-premises) side of the VPN connection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticRoutesOnly

Whether the VPN connection uses static routes exclusively. Static routes must be used for devices that don't support BGP.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Tags to apply to the connection. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransitGatewayId

The ID of the EC2 Transit Gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1DpdTimeoutAction

The action to take after DPD timeout occurs for the first VPN tunnel. Specify restart to restart the IKE initiation. Specify clear to end the IKE session. Valid values are `clear | none | restart`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1DpdTimeoutSeconds

The number of seconds after which a DPD timeout occurs for the first VPN tunnel. Valid value is equal or higher than `30`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1IkeVersions

The IKE versions that are permitted for the first VPN tunnel. Valid values are `ikev1 | ikev2`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1InsideCidr

The CIDR block of the inside IP addresses for the first VPN tunnel. Valid value is a size /30 CIDR block from the 169.254.0.0/16 range.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1InsideIpv6Cidr

The range of inside IPv6 addresses for the first VPN tunnel. Supports only EC2 Transit Gateway. Valid value is a size /126 CIDR block from the local fd00::/8 range.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1Phase1DhGroupNumbers

List of one or more Diffie-Hellman group numbers that are permitted for the first VPN tunnel for phase 1 IKE negotiations. Valid values are ` 2 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24`.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1Phase1EncryptionAlgorithms

List of one or more encryption algorithms that are permitted for the first VPN tunnel for phase 1 IKE negotiations. Valid values are `AES128 | AES256 | AES128-GCM-16 | AES256-GCM-16`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1Phase1IntegrityAlgorithms

One or more integrity algorithms that are permitted for the first VPN tunnel for phase 1 IKE negotiations. Valid values are `SHA1 | SHA2-256 | SHA2-384 | SHA2-512`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1Phase1LifetimeSeconds

The lifetime for phase 1 of the IKE negotiation for the first VPN tunnel, in seconds. Valid value is between `900` and `28800`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1Phase2DhGroupNumbers

List of one or more Diffie-Hellman group numbers that are permitted for the first VPN tunnel for phase 2 IKE negotiations. Valid values are `2 | 5 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24`.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1Phase2EncryptionAlgorithms

List of one or more encryption algorithms that are permitted for the first VPN tunnel for phase 2 IKE negotiations. Valid values are `AES128 | AES256 | AES128-GCM-16 | AES256-GCM-16`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1Phase2IntegrityAlgorithms

List of one or more integrity algorithms that are permitted for the first VPN tunnel for phase 2 IKE negotiations. Valid values are `SHA1 | SHA2-256 | SHA2-384 | SHA2-512`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1Phase2LifetimeSeconds

The lifetime for phase 2 of the IKE negotiation for the first VPN tunnel, in seconds. Valid value is between `900` and `3600`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1PresharedKey

The preshared key of the first VPN tunnel. The preshared key must be between 8 and 64 characters in length and cannot start with zero(0). Allowed characters are alphanumeric characters, periods(.) and underscores(_).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1RekeyFuzzPercentage

The percentage of the rekey window for the first VPN tunnel (determined by `tunnel1_rekey_margin_time_seconds`) during which the rekey time is randomly selected. Valid value is between `0` and `100`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1RekeyMarginTimeSeconds

The margin time, in seconds, before the phase 2 lifetime expires, during which the AWS side of the first VPN connection performs an IKE rekey. The exact time of the rekey is randomly selected based on the value for `tunnel1_rekey_fuzz_percentage`. Valid value is between `60` and half of `tunnel1_phase2_lifetime_seconds`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1ReplayWindowSize

The number of packets in an IKE replay window for the first VPN tunnel. Valid value is between `64` and `2048`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel1StartupAction

The action to take when the establishing the tunnel for the first VPN connection. By default, your customer gateway device must initiate the IKE negotiation and bring up the tunnel. Specify start for AWS to initiate the IKE negotiation. Valid values are `add | start`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2DpdTimeoutAction

The action to take after DPD timeout occurs for the second VPN tunnel. Specify restart to restart the IKE initiation. Specify clear to end the IKE session. Valid values are `clear | none | restart`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2DpdTimeoutSeconds

The number of seconds after which a DPD timeout occurs for the second VPN tunnel. Valid value is equal or higher than `30`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2IkeVersions

The IKE versions that are permitted for the second VPN tunnel. Valid values are `ikev1 | ikev2`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2InsideCidr

The CIDR block of the inside IP addresses for the second VPN tunnel. Valid value is a size /30 CIDR block from the 169.254.0.0/16 range.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2InsideIpv6Cidr

The range of inside IPv6 addresses for the second VPN tunnel. Supports only EC2 Transit Gateway. Valid value is a size /126 CIDR block from the local fd00::/8 range.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2Phase1DhGroupNumbers

List of one or more Diffie-Hellman group numbers that are permitted for the second VPN tunnel for phase 1 IKE negotiations. Valid values are ` 2 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24`.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2Phase1EncryptionAlgorithms

List of one or more encryption algorithms that are permitted for the second VPN tunnel for phase 1 IKE negotiations. Valid values are `AES128 | AES256 | AES128-GCM-16 | AES256-GCM-16`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2Phase1IntegrityAlgorithms

One or more integrity algorithms that are permitted for the second VPN tunnel for phase 1 IKE negotiations. Valid values are `SHA1 | SHA2-256 | SHA2-384 | SHA2-512`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2Phase1LifetimeSeconds

The lifetime for phase 1 of the IKE negotiation for the second VPN tunnel, in seconds. Valid value is between `900` and `28800`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2Phase2DhGroupNumbers

List of one or more Diffie-Hellman group numbers that are permitted for the second VPN tunnel for phase 2 IKE negotiations. Valid values are `2 | 5 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24`.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2Phase2EncryptionAlgorithms

List of one or more encryption algorithms that are permitted for the second VPN tunnel for phase 2 IKE negotiations. Valid values are `AES128 | AES256 | AES128-GCM-16 | AES256-GCM-16`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2Phase2IntegrityAlgorithms

List of one or more integrity algorithms that are permitted for the second VPN tunnel for phase 2 IKE negotiations. Valid values are `SHA1 | SHA2-256 | SHA2-384 | SHA2-512`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2Phase2LifetimeSeconds

The lifetime for phase 2 of the IKE negotiation for the second VPN tunnel, in seconds. Valid value is between `900` and `3600`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2PresharedKey

The preshared key of the second VPN tunnel. The preshared key must be between 8 and 64 characters in length and cannot start with zero(0). Allowed characters are alphanumeric characters, periods(.) and underscores(_).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2RekeyFuzzPercentage

The percentage of the rekey window for the second VPN tunnel (determined by `tunnel2_rekey_margin_time_seconds`) during which the rekey time is randomly selected. Valid value is between `0` and `100`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2RekeyMarginTimeSeconds

The margin time, in seconds, before the phase 2 lifetime expires, during which the AWS side of the second VPN connection performs an IKE rekey. The exact time of the rekey is randomly selected based on the value for `tunnel2_rekey_fuzz_percentage`. Valid value is between `60` and half of `tunnel2_phase2_lifetime_seconds`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2ReplayWindowSize

The number of packets in an IKE replay window for the second VPN tunnel. Valid value is between `64` and `2048`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnel2StartupAction

The action to take when the establishing the tunnel for the second VPN connection. By default, your customer gateway device must initiate the IKE negotiation and bring up the tunnel. Specify start for AWS to initiate the IKE negotiation. Valid values are `add | start`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TunnelInsideIpVersion

Indicate whether the VPN tunnels process IPv4 or IPv6 traffic. Valid values are `ipv4 | ipv6`. `ipv6` Supports only EC2 Transit Gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of VPN connection. The only type AWS supports at this time is "ipsec.1".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnGatewayId

The ID of the Virtual Private Gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### CustomerGatewayConfiguration

Returns the <code>CustomerGatewayConfiguration</code> value.

#### Id

Returns the <code>Id</code> value.

#### Routes

Returns the <code>Routes</code> value.

#### TransitGatewayAttachmentId

Returns the <code>TransitGatewayAttachmentId</code> value.

#### Tunnel1Address

Returns the <code>Tunnel1Address</code> value.

#### Tunnel1BgpAsn

Returns the <code>Tunnel1BgpAsn</code> value.

#### Tunnel1BgpHoldtime

Returns the <code>Tunnel1BgpHoldtime</code> value.

#### Tunnel1CgwInsideAddress

Returns the <code>Tunnel1CgwInsideAddress</code> value.

#### Tunnel1VgwInsideAddress

Returns the <code>Tunnel1VgwInsideAddress</code> value.

#### Tunnel2Address

Returns the <code>Tunnel2Address</code> value.

#### Tunnel2BgpAsn

Returns the <code>Tunnel2BgpAsn</code> value.

#### Tunnel2BgpHoldtime

Returns the <code>Tunnel2BgpHoldtime</code> value.

#### Tunnel2CgwInsideAddress

Returns the <code>Tunnel2CgwInsideAddress</code> value.

#### Tunnel2VgwInsideAddress

Returns the <code>Tunnel2VgwInsideAddress</code> value.

#### VgwTelemetry

Returns the <code>VgwTelemetry</code> value.

