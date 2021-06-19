# TF::Thunder::RouterOspf

`thunder_router_ospf` Provides details about thunder router ospf

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::RouterOspf",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#asnumber" title="AsNumber">AsNumber</a>" : <i>String</i>,
        "<a href="#autocostreferencebandwidth" title="AutoCostReferenceBandwidth">AutoCostReferenceBandwidth</a>" : <i>Double</i>,
        "<a href="#bfdallinterfaces" title="BfdAllInterfaces">BfdAllInterfaces</a>" : <i>Double</i>,
        "<a href="#defaultmetric" title="DefaultMetric">DefaultMetric</a>" : <i>Double</i>,
        "<a href="#maxconcurrentdd" title="MaxConcurrentDd">MaxConcurrentDd</a>" : <i>Double</i>,
        "<a href="#maximumarea" title="MaximumArea">MaximumArea</a>" : <i>Double</i>,
        "<a href="#processid" title="ProcessId">ProcessId</a>" : <i>Double</i>,
        "<a href="#rfc1583compatible" title="Rfc1583Compatible">Rfc1583Compatible</a>" : <i>Double</i>,
        "<a href="#sequence" title="Sequence">Sequence</a>" : <i>String</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#arealist" title="AreaList">AreaList</a>" : <i>[ <a href="arealistdefinition.md">AreaListDefinition</a>, ... ]</i>,
        "<a href="#defaultinformation" title="DefaultInformation">DefaultInformation</a>" : <i>[ <a href="defaultinformationdefinition.md">DefaultInformationDefinition</a>, ... ]</i>,
        "<a href="#distance" title="Distance">Distance</a>" : <i>[ <a href="distancedefinition.md">DistanceDefinition</a>, ... ]</i>,
        "<a href="#distributeinternallist" title="DistributeInternalList">DistributeInternalList</a>" : <i>[ <a href="distributeinternallistdefinition.md">DistributeInternalListDefinition</a>, ... ]</i>,
        "<a href="#distributelists" title="DistributeLists">DistributeLists</a>" : <i>[ <a href="distributelistsdefinition.md">DistributeListsDefinition</a>, ... ]</i>,
        "<a href="#hastandbyextracost" title="HaStandbyExtraCost">HaStandbyExtraCost</a>" : <i>[ <a href="hastandbyextracostdefinition.md">HaStandbyExtraCostDefinition</a>, ... ]</i>,
        "<a href="#hostlist" title="HostList">HostList</a>" : <i>[ <a href="hostlistdefinition.md">HostListDefinition</a>, ... ]</i>,
        "<a href="#logadjacencychangescfg" title="LogAdjacencyChangesCfg">LogAdjacencyChangesCfg</a>" : <i>[ <a href="logadjacencychangescfgdefinition.md">LogAdjacencyChangesCfgDefinition</a>, ... ]</i>,
        "<a href="#neighborlist" title="NeighborList">NeighborList</a>" : <i>[ <a href="neighborlistdefinition.md">NeighborListDefinition</a>, ... ]</i>,
        "<a href="#networklist" title="NetworkList">NetworkList</a>" : <i>[ <a href="networklistdefinition.md">NetworkListDefinition</a>, ... ]</i>,
        "<a href="#ospf1" title="Ospf1">Ospf1</a>" : <i>[ <a href="ospf1definition.md">Ospf1Definition</a>, ... ]</i>,
        "<a href="#overflow" title="Overflow">Overflow</a>" : <i>[ <a href="overflowdefinition.md">OverflowDefinition</a>, ... ]</i>,
        "<a href="#passiveinterface" title="PassiveInterface">PassiveInterface</a>" : <i>[ <a href="passiveinterfacedefinition.md">PassiveInterfaceDefinition</a>, ... ]</i>,
        "<a href="#redistribute" title="Redistribute">Redistribute</a>" : <i>[ <a href="redistributedefinition.md">RedistributeDefinition</a>, ... ]</i>,
        "<a href="#routerid" title="RouterId">RouterId</a>" : <i>[ <a href="routeriddefinition.md">RouterIdDefinition</a>, ... ]</i>,
        "<a href="#summaryaddresslist" title="SummaryAddressList">SummaryAddressList</a>" : <i>[ <a href="summaryaddresslistdefinition.md">SummaryAddressListDefinition</a>, ... ]</i>,
        "<a href="#timers" title="Timers">Timers</a>" : <i>[ <a href="timersdefinition.md">TimersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::RouterOspf
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#asnumber" title="AsNumber">AsNumber</a>: <i>String</i>
    <a href="#autocostreferencebandwidth" title="AutoCostReferenceBandwidth">AutoCostReferenceBandwidth</a>: <i>Double</i>
    <a href="#bfdallinterfaces" title="BfdAllInterfaces">BfdAllInterfaces</a>: <i>Double</i>
    <a href="#defaultmetric" title="DefaultMetric">DefaultMetric</a>: <i>Double</i>
    <a href="#maxconcurrentdd" title="MaxConcurrentDd">MaxConcurrentDd</a>: <i>Double</i>
    <a href="#maximumarea" title="MaximumArea">MaximumArea</a>: <i>Double</i>
    <a href="#processid" title="ProcessId">ProcessId</a>: <i>Double</i>
    <a href="#rfc1583compatible" title="Rfc1583Compatible">Rfc1583Compatible</a>: <i>Double</i>
    <a href="#sequence" title="Sequence">Sequence</a>: <i>String</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#arealist" title="AreaList">AreaList</a>: <i>
      - <a href="arealistdefinition.md">AreaListDefinition</a></i>
    <a href="#defaultinformation" title="DefaultInformation">DefaultInformation</a>: <i>
      - <a href="defaultinformationdefinition.md">DefaultInformationDefinition</a></i>
    <a href="#distance" title="Distance">Distance</a>: <i>
      - <a href="distancedefinition.md">DistanceDefinition</a></i>
    <a href="#distributeinternallist" title="DistributeInternalList">DistributeInternalList</a>: <i>
      - <a href="distributeinternallistdefinition.md">DistributeInternalListDefinition</a></i>
    <a href="#distributelists" title="DistributeLists">DistributeLists</a>: <i>
      - <a href="distributelistsdefinition.md">DistributeListsDefinition</a></i>
    <a href="#hastandbyextracost" title="HaStandbyExtraCost">HaStandbyExtraCost</a>: <i>
      - <a href="hastandbyextracostdefinition.md">HaStandbyExtraCostDefinition</a></i>
    <a href="#hostlist" title="HostList">HostList</a>: <i>
      - <a href="hostlistdefinition.md">HostListDefinition</a></i>
    <a href="#logadjacencychangescfg" title="LogAdjacencyChangesCfg">LogAdjacencyChangesCfg</a>: <i>
      - <a href="logadjacencychangescfgdefinition.md">LogAdjacencyChangesCfgDefinition</a></i>
    <a href="#neighborlist" title="NeighborList">NeighborList</a>: <i>
      - <a href="neighborlistdefinition.md">NeighborListDefinition</a></i>
    <a href="#networklist" title="NetworkList">NetworkList</a>: <i>
      - <a href="networklistdefinition.md">NetworkListDefinition</a></i>
    <a href="#ospf1" title="Ospf1">Ospf1</a>: <i>
      - <a href="ospf1definition.md">Ospf1Definition</a></i>
    <a href="#overflow" title="Overflow">Overflow</a>: <i>
      - <a href="overflowdefinition.md">OverflowDefinition</a></i>
    <a href="#passiveinterface" title="PassiveInterface">PassiveInterface</a>: <i>
      - <a href="passiveinterfacedefinition.md">PassiveInterfaceDefinition</a></i>
    <a href="#redistribute" title="Redistribute">Redistribute</a>: <i>
      - <a href="redistributedefinition.md">RedistributeDefinition</a></i>
    <a href="#routerid" title="RouterId">RouterId</a>: <i>
      - <a href="routeriddefinition.md">RouterIdDefinition</a></i>
    <a href="#summaryaddresslist" title="SummaryAddressList">SummaryAddressList</a>: <i>
      - <a href="summaryaddresslistdefinition.md">SummaryAddressListDefinition</a></i>
    <a href="#timers" title="Timers">Timers</a>: <i>
      - <a href="timersdefinition.md">TimersDefinition</a></i>
