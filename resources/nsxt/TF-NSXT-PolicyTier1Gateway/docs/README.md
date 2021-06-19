# TF::NSXT::PolicyTier1Gateway

This resource provides a method for the management of a Tier-1 Gateway. A Tier-1 Gateway is often used for tenants, users and applications. There can be many Tier-1 gateways connected to a common Tier-0 provider gateway.

This resource is applicable to NSX Global Manager and NSX Policy Manager.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NSXT::PolicyTier1Gateway",
    "Properties" : {
        "<a href="#defaultrulelogging" title="DefaultRuleLogging">DefaultRuleLogging</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dhcpconfigpath" title="DhcpConfigPath">DhcpConfigPath</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#edgeclusterpath" title="EdgeClusterPath">EdgeClusterPath</a>" : <i>String</i>,
        "<a href="#egressqosprofilepath" title="EgressQosProfilePath">EgressQosProfilePath</a>" : <i>String</i>,
        "<a href="#enablefirewall" title="EnableFirewall">EnableFirewall</a>" : <i>Boolean</i>,
        "<a href="#enablestandbyrelocation" title="EnableStandbyRelocation">EnableStandbyRelocation</a>" : <i>Boolean</i>,
        "<a href="#failovermode" title="FailoverMode">FailoverMode</a>" : <i>String</i>,
        "<a href="#forcewhitelisting" title="ForceWhitelisting">ForceWhitelisting</a>" : <i>Boolean</i>,
        "<a href="#ingressqosprofilepath" title="IngressQosProfilePath">IngressQosProfilePath</a>" : <i>String</i>,
        "<a href="#ipv6dadprofilepath" title="Ipv6DadProfilePath">Ipv6DadProfilePath</a>" : <i>String</i>,
        "<a href="#ipv6ndraprofilepath" title="Ipv6NdraProfilePath">Ipv6NdraProfilePath</a>" : <i>String</i>,
        "<a href="#nsxid" title="NsxId">NsxId</a>" : <i>String</i>,
        "<a href="#poolallocation" title="PoolAllocation">PoolAllocation</a>" : <i>String</i>,
        "<a href="#routeadvertisementtypes" title="RouteAdvertisementTypes">RouteAdvertisementTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#tier0path" title="Tier0Path">Tier0Path</a>" : <i>String</i>,
        "<a href="#intersiteconfig" title="IntersiteConfig">IntersiteConfig</a>" : <i>[ <a href="intersiteconfigdefinition.md">IntersiteConfigDefinition</a>, ... ]</i>,
        "<a href="#localeservice" title="LocaleService">LocaleService</a>" : <i>[ <a href="localeservicedefinition.md">LocaleServiceDefinition</a>, ... ]</i>,
        "<a href="#routeadvertisementrule" title="RouteAdvertisementRule">RouteAdvertisementRule</a>" : <i>[ <a href="routeadvertisementruledefinition.md">RouteAdvertisementRuleDefinition</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NSXT::PolicyTier1Gateway
Properties:
    <a href="#defaultrulelogging" title="DefaultRuleLogging">DefaultRuleLogging</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dhcpconfigpath" title="DhcpConfigPath">DhcpConfigPath</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#edgeclusterpath" title="EdgeClusterPath">EdgeClusterPath</a>: <i>String</i>
    <a href="#egressqosprofilepath" title="EgressQosProfilePath">EgressQosProfilePath</a>: <i>String</i>
    <a href="#enablefirewall" title="EnableFirewall">EnableFirewall</a>: <i>Boolean</i>
    <a href="#enablestandbyrelocation" title="EnableStandbyRelocation">EnableStandbyRelocation</a>: <i>Boolean</i>
    <a href="#failovermode" title="FailoverMode">FailoverMode</a>: <i>String</i>
    <a href="#forcewhitelisting" title="ForceWhitelisting">ForceWhitelisting</a>: <i>Boolean</i>
    <a href="#ingressqosprofilepath" title="IngressQosProfilePath">IngressQosProfilePath</a>: <i>String</i>
    <a href="#ipv6dadprofilepath" title="Ipv6DadProfilePath">Ipv6DadProfilePath</a>: <i>String</i>
    <a href="#ipv6ndraprofilepath" title="Ipv6NdraProfilePath">Ipv6NdraProfilePath</a>: <i>String</i>
    <a href="#nsxid" title="NsxId">NsxId</a>: <i>String</i>
    <a href="#poolallocation" title="PoolAllocation">PoolAllocation</a>: <i>String</i>
    <a href="#routeadvertisementtypes" title="RouteAdvertisementTypes">RouteAdvertisementTypes</a>: <i>
      - String</i>
    <a href="#tier0path" title="Tier0Path">Tier0Path</a>: <i>String</i>
    <a href="#intersiteconfig" title="IntersiteConfig">IntersiteConfig</a>: <i>
      - <a href="intersiteconfigdefinition.md">IntersiteConfigDefinition</a></i>
    <a href="#localeservice" title="LocaleService">LocaleService</a>: <i>
      - <a href="localeservicedefinition.md">LocaleServiceDefinition</a></i>
    <a href="#routeadvertisementrule" title="RouteAdvertisementRule">RouteAdvertisementRule</a>: <i>
      - <a href="routeadvertisementruledefinition.md">RouteAdvertisementRuleDefinition</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### DefaultRuleLogging

Boolean flag indicating if the default rule logging will be enabled or not. The default value is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhcpConfigPath

Policy path to DHCP server or relay configuration to use for this gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Display name of the resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdgeClusterPath

The path of the edge cluster where the Tier-0 is placed.
* `preferred_edge_paths` - (Optional) Policy paths to edge nodes. Specified edge is used as preferred edge cluster member when failover mode is set to `PREEMPTIVE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EgressQosProfilePath

QoS Profile path for egress traffic on link connected to Tier0 gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableFirewall

Boolean flag indicating if the edge firewall will be enabled or not. The default value is true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableStandbyRelocation

Boolean flag indicating if the standby relocation will be enabled or not. The default value is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailoverMode

This failover mode determines, whether the preferred service router instance for given logical router will preempt the peer. Accepted values are PREEMPTIVE/NON_PREEMPTIVE.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceWhitelisting

Boolean flag indicating if white-listing will be forced or not. The default value is false. This argument is deprecated and will be removed. Please use `nsxt_policy_predefined_gateway_policy` resource to control default action.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IngressQosProfilePath

QoS Profile path for ingress traffic on link connected to Tier0 gateway.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6DadProfilePath

Policy path to IPv6 DAD profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6NdraProfilePath

Policy path to IPv6 NDRA profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxId

The NSX ID of this resource. If set, this ID will be used to create the policy resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoolAllocation

Size of edge node allocation at for routing and load balancer service to meet performance and scalability requirements, one of `ROUTING`, `LB_SMALL`, `LB_MEDIUM`, `LB_LARGE`, `LB_XLARGE`. Default is `ROUTING`. Changing this attribute would force new resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteAdvertisementTypes

List of desired types of route advertisements, supported values: `TIER1_STATIC_ROUTES`, `TIER1_CONNECTED`, `TIER1_NAT`, `TIER1_LB_VIP`, `TIER1_LB_SNAT`, `TIER1_DNS_FORWARDER_IP`, `TIER1_IPSEC_LOCAL_ENDPOINT`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tier0Path

The path of the connected Tier0.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntersiteConfig

_Required_: No

_Type_: List of <a href="intersiteconfigdefinition.md">IntersiteConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocaleService

_Required_: No

_Type_: List of <a href="localeservicedefinition.md">LocaleServiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteAdvertisementRule

_Required_: No

_Type_: List of <a href="routeadvertisementruledefinition.md">RouteAdvertisementRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

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

#### Path

Returns the <code>Path</code> value.

#### Revision

Returns the <code>Revision</code> value.

