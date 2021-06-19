# TF::Thunder::RouterOspf AreaListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#areaipv4" title="AreaIpv4">AreaIpv4</a>" : <i>String</i>,
    "<a href="#areanum" title="AreaNum">AreaNum</a>" : <i>Double</i>,
    "<a href="#defaultcost" title="DefaultCost">DefaultCost</a>" : <i>Double</i>,
    "<a href="#shortcut" title="Shortcut">Shortcut</a>" : <i>String</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#authcfg" title="AuthCfg">AuthCfg</a>" : <i>[ <a href="authcfgdefinition.md">AuthCfgDefinition</a>, ... ]</i>,
    "<a href="#filterlists" title="FilterLists">FilterLists</a>" : <i>[ <a href="filterlistsdefinition.md">FilterListsDefinition</a>, ... ]</i>,
    "<a href="#nssacfg" title="NssaCfg">NssaCfg</a>" : <i>[ <a href="nssacfgdefinition.md">NssaCfgDefinition</a>, ... ]</i>,
    "<a href="#rangelist" title="RangeList">RangeList</a>" : <i>[ <a href="rangelistdefinition.md">RangeListDefinition</a>, ... ]</i>,
    "<a href="#stubcfg" title="StubCfg">StubCfg</a>" : <i>[ <a href="stubcfgdefinition.md">StubCfgDefinition</a>, ... ]</i>,
    "<a href="#virtuallinklist" title="VirtualLinkList">VirtualLinkList</a>" : <i>[ <a href="virtuallinklistdefinition.md">VirtualLinkListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#areaipv4" title="AreaIpv4">AreaIpv4</a>: <i>String</i>
<a href="#areanum" title="AreaNum">AreaNum</a>: <i>Double</i>
<a href="#defaultcost" title="DefaultCost">DefaultCost</a>: <i>Double</i>
<a href="#shortcut" title="Shortcut">Shortcut</a>: <i>String</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#authcfg" title="AuthCfg">AuthCfg</a>: <i>
      - <a href="authcfgdefinition.md">AuthCfgDefinition</a></i>
<a href="#filterlists" title="FilterLists">FilterLists</a>: <i>
      - <a href="filterlistsdefinition.md">FilterListsDefinition</a></i>
<a href="#nssacfg" title="NssaCfg">NssaCfg</a>: <i>
      - <a href="nssacfgdefinition.md">NssaCfgDefinition</a></i>
<a href="#rangelist" title="RangeList">RangeList</a>: <i>
      - <a href="rangelistdefinition.md">RangeListDefinition</a></i>
<a href="#stubcfg" title="StubCfg">StubCfg</a>: <i>
      - <a href="stubcfgdefinition.md">StubCfgDefinition</a></i>
<a href="#virtuallinklist" title="VirtualLinkList">VirtualLinkList</a>: <i>
      - <a href="virtuallinklistdefinition.md">VirtualLinkListDefinition</a></i>
</pre>

## Properties

#### AreaIpv4

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AreaNum

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultCost

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shortcut

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthCfg

_Required_: No

_Type_: List of <a href="authcfgdefinition.md">AuthCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterLists

_Required_: No

_Type_: List of <a href="filterlistsdefinition.md">FilterListsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NssaCfg

_Required_: No

_Type_: List of <a href="nssacfgdefinition.md">NssaCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RangeList

_Required_: No

_Type_: List of <a href="rangelistdefinition.md">RangeListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StubCfg

_Required_: No

_Type_: List of <a href="stubcfgdefinition.md">StubCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualLinkList

_Required_: No

_Type_: List of <a href="virtuallinklistdefinition.md">VirtualLinkListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

