# TF::FortiOS::RouterIsis

Configure IS-IS.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::RouterIsis",
    "Properties" : {
        "<a href="#adjacencycheck" title="AdjacencyCheck">AdjacencyCheck</a>" : <i>String</i>,
        "<a href="#adjacencycheck6" title="AdjacencyCheck6">AdjacencyCheck6</a>" : <i>String</i>,
        "<a href="#advpassiveonly" title="AdvPassiveOnly">AdvPassiveOnly</a>" : <i>String</i>,
        "<a href="#advpassiveonly6" title="AdvPassiveOnly6">AdvPassiveOnly6</a>" : <i>String</i>,
        "<a href="#authkeychainl1" title="AuthKeychainL1">AuthKeychainL1</a>" : <i>String</i>,
        "<a href="#authkeychainl2" title="AuthKeychainL2">AuthKeychainL2</a>" : <i>String</i>,
        "<a href="#authmodel1" title="AuthModeL1">AuthModeL1</a>" : <i>String</i>,
        "<a href="#authmodel2" title="AuthModeL2">AuthModeL2</a>" : <i>String</i>,
        "<a href="#authpasswordl1" title="AuthPasswordL1">AuthPasswordL1</a>" : <i>String</i>,
        "<a href="#authpasswordl2" title="AuthPasswordL2">AuthPasswordL2</a>" : <i>String</i>,
        "<a href="#authsendonlyl1" title="AuthSendonlyL1">AuthSendonlyL1</a>" : <i>String</i>,
        "<a href="#authsendonlyl2" title="AuthSendonlyL2">AuthSendonlyL2</a>" : <i>String</i>,
        "<a href="#defaultoriginate" title="DefaultOriginate">DefaultOriginate</a>" : <i>String</i>,
        "<a href="#defaultoriginate6" title="DefaultOriginate6">DefaultOriginate6</a>" : <i>String</i>,
        "<a href="#dynamichostname" title="DynamicHostname">DynamicHostname</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#ignorelsperrors" title="IgnoreLspErrors">IgnoreLspErrors</a>" : <i>String</i>,
        "<a href="#istype" title="IsType">IsType</a>" : <i>String</i>,
        "<a href="#lspgenintervall1" title="LspGenIntervalL1">LspGenIntervalL1</a>" : <i>Double</i>,
        "<a href="#lspgenintervall2" title="LspGenIntervalL2">LspGenIntervalL2</a>" : <i>Double</i>,
        "<a href="#lsprefreshinterval" title="LspRefreshInterval">LspRefreshInterval</a>" : <i>Double</i>,
        "<a href="#maxlsplifetime" title="MaxLspLifetime">MaxLspLifetime</a>" : <i>Double</i>,
        "<a href="#metricstyle" title="MetricStyle">MetricStyle</a>" : <i>String</i>,
        "<a href="#overloadbit" title="OverloadBit">OverloadBit</a>" : <i>String</i>,
        "<a href="#overloadbitonstartup" title="OverloadBitOnStartup">OverloadBitOnStartup</a>" : <i>Double</i>,
        "<a href="#overloadbitsuppress" title="OverloadBitSuppress">OverloadBitSuppress</a>" : <i>String</i>,
        "<a href="#redistribute6l1" title="Redistribute6L1">Redistribute6L1</a>" : <i>String</i>,
        "<a href="#redistribute6l1list" title="Redistribute6L1List">Redistribute6L1List</a>" : <i>String</i>,
        "<a href="#redistribute6l2" title="Redistribute6L2">Redistribute6L2</a>" : <i>String</i>,
        "<a href="#redistribute6l2list" title="Redistribute6L2List">Redistribute6L2List</a>" : <i>String</i>,
        "<a href="#redistributel1" title="RedistributeL1">RedistributeL1</a>" : <i>String</i>,
        "<a href="#redistributel1list" title="RedistributeL1List">RedistributeL1List</a>" : <i>String</i>,
        "<a href="#redistributel2" title="RedistributeL2">RedistributeL2</a>" : <i>String</i>,
        "<a href="#redistributel2list" title="RedistributeL2List">RedistributeL2List</a>" : <i>String</i>,
        "<a href="#spfintervalexpl1" title="SpfIntervalExpL1">SpfIntervalExpL1</a>" : <i>String</i>,
        "<a href="#spfintervalexpl2" title="SpfIntervalExpL2">SpfIntervalExpL2</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#isisinterface" title="IsisInterface">IsisInterface</a>" : <i>[ <a href="isisinterfacedefinition.md">IsisInterfaceDefinition</a>, ... ]</i>,
        "<a href="#isisnet" title="IsisNet">IsisNet</a>" : <i>[ <a href="isisnetdefinition.md">IsisNetDefinition</a>, ... ]</i>,
        "<a href="#redistribute" title="Redistribute">Redistribute</a>" : <i>[ <a href="redistributedefinition.md">RedistributeDefinition</a>, ... ]</i>,
        "<a href="#redistribute6" title="Redistribute6">Redistribute6</a>" : <i>[ <a href="redistribute6definition.md">Redistribute6Definition</a>, ... ]</i>,
        "<a href="#summaryaddress" title="SummaryAddress">SummaryAddress</a>" : <i>[ <a href="summaryaddressdefinition.md">SummaryAddressDefinition</a>, ... ]</i>,
        "<a href="#summaryaddress6" title="SummaryAddress6">SummaryAddress6</a>" : <i>[ <a href="summaryaddress6definition.md">SummaryAddress6Definition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::RouterIsis
Properties:
    <a href="#adjacencycheck" title="AdjacencyCheck">AdjacencyCheck</a>: <i>String</i>
    <a href="#adjacencycheck6" title="AdjacencyCheck6">AdjacencyCheck6</a>: <i>String</i>
    <a href="#advpassiveonly" title="AdvPassiveOnly">AdvPassiveOnly</a>: <i>String</i>
    <a href="#advpassiveonly6" title="AdvPassiveOnly6">AdvPassiveOnly6</a>: <i>String</i>
    <a href="#authkeychainl1" title="AuthKeychainL1">AuthKeychainL1</a>: <i>String</i>
    <a href="#authkeychainl2" title="AuthKeychainL2">AuthKeychainL2</a>: <i>String</i>
    <a href="#authmodel1" title="AuthModeL1">AuthModeL1</a>: <i>String</i>
    <a href="#authmodel2" title="AuthModeL2">AuthModeL2</a>: <i>String</i>
    <a href="#authpasswordl1" title="AuthPasswordL1">AuthPasswordL1</a>: <i>String</i>
    <a href="#authpasswordl2" title="AuthPasswordL2">AuthPasswordL2</a>: <i>String</i>
    <a href="#authsendonlyl1" title="AuthSendonlyL1">AuthSendonlyL1</a>: <i>String</i>
    <a href="#authsendonlyl2" title="AuthSendonlyL2">AuthSendonlyL2</a>: <i>String</i>
    <a href="#defaultoriginate" title="DefaultOriginate">DefaultOriginate</a>: <i>String</i>
    <a href="#defaultoriginate6" title="DefaultOriginate6">DefaultOriginate6</a>: <i>String</i>
    <a href="#dynamichostname" title="DynamicHostname">DynamicHostname</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#ignorelsperrors" title="IgnoreLspErrors">IgnoreLspErrors</a>: <i>String</i>
    <a href="#istype" title="IsType">IsType</a>: <i>String</i>
    <a href="#lspgenintervall1" title="LspGenIntervalL1">LspGenIntervalL1</a>: <i>Double</i>
    <a href="#lspgenintervall2" title="LspGenIntervalL2">LspGenIntervalL2</a>: <i>Double</i>
    <a href="#lsprefreshinterval" title="LspRefreshInterval">LspRefreshInterval</a>: <i>Double</i>
    <a href="#maxlsplifetime" title="MaxLspLifetime">MaxLspLifetime</a>: <i>Double</i>
    <a href="#metricstyle" title="MetricStyle">MetricStyle</a>: <i>String</i>
    <a href="#overloadbit" title="OverloadBit">OverloadBit</a>: <i>String</i>
    <a href="#overloadbitonstartup" title="OverloadBitOnStartup">OverloadBitOnStartup</a>: <i>Double</i>
    <a href="#overloadbitsuppress" title="OverloadBitSuppress">OverloadBitSuppress</a>: <i>String</i>
    <a href="#redistribute6l1" title="Redistribute6L1">Redistribute6L1</a>: <i>String</i>
    <a href="#redistribute6l1list" title="Redistribute6L1List">Redistribute6L1List</a>: <i>String</i>
    <a href="#redistribute6l2" title="Redistribute6L2">Redistribute6L2</a>: <i>String</i>
    <a href="#redistribute6l2list" title="Redistribute6L2List">Redistribute6L2List</a>: <i>String</i>
    <a href="#redistributel1" title="RedistributeL1">RedistributeL1</a>: <i>String</i>
    <a href="#redistributel1list" title="RedistributeL1List">RedistributeL1List</a>: <i>String</i>
    <a href="#redistributel2" title="RedistributeL2">RedistributeL2</a>: <i>String</i>
    <a href="#redistributel2list" title="RedistributeL2List">RedistributeL2List</a>: <i>String</i>
    <a href="#spfintervalexpl1" title="SpfIntervalExpL1">SpfIntervalExpL1</a>: <i>String</i>
    <a href="#spfintervalexpl2" title="SpfIntervalExpL2">SpfIntervalExpL2</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#isisinterface" title="IsisInterface">IsisInterface</a>: <i>
      - <a href="isisinterfacedefinition.md">IsisInterfaceDefinition</a></i>
    <a href="#isisnet" title="IsisNet">IsisNet</a>: <i>
      - <a href="isisnetdefinition.md">IsisNetDefinition</a></i>
    <a href="#redistribute" title="Redistribute">Redistribute</a>: <i>
      - <a href="redistributedefinition.md">RedistributeDefinition</a></i>
    <a href="#redistribute6" title="Redistribute6">Redistribute6</a>: <i>
      - <a href="redistribute6definition.md">Redistribute6Definition</a></i>
    <a href="#summaryaddress" title="SummaryAddress">SummaryAddress</a>: <i>
      - <a href="summaryaddressdefinition.md">SummaryAddressDefinition</a></i>
    <a href="#summaryaddress6" title="SummaryAddress6">SummaryAddress6</a>: <i>
      - <a href="summaryaddress6definition.md">SummaryAddress6Definition</a></i>
</pre>

## Properties

#### AdjacencyCheck

Enable/disable adjacency check. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdjacencyCheck6

Enable/disable IPv6 adjacency check. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvPassiveOnly

Enable/disable IS-IS advertisement of passive interfaces only. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvPassiveOnly6

Enable/disable IPv6 IS-IS advertisement of passive interfaces only. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthKeychainL1

Authentication key-chain for level 1 PDUs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthKeychainL2

Authentication key-chain for level 2 PDUs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthModeL1

Level 1 authentication mode. Valid values: `password`, `md5`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthModeL2

Level 2 authentication mode. Valid values: `password`, `md5`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthPasswordL1

Authentication password for level 1 PDUs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthPasswordL2

Authentication password for level 2 PDUs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthSendonlyL1

Enable/disable level 1 authentication send-only. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthSendonlyL2

Enable/disable level 2 authentication send-only. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultOriginate

Enable/disable distribution of default route information. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultOriginate6

Enable/disable distribution of default IPv6 route information. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicHostname

Enable/disable dynamic hostname. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreLspErrors

Enable/disable ignoring of LSP errors with bad checksums. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsType

IS type. Valid values: `level-1-2`, `level-1`, `level-2-only`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LspGenIntervalL1

Minimum interval for level 1 LSP regenerating.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LspGenIntervalL2

Minimum interval for level 2 LSP regenerating.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LspRefreshInterval

LSP refresh time in seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxLspLifetime

Maximum LSP lifetime in seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricStyle

Use old-style (ISO 10589) or new-style packet formats Valid values: `narrow`, `wide`, `transition`, `narrow-transition`, `narrow-transition-l1`, `narrow-transition-l2`, `wide-l1`, `wide-l2`, `wide-transition`, `wide-transition-l1`, `wide-transition-l2`, `transition-l1`, `transition-l2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverloadBit

Enable/disable signal other routers not to use us in SPF. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverloadBitOnStartup

Overload-bit only temporarily after reboot.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverloadBitSuppress

Suppress overload-bit for the specific prefixes. Valid values: `external`, `interlevel`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redistribute6L1

Enable/disable redistribution of level 1 IPv6 routes into level 2. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redistribute6L1List

Access-list for IPv6 route redistribution from l1 to l2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redistribute6L2

Enable/disable redistribution of level 2 IPv6 routes into level 1. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redistribute6L2List

Access-list for IPv6 route redistribution from l2 to l1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedistributeL1

Enable/disable redistribution of level 1 routes into level 2. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedistributeL1List

Access-list for route redistribution from l1 to l2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedistributeL2

Enable/disable redistribution of level 2 routes into level 1. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedistributeL2List

Access-list for route redistribution from l2 to l1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpfIntervalExpL1

Level 1 SPF calculation delay.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpfIntervalExpL2

Level 2 SPF calculation delay.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsisInterface

_Required_: No

_Type_: List of <a href="isisinterfacedefinition.md">IsisInterfaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsisNet

_Required_: No

_Type_: List of <a href="isisnetdefinition.md">IsisNetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redistribute

_Required_: No

_Type_: List of <a href="redistributedefinition.md">RedistributeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redistribute6

_Required_: No

_Type_: List of <a href="redistribute6definition.md">Redistribute6Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SummaryAddress

_Required_: No

_Type_: List of <a href="summaryaddressdefinition.md">SummaryAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SummaryAddress6

_Required_: No

_Type_: List of <a href="summaryaddress6definition.md">SummaryAddress6Definition</a>

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

