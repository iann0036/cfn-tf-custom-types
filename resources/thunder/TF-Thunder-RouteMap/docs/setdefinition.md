# TF::Thunder::RouteMap SetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#atomicaggregate" title="AtomicAggregate">AtomicAggregate</a>" : <i>Double</i>,
    "<a href="#community" title="Community">Community</a>" : <i>[ <a href="communitydefinition.md">CommunityDefinition</a>, ... ]</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#aggregator" title="Aggregator">Aggregator</a>" : <i>[ <a href="aggregatordefinition.md">AggregatorDefinition</a>, ... ]</i>,
    "<a href="#aspath" title="AsPath">AsPath</a>" : <i>[ <a href="aspathdefinition.md">AsPathDefinition</a>, ... ]</i>,
    "<a href="#commlist" title="CommList">CommList</a>" : <i>[ <a href="commlistdefinition.md">CommListDefinition</a>, ... ]</i>,
    "<a href="#dampeningcfg" title="DampeningCfg">DampeningCfg</a>" : <i>[ <a href="dampeningcfgdefinition.md">DampeningCfgDefinition</a>, ... ]</i>,
    "<a href="#ddos" title="Ddos">Ddos</a>" : <i>[ <a href="ddosdefinition.md">DdosDefinition</a>, ... ]</i>,
    "<a href="#extcommunity" title="Extcommunity">Extcommunity</a>" : <i>[ <a href="extcommunitydefinition.md">ExtcommunityDefinition</a>, ... ]</i>,
    "<a href="#ip" title="Ip">Ip</a>" : <i>[ <a href="ipdefinition.md">IpDefinition</a>, ... ]</i>,
    "<a href="#ipv6" title="Ipv6">Ipv6</a>" : <i>[ <a href="ipv6definition.md">Ipv6Definition</a>, ... ]</i>,
    "<a href="#level" title="Level">Level</a>" : <i>[ <a href="leveldefinition.md">LevelDefinition</a>, ... ]</i>,
    "<a href="#localpreference" title="LocalPreference">LocalPreference</a>" : <i>[ <a href="localpreferencedefinition.md">LocalPreferenceDefinition</a>, ... ]</i>,
    "<a href="#metric" title="Metric">Metric</a>" : <i>[ <a href="metricdefinition.md">MetricDefinition</a>, ... ]</i>,
    "<a href="#metrictype" title="MetricType">MetricType</a>" : <i>[ <a href="metrictypedefinition.md">MetricTypeDefinition</a>, ... ]</i>,
    "<a href="#origin" title="Origin">Origin</a>" : <i>[ <a href="origindefinition.md">OriginDefinition</a>, ... ]</i>,
    "<a href="#originatorid" title="OriginatorId">OriginatorId</a>" : <i>[ <a href="originatoriddefinition.md">OriginatorIdDefinition</a>, ... ]</i>,
    "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>,
    "<a href="#weight" title="Weight">Weight</a>" : <i>[ <a href="weightdefinition.md">WeightDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#atomicaggregate" title="AtomicAggregate">AtomicAggregate</a>: <i>Double</i>
<a href="#community" title="Community">Community</a>: <i>
      - <a href="communitydefinition.md">CommunityDefinition</a></i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#aggregator" title="Aggregator">Aggregator</a>: <i>
      - <a href="aggregatordefinition.md">AggregatorDefinition</a></i>
<a href="#aspath" title="AsPath">AsPath</a>: <i>
      - <a href="aspathdefinition.md">AsPathDefinition</a></i>
<a href="#commlist" title="CommList">CommList</a>: <i>
      - <a href="commlistdefinition.md">CommListDefinition</a></i>
<a href="#dampeningcfg" title="DampeningCfg">DampeningCfg</a>: <i>
      - <a href="dampeningcfgdefinition.md">DampeningCfgDefinition</a></i>
<a href="#ddos" title="Ddos">Ddos</a>: <i>
      - <a href="ddosdefinition.md">DdosDefinition</a></i>
<a href="#extcommunity" title="Extcommunity">Extcommunity</a>: <i>
      - <a href="extcommunitydefinition.md">ExtcommunityDefinition</a></i>
<a href="#ip" title="Ip">Ip</a>: <i>
      - <a href="ipdefinition.md">IpDefinition</a></i>
<a href="#ipv6" title="Ipv6">Ipv6</a>: <i>
      - <a href="ipv6definition.md">Ipv6Definition</a></i>
<a href="#level" title="Level">Level</a>: <i>
      - <a href="leveldefinition.md">LevelDefinition</a></i>
<a href="#localpreference" title="LocalPreference">LocalPreference</a>: <i>
      - <a href="localpreferencedefinition.md">LocalPreferenceDefinition</a></i>
<a href="#metric" title="Metric">Metric</a>: <i>
      - <a href="metricdefinition.md">MetricDefinition</a></i>
<a href="#metrictype" title="MetricType">MetricType</a>: <i>
      - <a href="metrictypedefinition.md">MetricTypeDefinition</a></i>
<a href="#origin" title="Origin">Origin</a>: <i>
      - <a href="origindefinition.md">OriginDefinition</a></i>
<a href="#originatorid" title="OriginatorId">OriginatorId</a>: <i>
      - <a href="originatoriddefinition.md">OriginatorIdDefinition</a></i>
<a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
<a href="#weight" title="Weight">Weight</a>: <i>
      - <a href="weightdefinition.md">WeightDefinition</a></i>
</pre>

## Properties

#### AtomicAggregate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Community

_Required_: No

_Type_: List of <a href="communitydefinition.md">CommunityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Aggregator

_Required_: No

_Type_: List of <a href="aggregatordefinition.md">AggregatorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsPath

_Required_: No

_Type_: List of <a href="aspathdefinition.md">AsPathDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommList

_Required_: No

_Type_: List of <a href="commlistdefinition.md">CommListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DampeningCfg

_Required_: No

_Type_: List of <a href="dampeningcfgdefinition.md">DampeningCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ddos

_Required_: No

_Type_: List of <a href="ddosdefinition.md">DdosDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Extcommunity

_Required_: No

_Type_: List of <a href="extcommunitydefinition.md">ExtcommunityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

_Required_: No

_Type_: List of <a href="ipdefinition.md">IpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6

_Required_: No

_Type_: List of <a href="ipv6definition.md">Ipv6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Level

_Required_: No

_Type_: List of <a href="leveldefinition.md">LevelDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalPreference

_Required_: No

_Type_: List of <a href="localpreferencedefinition.md">LocalPreferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: No

_Type_: List of <a href="metricdefinition.md">MetricDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricType

_Required_: No

_Type_: List of <a href="metrictypedefinition.md">MetricTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Origin

_Required_: No

_Type_: List of <a href="origindefinition.md">OriginDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginatorId

_Required_: No

_Type_: List of <a href="originatoriddefinition.md">OriginatorIdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

_Required_: No

_Type_: List of <a href="weightdefinition.md">WeightDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

