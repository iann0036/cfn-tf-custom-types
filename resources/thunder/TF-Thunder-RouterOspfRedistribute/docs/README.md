# TF::Thunder::RouterOspfRedistribute

`thunder_router_ospf_redistribute` Provides details about thunder router ospf redistribute

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::RouterOspfRedistribute",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#asnumber" title="AsNumber">AsNumber</a>" : <i>String</i>,
        "<a href="#ipnat" title="IpNat">IpNat</a>" : <i>Double</i>,
        "<a href="#metricipnat" title="MetricIpNat">MetricIpNat</a>" : <i>Double</i>,
        "<a href="#metrictypeipnat" title="MetricTypeIpNat">MetricTypeIpNat</a>" : <i>String</i>,
        "<a href="#processid" title="ProcessId">ProcessId</a>" : <i>Double</i>,
        "<a href="#routemapipnat" title="RouteMapIpNat">RouteMapIpNat</a>" : <i>String</i>,
        "<a href="#sequence" title="Sequence">Sequence</a>" : <i>String</i>,
        "<a href="#tagipnat" title="TagIpNat">TagIpNat</a>" : <i>Double</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#ipnatfloatinglist" title="IpNatFloatingList">IpNatFloatingList</a>" : <i>[ <a href="ipnatfloatinglistdefinition.md">IpNatFloatingListDefinition</a>, ... ]</i>,
        "<a href="#ospflist" title="OspfList">OspfList</a>" : <i>[ <a href="ospflistdefinition.md">OspfListDefinition</a>, ... ]</i>,
        "<a href="#redistlist" title="RedistList">RedistList</a>" : <i>[ <a href="redistlistdefinition.md">RedistListDefinition</a>, ... ]</i>,
        "<a href="#vipfloatinglist" title="VipFloatingList">VipFloatingList</a>" : <i>[ <a href="vipfloatinglistdefinition.md">VipFloatingListDefinition</a>, ... ]</i>,
        "<a href="#viplist" title="VipList">VipList</a>" : <i>[ <a href="viplistdefinition.md">VipListDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::RouterOspfRedistribute
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#asnumber" title="AsNumber">AsNumber</a>: <i>String</i>
    <a href="#ipnat" title="IpNat">IpNat</a>: <i>Double</i>
    <a href="#metricipnat" title="MetricIpNat">MetricIpNat</a>: <i>Double</i>
    <a href="#metrictypeipnat" title="MetricTypeIpNat">MetricTypeIpNat</a>: <i>String</i>
    <a href="#processid" title="ProcessId">ProcessId</a>: <i>Double</i>
    <a href="#routemapipnat" title="RouteMapIpNat">RouteMapIpNat</a>: <i>String</i>
    <a href="#sequence" title="Sequence">Sequence</a>: <i>String</i>
    <a href="#tagipnat" title="TagIpNat">TagIpNat</a>: <i>Double</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#ipnatfloatinglist" title="IpNatFloatingList">IpNatFloatingList</a>: <i>
      - <a href="ipnatfloatinglistdefinition.md">IpNatFloatingListDefinition</a></i>
    <a href="#ospflist" title="OspfList">OspfList</a>: <i>
      - <a href="ospflistdefinition.md">OspfListDefinition</a></i>
    <a href="#redistlist" title="RedistList">RedistList</a>: <i>
      - <a href="redistlistdefinition.md">RedistListDefinition</a></i>
    <a href="#vipfloatinglist" title="VipFloatingList">VipFloatingList</a>: <i>
      - <a href="vipfloatinglistdefinition.md">VipFloatingListDefinition</a></i>
    <a href="#viplist" title="VipList">VipList</a>: <i>
      - <a href="viplistdefinition.md">VipListDefinition</a></i>
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

#### IpNat

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricIpNat

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricTypeIpNat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteMapIpNat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sequence

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagIpNat

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpNatFloatingList

_Required_: No

_Type_: List of <a href="ipnatfloatinglistdefinition.md">IpNatFloatingListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfList

_Required_: No

_Type_: List of <a href="ospflistdefinition.md">OspfListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedistList

_Required_: No

_Type_: List of <a href="redistlistdefinition.md">RedistListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipFloatingList

_Required_: No

_Type_: List of <a href="vipfloatinglistdefinition.md">VipFloatingListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipList

_Required_: No

_Type_: List of <a href="viplistdefinition.md">VipListDefinition</a>

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

