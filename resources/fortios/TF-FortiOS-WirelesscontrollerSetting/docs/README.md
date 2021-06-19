# TF::FortiOS::WirelesscontrollerSetting

VDOM wireless controller configuration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::WirelesscontrollerSetting",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
        "<a href="#country" title="Country">Country</a>" : <i>String</i>,
        "<a href="#darrpoptimize" title="DarrpOptimize">DarrpOptimize</a>" : <i>Double</i>,
        "<a href="#deviceholdoff" title="DeviceHoldoff">DeviceHoldoff</a>" : <i>Double</i>,
        "<a href="#deviceidle" title="DeviceIdle">DeviceIdle</a>" : <i>Double</i>,
        "<a href="#deviceweight" title="DeviceWeight">DeviceWeight</a>" : <i>Double</i>,
        "<a href="#duplicatessid" title="DuplicateSsid">DuplicateSsid</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#fakessidaction" title="FakeSsidAction">FakeSsidAction</a>" : <i>String</i>,
        "<a href="#fapccompatibility" title="FapcCompatibility">FapcCompatibility</a>" : <i>String</i>,
        "<a href="#phishingssiddetect" title="PhishingSsidDetect">PhishingSsidDetect</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#wfacompatibility" title="WfaCompatibility">WfaCompatibility</a>" : <i>String</i>,
        "<a href="#darrpoptimizeschedules" title="DarrpOptimizeSchedules">DarrpOptimizeSchedules</a>" : <i>[ <a href="darrpoptimizeschedulesdefinition.md">DarrpOptimizeSchedulesDefinition</a>, ... ]</i>,
        "<a href="#offendingssid" title="OffendingSsid">OffendingSsid</a>" : <i>[ <a href="offendingssiddefinition.md">OffendingSsidDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::WirelesscontrollerSetting
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
    <a href="#country" title="Country">Country</a>: <i>String</i>
    <a href="#darrpoptimize" title="DarrpOptimize">DarrpOptimize</a>: <i>Double</i>
    <a href="#deviceholdoff" title="DeviceHoldoff">DeviceHoldoff</a>: <i>Double</i>
    <a href="#deviceidle" title="DeviceIdle">DeviceIdle</a>: <i>Double</i>
    <a href="#deviceweight" title="DeviceWeight">DeviceWeight</a>: <i>Double</i>
    <a href="#duplicatessid" title="DuplicateSsid">DuplicateSsid</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#fakessidaction" title="FakeSsidAction">FakeSsidAction</a>: <i>String</i>
    <a href="#fapccompatibility" title="FapcCompatibility">FapcCompatibility</a>: <i>String</i>
    <a href="#phishingssiddetect" title="PhishingSsidDetect">PhishingSsidDetect</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#wfacompatibility" title="WfaCompatibility">WfaCompatibility</a>: <i>String</i>
    <a href="#darrpoptimizeschedules" title="DarrpOptimizeSchedules">DarrpOptimizeSchedules</a>: <i>
      - <a href="darrpoptimizeschedulesdefinition.md">DarrpOptimizeSchedulesDefinition</a></i>
    <a href="#offendingssid" title="OffendingSsid">OffendingSsid</a>: <i>
      - <a href="offendingssiddefinition.md">OffendingSsidDefinition</a></i>
</pre>

## Properties

#### AccountId

FortiCloud customer account ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Country

Country or region in which the FortiGate is located. The country determines the 802.11 bands and channels that are available.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DarrpOptimize

Time for running Dynamic Automatic Radio Resource Provisioning (DARRP) optimizations (0 - 86400 sec, default = 86400, 0 = disable).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceHoldoff

Lower limit of creation time of device for identification in minutes (0 - 60, default = 5).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceIdle

Upper limit of idle time of device for identification in minutes (0 - 14400, default = 1440).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceWeight

Upper limit of confidence of device for identification (0 - 255, default = 1, 0 = disable).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DuplicateSsid

Enable/disable allowing Virtual Access Points (VAPs) to use the same SSID name in the same VDOM. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FakeSsidAction

Actions taken for detected fake SSID. Valid values: `log`, `suppress`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FapcCompatibility

Enable/disable FAP-C series compatibility. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhishingSsidDetect

Enable/disable phishing SSID detection. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WfaCompatibility

Enable/disable WFA compatibility. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DarrpOptimizeSchedules

_Required_: No

_Type_: List of <a href="darrpoptimizeschedulesdefinition.md">DarrpOptimizeSchedulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OffendingSsid

_Required_: No

_Type_: List of <a href="offendingssiddefinition.md">OffendingSsidDefinition</a>

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

