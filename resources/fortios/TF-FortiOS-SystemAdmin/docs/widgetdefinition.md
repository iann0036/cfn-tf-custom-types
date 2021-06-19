# TF::FortiOS::SystemAdmin WidgetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#fabricdevice" title="FabricDevice">FabricDevice</a>" : <i>String</i>,
    "<a href="#height" title="Height">Height</a>" : <i>Double</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#industry" title="Industry">Industry</a>" : <i>String</i>,
    "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
    "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    "<a href="#reportby" title="ReportBy">ReportBy</a>" : <i>String</i>,
    "<a href="#sortby" title="SortBy">SortBy</a>" : <i>String</i>,
    "<a href="#timeframe" title="Timeframe">Timeframe</a>" : <i>String</i>,
    "<a href="#title" title="Title">Title</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#visualization" title="Visualization">Visualization</a>" : <i>String</i>,
    "<a href="#width" title="Width">Width</a>" : <i>Double</i>,
    "<a href="#xpos" title="XPos">XPos</a>" : <i>Double</i>,
    "<a href="#ypos" title="YPos">YPos</a>" : <i>Double</i>,
    "<a href="#filters" title="Filters">Filters</a>" : <i>[ <a href="filtersdefinition.md">FiltersDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#fabricdevice" title="FabricDevice">FabricDevice</a>: <i>String</i>
<a href="#height" title="Height">Height</a>: <i>Double</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#industry" title="Industry">Industry</a>: <i>String</i>
<a href="#interface" title="Interface">Interface</a>: <i>String</i>
<a href="#region" title="Region">Region</a>: <i>String</i>
<a href="#reportby" title="ReportBy">ReportBy</a>: <i>String</i>
<a href="#sortby" title="SortBy">SortBy</a>: <i>String</i>
<a href="#timeframe" title="Timeframe">Timeframe</a>: <i>String</i>
<a href="#title" title="Title">Title</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#visualization" title="Visualization">Visualization</a>: <i>String</i>
<a href="#width" title="Width">Width</a>: <i>Double</i>
<a href="#xpos" title="XPos">XPos</a>: <i>Double</i>
<a href="#ypos" title="YPos">YPos</a>: <i>Double</i>
<a href="#filters" title="Filters">Filters</a>: <i>
      - <a href="filtersdefinition.md">FiltersDefinition</a></i>
</pre>

## Properties

#### FabricDevice

Fabric device to monitor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Height

Height.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Widget ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Industry

Security Audit Rating industry. Valid values: `default`, `custom`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

Interface to monitor.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

Security Audit Rating region. Valid values: `default`, `custom`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReportBy

Field to aggregate the data by. Valid values: `source`, `destination`, `country`, `intfpair`, `srcintf`, `dstintf`, `policy`, `wificlient`, `shaper`, `endpoint-vulnerability`, `endpoint-device`, `application`, `cloud-app`, `cloud-user`, `web-domain`, `web-category`, `web-search-phrase`, `threat`, `system`, `unauth`, `admin`, `vpn`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SortBy

Field to sort the data by.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeframe

Timeframe period of reported data. Valid values: `realtime`, `5min`, `hour`, `day`, `week`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

Widget title.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Widget type. Valid values: `sysinfo`, `licinfo`, `vminfo`, `forticloud`, `cpu-usage`, `memory-usage`, `disk-usage`, `log-rate`, `sessions`, `session-rate`, `tr-history`, `analytics`, `usb-modem`, `admins`, `security-fabric`, `security-fabric-ranking`, `ha-status`, `vulnerability-summary`, `host-scan-summary`, `fortiview`, `botnet-activity`, `fortimail`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Visualization

Visualization to use. Valid values: `table`, `bubble`, `country`, `chord`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Width

Width.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### XPos

X position.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### YPos

Y position.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filters

_Required_: No

_Type_: List of <a href="filtersdefinition.md">FiltersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

