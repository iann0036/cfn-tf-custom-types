# TF::Thunder::RouterOspf RedistributeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipnat" title="IpNat">IpNat</a>" : <i>Double</i>,
    "<a href="#metricipnat" title="MetricIpNat">MetricIpNat</a>" : <i>Double</i>,
    "<a href="#metrictypeipnat" title="MetricTypeIpNat">MetricTypeIpNat</a>" : <i>String</i>,
    "<a href="#routemapipnat" title="RouteMapIpNat">RouteMapIpNat</a>" : <i>String</i>,
    "<a href="#tagipnat" title="TagIpNat">TagIpNat</a>" : <i>Double</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#ipnatfloatinglist" title="IpNatFloatingList">IpNatFloatingList</a>" : <i>[ <a href="ipnatfloatinglistdefinition.md">IpNatFloatingListDefinition</a>, ... ]</i>,
    "<a href="#ospflist" title="OspfList">OspfList</a>" : <i>[ <a href="ospflistdefinition.md">OspfListDefinition</a>, ... ]</i>,
    "<a href="#redistlist" title="RedistList">RedistList</a>" : <i>[ <a href="redistlistdefinition.md">RedistListDefinition</a>, ... ]</i>,
    "<a href="#vipfloatinglist" title="VipFloatingList">VipFloatingList</a>" : <i>[ <a href="vipfloatinglistdefinition.md">VipFloatingListDefinition</a>, ... ]</i>,
    "<a href="#viplist" title="VipList">VipList</a>" : <i>[ <a href="viplistdefinition.md">VipListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ipnat" title="IpNat">IpNat</a>: <i>Double</i>
<a href="#metricipnat" title="MetricIpNat">MetricIpNat</a>: <i>Double</i>
<a href="#metrictypeipnat" title="MetricTypeIpNat">MetricTypeIpNat</a>: <i>String</i>
<a href="#routemapipnat" title="RouteMapIpNat">RouteMapIpNat</a>: <i>String</i>
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

#### RouteMapIpNat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagIpNat

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

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

