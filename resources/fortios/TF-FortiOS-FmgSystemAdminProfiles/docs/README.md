# TF::FortiOS::FmgSystemAdminProfiles

This resource supports Create/Read/Update/Delete admin profiles for FortiManager

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FmgSystemAdminProfiles",
    "Properties" : {
        "<a href="#adompolicypackages" title="AdomPolicyPackages">AdomPolicyPackages</a>" : <i>String</i>,
        "<a href="#adomswitch" title="AdomSwitch">AdomSwitch</a>" : <i>String</i>,
        "<a href="#assignment" title="Assignment">Assignment</a>" : <i>String</i>,
        "<a href="#configretrieve" title="ConfigRetrieve">ConfigRetrieve</a>" : <i>String</i>,
        "<a href="#configrevert" title="ConfigRevert">ConfigRevert</a>" : <i>String</i>,
        "<a href="#consistencycheck" title="ConsistencyCheck">ConsistencyCheck</a>" : <i>String</i>,
        "<a href="#deploymanagement" title="DeployManagement">DeployManagement</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#deviceap" title="DeviceAp">DeviceAp</a>" : <i>String</i>,
        "<a href="#deviceconfig" title="DeviceConfig">DeviceConfig</a>" : <i>String</i>,
        "<a href="#deviceforticlient" title="DeviceForticlient">DeviceForticlient</a>" : <i>String</i>,
        "<a href="#devicefortiswitch" title="DeviceFortiswitch">DeviceFortiswitch</a>" : <i>String</i>,
        "<a href="#devicemanager" title="DeviceManager">DeviceManager</a>" : <i>String</i>,
        "<a href="#deviceoperation" title="DeviceOperation">DeviceOperation</a>" : <i>String</i>,
        "<a href="#deviceprofile" title="DeviceProfile">DeviceProfile</a>" : <i>String</i>,
        "<a href="#devicerevisiondeletion" title="DeviceRevisionDeletion">DeviceRevisionDeletion</a>" : <i>String</i>,
        "<a href="#devicewanlinkloadbalance" title="DeviceWanLinkLoadBalance">DeviceWanLinkLoadBalance</a>" : <i>String</i>,
        "<a href="#fortiguardcenter" title="FortiguardCenter">FortiguardCenter</a>" : <i>String</i>,
        "<a href="#fortiguardcenteradvanced" title="FortiguardCenterAdvanced">FortiguardCenterAdvanced</a>" : <i>String</i>,
        "<a href="#fortiguardcenterfirmwaremanagerment" title="FortiguardCenterFirmwareManagerment">FortiguardCenterFirmwareManagerment</a>" : <i>String</i>,
        "<a href="#fortiguardcenterlicensing" title="FortiguardCenterLicensing">FortiguardCenterLicensing</a>" : <i>String</i>,
        "<a href="#globalpolicypackages" title="GlobalPolicyPackages">GlobalPolicyPackages</a>" : <i>String</i>,
        "<a href="#importpolicypackages" title="ImportPolicyPackages">ImportPolicyPackages</a>" : <i>String</i>,
        "<a href="#intfmapping" title="IntfMapping">IntfMapping</a>" : <i>String</i>,
        "<a href="#logviewer" title="LogViewer">LogViewer</a>" : <i>String</i>,
        "<a href="#policyobjects" title="PolicyObjects">PolicyObjects</a>" : <i>String</i>,
        "<a href="#profileid" title="Profileid">Profileid</a>" : <i>String</i>,
        "<a href="#setinstalltargets" title="SetInstallTargets">SetInstallTargets</a>" : <i>String</i>,
        "<a href="#systemsetting" title="SystemSetting">SystemSetting</a>" : <i>String</i>,
        "<a href="#terminalaccess" title="TerminalAccess">TerminalAccess</a>" : <i>String</i>,
        "<a href="#vpnmanager" title="VpnManager">VpnManager</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FmgSystemAdminProfiles
Properties:
    <a href="#adompolicypackages" title="AdomPolicyPackages">AdomPolicyPackages</a>: <i>String</i>
    <a href="#adomswitch" title="AdomSwitch">AdomSwitch</a>: <i>String</i>
    <a href="#assignment" title="Assignment">Assignment</a>: <i>String</i>
    <a href="#configretrieve" title="ConfigRetrieve">ConfigRetrieve</a>: <i>String</i>
    <a href="#configrevert" title="ConfigRevert">ConfigRevert</a>: <i>String</i>
    <a href="#consistencycheck" title="ConsistencyCheck">ConsistencyCheck</a>: <i>String</i>
    <a href="#deploymanagement" title="DeployManagement">DeployManagement</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#deviceap" title="DeviceAp">DeviceAp</a>: <i>String</i>
    <a href="#deviceconfig" title="DeviceConfig">DeviceConfig</a>: <i>String</i>
    <a href="#deviceforticlient" title="DeviceForticlient">DeviceForticlient</a>: <i>String</i>
    <a href="#devicefortiswitch" title="DeviceFortiswitch">DeviceFortiswitch</a>: <i>String</i>
    <a href="#devicemanager" title="DeviceManager">DeviceManager</a>: <i>String</i>
    <a href="#deviceoperation" title="DeviceOperation">DeviceOperation</a>: <i>String</i>
    <a href="#deviceprofile" title="DeviceProfile">DeviceProfile</a>: <i>String</i>
    <a href="#devicerevisiondeletion" title="DeviceRevisionDeletion">DeviceRevisionDeletion</a>: <i>String</i>
    <a href="#devicewanlinkloadbalance" title="DeviceWanLinkLoadBalance">DeviceWanLinkLoadBalance</a>: <i>String</i>
    <a href="#fortiguardcenter" title="FortiguardCenter">FortiguardCenter</a>: <i>String</i>
    <a href="#fortiguardcenteradvanced" title="FortiguardCenterAdvanced">FortiguardCenterAdvanced</a>: <i>String</i>
    <a href="#fortiguardcenterfirmwaremanagerment" title="FortiguardCenterFirmwareManagerment">FortiguardCenterFirmwareManagerment</a>: <i>String</i>
    <a href="#fortiguardcenterlicensing" title="FortiguardCenterLicensing">FortiguardCenterLicensing</a>: <i>String</i>
    <a href="#globalpolicypackages" title="GlobalPolicyPackages">GlobalPolicyPackages</a>: <i>String</i>
    <a href="#importpolicypackages" title="ImportPolicyPackages">ImportPolicyPackages</a>: <i>String</i>
    <a href="#intfmapping" title="IntfMapping">IntfMapping</a>: <i>String</i>
    <a href="#logviewer" title="LogViewer">LogViewer</a>: <i>String</i>
    <a href="#policyobjects" title="PolicyObjects">PolicyObjects</a>: <i>String</i>
    <a href="#profileid" title="Profileid">Profileid</a>: <i>String</i>
    <a href="#setinstalltargets" title="SetInstallTargets">SetInstallTargets</a>: <i>String</i>
    <a href="#systemsetting" title="SystemSetting">SystemSetting</a>: <i>String</i>
    <a href="#terminalaccess" title="TerminalAccess">TerminalAccess</a>: <i>String</i>
    <a href="#vpnmanager" title="VpnManager">VpnManager</a>: <i>String</i>
</pre>

## Properties

#### AdomPolicyPackages

Adom policy packages.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdomSwitch

Administrator Domain.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Assignment

Assignment Permission.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigRetrieve

Configuration Retrieve.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigRevert

Revert Configuration from Revision History.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsistencyCheck

Consistency check.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeployManagement

Install to devices.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceAp

Manage AP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceConfig

Manage device configurations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceForticlient

Manage FortiClient.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceFortiswitch

Manage FortiSwitch.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceManager

Device Manager.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceOperation

Device add/delete/edit.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceProfile

Device profile permission.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceRevisionDeletion

Delete device revision.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceWanLinkLoadBalance

Manage WAN link load balance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortiguardCenter

FortiGuard Center.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortiguardCenterAdvanced

FortiGuard Center Advanced.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortiguardCenterFirmwareManagerment

FortiGuard Center Firmware Managerment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortiguardCenterLicensing

FortiGuard Center Licensing.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlobalPolicyPackages

Global policy packages.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImportPolicyPackages

Import Policy Package.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntfMapping

Interface Mapping.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogViewer

Log Viewer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyObjects

Policy objects permission.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Profileid

Profile name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SetInstallTargets

Edit installation targets.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemSetting

System Setting.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminalAccess

Terminal access.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnManager

VPN Manager.

_Required_: No

_Type_: String

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

