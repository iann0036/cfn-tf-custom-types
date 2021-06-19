# TF::FortiOS::WirelesscontrollerQosprofile

Configure WiFi quality of service (QoS) profiles.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::WirelesscontrollerQosprofile",
    "Properties" : {
        "<a href="#bandwidthadmissioncontrol" title="BandwidthAdmissionControl">BandwidthAdmissionControl</a>" : <i>String</i>,
        "<a href="#bandwidthcapacity" title="BandwidthCapacity">BandwidthCapacity</a>" : <i>Double</i>,
        "<a href="#burst" title="Burst">Burst</a>" : <i>String</i>,
        "<a href="#calladmissioncontrol" title="CallAdmissionControl">CallAdmissionControl</a>" : <i>String</i>,
        "<a href="#callcapacity" title="CallCapacity">CallCapacity</a>" : <i>Double</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#downlink" title="Downlink">Downlink</a>" : <i>Double</i>,
        "<a href="#downlinksta" title="DownlinkSta">DownlinkSta</a>" : <i>Double</i>,
        "<a href="#dscpwmmmapping" title="DscpWmmMapping">DscpWmmMapping</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#uplink" title="Uplink">Uplink</a>" : <i>Double</i>,
        "<a href="#uplinksta" title="UplinkSta">UplinkSta</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#wmm" title="Wmm">Wmm</a>" : <i>String</i>,
        "<a href="#wmmbedscp" title="WmmBeDscp">WmmBeDscp</a>" : <i>Double</i>,
        "<a href="#wmmbkdscp" title="WmmBkDscp">WmmBkDscp</a>" : <i>Double</i>,
        "<a href="#wmmdscpmarking" title="WmmDscpMarking">WmmDscpMarking</a>" : <i>String</i>,
        "<a href="#wmmuapsd" title="WmmUapsd">WmmUapsd</a>" : <i>String</i>,
        "<a href="#wmmvidscp" title="WmmViDscp">WmmViDscp</a>" : <i>Double</i>,
        "<a href="#wmmvodscp" title="WmmVoDscp">WmmVoDscp</a>" : <i>Double</i>,
        "<a href="#dscpwmmbe" title="DscpWmmBe">DscpWmmBe</a>" : <i>[ <a href="dscpwmmbedefinition.md">DscpWmmBeDefinition</a>, ... ]</i>,
        "<a href="#dscpwmmbk" title="DscpWmmBk">DscpWmmBk</a>" : <i>[ <a href="dscpwmmbkdefinition.md">DscpWmmBkDefinition</a>, ... ]</i>,
        "<a href="#dscpwmmvi" title="DscpWmmVi">DscpWmmVi</a>" : <i>[ <a href="dscpwmmvidefinition.md">DscpWmmViDefinition</a>, ... ]</i>,
        "<a href="#dscpwmmvo" title="DscpWmmVo">DscpWmmVo</a>" : <i>[ <a href="dscpwmmvodefinition.md">DscpWmmVoDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::WirelesscontrollerQosprofile
Properties:
    <a href="#bandwidthadmissioncontrol" title="BandwidthAdmissionControl">BandwidthAdmissionControl</a>: <i>String</i>
    <a href="#bandwidthcapacity" title="BandwidthCapacity">BandwidthCapacity</a>: <i>Double</i>
    <a href="#burst" title="Burst">Burst</a>: <i>String</i>
    <a href="#calladmissioncontrol" title="CallAdmissionControl">CallAdmissionControl</a>: <i>String</i>
    <a href="#callcapacity" title="CallCapacity">CallCapacity</a>: <i>Double</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#downlink" title="Downlink">Downlink</a>: <i>Double</i>
    <a href="#downlinksta" title="DownlinkSta">DownlinkSta</a>: <i>Double</i>
    <a href="#dscpwmmmapping" title="DscpWmmMapping">DscpWmmMapping</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#uplink" title="Uplink">Uplink</a>: <i>Double</i>
    <a href="#uplinksta" title="UplinkSta">UplinkSta</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#wmm" title="Wmm">Wmm</a>: <i>String</i>
    <a href="#wmmbedscp" title="WmmBeDscp">WmmBeDscp</a>: <i>Double</i>
    <a href="#wmmbkdscp" title="WmmBkDscp">WmmBkDscp</a>: <i>Double</i>
    <a href="#wmmdscpmarking" title="WmmDscpMarking">WmmDscpMarking</a>: <i>String</i>
    <a href="#wmmuapsd" title="WmmUapsd">WmmUapsd</a>: <i>String</i>
    <a href="#wmmvidscp" title="WmmViDscp">WmmViDscp</a>: <i>Double</i>
    <a href="#wmmvodscp" title="WmmVoDscp">WmmVoDscp</a>: <i>Double</i>
    <a href="#dscpwmmbe" title="DscpWmmBe">DscpWmmBe</a>: <i>
      - <a href="dscpwmmbedefinition.md">DscpWmmBeDefinition</a></i>
    <a href="#dscpwmmbk" title="DscpWmmBk">DscpWmmBk</a>: <i>
      - <a href="dscpwmmbkdefinition.md">DscpWmmBkDefinition</a></i>
    <a href="#dscpwmmvi" title="DscpWmmVi">DscpWmmVi</a>: <i>
      - <a href="dscpwmmvidefinition.md">DscpWmmViDefinition</a></i>
    <a href="#dscpwmmvo" title="DscpWmmVo">DscpWmmVo</a>: <i>
      - <a href="dscpwmmvodefinition.md">DscpWmmVoDefinition</a></i>
</pre>

## Properties

#### BandwidthAdmissionControl

Enable/disable WMM bandwidth admission control. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BandwidthCapacity

Maximum bandwidth capacity allowed (1 - 600000 Kbps, default = 2000).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Burst

Enable/disable client rate burst. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CallAdmissionControl

Enable/disable WMM call admission control. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CallCapacity

Maximum number of Voice over WLAN (VoWLAN) phones allowed (0 - 60, default = 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Downlink

Maximum downlink bandwidth for Virtual Access Points (VAPs) (0 - 2097152 Kbps, default = 0, 0 means no limit).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DownlinkSta

Maximum downlink bandwidth for clients (0 - 2097152 Kbps, default = 0, 0 means no limit).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DscpWmmMapping

Enable/disable Differentiated Services Code Point (DSCP) mapping. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

WiFi QoS profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uplink

Maximum uplink bandwidth for Virtual Access Points (VAPs) (0 - 2097152 Kbps, default = 0, 0 means no limit).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UplinkSta

Maximum uplink bandwidth for clients (0 - 2097152 Kbps, default = 0, 0 means no limit).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Wmm

Enable/disable WiFi multi-media (WMM) control. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WmmBeDscp

DSCP marking for best effort access (default = 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WmmBkDscp

DSCP marking for background access (default = 8).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WmmDscpMarking

Enable/disable WMM Differentiated Services Code Point (DSCP) marking. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WmmUapsd

Enable/disable WMM Unscheduled Automatic Power Save Delivery (U-APSD) power save mode. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WmmViDscp

DSCP marking for video access (default = 32).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WmmVoDscp

DSCP marking for voice access (default = 48).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DscpWmmBe

_Required_: No

_Type_: List of <a href="dscpwmmbedefinition.md">DscpWmmBeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DscpWmmBk

_Required_: No

_Type_: List of <a href="dscpwmmbkdefinition.md">DscpWmmBkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DscpWmmVi

_Required_: No

_Type_: List of <a href="dscpwmmvidefinition.md">DscpWmmViDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DscpWmmVo

_Required_: No

_Type_: List of <a href="dscpwmmvodefinition.md">DscpWmmVoDefinition</a>

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

