# TF::FortiOS::EndpointcontrolProfile ForticlientWinmacSettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#avrealtimeprotection" title="AvRealtimeProtection">AvRealtimeProtection</a>" : <i>String</i>,
    "<a href="#avsignatureuptodate" title="AvSignatureUpToDate">AvSignatureUpToDate</a>" : <i>String</i>,
    "<a href="#forticlientapplicationfirewall" title="ForticlientApplicationFirewall">ForticlientApplicationFirewall</a>" : <i>String</i>,
    "<a href="#forticlientapplicationfirewalllist" title="ForticlientApplicationFirewallList">ForticlientApplicationFirewallList</a>" : <i>String</i>,
    "<a href="#forticlientav" title="ForticlientAv">ForticlientAv</a>" : <i>String</i>,
    "<a href="#forticlientemscompliance" title="ForticlientEmsCompliance">ForticlientEmsCompliance</a>" : <i>String</i>,
    "<a href="#forticlientemscomplianceaction" title="ForticlientEmsComplianceAction">ForticlientEmsComplianceAction</a>" : <i>String</i>,
    "<a href="#forticlientlinuxver" title="ForticlientLinuxVer">ForticlientLinuxVer</a>" : <i>String</i>,
    "<a href="#forticlientlogupload" title="ForticlientLogUpload">ForticlientLogUpload</a>" : <i>String</i>,
    "<a href="#forticlientloguploadlevel" title="ForticlientLogUploadLevel">ForticlientLogUploadLevel</a>" : <i>String</i>,
    "<a href="#forticlientloguploadserver" title="ForticlientLogUploadServer">ForticlientLogUploadServer</a>" : <i>String</i>,
    "<a href="#forticlientmacver" title="ForticlientMacVer">ForticlientMacVer</a>" : <i>String</i>,
    "<a href="#forticlientminimumsoftwareversion" title="ForticlientMinimumSoftwareVersion">ForticlientMinimumSoftwareVersion</a>" : <i>String</i>,
    "<a href="#forticlientregistrationcomplianceaction" title="ForticlientRegistrationComplianceAction">ForticlientRegistrationComplianceAction</a>" : <i>String</i>,
    "<a href="#forticlientsecurityposture" title="ForticlientSecurityPosture">ForticlientSecurityPosture</a>" : <i>String</i>,
    "<a href="#forticlientsecurityposturecomplianceaction" title="ForticlientSecurityPostureComplianceAction">ForticlientSecurityPostureComplianceAction</a>" : <i>String</i>,
    "<a href="#forticlientsystemcompliance" title="ForticlientSystemCompliance">ForticlientSystemCompliance</a>" : <i>String</i>,
    "<a href="#forticlientsystemcomplianceaction" title="ForticlientSystemComplianceAction">ForticlientSystemComplianceAction</a>" : <i>String</i>,
    "<a href="#forticlientvulnscan" title="ForticlientVulnScan">ForticlientVulnScan</a>" : <i>String</i>,
    "<a href="#forticlientvulnscancomplianceaction" title="ForticlientVulnScanComplianceAction">ForticlientVulnScanComplianceAction</a>" : <i>String</i>,
    "<a href="#forticlientvulnscanenforce" title="ForticlientVulnScanEnforce">ForticlientVulnScanEnforce</a>" : <i>String</i>,
    "<a href="#forticlientvulnscanenforcegrace" title="ForticlientVulnScanEnforceGrace">ForticlientVulnScanEnforceGrace</a>" : <i>Double</i>,
    "<a href="#forticlientvulnscanexempt" title="ForticlientVulnScanExempt">ForticlientVulnScanExempt</a>" : <i>String</i>,
    "<a href="#forticlientwf" title="ForticlientWf">ForticlientWf</a>" : <i>String</i>,
    "<a href="#forticlientwfprofile" title="ForticlientWfProfile">ForticlientWfProfile</a>" : <i>String</i>,
    "<a href="#forticlientwinver" title="ForticlientWinVer">ForticlientWinVer</a>" : <i>String</i>,
    "<a href="#osavsoftwareinstalled" title="OsAvSoftwareInstalled">OsAvSoftwareInstalled</a>" : <i>String</i>,
    "<a href="#sandboxaddress" title="SandboxAddress">SandboxAddress</a>" : <i>String</i>,
    "<a href="#sandboxanalysis" title="SandboxAnalysis">SandboxAnalysis</a>" : <i>String</i>,
    "<a href="#forticlientemsentries" title="ForticlientEmsEntries">ForticlientEmsEntries</a>" : <i>[ <a href="forticlientemsentriesdefinition.md">ForticlientEmsEntriesDefinition</a>, ... ]</i>,
    "<a href="#forticlientoperatingsystem" title="ForticlientOperatingSystem">ForticlientOperatingSystem</a>" : <i>[ <a href="forticlientoperatingsystemdefinition.md">ForticlientOperatingSystemDefinition</a>, ... ]</i>,
    "<a href="#forticlientownfile" title="ForticlientOwnFile">ForticlientOwnFile</a>" : <i>[ <a href="forticlientownfiledefinition.md">ForticlientOwnFileDefinition</a>, ... ]</i>,
    "<a href="#forticlientregistryentry" title="ForticlientRegistryEntry">ForticlientRegistryEntry</a>" : <i>[ <a href="forticlientregistryentrydefinition.md">ForticlientRegistryEntryDefinition</a>, ... ]</i>,
    "<a href="#forticlientrunningapp" title="ForticlientRunningApp">ForticlientRunningApp</a>" : <i>[ <a href="forticlientrunningappdefinition.md">ForticlientRunningAppDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#avrealtimeprotection" title="AvRealtimeProtection">AvRealtimeProtection</a>: <i>String</i>
