# TF::Volterra::ForwardProxyPolicy RulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#alldestinations" title="AllDestinations">AllDestinations</a>" : <i>Boolean</i>,
    "<a href="#allsources" title="AllSources">AllSources</a>" : <i>Boolean</i>,
    "<a href="#insidesources" title="InsideSources">InsideSources</a>" : <i>Boolean</i>,
    "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
    "<a href="#nohttpconnectport" title="NoHttpConnectPort">NoHttpConnectPort</a>" : <i>Boolean</i>,
    "<a href="#ruledescription" title="RuleDescription">RuleDescription</a>" : <i>String</i>,
    "<a href="#rulename" title="RuleName">RuleName</a>" : <i>String</i>,
    "<a href="#dstasnlist" title="DstAsnList">DstAsnList</a>" : <i>[ <a href="dstasnlistdefinition.md">DstAsnListDefinition</a>, ... ]</i>,
    "<a href="#dstasnset" title="DstAsnSet">DstAsnSet</a>" : <i>[ <a href="dstasnsetdefinition.md">DstAsnSetDefinition</a>, ... ]</i>,
    "<a href="#dstipprefixset" title="DstIpPrefixSet">DstIpPrefixSet</a>" : <i>[ <a href="dstipprefixsetdefinition.md">DstIpPrefixSetDefinition</a>, ... ]</i>,
    "<a href="#dstlabelselector" title="DstLabelSelector">DstLabelSelector</a>" : <i>[ <a href="dstlabelselectordefinition.md">DstLabelSelectorDefinition</a>, ... ]</i>,
    "<a href="#dstprefixlist" title="DstPrefixList">DstPrefixList</a>" : <i>[ <a href="dstprefixlistdefinition.md">DstPrefixListDefinition</a>, ... ]</i>,
    "<a href="#httplist" title="HttpList">HttpList</a>" : <i>[ <a href="httplistdefinition.md">HttpListDefinition</a>, ... ]</i>,
    "<a href="#interface" title="Interface">Interface</a>" : <i>[ <a href="interfacedefinition.md">InterfaceDefinition</a>, ... ]</i>,
    "<a href="#ipprefixset" title="IpPrefixSet">IpPrefixSet</a>" : <i>[ <a href="ipprefixsetdefinition.md">IpPrefixSetDefinition</a>, ... ]</i>,
    "<a href="#labelselector" title="LabelSelector">LabelSelector</a>" : <i>[ <a href="labelselectordefinition.md">LabelSelectorDefinition</a>, ... ]</i>,
    "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>,
    "<a href="#portmatcher" title="PortMatcher">PortMatcher</a>" : <i>[ <a href="portmatcherdefinition.md">PortMatcherDefinition</a>, ... ]</i>,
    "<a href="#prefixlist" title="PrefixList">PrefixList</a>" : <i>[ <a href="prefixlistdefinition.md">PrefixListDefinition</a>, ... ]</i>,
    "<a href="#tlslist" title="TlsList">TlsList</a>" : <i>[ <a href="tlslistdefinition.md">TlsListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#alldestinations" title="AllDestinations">AllDestinations</a>: <i>Boolean</i>
<a href="#allsources" title="AllSources">AllSources</a>: <i>Boolean</i>
<a href="#insidesources" title="InsideSources">InsideSources</a>: <i>Boolean</i>
<a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
<a href="#nohttpconnectport" title="NoHttpConnectPort">NoHttpConnectPort</a>: <i>Boolean</i>
<a href="#ruledescription" title="RuleDescription">RuleDescription</a>: <i>String</i>
<a href="#rulename" title="RuleName">RuleName</a>: <i>String</i>
<a href="#dstasnlist" title="DstAsnList">DstAsnList</a>: <i>
      - <a href="dstasnlistdefinition.md">DstAsnListDefinition</a></i>
<a href="#dstasnset" title="DstAsnSet">DstAsnSet</a>: <i>
      - <a href="dstasnsetdefinition.md">DstAsnSetDefinition</a></i>
<a href="#dstipprefixset" title="DstIpPrefixSet">DstIpPrefixSet</a>: <i>
      - <a href="dstipprefixsetdefinition.md">DstIpPrefixSetDefinition</a></i>
<a href="#dstlabelselector" title="DstLabelSelector">DstLabelSelector</a>: <i>
      - <a href="dstlabelselectordefinition.md">DstLabelSelectorDefinition</a></i>
<a href="#dstprefixlist" title="DstPrefixList">DstPrefixList</a>: <i>
      - <a href="dstprefixlistdefinition.md">DstPrefixListDefinition</a></i>
<a href="#httplist" title="HttpList">HttpList</a>: <i>
      - <a href="httplistdefinition.md">HttpListDefinition</a></i>
<a href="#interface" title="Interface">Interface</a>: <i>
      - <a href="interfacedefinition.md">InterfaceDefinition</a></i>
<a href="#ipprefixset" title="IpPrefixSet">IpPrefixSet</a>: <i>
      - <a href="ipprefixsetdefinition.md">IpPrefixSetDefinition</a></i>
<a href="#labelselector" title="LabelSelector">LabelSelector</a>: <i>
      - <a href="labelselectordefinition.md">LabelSelectorDefinition</a></i>
<a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
<a href="#portmatcher" title="PortMatcher">PortMatcher</a>: <i>
      - <a href="portmatcherdefinition.md">PortMatcherDefinition</a></i>
<a href="#prefixlist" title="PrefixList">PrefixList</a>: <i>
      - <a href="prefixlistdefinition.md">PrefixListDefinition</a></i>
<a href="#tlslist" title="TlsList">TlsList</a>: <i>
      - <a href="tlslistdefinition.md">TlsListDefinition</a></i>
</pre>

## Properties

#### Action

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllDestinations

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllSources

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsideSources

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoHttpConnectPort

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

#### DstAsnList

_Required_: No

_Type_: List of <a href="dstasnlistdefinition.md">DstAsnListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstAsnSet

_Required_: No

_Type_: List of <a href="dstasnsetdefinition.md">DstAsnSetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstIpPrefixSet

_Required_: No

_Type_: List of <a href="dstipprefixsetdefinition.md">DstIpPrefixSetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstLabelSelector

_Required_: No

_Type_: List of <a href="dstlabelselectordefinition.md">DstLabelSelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DstPrefixList

_Required_: No

_Type_: List of <a href="dstprefixlistdefinition.md">DstPrefixListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpList

_Required_: No

_Type_: List of <a href="httplistdefinition.md">HttpListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

_Required_: No

_Type_: List of <a href="interfacedefinition.md">InterfaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpPrefixSet

_Required_: No

_Type_: List of <a href="ipprefixsetdefinition.md">IpPrefixSetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LabelSelector

_Required_: No

_Type_: List of <a href="labelselectordefinition.md">LabelSelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortMatcher

_Required_: No

_Type_: List of <a href="portmatcherdefinition.md">PortMatcherDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixList

_Required_: No

_Type_: List of <a href="prefixlistdefinition.md">PrefixListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsList

_Required_: No

_Type_: List of <a href="tlslistdefinition.md">TlsListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

