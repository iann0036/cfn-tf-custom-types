# TF::FortiOS::RouterIsis IsisInterfaceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authkeychainl1" title="AuthKeychainL1">AuthKeychainL1</a>" : <i>String</i>,
    "<a href="#authkeychainl2" title="AuthKeychainL2">AuthKeychainL2</a>" : <i>String</i>,
    "<a href="#authmodel1" title="AuthModeL1">AuthModeL1</a>" : <i>String</i>,
    "<a href="#authmodel2" title="AuthModeL2">AuthModeL2</a>" : <i>String</i>,
    "<a href="#authpasswordl1" title="AuthPasswordL1">AuthPasswordL1</a>" : <i>String</i>,
    "<a href="#authpasswordl2" title="AuthPasswordL2">AuthPasswordL2</a>" : <i>String</i>,
    "<a href="#authsendonlyl1" title="AuthSendOnlyL1">AuthSendOnlyL1</a>" : <i>String</i>,
    "<a href="#authsendonlyl2" title="AuthSendOnlyL2">AuthSendOnlyL2</a>" : <i>String</i>,
    "<a href="#circuittype" title="CircuitType">CircuitType</a>" : <i>String</i>,
    "<a href="#csnpintervall1" title="CsnpIntervalL1">CsnpIntervalL1</a>" : <i>Double</i>,
    "<a href="#csnpintervall2" title="CsnpIntervalL2">CsnpIntervalL2</a>" : <i>Double</i>,
    "<a href="#hellointervall1" title="HelloIntervalL1">HelloIntervalL1</a>" : <i>Double</i>,
    "<a href="#hellointervall2" title="HelloIntervalL2">HelloIntervalL2</a>" : <i>Double</i>,
    "<a href="#hellomultiplierl1" title="HelloMultiplierL1">HelloMultiplierL1</a>" : <i>Double</i>,
    "<a href="#hellomultiplierl2" title="HelloMultiplierL2">HelloMultiplierL2</a>" : <i>Double</i>,
    "<a href="#hellopadding" title="HelloPadding">HelloPadding</a>" : <i>String</i>,
    "<a href="#lspinterval" title="LspInterval">LspInterval</a>" : <i>Double</i>,
    "<a href="#lspretransmitinterval" title="LspRetransmitInterval">LspRetransmitInterval</a>" : <i>Double</i>,
    "<a href="#meshgroup" title="MeshGroup">MeshGroup</a>" : <i>String</i>,
    "<a href="#meshgroupid" title="MeshGroupId">MeshGroupId</a>" : <i>Double</i>,
    "<a href="#metricl1" title="MetricL1">MetricL1</a>" : <i>Double</i>,
    "<a href="#metricl2" title="MetricL2">MetricL2</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#networktype" title="NetworkType">NetworkType</a>" : <i>String</i>,
    "<a href="#priorityl1" title="PriorityL1">PriorityL1</a>" : <i>Double</i>,
    "<a href="#priorityl2" title="PriorityL2">PriorityL2</a>" : <i>Double</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#status6" title="Status6">Status6</a>" : <i>String</i>,
    "<a href="#widemetricl1" title="WideMetricL1">WideMetricL1</a>" : <i>Double</i>,
    "<a href="#widemetricl2" title="WideMetricL2">WideMetricL2</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#authkeychainl1" title="AuthKeychainL1">AuthKeychainL1</a>: <i>String</i>