<a href="#avsignatureuptodate" title="AvSignatureUpToDate">AvSignatureUpToDate</a>: <i>String</i>
<a href="#forticlientapplicationfirewall" title="ForticlientApplicationFirewall">ForticlientApplicationFirewall</a>: <i>String</i>
<a href="#forticlientapplicationfirewalllist" title="ForticlientApplicationFirewallList">ForticlientApplicationFirewallList</a>: <i>String</i>
<a href="#forticlientav" title="ForticlientAv">ForticlientAv</a>: <i>String</i>
<a href="#forticlientemscompliance" title="ForticlientEmsCompliance">ForticlientEmsCompliance</a>: <i>String</i>
<a href="#forticlientemscomplianceaction" title="ForticlientEmsComplianceAction">ForticlientEmsComplianceAction</a>: <i>String</i>
<a href="#forticlientlinuxver" title="ForticlientLinuxVer">ForticlientLinuxVer</a>: <i>String</i>
<a href="#forticlientlogupload" title="ForticlientLogUpload">ForticlientLogUpload</a>: <i>String</i>
<a href="#forticlientloguploadlevel" title="ForticlientLogUploadLevel">ForticlientLogUploadLevel</a>: <i>String</i>
<a href="#forticlientloguploadserver" title="ForticlientLogUploadServer">ForticlientLogUploadServer</a>: <i>String</i>
<a href="#forticlientmacver" title="ForticlientMacVer">ForticlientMacVer</a>: <i>String</i>
<a href="#forticlientminimumsoftwareversion" title="ForticlientMinimumSoftwareVersion">ForticlientMinimumSoftwareVersion</a>: <i>String</i>
<a href="#forticlientregistrationcomplianceaction" title="ForticlientRegistrationComplianceAction">ForticlientRegistrationComplianceAction</a>: <i>String</i>
<a href="#forticlientsecurityposture" title="ForticlientSecurityPosture">ForticlientSecurityPosture</a>: <i>String</i>
<a href="#forticlientsecurityposturecomplianceaction" title="ForticlientSecurityPostureComplianceAction">ForticlientSecurityPostureComplianceAction</a>: <i>String</i>
<a href="#forticlientsystemcompliance" title="ForticlientSystemCompliance">ForticlientSystemCompliance</a>: <i>String</i>
<a href="#forticlientsystemcomplianceaction" title="ForticlientSystemComplianceAction">ForticlientSystemComplianceAction</a>: <i>String</i>
<a href="#forticlientvulnscan" title="ForticlientVulnScan">ForticlientVulnScan</a>: <i>String</i>
<a href="#forticlientvulnscancomplianceaction" title="ForticlientVulnScanComplianceAction">ForticlientVulnScanComplianceAction</a>: <i>String</i>
<a href="#forticlientvulnscanenforce" title="ForticlientVulnScanEnforce">ForticlientVulnScanEnforce</a>: <i>String</i>
<a href="#forticlientvulnscanenforcegrace" title="ForticlientVulnScanEnforceGrace">ForticlientVulnScanEnforceGrace</a>: <i>Double</i>
<a href="#forticlientvulnscanexempt" title="ForticlientVulnScanExempt">ForticlientVulnScanExempt</a>: <i>String</i>
<a href="#forticlientwf" title="ForticlientWf">ForticlientWf</a>: <i>String</i>
<a href="#forticlientwfprofile" title="ForticlientWfProfile">ForticlientWfProfile</a>: <i>String</i>
<a href="#forticlientwinver" title="ForticlientWinVer">ForticlientWinVer</a>: <i>String</i>
<a href="#osavsoftwareinstalled" title="OsAvSoftwareInstalled">OsAvSoftwareInstalled</a>: <i>String</i>
<a href="#sandboxaddress" title="SandboxAddress">SandboxAddress</a>: <i>String</i>
<a href="#sandboxanalysis" title="SandboxAnalysis">SandboxAnalysis</a>: <i>String</i>
<a href="#forticlientemsentries" title="ForticlientEmsEntries">ForticlientEmsEntries</a>: <i>
      - <a href="forticlientemsentriesdefinition.md">ForticlientEmsEntriesDefinition</a></i>
