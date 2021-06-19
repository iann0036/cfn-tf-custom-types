# TF::Thunder::RouteMap MatchDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#aspath" title="AsPath">AsPath</a>" : <i>[ <a href="aspathdefinition.md">AsPathDefinition</a>, ... ]</i>,
    "<a href="#community" title="Community">Community</a>" : <i>[ <a href="communitydefinition.md">CommunityDefinition</a>, ... ]</i>,
    "<a href="#extcommunity" title="Extcommunity">Extcommunity</a>" : <i>[ <a href="extcommunitydefinition.md">ExtcommunityDefinition</a>, ... ]</i>,
    "<a href="#group" title="Group">Group</a>" : <i>[ <a href="groupdefinition.md">GroupDefinition</a>, ... ]</i>,
    "<a href="#interface" title="Interface">Interface</a>" : <i>[ <a href="interfacedefinition.md">InterfaceDefinition</a>, ... ]</i>,
    "<a href="#ip" title="Ip">Ip</a>" : <i>[ <a href="ipdefinition.md">IpDefinition</a>, ... ]</i>,
    "<a href="#ipv6" title="Ipv6">Ipv6</a>" : <i>[ <a href="ipv6definition.md">Ipv6Definition</a>, ... ]</i>,
    "<a href="#localpreference" title="LocalPreference">LocalPreference</a>" : <i>[ <a href="localpreferencedefinition.md">LocalPreferenceDefinition</a>, ... ]</i>,
    "<a href="#metric" title="Metric">Metric</a>" : <i>[ <a href="metricdefinition.md">MetricDefinition</a>, ... ]</i>,
    "<a href="#origin" title="Origin">Origin</a>" : <i>[ <a href="origindefinition.md">OriginDefinition</a>, ... ]</i>,
    "<a href="#routetype" title="RouteType">RouteType</a>" : <i>[ <a href="routetypedefinition.md">RouteTypeDefinition</a>, ... ]</i>,
    "<a href="#scaleout" title="Scaleout">Scaleout</a>" : <i>[ <a href="scaleoutdefinition.md">ScaleoutDefinition</a>, ... ]</i>,
    "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#aspath" title="AsPath">AsPath</a>: <i>
      - <a href="aspathdefinition.md">AsPathDefinition</a></i>
<a href="#community" title="Community">Community</a>: <i>
      - <a href="communitydefinition.md">CommunityDefinition</a></i>
<a href="#extcommunity" title="Extcommunity">Extcommunity</a>: <i>
      - <a href="extcommunitydefinition.md">ExtcommunityDefinition</a></i>
<a href="#group" title="Group">Group</a>: <i>
      - <a href="groupdefinition.md">GroupDefinition</a></i>
<a href="#interface" title="Interface">Interface</a>: <i>
      - <a href="interfacedefinition.md">InterfaceDefinition</a></i>
<a href="#ip" title="Ip">Ip</a>: <i>
      - <a href="ipdefinition.md">IpDefinition</a></i>
<a href="#ipv6" title="Ipv6">Ipv6</a>: <i>
      - <a href="ipv6definition.md">Ipv6Definition</a></i>
<a href="#localpreference" title="LocalPreference">LocalPreference</a>: <i>
      - <a href="localpreferencedefinition.md">LocalPreferenceDefinition</a></i>
<a href="#metric" title="Metric">Metric</a>: <i>
      - <a href="metricdefinition.md">MetricDefinition</a></i>
<a href="#origin" title="Origin">Origin</a>: <i>
      - <a href="origindefinition.md">OriginDefinition</a></i>
<a href="#routetype" title="RouteType">RouteType</a>: <i>
      - <a href="routetypedefinition.md">RouteTypeDefinition</a></i>
<a href="#scaleout" title="Scaleout">Scaleout</a>: <i>
      - <a href="scaleoutdefinition.md">ScaleoutDefinition</a></i>
<a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsPath

_Required_: No

_Type_: List of <a href="aspathdefinition.md">AsPathDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Community

_Required_: No

_Type_: List of <a href="communitydefinition.md">CommunityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Extcommunity

_Required_: No

_Type_: List of <a href="extcommunitydefinition.md">ExtcommunityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

_Required_: No

_Type_: List of <a href="groupdefinition.md">GroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

_Required_: No

_Type_: List of <a href="interfacedefinition.md">InterfaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

_Required_: No

_Type_: List of <a href="ipdefinition.md">IpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6

_Required_: No

_Type_: List of <a href="ipv6definition.md">Ipv6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalPreference

_Required_: No

_Type_: List of <a href="localpreferencedefinition.md">LocalPreferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: No

_Type_: List of <a href="metricdefinition.md">MetricDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Origin

_Required_: No

_Type_: List of <a href="origindefinition.md">OriginDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteType

_Required_: No

_Type_: List of <a href="routetypedefinition.md">RouteTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scaleout

_Required_: No

_Type_: List of <a href="scaleoutdefinition.md">ScaleoutDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