<a href="#authkeychainl2" title="AuthKeychainL2">AuthKeychainL2</a>: <i>String</i>
<a href="#authmodel1" title="AuthModeL1">AuthModeL1</a>: <i>String</i>
<a href="#authmodel2" title="AuthModeL2">AuthModeL2</a>: <i>String</i>
<a href="#authpasswordl1" title="AuthPasswordL1">AuthPasswordL1</a>: <i>String</i>
<a href="#authpasswordl2" title="AuthPasswordL2">AuthPasswordL2</a>: <i>String</i>
<a href="#authsendonlyl1" title="AuthSendOnlyL1">AuthSendOnlyL1</a>: <i>String</i>
<a href="#authsendonlyl2" title="AuthSendOnlyL2">AuthSendOnlyL2</a>: <i>String</i>
<a href="#circuittype" title="CircuitType">CircuitType</a>: <i>String</i>
<a href="#csnpintervall1" title="CsnpIntervalL1">CsnpIntervalL1</a>: <i>Double</i>
<a href="#csnpintervall2" title="CsnpIntervalL2">CsnpIntervalL2</a>: <i>Double</i>
<a href="#hellointervall1" title="HelloIntervalL1">HelloIntervalL1</a>: <i>Double</i>
<a href="#hellointervall2" title="HelloIntervalL2">HelloIntervalL2</a>: <i>Double</i>
<a href="#hellomultiplierl1" title="HelloMultiplierL1">HelloMultiplierL1</a>: <i>Double</i>
<a href="#hellomultiplierl2" title="HelloMultiplierL2">HelloMultiplierL2</a>: <i>Double</i>
<a href="#hellopadding" title="HelloPadding">HelloPadding</a>: <i>String</i>
<a href="#lspinterval" title="LspInterval">LspInterval</a>: <i>Double</i>
<a href="#lspretransmitinterval" title="LspRetransmitInterval">LspRetransmitInterval</a>: <i>Double</i>
<a href="#meshgroup" title="MeshGroup">MeshGroup</a>: <i>String</i>
<a href="#meshgroupid" title="MeshGroupId">MeshGroupId</a>: <i>Double</i>
<a href="#metricl1" title="MetricL1">MetricL1</a>: <i>Double</i>
<a href="#metricl2" title="MetricL2">MetricL2</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#networktype" title="NetworkType">NetworkType</a>: <i>String</i>
<a href="#priorityl1" title="PriorityL1">PriorityL1</a>: <i>Double</i>
<a href="#priorityl2" title="PriorityL2">PriorityL2</a>: <i>Double</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#status6" title="Status6">Status6</a>: <i>String</i>
<a href="#widemetricl1" title="WideMetricL1">WideMetricL1</a>: <i>Double</i>
<a href="#widemetricl2" title="WideMetricL2">WideMetricL2</a>: <i>Double</i>
</pre>

## Properties

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

Level 1 authentication mode. Valid values: `md5`, `password`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthModeL2

Level 2 authentication mode. Valid values: `md5`, `password`.

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

#### AuthSendOnlyL1

Enable/disable authentication send-only for level 1 PDUs. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthSendOnlyL2

Enable/disable authentication send-only for level 2 PDUs. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CircuitType

IS-IS interface's circuit type Valid values: `level-1-2`, `level-1`, `level-2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CsnpIntervalL1

Level 1 CSNP interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CsnpIntervalL2

Level 2 CSNP interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HelloIntervalL1

Level 1 hello interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HelloIntervalL2

Level 2 hello interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HelloMultiplierL1

Level 1 multiplier for Hello holding time.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HelloMultiplierL2

Level 2 multiplier for Hello holding time.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HelloPadding

Enable/disable padding to IS-IS hello packets. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LspInterval

LSP transmission interval (milliseconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LspRetransmitInterval

LSP retransmission interval (sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MeshGroup

Enable/disable IS-IS mesh group. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MeshGroupId

Mesh group ID <0-4294967295>, 0: mesh-group blocked.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricL1

Level 1 metric for interface.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricL2

Level 2 metric for interface.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

IS-IS interface name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkType

IS-IS interface's network type Valid values: `broadcast`, `point-to-point`, `loopback`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PriorityL1

Level 1 priority.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PriorityL2

Level 2 priority.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable interface for IS-IS. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status6

Enable/disable IPv6 interface for IS-IS. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WideMetricL1

Level 1 wide metric for interface.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WideMetricL2

Level 2 wide metric for interface.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