</pre>

## Properties

#### Action

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsNumber

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoCostReferenceBandwidth

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BfdAllInterfaces

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultMetric

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConcurrentDd

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumArea

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rfc1583Compatible

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sequence

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AreaList

_Required_: No

_Type_: List of <a href="arealistdefinition.md">AreaListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultInformation

_Required_: No

_Type_: List of <a href="defaultinformationdefinition.md">DefaultInformationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Distance

_Required_: No

_Type_: List of <a href="distancedefinition.md">DistanceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributeInternalList

_Required_: No

_Type_: List of <a href="distributeinternallistdefinition.md">DistributeInternalListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributeLists

_Required_: No

_Type_: List of <a href="distributelistsdefinition.md">DistributeListsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaStandbyExtraCost

_Required_: No

_Type_: List of <a href="hastandbyextracostdefinition.md">HaStandbyExtraCostDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostList

_Required_: No

_Type_: List of <a href="hostlistdefinition.md">HostListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAdjacencyChangesCfg

_Required_: No

_Type_: List of <a href="logadjacencychangescfgdefinition.md">LogAdjacencyChangesCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NeighborList

_Required_: No

_Type_: List of <a href="neighborlistdefinition.md">NeighborListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkList

_Required_: No

_Type_: List of <a href="networklistdefinition.md">NetworkListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ospf1

_Required_: No

_Type_: List of <a href="ospf1definition.md">Ospf1Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Overflow

_Required_: No

_Type_: List of <a href="overflowdefinition.md">OverflowDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PassiveInterface

_Required_: No

_Type_: List of <a href="passiveinterfacedefinition.md">PassiveInterfaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redistribute

_Required_: No

_Type_: List of <a href="redistributedefinition.md">RedistributeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouterId

_Required_: No

_Type_: List of <a href="routeriddefinition.md">RouterIdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SummaryAddressList

_Required_: No

_Type_: List of <a href="summaryaddresslistdefinition.md">SummaryAddressListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timers

_Required_: No

_Type_: List of <a href="timersdefinition.md">TimersDefinition</a>

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

