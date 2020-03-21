# Terraform::OVH::DedicatedServerInstallTask Details

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#changelog" title="ChangeLog">ChangeLog</a>" : <i>String</i>,
    "<a href="#customhostname" title="CustomHostname">CustomHostname</a>" : <i>String</i>,
    "<a href="#diskgroupid" title="DiskGroupId">DiskGroupId</a>" : <i>Double</i>,
    "<a href="#installrtm" title="InstallRtm">InstallRtm</a>" : <i>Boolean</i>,
    "<a href="#installsqlserver" title="InstallSqlServer">InstallSqlServer</a>" : <i>Boolean</i>,
    "<a href="#language" title="Language">Language</a>" : <i>String</i>,
    "<a href="#noraid" title="NoRaid">NoRaid</a>" : <i>Boolean</i>,
    "<a href="#postinstallationscriptlink" title="PostInstallationScriptLink">PostInstallationScriptLink</a>" : <i>String</i>,
    "<a href="#postinstallationscriptreturn" title="PostInstallationScriptReturn">PostInstallationScriptReturn</a>" : <i>String</i>,
    "<a href="#resethwraid" title="ResetHwRaid">ResetHwRaid</a>" : <i>Boolean</i>,
    "<a href="#softraiddevices" title="SoftRaidDevices">SoftRaidDevices</a>" : <i>Double</i>,
    "<a href="#sshkeyname" title="SshKeyName">SshKeyName</a>" : <i>String</i>,
    "<a href="#usedistribkernel" title="UseDistribKernel">UseDistribKernel</a>" : <i>Boolean</i>,
    "<a href="#usespla" title="UseSpla">UseSpla</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#changelog" title="ChangeLog">ChangeLog</a>: <i>String</i>
<a href="#customhostname" title="CustomHostname">CustomHostname</a>: <i>String</i>
<a href="#diskgroupid" title="DiskGroupId">DiskGroupId</a>: <i>Double</i>
<a href="#installrtm" title="InstallRtm">InstallRtm</a>: <i>Boolean</i>
<a href="#installsqlserver" title="InstallSqlServer">InstallSqlServer</a>: <i>Boolean</i>
<a href="#language" title="Language">Language</a>: <i>String</i>
<a href="#noraid" title="NoRaid">NoRaid</a>: <i>Boolean</i>
<a href="#postinstallationscriptlink" title="PostInstallationScriptLink">PostInstallationScriptLink</a>: <i>String</i>
<a href="#postinstallationscriptreturn" title="PostInstallationScriptReturn">PostInstallationScriptReturn</a>: <i>String</i>
<a href="#resethwraid" title="ResetHwRaid">ResetHwRaid</a>: <i>Boolean</i>
<a href="#softraiddevices" title="SoftRaidDevices">SoftRaidDevices</a>: <i>Double</i>
<a href="#sshkeyname" title="SshKeyName">SshKeyName</a>: <i>String</i>
<a href="#usedistribkernel" title="UseDistribKernel">UseDistribKernel</a>: <i>Boolean</i>
<a href="#usespla" title="UseSpla">UseSpla</a>: <i>Boolean</i>
</pre>

## Properties

#### ChangeLog

Template change log details.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomHostname

Set up the server using the provided hostname instead of the default hostname.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskGroupId

Disk group id.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstallRtm

set to true to install RTM.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstallSqlServer

set to true to install sql server (Windows template only).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Language

language.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoRaid

set to true to disable RAID.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostInstallationScriptLink

Indicate the URL where your postinstall customisation script is located.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostInstallationScriptReturn

Indicate the string returned by your postinstall customisation script on successful execution. Advice: your script should return a unique validation string in case of succes. A good example is 'loh1Xee7eo OK OK OK UGh8Ang1Gu'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResetHwRaid

set to true to make a hardware raid reset.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SoftRaidDevices

soft raid devices.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeyName

Name of the ssh key that should be installed. Password login will be disabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseDistribKernel

Use the distribution's native kernel instead of the recommended OVH Kernel.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseSpla

set to true to use SPLA.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

