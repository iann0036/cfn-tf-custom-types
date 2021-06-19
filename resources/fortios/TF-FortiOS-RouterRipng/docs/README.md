# TF::FortiOS::RouterRipng

Configure RIPng.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::RouterRipng",
    "Properties" : {
        "<a href="#defaultinformationoriginate" title="DefaultInformationOriginate">DefaultInformationOriginate</a>" : <i>String</i>,
        "<a href="#defaultmetric" title="DefaultMetric">DefaultMetric</a>" : <i>Double</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#garbagetimer" title="GarbageTimer">GarbageTimer</a>" : <i>Double</i>,
        "<a href="#maxoutmetric" title="MaxOutMetric">MaxOutMetric</a>" : <i>Double</i>,
        "<a href="#timeouttimer" title="TimeoutTimer">TimeoutTimer</a>" : <i>Double</i>,
        "<a href="#updatetimer" title="UpdateTimer">UpdateTimer</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#aggregateaddress" title="AggregateAddress">AggregateAddress</a>" : <i>[ <a href="aggregateaddressdefinition.md">AggregateAddressDefinition</a>, ... ]</i>,
        "<a href="#distance" title="Distance">Distance</a>" : <i>[ <a href="distancedefinition.md">DistanceDefinition</a>, ... ]</i>,
        "<a href="#distributelist" title="DistributeList">DistributeList</a>" : <i>[ <a href="distributelistdefinition.md">DistributeListDefinition</a>, ... ]</i>,
        "<a href="#interface" title="Interface">Interface</a>" : <i>[ <a href="interfacedefinition.md">InterfaceDefinition</a>, ... ]</i>,
        "<a href="#neighbor" title="Neighbor">Neighbor</a>" : <i>[ <a href="neighbordefinition.md">NeighborDefinition</a>, ... ]</i>,
        "<a href="#network" title="Network">Network</a>" : <i>[ <a href="networkdefinition.md">NetworkDefinition</a>, ... ]</i>,
        "<a href="#offsetlist" title="OffsetList">OffsetList</a>" : <i>[ <a href="offsetlistdefinition.md">OffsetListDefinition</a>, ... ]</i>,
        "<a href="#passiveinterface" title="PassiveInterface">PassiveInterface</a>" : <i>[ <a href="passiveinterfacedefinition.md">PassiveInterfaceDefinition</a>, ... ]</i>,
        "<a href="#redistribute" title="Redistribute">Redistribute</a>" : <i>[ <a href="redistributedefinition.md">RedistributeDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::RouterRipng
Properties:
    <a href="#defaultinformationoriginate" title="DefaultInformationOriginate">DefaultInformationOriginate</a>: <i>String</i>
    <a href="#defaultmetric" title="DefaultMetric">DefaultMetric</a>: <i>Double</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#garbagetimer" title="GarbageTimer">GarbageTimer</a>: <i>Double</i>
    <a href="#maxoutmetric" title="MaxOutMetric">MaxOutMetric</a>: <i>Double</i>
    <a href="#timeouttimer" title="TimeoutTimer">TimeoutTimer</a>: <i>Double</i>
    <a href="#updatetimer" title="UpdateTimer">UpdateTimer</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#aggregateaddress" title="AggregateAddress">AggregateAddress</a>: <i>
      - <a href="aggregateaddressdefinition.md">AggregateAddressDefinition</a></i>
    <a href="#distance" title="Distance">Distance</a>: <i>
      - <a href="distancedefinition.md">DistanceDefinition</a></i>
    <a href="#distributelist" title="DistributeList">DistributeList</a>: <i>
      - <a href="distributelistdefinition.md">DistributeListDefinition</a></i>
    <a href="#interface" title="Interface">Interface</a>: <i>
      - <a href="interfacedefinition.md">InterfaceDefinition</a></i>
    <a href="#neighbor" title="Neighbor">Neighbor</a>: <i>
      - <a href="neighbordefinition.md">NeighborDefinition</a></i>
    <a href="#network" title="Network">Network</a>: <i>
      - <a href="networkdefinition.md">NetworkDefinition</a></i>
    <a href="#offsetlist" title="OffsetList">OffsetList</a>: <i>
      - <a href="offsetlistdefinition.md">OffsetListDefinition</a></i>
    <a href="#passiveinterface" title="PassiveInterface">PassiveInterface</a>: <i>
      - <a href="passiveinterfacedefinition.md">PassiveInterfaceDefinition</a></i>
    <a href="#redistribute" title="Redistribute">Redistribute</a>: <i>
      - <a href="redistributedefinition.md">RedistributeDefinition</a></i>
</pre>

## Properties

#### DefaultInformationOriginate

Enable/disable generation of default route. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultMetric

Default metric.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GarbageTimer

Garbage timer.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxOutMetric

Maximum metric allowed to output(0 means 'not set').

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutTimer

Timeout timer.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateTimer

Update timer.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AggregateAddress

_Required_: No

_Type_: List of <a href="aggregateaddressdefinition.md">AggregateAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Distance

_Required_: No

_Type_: List of <a href="distancedefinition.md">DistanceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributeList

_Required_: No

_Type_: List of <a href="distributelistdefinition.md">DistributeListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

_Required_: No

_Type_: List of <a href="interfacedefinition.md">InterfaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Neighbor

_Required_: No

_Type_: List of <a href="neighbordefinition.md">NeighborDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: List of <a href="networkdefinition.md">NetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OffsetList

_Required_: No

_Type_: List of <a href="offsetlistdefinition.md">OffsetListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PassiveInterface

_Required_: No

_Type_: List of <a href="passiveinterfacedefinition.md">PassiveInterfaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redistribute

_Required_: No

_Type_: List of <a href="redistributedefinition.md">RedistributeDefinition</a>

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

