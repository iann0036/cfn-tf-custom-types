# TF::FortiOS::Wirelesscontrollerhotspot20Hsprofile

Configure hotspot profile.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::Wirelesscontrollerhotspot20Hsprofile",
    "Properties" : {
        "<a href="#accessnetworkasra" title="AccessNetworkAsra">AccessNetworkAsra</a>" : <i>String</i>,
        "<a href="#accessnetworkesr" title="AccessNetworkEsr">AccessNetworkEsr</a>" : <i>String</i>,
        "<a href="#accessnetworkinternet" title="AccessNetworkInternet">AccessNetworkInternet</a>" : <i>String</i>,
        "<a href="#accessnetworktype" title="AccessNetworkType">AccessNetworkType</a>" : <i>String</i>,
        "<a href="#accessnetworkuesa" title="AccessNetworkUesa">AccessNetworkUesa</a>" : <i>String</i>,
        "<a href="#anqpdomainid" title="AnqpDomainId">AnqpDomainId</a>" : <i>Double</i>,
        "<a href="#bsstransition" title="BssTransition">BssTransition</a>" : <i>String</i>,
        "<a href="#conncap" title="ConnCap">ConnCap</a>" : <i>String</i>,
        "<a href="#deauthrequesttimeout" title="DeauthRequestTimeout">DeauthRequestTimeout</a>" : <i>Double</i>,
        "<a href="#dgaf" title="Dgaf">Dgaf</a>" : <i>String</i>,
        "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#gascomebackdelay" title="GasComebackDelay">GasComebackDelay</a>" : <i>Double</i>,
        "<a href="#gasfragmentationlimit" title="GasFragmentationLimit">GasFragmentationLimit</a>" : <i>Double</i>,
        "<a href="#hessid" title="Hessid">Hessid</a>" : <i>String</i>,
        "<a href="#ipaddrtype" title="IpAddrType">IpAddrType</a>" : <i>String</i>,
        "<a href="#l2tif" title="L2tif">L2tif</a>" : <i>String</i>,
        "<a href="#n3gppplmn" title="N3gppPlmn">N3gppPlmn</a>" : <i>String</i>,
        "<a href="#nairealm" title="NaiRealm">NaiRealm</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkauth" title="NetworkAuth">NetworkAuth</a>" : <i>String</i>,
        "<a href="#operfriendlyname" title="OperFriendlyName">OperFriendlyName</a>" : <i>String</i>,
        "<a href="#osussid" title="OsuSsid">OsuSsid</a>" : <i>String</i>,
        "<a href="#pamebi" title="PameBi">PameBi</a>" : <i>String</i>,
        "<a href="#proxyarp" title="ProxyArp">ProxyArp</a>" : <i>String</i>,
        "<a href="#qosmap" title="QosMap">QosMap</a>" : <i>String</i>,
        "<a href="#roamingconsortium" title="RoamingConsortium">RoamingConsortium</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#venuegroup" title="VenueGroup">VenueGroup</a>" : <i>String</i>,
        "<a href="#venuename" title="VenueName">VenueName</a>" : <i>String</i>,
        "<a href="#venuetype" title="VenueType">VenueType</a>" : <i>String</i>,
        "<a href="#wanmetrics" title="WanMetrics">WanMetrics</a>" : <i>String</i>,
        "<a href="#wnmsleepmode" title="WnmSleepMode">WnmSleepMode</a>" : <i>String</i>,
        "<a href="#osuprovider" title="OsuProvider">OsuProvider</a>" : <i>[ <a href="osuproviderdefinition.md">OsuProviderDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::Wirelesscontrollerhotspot20Hsprofile
Properties:
    <a href="#accessnetworkasra" title="AccessNetworkAsra">AccessNetworkAsra</a>: <i>String</i>
    <a href="#accessnetworkesr" title="AccessNetworkEsr">AccessNetworkEsr</a>: <i>String</i>
    <a href="#accessnetworkinternet" title="AccessNetworkInternet">AccessNetworkInternet</a>: <i>String</i>
    <a href="#accessnetworktype" title="AccessNetworkType">AccessNetworkType</a>: <i>String</i>
    <a href="#accessnetworkuesa" title="AccessNetworkUesa">AccessNetworkUesa</a>: <i>String</i>
    <a href="#anqpdomainid" title="AnqpDomainId">AnqpDomainId</a>: <i>Double</i>
    <a href="#bsstransition" title="BssTransition">BssTransition</a>: <i>String</i>
    <a href="#conncap" title="ConnCap">ConnCap</a>: <i>String</i>
    <a href="#deauthrequesttimeout" title="DeauthRequestTimeout">DeauthRequestTimeout</a>: <i>Double</i>
    <a href="#dgaf" title="Dgaf">Dgaf</a>: <i>String</i>
    <a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#gascomebackdelay" title="GasComebackDelay">GasComebackDelay</a>: <i>Double</i>
    <a href="#gasfragmentationlimit" title="GasFragmentationLimit">GasFragmentationLimit</a>: <i>Double</i>
    <a href="#hessid" title="Hessid">Hessid</a>: <i>String</i>
    <a href="#ipaddrtype" title="IpAddrType">IpAddrType</a>: <i>String</i>
    <a href="#l2tif" title="L2tif">L2tif</a>: <i>String</i>
    <a href="#n3gppplmn" title="N3gppPlmn">N3gppPlmn</a>: <i>String</i>
    <a href="#nairealm" title="NaiRealm">NaiRealm</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkauth" title="NetworkAuth">NetworkAuth</a>: <i>String</i>
    <a href="#operfriendlyname" title="OperFriendlyName">OperFriendlyName</a>: <i>String</i>
    <a href="#osussid" title="OsuSsid">OsuSsid</a>: <i>String</i>
    <a href="#pamebi" title="PameBi">PameBi</a>: <i>String</i>
    <a href="#proxyarp" title="ProxyArp">ProxyArp</a>: <i>String</i>
    <a href="#qosmap" title="QosMap">QosMap</a>: <i>String</i>
    <a href="#roamingconsortium" title="RoamingConsortium">RoamingConsortium</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#venuegroup" title="VenueGroup">VenueGroup</a>: <i>String</i>
    <a href="#venuename" title="VenueName">VenueName</a>: <i>String</i>
    <a href="#venuetype" title="VenueType">VenueType</a>: <i>String</i>
    <a href="#wanmetrics" title="WanMetrics">WanMetrics</a>: <i>String</i>
    <a href="#wnmsleepmode" title="WnmSleepMode">WnmSleepMode</a>: <i>String</i>
    <a href="#osuprovider" title="OsuProvider">OsuProvider</a>: <i>
      - <a href="osuproviderdefinition.md">OsuProviderDefinition</a></i>
</pre>

## Properties

#### AccessNetworkAsra

Enable/disable additional step required for access (ASRA). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessNetworkEsr

Enable/disable emergency services reachable (ESR). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessNetworkInternet

Enable/disable connectivity to the Internet. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessNetworkType

Access network type. Valid values: `private-network`, `private-network-with-guest-access`, `chargeable-public-network`, `free-public-network`, `personal-device-network`, `emergency-services-only-network`, `test-or-experimental`, `wildcard`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessNetworkUesa

Enable/disable unauthenticated emergency service accessible (UESA). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnqpDomainId

ANQP Domain ID (0-65535).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BssTransition

Enable/disable basic service set (BSS) transition Support. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnCap

Connection capability name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeauthRequestTimeout

Deauthentication request timeout (in seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dgaf

Enable/disable downstream group-addressed forwarding (DGAF). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainName

Domain name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GasComebackDelay

GAS comeback delay (0 or 100 - 4000 milliseconds, default = 500).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GasFragmentationLimit

GAS fragmentation limit (512 - 4096, default = 1024).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hessid

Homogeneous extended service set identifier (HESSID).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddrType

IP address type name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L2tif

Enable/disable Layer 2 traffic inspection and filtering. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### N3gppPlmn

3GPP PLMN name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NaiRealm

NAI realm list name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Hotspot profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkAuth

Network authentication name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperFriendlyName

Operator friendly name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsuSsid

Online sign up (OSU) SSID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PameBi

Enable/disable Pre-Association Message Exchange BSSID Independent (PAME-BI). Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyArp

Enable/disable Proxy ARP. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QosMap

QoS MAP set ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoamingConsortium

Roaming consortium list name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VenueGroup

Venue group. Valid values: `unspecified`, `assembly`, `business`, `educational`, `factory`, `institutional`, `mercantile`, `residential`, `storage`, `utility`, `vehicular`, `outdoor`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VenueName

Venue name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VenueType

Venue type. Valid values: `unspecified`, `arena`, `stadium`, `passenger-terminal`, `amphitheater`, `amusement-park`, `place-of-worship`, `convention-center`, `library`, `museum`, `restaurant`, `theater`, `bar`, `coffee-shop`, `zoo-or-aquarium`, `emergency-center`, `doctor-office`, `bank`, `fire-station`, `police-station`, `post-office`, `professional-office`, `research-facility`, `attorney-office`, `primary-school`, `secondary-school`, `university-or-college`, `factory`, `hospital`, `long-term-care-facility`, `rehab-center`, `group-home`, `prison-or-jail`, `retail-store`, `grocery-market`, `auto-service-station`, `shopping-mall`, `gas-station`, `private`, `hotel-or-motel`, `dormitory`, `boarding-house`, `automobile`, `airplane`, `bus`, `ferry`, `ship-or-boat`, `train`, `motor-bike`, `muni-mesh-network`, `city-park`, `rest-area`, `traffic-control`, `bus-stop`, `kiosk`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WanMetrics

WAN metric name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WnmSleepMode

Enable/disable wireless network management (WNM) sleep mode. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsuProvider

_Required_: No

_Type_: List of <a href="osuproviderdefinition.md">OsuProviderDefinition</a>

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

