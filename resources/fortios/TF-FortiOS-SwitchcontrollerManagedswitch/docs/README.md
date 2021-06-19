# TF::FortiOS::SwitchcontrollerManagedswitch

Configure FortiSwitch devices that are managed by this FortiGate.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SwitchcontrollerManagedswitch",
    "Properties" : {
        "<a href="#accessprofile" title="AccessProfile">AccessProfile</a>" : <i>String</i>,
        "<a href="#delayedrestarttrigger" title="DelayedRestartTrigger">DelayedRestartTrigger</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#directlyconnected" title="DirectlyConnected">DirectlyConnected</a>" : <i>Double</i>,
        "<a href="#dynamiccapability" title="DynamicCapability">DynamicCapability</a>" : <i>Double</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#dynamicallydiscovered" title="DynamicallyDiscovered">DynamicallyDiscovered</a>" : <i>Double</i>,
        "<a href="#firmwareprovision" title="FirmwareProvision">FirmwareProvision</a>" : <i>String</i>,
        "<a href="#firmwareprovisionversion" title="FirmwareProvisionVersion">FirmwareProvisionVersion</a>" : <i>String</i>,
        "<a href="#flowidentity" title="FlowIdentity">FlowIdentity</a>" : <i>String</i>,
        "<a href="#fswwan1admin" title="FswWan1Admin">FswWan1Admin</a>" : <i>String</i>,
        "<a href="#fswwan1peer" title="FswWan1Peer">FswWan1Peer</a>" : <i>String</i>,
        "<a href="#fswwan2admin" title="FswWan2Admin">FswWan2Admin</a>" : <i>String</i>,
        "<a href="#fswwan2peer" title="FswWan2Peer">FswWan2Peer</a>" : <i>String</i>,
        "<a href="#l3discovered" title="L3Discovered">L3Discovered</a>" : <i>Double</i>,
        "<a href="#maxallowedtrunkmembers" title="MaxAllowedTrunkMembers">MaxAllowedTrunkMembers</a>" : <i>Double</i>,
        "<a href="#mclagigmpsnoopingaware" title="MclagIgmpSnoopingAware">MclagIgmpSnoopingAware</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#overridesnmpcommunity" title="OverrideSnmpCommunity">OverrideSnmpCommunity</a>" : <i>String</i>,
        "<a href="#overridesnmpsysinfo" title="OverrideSnmpSysinfo">OverrideSnmpSysinfo</a>" : <i>String</i>,
        "<a href="#overridesnmptrapthreshold" title="OverrideSnmpTrapThreshold">OverrideSnmpTrapThreshold</a>" : <i>String</i>,
        "<a href="#overridesnmpuser" title="OverrideSnmpUser">OverrideSnmpUser</a>" : <i>String</i>,
        "<a href="#ownervdom" title="OwnerVdom">OwnerVdom</a>" : <i>String</i>,
        "<a href="#poedetectiontype" title="PoeDetectionType">PoeDetectionType</a>" : <i>Double</i>,
        "<a href="#poelldpdetection" title="PoeLldpDetection">PoeLldpDetection</a>" : <i>String</i>,
        "<a href="#poeprestandarddetection" title="PoePreStandardDetection">PoePreStandardDetection</a>" : <i>String</i>,
        "<a href="#preprovisioned" title="PreProvisioned">PreProvisioned</a>" : <i>Double</i>,
        "<a href="#qosdroppolicy" title="QosDropPolicy">QosDropPolicy</a>" : <i>String</i>,
        "<a href="#qosredprobability" title="QosRedProbability">QosRedProbability</a>" : <i>Double</i>,
        "<a href="#stagedimageversion" title="StagedImageVersion">StagedImageVersion</a>" : <i>String</i>,
        "<a href="#switchdevicetag" title="SwitchDeviceTag">SwitchDeviceTag</a>" : <i>String</i>,
        "<a href="#switchdhcpopt43key" title="SwitchDhcpOpt43Key">SwitchDhcpOpt43Key</a>" : <i>String</i>,
        "<a href="#switchid" title="SwitchId">SwitchId</a>" : <i>String</i>,
        "<a href="#switchprofile" title="SwitchProfile">SwitchProfile</a>" : <i>String</i>,
        "<a href="#tdrsupported" title="TdrSupported">TdrSupported</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>,
        "<a href="#customcommand" title="CustomCommand">CustomCommand</a>" : <i>[ <a href="customcommanddefinition.md">CustomCommandDefinition</a>, ... ]</i>,
        "<a href="#igmpsnooping" title="IgmpSnooping">IgmpSnooping</a>" : <i>[ <a href="igmpsnoopingdefinition.md">IgmpSnoopingDefinition</a>, ... ]</i>,
        "<a href="#ipsourceguard" title="IpSourceGuard">IpSourceGuard</a>" : <i>[ <a href="ipsourceguarddefinition.md">IpSourceGuardDefinition</a>, ... ]</i>,
        "<a href="#mirror" title="Mirror">Mirror</a>" : <i>[ <a href="mirrordefinition.md">MirrorDefinition</a>, ... ]</i>,
        "<a href="#n8021xsettings" title="N8021xSettings">N8021xSettings</a>" : <i>[ <a href="n8021xsettingsdefinition.md">N8021xSettingsDefinition</a>, ... ]</i>,
        "<a href="#ports" title="Ports">Ports</a>" : <i>[ <a href="portsdefinition.md">PortsDefinition</a>, ... ]</i>,
        "<a href="#remotelog" title="RemoteLog">RemoteLog</a>" : <i>[ <a href="remotelogdefinition.md">RemoteLogDefinition</a>, ... ]</i>,
        "<a href="#snmpcommunity" title="SnmpCommunity">SnmpCommunity</a>" : <i>[ <a href="snmpcommunitydefinition.md">SnmpCommunityDefinition</a>, ... ]</i>,
        "<a href="#snmpsysinfo" title="SnmpSysinfo">SnmpSysinfo</a>" : <i>[ <a href="snmpsysinfodefinition.md">SnmpSysinfoDefinition</a>, ... ]</i>,
        "<a href="#snmptrapthreshold" title="SnmpTrapThreshold">SnmpTrapThreshold</a>" : <i>[ <a href="snmptrapthresholddefinition.md">SnmpTrapThresholdDefinition</a>, ... ]</i>,
        "<a href="#snmpuser" title="SnmpUser">SnmpUser</a>" : <i>[ <a href="snmpuserdefinition.md">SnmpUserDefinition</a>, ... ]</i>,
        "<a href="#staticmac" title="StaticMac">StaticMac</a>" : <i>[ <a href="staticmacdefinition.md">StaticMacDefinition</a>, ... ]</i>,
        "<a href="#stormcontrol" title="StormControl">StormControl</a>" : <i>[ <a href="stormcontroldefinition.md">StormControlDefinition</a>, ... ]</i>,
        "<a href="#stpinstance" title="StpInstance">StpInstance</a>" : <i>[ <a href="stpinstancedefinition.md">StpInstanceDefinition</a>, ... ]</i>,
        "<a href="#stpsettings" title="StpSettings">StpSettings</a>" : <i>[ <a href="stpsettingsdefinition.md">StpSettingsDefinition</a>, ... ]</i>,
        "<a href="#switchlog" title="SwitchLog">SwitchLog</a>" : <i>[ <a href="switchlogdefinition.md">SwitchLogDefinition</a>, ... ]</i>,
        "<a href="#switchstpsettings" title="SwitchStpSettings">SwitchStpSettings</a>" : <i>[ <a href="switchstpsettingsdefinition.md">SwitchStpSettingsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SwitchcontrollerManagedswitch
Properties:
    <a href="#accessprofile" title="AccessProfile">AccessProfile</a>: <i>String</i>
    <a href="#delayedrestarttrigger" title="DelayedRestartTrigger">DelayedRestartTrigger</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#directlyconnected" title="DirectlyConnected">DirectlyConnected</a>: <i>Double</i>
    <a href="#dynamiccapability" title="DynamicCapability">DynamicCapability</a>: <i>Double</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#dynamicallydiscovered" title="DynamicallyDiscovered">DynamicallyDiscovered</a>: <i>Double</i>
    <a href="#firmwareprovision" title="FirmwareProvision">FirmwareProvision</a>: <i>String</i>
    <a href="#firmwareprovisionversion" title="FirmwareProvisionVersion">FirmwareProvisionVersion</a>: <i>String</i>
    <a href="#flowidentity" title="FlowIdentity">FlowIdentity</a>: <i>String</i>
    <a href="#fswwan1admin" title="FswWan1Admin">FswWan1Admin</a>: <i>String</i>
    <a href="#fswwan1peer" title="FswWan1Peer">FswWan1Peer</a>: <i>String</i>
    <a href="#fswwan2admin" title="FswWan2Admin">FswWan2Admin</a>: <i>String</i>
    <a href="#fswwan2peer" title="FswWan2Peer">FswWan2Peer</a>: <i>String</i>
    <a href="#l3discovered" title="L3Discovered">L3Discovered</a>: <i>Double</i>
    <a href="#maxallowedtrunkmembers" title="MaxAllowedTrunkMembers">MaxAllowedTrunkMembers</a>: <i>Double</i>
    <a href="#mclagigmpsnoopingaware" title="MclagIgmpSnoopingAware">MclagIgmpSnoopingAware</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#overridesnmpcommunity" title="OverrideSnmpCommunity">OverrideSnmpCommunity</a>: <i>String</i>
    <a href="#overridesnmpsysinfo" title="OverrideSnmpSysinfo">OverrideSnmpSysinfo</a>: <i>String</i>
    <a href="#overridesnmptrapthreshold" title="OverrideSnmpTrapThreshold">OverrideSnmpTrapThreshold</a>: <i>String</i>
    <a href="#overridesnmpuser" title="OverrideSnmpUser">OverrideSnmpUser</a>: <i>String</i>
    <a href="#ownervdom" title="OwnerVdom">OwnerVdom</a>: <i>String</i>
    <a href="#poedetectiontype" title="PoeDetectionType">PoeDetectionType</a>: <i>Double</i>
    <a href="#poelldpdetection" title="PoeLldpDetection">PoeLldpDetection</a>: <i>String</i>
    <a href="#poeprestandarddetection" title="PoePreStandardDetection">PoePreStandardDetection</a>: <i>String</i>
    <a href="#preprovisioned" title="PreProvisioned">PreProvisioned</a>: <i>Double</i>
    <a href="#qosdroppolicy" title="QosDropPolicy">QosDropPolicy</a>: <i>String</i>
    <a href="#qosredprobability" title="QosRedProbability">QosRedProbability</a>: <i>Double</i>
    <a href="#stagedimageversion" title="StagedImageVersion">StagedImageVersion</a>: <i>String</i>
    <a href="#switchdevicetag" title="SwitchDeviceTag">SwitchDeviceTag</a>: <i>String</i>
    <a href="#switchdhcpopt43key" title="SwitchDhcpOpt43Key">SwitchDhcpOpt43Key</a>: <i>String</i>
    <a href="#switchid" title="SwitchId">SwitchId</a>: <i>String</i>
    <a href="#switchprofile" title="SwitchProfile">SwitchProfile</a>: <i>String</i>
    <a href="#tdrsupported" title="TdrSupported">TdrSupported</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
    <a href="#customcommand" title="CustomCommand">CustomCommand</a>: <i>
      - <a href="customcommanddefinition.md">CustomCommandDefinition</a></i>
    <a href="#igmpsnooping" title="IgmpSnooping">IgmpSnooping</a>: <i>
      - <a href="igmpsnoopingdefinition.md">IgmpSnoopingDefinition</a></i>
    <a href="#ipsourceguard" title="IpSourceGuard">IpSourceGuard</a>: <i>
      - <a href="ipsourceguarddefinition.md">IpSourceGuardDefinition</a></i>
    <a href="#mirror" title="Mirror">Mirror</a>: <i>
      - <a href="mirrordefinition.md">MirrorDefinition</a></i>
    <a href="#n8021xsettings" title="N8021xSettings">N8021xSettings</a>: <i>
      - <a href="n8021xsettingsdefinition.md">N8021xSettingsDefinition</a></i>
    <a href="#ports" title="Ports">Ports</a>: <i>
      - <a href="portsdefinition.md">PortsDefinition</a></i>
    <a href="#remotelog" title="RemoteLog">RemoteLog</a>: <i>
      - <a href="remotelogdefinition.md">RemoteLogDefinition</a></i>
    <a href="#snmpcommunity" title="SnmpCommunity">SnmpCommunity</a>: <i>
      - <a href="snmpcommunitydefinition.md">SnmpCommunityDefinition</a></i>
    <a href="#snmpsysinfo" title="SnmpSysinfo">SnmpSysinfo</a>: <i>
      - <a href="snmpsysinfodefinition.md">SnmpSysinfoDefinition</a></i>
    <a href="#snmptrapthreshold" title="SnmpTrapThreshold">SnmpTrapThreshold</a>: <i>
      - <a href="snmptrapthresholddefinition.md">SnmpTrapThresholdDefinition</a></i>
    <a href="#snmpuser" title="SnmpUser">SnmpUser</a>: <i>
      - <a href="snmpuserdefinition.md">SnmpUserDefinition</a></i>
    <a href="#staticmac" title="StaticMac">StaticMac</a>: <i>
      - <a href="staticmacdefinition.md">StaticMacDefinition</a></i>
    <a href="#stormcontrol" title="StormControl">StormControl</a>: <i>
      - <a href="stormcontroldefinition.md">StormControlDefinition</a></i>
    <a href="#stpinstance" title="StpInstance">StpInstance</a>: <i>
      - <a href="stpinstancedefinition.md">StpInstanceDefinition</a></i>
    <a href="#stpsettings" title="StpSettings">StpSettings</a>: <i>
      - <a href="stpsettingsdefinition.md">StpSettingsDefinition</a></i>
    <a href="#switchlog" title="SwitchLog">SwitchLog</a>: <i>
      - <a href="switchlogdefinition.md">SwitchLogDefinition</a></i>
    <a href="#switchstpsettings" title="SwitchStpSettings">SwitchStpSettings</a>: <i>
      - <a href="switchstpsettingsdefinition.md">SwitchStpSettingsDefinition</a></i>
</pre>

## Properties

#### AccessProfile

FortiSwitch access profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DelayedRestartTrigger

Delayed restart triggered for this FortiSwitch.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectlyConnected

Directly connected FortiSwitch.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicCapability

List of features this FortiSwitch supports (not configurable) that is sent to the FortiGate device for subsequent configuration initiated by the FortiGate device.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicallyDiscovered

Dynamically discovered FortiSwitch.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirmwareProvision

Enable/disable provisioning of firmware to FortiSwitches on join connection. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirmwareProvisionVersion

Firmware version to provision to this FortiSwitch on bootup (major.minor.build, i.e. 6.2.1234).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlowIdentity

Flow-tracking netflow ipfix switch identity in hex format(00000000-FFFFFFFF default=0).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FswWan1Admin

FortiSwitch WAN1 admin status; enable to authorize the FortiSwitch as a managed switch. Valid values: `discovered`, `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FswWan1Peer

Fortiswitch WAN1 peer port.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FswWan2Admin

FortiSwitch WAN2 admin status; enable to authorize the FortiSwitch as a managed switch. Valid values: `discovered`, `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FswWan2Peer

FortiSwitch WAN2 peer port.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L3Discovered

Layer 3 management discovered.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxAllowedTrunkMembers

FortiSwitch maximum allowed trunk members.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MclagIgmpSnoopingAware

Enable/disable MCLAG IGMP-snooping awareness. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Managed-switch name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideSnmpCommunity

Enable/disable overriding the global SNMP communities. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideSnmpSysinfo

Enable/disable overriding the global SNMP system information. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideSnmpTrapThreshold

Enable/disable overriding the global SNMP trap threshold values. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideSnmpUser

Enable/disable overriding the global SNMP users. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OwnerVdom

VDOM which owner of port belongs to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoeDetectionType

PoE detection type for FortiSwitch.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoeLldpDetection

Enable/disable PoE LLDP detection. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoePreStandardDetection

Enable/disable PoE pre-standard detection. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreProvisioned

Pre-provisioned managed switch.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QosDropPolicy

Set QoS drop-policy. Valid values: `taildrop`, `random-early-detection`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QosRedProbability

Set QoS RED/WRED drop probability.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StagedImageVersion

Staged image version for FortiSwitch.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchDeviceTag

User definable label/tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchDhcpOpt43Key

DHCP option43 key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchId

Managed-switch id.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchProfile

FortiSwitch profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TdrSupported

TDR supported.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Indication of switch type, physical or virtual. Valid values: `virtual`, `physical`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

FortiSwitch version.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomCommand

_Required_: No

_Type_: List of <a href="customcommanddefinition.md">CustomCommandDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgmpSnooping

_Required_: No

_Type_: List of <a href="igmpsnoopingdefinition.md">IgmpSnoopingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpSourceGuard

_Required_: No

_Type_: List of <a href="ipsourceguarddefinition.md">IpSourceGuardDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mirror

_Required_: No

_Type_: List of <a href="mirrordefinition.md">MirrorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### N8021xSettings

_Required_: No

_Type_: List of <a href="n8021xsettingsdefinition.md">N8021xSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

_Required_: No

_Type_: List of <a href="portsdefinition.md">PortsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteLog

_Required_: No

_Type_: List of <a href="remotelogdefinition.md">RemoteLogDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnmpCommunity

_Required_: No

_Type_: List of <a href="snmpcommunitydefinition.md">SnmpCommunityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnmpSysinfo

_Required_: No

_Type_: List of <a href="snmpsysinfodefinition.md">SnmpSysinfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnmpTrapThreshold

_Required_: No

_Type_: List of <a href="snmptrapthresholddefinition.md">SnmpTrapThresholdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnmpUser

_Required_: No

_Type_: List of <a href="snmpuserdefinition.md">SnmpUserDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticMac

_Required_: No

_Type_: List of <a href="staticmacdefinition.md">StaticMacDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StormControl

_Required_: No

_Type_: List of <a href="stormcontroldefinition.md">StormControlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StpInstance

_Required_: No

_Type_: List of <a href="stpinstancedefinition.md">StpInstanceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StpSettings

_Required_: No

_Type_: List of <a href="stpsettingsdefinition.md">StpSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchLog

_Required_: No

_Type_: List of <a href="switchlogdefinition.md">SwitchLogDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchStpSettings

_Required_: No

_Type_: List of <a href="switchstpsettingsdefinition.md">SwitchStpSettingsDefinition</a>

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

