# TF::FortiOS::RouterOspf6

Configure IPv6 OSPF.

~> The provider supports the definition of Ospf6-Interface in Router Ospf6 `fortios_router_ospf6`, and also allows the definition of separate Ospf6-Interface resources `fortios_routerospf6_ospf6interface`, but do not use a `fortios_router_ospf6` with in-line Ospf6-Interface in conjunction with any `fortios_routerospf6_ospf6interface` resources, otherwise conflicts and overwrite will occur.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::RouterOspf6",
    "Properties" : {
        "<a href="#abrtype" title="AbrType">AbrType</a>" : <i>String</i>,
        "<a href="#autocostrefbandwidth" title="AutoCostRefBandwidth">AutoCostRefBandwidth</a>" : <i>Double</i>,
        "<a href="#bfd" title="Bfd">Bfd</a>" : <i>String</i>,
        "<a href="#defaultinformationmetric" title="DefaultInformationMetric">DefaultInformationMetric</a>" : <i>Double</i>,
        "<a href="#defaultinformationmetrictype" title="DefaultInformationMetricType">DefaultInformationMetricType</a>" : <i>String</i>,
        "<a href="#defaultinformationoriginate" title="DefaultInformationOriginate">DefaultInformationOriginate</a>" : <i>String</i>,
        "<a href="#defaultinformationroutemap" title="DefaultInformationRouteMap">DefaultInformationRouteMap</a>" : <i>String</i>,
        "<a href="#defaultmetric" title="DefaultMetric">DefaultMetric</a>" : <i>Double</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#logneighbourchanges" title="LogNeighbourChanges">LogNeighbourChanges</a>" : <i>String</i>,
        "<a href="#routerid" title="RouterId">RouterId</a>" : <i>String</i>,
        "<a href="#spftimers" title="SpfTimers">SpfTimers</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#area" title="Area">Area</a>" : <i>[ <a href="areadefinition.md">AreaDefinition</a>, ... ]</i>,
        "<a href="#ospf6interface" title="Ospf6Interface">Ospf6Interface</a>" : <i>[ <a href="ospf6interfacedefinition.md">Ospf6InterfaceDefinition</a>, ... ]</i>,
        "<a href="#passiveinterface" title="PassiveInterface">PassiveInterface</a>" : <i>[ <a href="passiveinterfacedefinition.md">PassiveInterfaceDefinition</a>, ... ]</i>,
        "<a href="#redistribute" title="Redistribute">Redistribute</a>" : <i>[ <a href="redistributedefinition.md">RedistributeDefinition</a>, ... ]</i>,
        "<a href="#summaryaddress" title="SummaryAddress">SummaryAddress</a>" : <i>[ <a href="summaryaddressdefinition.md">SummaryAddressDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::RouterOspf6
Properties:
    <a href="#abrtype" title="AbrType">AbrType</a>: <i>String</i>
    <a href="#autocostrefbandwidth" title="AutoCostRefBandwidth">AutoCostRefBandwidth</a>: <i>Double</i>
    <a href="#bfd" title="Bfd">Bfd</a>: <i>String</i>
    <a href="#defaultinformationmetric" title="DefaultInformationMetric">DefaultInformationMetric</a>: <i>Double</i>
    <a href="#defaultinformationmetrictype" title="DefaultInformationMetricType">DefaultInformationMetricType</a>: <i>String</i>
    <a href="#defaultinformationoriginate" title="DefaultInformationOriginate">DefaultInformationOriginate</a>: <i>String</i>
    <a href="#defaultinformationroutemap" title="DefaultInformationRouteMap">DefaultInformationRouteMap</a>: <i>String</i>
    <a href="#defaultmetric" title="DefaultMetric">DefaultMetric</a>: <i>Double</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#logneighbourchanges" title="LogNeighbourChanges">LogNeighbourChanges</a>: <i>String</i>
    <a href="#routerid" title="RouterId">RouterId</a>: <i>String</i>
    <a href="#spftimers" title="SpfTimers">SpfTimers</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#area" title="Area">Area</a>: <i>
      - <a href="areadefinition.md">AreaDefinition</a></i>
    <a href="#ospf6interface" title="Ospf6Interface">Ospf6Interface</a>: <i>
      - <a href="ospf6interfacedefinition.md">Ospf6InterfaceDefinition</a></i>
    <a href="#passiveinterface" title="PassiveInterface">PassiveInterface</a>: <i>
      - <a href="passiveinterfacedefinition.md">PassiveInterfaceDefinition</a></i>
    <a href="#redistribute" title="Redistribute">Redistribute</a>: <i>
      - <a href="redistributedefinition.md">RedistributeDefinition</a></i>
    <a href="#summaryaddress" title="SummaryAddress">SummaryAddress</a>: <i>
      - <a href="summaryaddressdefinition.md">SummaryAddressDefinition</a></i>
</pre>

## Properties

#### AbrType

Area border router type. Valid values: `cisco`, `ibm`, `standard`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoCostRefBandwidth

Reference bandwidth in terms of megabits per second.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bfd

Enable/disable Bidirectional Forwarding Detection (BFD). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

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

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogNeighbourChanges

Enable logging of OSPFv3 neighbour's changes Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouterId

A.B.C.D, in IPv4 address format.

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

#### Ospf6Interface

_Required_: No

_Type_: List of <a href="ospf6interfacedefinition.md">Ospf6InterfaceDefinition</a>

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

