# TF::Volterra::NetworkPolicy EgressRulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#alltcptraffic" title="AllTcpTraffic">AllTcpTraffic</a>" : <i>Boolean</i>,
    "<a href="#alltraffic" title="AllTraffic">AllTraffic</a>" : <i>Boolean</i>,
    "<a href="#alludptraffic" title="AllUdpTraffic">AllUdpTraffic</a>" : <i>Boolean</i>,
    "<a href="#any" title="Any">Any</a>" : <i>Boolean</i>,
    "<a href="#insideendpoints" title="InsideEndpoints">InsideEndpoints</a>" : <i>Boolean</i>,
    "<a href="#keys" title="Keys">Keys</a>" : <i>[ String, ... ]</i>,
    "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
    "<a href="#outsideendpoints" title="OutsideEndpoints">OutsideEndpoints</a>" : <i>Boolean</i>,
    "<a href="#ruledescription" title="RuleDescription">RuleDescription</a>" : <i>String</i>,
    "<a href="#rulename" title="RuleName">RuleName</a>" : <i>String</i>,
    "<a href="#advaction" title="AdvAction">AdvAction</a>" : <i>[ <a href="advactiondefinition.md">AdvActionDefinition</a>, ... ]</i>,
    "<a href="#applications" title="Applications">Applications</a>" : <i>[ <a href="applicationsdefinition.md">ApplicationsDefinition</a>, ... ]</i>,
    "<a href="#ipprefixset" title="IpPrefixSet">IpPrefixSet</a>" : <i>[ <a href="ipprefixsetdefinition.md">IpPrefixSetDefinition</a>, ... ]</i>,
    "<a href="#labelmatcher" title="LabelMatcher">LabelMatcher</a>" : <i>[ <a href="labelmatcherdefinition.md">LabelMatcherDefinition</a>, ... ]</i>,
    "<a href="#labelselector" title="LabelSelector">LabelSelector</a>" : <i>[ <a href="labelselectordefinition.md">LabelSelectorDefinition</a>, ... ]</i>,
    "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>,
    "<a href="#prefixlist" title="PrefixList">PrefixList</a>" : <i>[ <a href="prefixlistdefinition.md">PrefixListDefinition</a>, ... ]</i>,
    "<a href="#protocolportrange" title="ProtocolPortRange">ProtocolPortRange</a>" : <i>[ <a href="protocolportrangedefinition.md">ProtocolPortRangeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#alltcptraffic" title="AllTcpTraffic">AllTcpTraffic</a>: <i>Boolean</i>
<a href="#alltraffic" title="AllTraffic">AllTraffic</a>: <i>Boolean</i>
<a href="#alludptraffic" title="AllUdpTraffic">AllUdpTraffic</a>: <i>Boolean</i>
<a href="#any" title="Any">Any</a>: <i>Boolean</i>
<a href="#insideendpoints" title="InsideEndpoints">InsideEndpoints</a>: <i>Boolean</i>
<a href="#keys" title="Keys">Keys</a>: <i>
      - String</i>
<a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
<a href="#outsideendpoints" title="OutsideEndpoints">OutsideEndpoints</a>: <i>Boolean</i>
<a href="#ruledescription" title="RuleDescription">RuleDescription</a>: <i>String</i>
<a href="#rulename" title="RuleName">RuleName</a>: <i>String</i>
<a href="#advaction" title="AdvAction">AdvAction</a>: <i>
      - <a href="advactiondefinition.md">AdvActionDefinition</a></i>
<a href="#applications" title="Applications">Applications</a>: <i>
      - <a href="applicationsdefinition.md">ApplicationsDefinition</a></i>
<a href="#ipprefixset" title="IpPrefixSet">IpPrefixSet</a>: <i>
      - <a href="ipprefixsetdefinition.md">IpPrefixSetDefinition</a></i>
<a href="#labelmatcher" title="LabelMatcher">LabelMatcher</a>: <i>
      - <a href="labelmatcherdefinition.md">LabelMatcherDefinition</a></i>
<a href="#labelselector" title="LabelSelector">LabelSelector</a>: <i>
      - <a href="labelselectordefinition.md">LabelSelectorDefinition</a></i>
<a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
<a href="#prefixlist" title="PrefixList">PrefixList</a>: <i>
      - <a href="prefixlistdefinition.md">PrefixListDefinition</a></i>
<a href="#protocolportrange" title="ProtocolPortRange">ProtocolPortRange</a>: <i>
      - <a href="protocolportrangedefinition.md">ProtocolPortRangeDefinition</a></i>
</pre>

## Properties

#### Action

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllTcpTraffic

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllTraffic

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllUdpTraffic

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Any

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsideEndpoints

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Keys

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutsideEndpoints

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleDescription

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvAction

_Required_: No

_Type_: List of <a href="advactiondefinition.md">AdvActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Applications

_Required_: No

_Type_: List of <a href="applicationsdefinition.md">ApplicationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpPrefixSet

_Required_: No

_Type_: List of <a href="ipprefixsetdefinition.md">IpPrefixSetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LabelMatcher

_Required_: No

_Type_: List of <a href="labelmatcherdefinition.md">LabelMatcherDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LabelSelector

_Required_: No

_Type_: List of <a href="labelselectordefinition.md">LabelSelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixList

_Required_: No

_Type_: List of <a href="prefixlistdefinition.md">PrefixListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolPortRange

_Required_: No

_Type_: List of <a href="protocolportrangedefinition.md">ProtocolPortRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

