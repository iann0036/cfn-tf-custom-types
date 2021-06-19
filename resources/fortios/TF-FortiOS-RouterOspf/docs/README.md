# TF::FortiOS::RouterOspf

Configure OSPF.

~> The provider supports the definition of Ospf-Interface in Router Ospf `fortios_router_ospf`, and also allows the definition of separate Ospf-Interface resources `fortios_routerospf_ospfinterface`, but do not use a `fortios_router_ospf` with in-line Ospf-Interface in conjunction with any `fortios_routerospf_ospfinterface` resources, otherwise conflicts and overwrite will occur.

~> The provider supports the definition of Network in Router Ospf `fortios_router_ospf`, and also allows the definition of separate Network resources `fortios_routerospf_network`, but do not use a `fortios_router_ospf` with in-line Network in conjunction with any `fortios_routerospf_network` resources, otherwise conflicts and overwrite will occur.

~> The provider supports the definition of Neighbor in Router Ospf `fortios_router_ospf`, and also allows the definition of separate Neighbor resources `fortios_routerospf_neighbor`, but do not use a `fortios_router_ospf` with in-line Neighbor in conjunction with any ...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::RouterOspf",
    "Properties" : {
        "<a href="#abrtype" title="AbrType">AbrType</a>" : <i>String</i>,
        "<a href="#autocostrefbandwidth" title="AutoCostRefBandwidth">AutoCostRefBandwidth</a>" : <i>Double</i>,
        "<a href="#bfd" title="Bfd">Bfd</a>" : <i>String</i>,
        "<a href="#databaseoverflow" title="DatabaseOverflow">DatabaseOverflow</a>" : <i>String</i>,
        "<a href="#databaseoverflowmaxlsas" title="DatabaseOverflowMaxLsas">DatabaseOverflowMaxLsas</a>" : <i>Double</i>,
        "<a href="#databaseoverflowtimetorecover" title="DatabaseOverflowTimeToRecover">DatabaseOverflowTimeToRecover</a>" : <i>Double</i>,
        "<a href="#defaultinformationmetric" title="DefaultInformationMetric">DefaultInformationMetric</a>" : <i>Double</i>,
        "<a href="#defaultinformationmetrictype" title="DefaultInformationMetricType">DefaultInformationMetricType</a>" : <i>String</i>,
        "<a href="#defaultinformationoriginate" title="DefaultInformationOriginate">DefaultInformationOriginate</a>" : <i>String</i>,
        "<a href="#defaultinformationroutemap" title="DefaultInformationRouteMap">DefaultInformationRouteMap</a>" : <i>String</i>,
        "<a href="#defaultmetric" title="DefaultMetric">DefaultMetric</a>" : <i>Double</i>,
        "<a href="#distance" title="Distance">Distance</a>" : <i>Double</i>,
        "<a href="#distanceexternal" title="DistanceExternal">DistanceExternal</a>" : <i>Double</i>,
        "<a href="#distanceinterarea" title="DistanceInterArea">DistanceInterArea</a>" : <i>Double</i>,
        "<a href="#distanceintraarea" title="DistanceIntraArea">DistanceIntraArea</a>" : <i>Double</i>,
        "<a href="#distributelistin" title="DistributeListIn">DistributeListIn</a>" : <i>String</i>,
        "<a href="#distributeroutemapin" title="DistributeRouteMapIn">DistributeRouteMapIn</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#logneighbourchanges" title="LogNeighbourChanges">LogNeighbourChanges</a>" : <i>String</i>,
        "<a href="#restartmode" title="RestartMode">RestartMode</a>" : <i>String</i>,
        "<a href="#restartperiod" title="RestartPeriod">RestartPeriod</a>" : <i>Double</i>,
        "<a href="#rfc1583compatible" title="Rfc1583Compatible">Rfc1583Compatible</a>" : <i>String</i>,
        "<a href="#routerid" title="RouterId">RouterId</a>" : <i>String</i>,
        "<a href="#spftimers" title="SpfTimers">SpfTimers</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#area" title="Area">Area</a>" : <i>[ <a href="areadefinition.md">AreaDefinition</a>, ... ]</i>,
        "<a href="#distributelist" title="DistributeList">DistributeList</a>" : <i>[ <a href="distributelistdefinition.md">DistributeListDefinition</a>, ... ]</i>,
        "<a href="#neighbor" title="Neighbor">Neighbor</a>" : <i>[ <a href="neighbordefinition.md">NeighborDefinition</a>, ... ]</i>,
        "<a href="#network" title="Network">Network</a>" : <i>[ <a href="networkdefinition.md">NetworkDefinition</a>, ... ]</i>,
        "<a href="#ospfinterface" title="OspfInterface">OspfInterface</a>" : <i>[ <a href="ospfinterfacedefinition.md">OspfInterfaceDefinition</a>, ... ]</i>,
        "<a href="#passiveinterface" title="PassiveInterface">PassiveInterface</a>" : <i>[ <a href="passiveinterfacedefinition.md">PassiveInterfaceDefinition</a>, ... ]</i>,
        "<a href="#redistribute" title="Redistribute">Redistribute</a>" : <i>[ <a href="redistributedefinition.md">RedistributeDefinition</a>, ... ]</i>,
        "<a href="#summaryaddress" title="SummaryAddress">SummaryAddress</a>" : <i>[ <a href="summaryaddressdefinition.md">SummaryAddressDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::RouterOspf
Properties:
    <a href="#abrtype" title="AbrType">AbrType</a>: <i>String</i>
    <a href="#autocostrefbandwidth" title="AutoCostRefBandwidth">AutoCostRefBandwidth</a>: <i>Double</i>
    <a href="#bfd" title="Bfd">Bfd</a>: <i>String</i>
    <a href="#databaseoverflow" title="DatabaseOverflow">DatabaseOverflow</a>: <i>String</i>
    <a href="#databaseoverflowmaxlsas" title="DatabaseOverflowMaxLsas">DatabaseOverflowMaxLsas</a>: <i>Double</i>
    <a href="#databaseoverflowtimetorecover" title="DatabaseOverflowTimeToRecover">DatabaseOverflowTimeToRecover</a>: <i>Double</i>
    <a href="#defaultinformationmetric" title="DefaultInformationMetric">DefaultInformationMetric</a>: <i>Double</i>
    <a href="#defaultinformationmetrictype" title="DefaultInformationMetricType">DefaultInformationMetricType</a>: <i>String</i>
    <a href="#defaultinformationoriginate" title="DefaultInformationOriginate">DefaultInformationOriginate</a>: <i>String</i>
    <a href="#defaultinformationroutemap" title="DefaultInformationRouteMap">DefaultInformationRouteMap</a>: <i>String</i>
    <a href="#defaultmetric" title="DefaultMetric">DefaultMetric</a>: <i>Double</i>
    <a href="#distance" title="Distance">Distance</a>: <i>Double</i>
    <a href="#distanceexternal" title="DistanceExternal">DistanceExternal</a>: <i>Double</i>
    <a href="#distanceinterarea" title="DistanceInterArea">DistanceInterArea</a>: <i>Double</i>
    <a href="#distanceintraarea" title="DistanceIntraArea">DistanceIntraArea</a>: <i>Double</i>
    <a href="#distributelistin" title="DistributeListIn">DistributeListIn</a>: <i>String</i>
    <a href="#distributeroutemapin" title="DistributeRouteMapIn">DistributeRouteMapIn</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#logneighbourchanges" title="LogNeighbourChanges">LogNeighbourChanges</a>: <i>String</i>
    <a href="#restartmode" title="RestartMode">RestartMode</a>: <i>String</i>
    <a href="#restartperiod" title="RestartPeriod">RestartPeriod</a>: <i>Double</i>
    <a href="#rfc1583compatible" title="Rfc1583Compatible">Rfc1583Compatible</a>: <i>String</i>
    <a href="#routerid" title="RouterId">RouterId</a>: <i>String</i>
    <a href="#spftimers" title="SpfTimers">SpfTimers</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#area" title="Area">Area</a>: <i>
      - <a href="areadefinition.md">AreaDefinition</a></i>
    <a href="#distributelist" title="DistributeList">DistributeList</a>: <i>
      - <a href="distributelistdefinition.md">DistributeListDefinition</a></i>
    <a href="#neighbor" title="Neighbor">Neighbor</a>: <i>
      - <a href="neighbordefinition.md">NeighborDefinition</a></i>
    <a href="#network" title="Network">Network</a>: <i>
      - <a href="networkdefinition.md">NetworkDefinition</a></i>
    <a href="#ospfinterface" title="OspfInterface">OspfInterface</a>: <i>
      - <a href="ospfinterfacedefinition.md">OspfInterfaceDefinition</a></i>
    <a href="#passiveinterface" title="PassiveInterface">PassiveInterface</a>: <i>
      - <a href="passiveinterfacedefinition.md">PassiveInterfaceDefinition</a></i>
    <a href="#redistribute" title="Redistribute">Redistribute</a>: <i>
      - <a href="redistributedefinition.md">RedistributeDefinition</a></i>
    <a href="#summaryaddress" title="SummaryAddress">SummaryAddress</a>: <i>
      - <a href="summaryaddressdefinition.md">SummaryAddressDefinition</a></i>
</pre>

## Properties

#### AbrType

Area border router type. Valid values: `cisco`, `ibm`, `shortcut`, `standard`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoCostRefBandwidth

Reference bandwidth in terms of megabits per second.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bfd

Bidirectional Forwarding Detection (BFD). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseOverflow

Enable/disable database overflow. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseOverflowMaxLsas

Database overflow maximum LSAs.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseOverflowTimeToRecover

Database overflow time to recover (sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultInformationMetric

Default information metric.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultInformationMetricType

Default information metric type. Valid values: `1`, `2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultInformationOriginate

Enable/disable generation of default route. Valid values: `enable`, `always`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultInformationRouteMap

Default information route map.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultMetric

Default metric of redistribute routes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Distance

Distance of the route.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistanceExternal

Administrative external distance.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistanceInterArea

Administrative inter-area distance.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistanceIntraArea

Administrative intra-area distance.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributeListIn

Filter incoming routes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributeRouteMapIn

Filter incoming external routes by route-map.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogNeighbourChanges

Enable logging of OSPF neighbour's changes Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestartMode

OSPF restart mode (graceful or LLS). Valid values: `none`, `lls`, `graceful-restart`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestartPeriod

Graceful restart period.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rfc1583Compatible

Enable/disable RFC1583 compatibility. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouterId

Router ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpfTimers

SPF calculation frequency.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Area

_Required_: No

_Type_: List of <a href="areadefinition.md">AreaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributeList

_Required_: No

_Type_: List of <a href="distributelistdefinition.md">DistributeListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Neighbor

_Required_: No

_Type_: List of <a href="neighbordefinition.md">NeighborDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: List of <a href="networkdefinition.md">NetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfInterface

_Required_: No

_Type_: List of <a href="ospfinterfacedefinition.md">OspfInterfaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PassiveInterface

_Required_: No

_Type_: List of <a href="passiveinterfacedefinition.md">PassiveInterfaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redistribute

_Required_: No

_Type_: List of <a href="redistributedefinition.md">RedistributeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SummaryAddress

_Required_: No

_Type_: List of <a href="summaryaddressdefinition.md">SummaryAddressDefinition</a>

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