<a href="#forticlientoperatingsystem" title="ForticlientOperatingSystem">ForticlientOperatingSystem</a>: <i>
      - <a href="forticlientoperatingsystemdefinition.md">ForticlientOperatingSystemDefinition</a></i>
<a href="#forticlientownfile" title="ForticlientOwnFile">ForticlientOwnFile</a>: <i>
      - <a href="forticlientownfiledefinition.md">ForticlientOwnFileDefinition</a></i>
<a href="#forticlientregistryentry" title="ForticlientRegistryEntry">ForticlientRegistryEntry</a>: <i>
      - <a href="forticlientregistryentrydefinition.md">ForticlientRegistryEntryDefinition</a></i>
<a href="#forticlientrunningapp" title="ForticlientRunningApp">ForticlientRunningApp</a>: <i>
      - <a href="forticlientrunningappdefinition.md">ForticlientRunningAppDefinition</a></i>
</pre>

## Properties

#### AvRealtimeProtection

Enable/disable FortiClient AntiVirus real-time protection. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvSignatureUpToDate

Enable/disable FortiClient AV signature updates. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientApplicationFirewall

Enable/disable the FortiClient application firewall. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientApplicationFirewallList

FortiClient application firewall rule list.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientAv

Enable/disable FortiClient AntiVirus scanning. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientEmsCompliance

Enable/disable FortiClient Enterprise Management Server (EMS) compliance. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientEmsComplianceAction

FortiClient EMS compliance action. Valid values: `block`, `warning`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientLinuxVer

Minimum FortiClient Linux version.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientLogUpload

Enable/disable uploading FortiClient logs. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientLogUploadLevel

Select the FortiClient logs to upload. Valid values: `traffic`, `vulnerability`, `event`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientLogUploadServer

IP address or FQDN of the server to which to upload FortiClient logs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientMacVer

Minimum FortiClient Mac OS version.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientMinimumSoftwareVersion

Enable/disable requiring clients to run FortiClient with a minimum software version number. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientRegistrationComplianceAction

FortiClient registration compliance action. Valid values: `block`, `warning`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientSecurityPosture

Enable/disable FortiClient security posture check options. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientSecurityPostureComplianceAction

FortiClient security posture compliance action. Valid values: `block`, `warning`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientSystemCompliance

Enable/disable enforcement of FortiClient system compliance. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientSystemComplianceAction

Block or warn clients not compliant with FortiClient requirements. Valid values: `block`, `warning`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientVulnScan

Enable/disable FortiClient vulnerability scanning. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientVulnScanComplianceAction

FortiClient vulnerability compliance action. Valid values: `block`, `warning`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientVulnScanEnforce

Configure the level of the vulnerability found that causes a FortiClient vulnerability compliance action. Valid values: `critical`, `high`, `medium`, `low`, `info`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientVulnScanEnforceGrace

FortiClient vulnerability scan enforcement grace period (0 - 30 days, default = 1).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientVulnScanExempt

Enable/disable compliance exemption for vulnerabilities that cannot be patched automatically. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientWf

Enable/disable FortiClient web filtering. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientWfProfile

The FortiClient web filter profile to apply.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientWinVer

Minimum FortiClient Windows version.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsAvSoftwareInstalled

Enable/disable checking for OS recognized AntiVirus software. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SandboxAddress

FortiSandbox address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SandboxAnalysis

Enable/disable sending files to FortiSandbox for analysis. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientEmsEntries

_Required_: No

_Type_: List of <a href="forticlientemsentriesdefinition.md">ForticlientEmsEntriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientOperatingSystem

_Required_: No

_Type_: List of <a href="forticlientoperatingsystemdefinition.md">ForticlientOperatingSystemDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientOwnFile

_Required_: No

_Type_: List of <a href="forticlientownfiledefinition.md">ForticlientOwnFileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientRegistryEntry

_Required_: No

_Type_: List of <a href="forticlientregistryentrydefinition.md">ForticlientRegistryEntryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientRunningApp

_Required_: No

_Type_: List of <a href="forticlientrunningappdefinition.md">ForticlientRunningAppDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

