# TF::Thunder::RouterOspfArea

`thunder_router_ospf_area` Provides details about thunder router ospf area

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::RouterOspfArea",
    "Properties" : {
        "<a href="#areaipv4" title="AreaIpv4">AreaIpv4</a>" : <i>String</i>,
        "<a href="#areanum" title="AreaNum">AreaNum</a>" : <i>Double</i>,
        "<a href="#asnumber" title="AsNumber">AsNumber</a>" : <i>String</i>,
        "<a href="#defaultcost" title="DefaultCost">DefaultCost</a>" : <i>Double</i>,
        "<a href="#processid" title="ProcessId">ProcessId</a>" : <i>Double</i>,
        "<a href="#shortcut" title="Shortcut">Shortcut</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#authcfg" title="AuthCfg">AuthCfg</a>" : <i>[ <a href="authcfgdefinition.md">AuthCfgDefinition</a>, ... ]</i>,
        "<a href="#filterlists" title="FilterLists">FilterLists</a>" : <i>[ <a href="filterlistsdefinition.md">FilterListsDefinition</a>, ... ]</i>,
        "<a href="#nssacfg" title="NssaCfg">NssaCfg</a>" : <i>[ <a href="nssacfgdefinition.md">NssaCfgDefinition</a>, ... ]</i>,
        "<a href="#rangelist" title="RangeList">RangeList</a>" : <i>[ <a href="rangelistdefinition.md">RangeListDefinition</a>, ... ]</i>,
        "<a href="#stubcfg" title="StubCfg">StubCfg</a>" : <i>[ <a href="stubcfgdefinition.md">StubCfgDefinition</a>, ... ]</i>,
        "<a href="#virtuallinklist" title="VirtualLinkList">VirtualLinkList</a>" : <i>[ <a href="virtuallinklistdefinition.md">VirtualLinkListDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::RouterOspfArea
Properties:
    <a href="#areaipv4" title="AreaIpv4">AreaIpv4</a>: <i>String</i>
    <a href="#areanum" title="AreaNum">AreaNum</a>: <i>Double</i>
    <a href="#asnumber" title="AsNumber">AsNumber</a>: <i>String</i>
    <a href="#defaultcost" title="DefaultCost">DefaultCost</a>: <i>Double</i>
    <a href="#processid" title="ProcessId">ProcessId</a>: <i>Double</i>
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

#### AsNumber

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultCost

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shortcut

'default': Set default shortcutting behavior; 'disable': Disable shortcutting through the area; 'enable': Enable shortcutting through the area;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

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

