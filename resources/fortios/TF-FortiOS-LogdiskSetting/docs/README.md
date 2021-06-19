# TF::FortiOS::LogdiskSetting

Settings for local disk logging.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::LogdiskSetting",
    "Properties" : {
        "<a href="#diskfull" title="Diskfull">Diskfull</a>" : <i>String</i>,
        "<a href="#dlparchivequota" title="DlpArchiveQuota">DlpArchiveQuota</a>" : <i>Double</i>,
        "<a href="#fullfinalwarningthreshold" title="FullFinalWarningThreshold">FullFinalWarningThreshold</a>" : <i>Double</i>,
        "<a href="#fullfirstwarningthreshold" title="FullFirstWarningThreshold">FullFirstWarningThreshold</a>" : <i>Double</i>,
        "<a href="#fullsecondwarningthreshold" title="FullSecondWarningThreshold">FullSecondWarningThreshold</a>" : <i>Double</i>,
        "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
        "<a href="#interfaceselectmethod" title="InterfaceSelectMethod">InterfaceSelectMethod</a>" : <i>String</i>,
        "<a href="#ipsarchive" title="IpsArchive">IpsArchive</a>" : <i>String</i>,
        "<a href="#logquota" title="LogQuota">LogQuota</a>" : <i>Double</i>,
        "<a href="#maxlogfilesize" title="MaxLogFileSize">MaxLogFileSize</a>" : <i>Double</i>,
        "<a href="#maxpolicypacketcapturesize" title="MaxPolicyPacketCaptureSize">MaxPolicyPacketCaptureSize</a>" : <i>Double</i>,
        "<a href="#maximumlogage" title="MaximumLogAge">MaximumLogAge</a>" : <i>Double</i>,
        "<a href="#reportquota" title="ReportQuota">ReportQuota</a>" : <i>Double</i>,
        "<a href="#rollday" title="RollDay">RollDay</a>" : <i>String</i>,
        "<a href="#rollschedule" title="RollSchedule">RollSchedule</a>" : <i>String</i>,
        "<a href="#rolltime" title="RollTime">RollTime</a>" : <i>String</i>,
        "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#upload" title="Upload">Upload</a>" : <i>String</i>,
        "<a href="#uploaddeletefiles" title="UploadDeleteFiles">UploadDeleteFiles</a>" : <i>String</i>,
        "<a href="#uploaddestination" title="UploadDestination">UploadDestination</a>" : <i>String</i>,
        "<a href="#uploadsslconn" title="UploadSslConn">UploadSslConn</a>" : <i>String</i>,
        "<a href="#uploaddir" title="Uploaddir">Uploaddir</a>" : <i>String</i>,
        "<a href="#uploadip" title="Uploadip">Uploadip</a>" : <i>String</i>,
        "<a href="#uploadpass" title="Uploadpass">Uploadpass</a>" : <i>String</i>,
        "<a href="#uploadport" title="Uploadport">Uploadport</a>" : <i>Double</i>,
        "<a href="#uploadsched" title="Uploadsched">Uploadsched</a>" : <i>String</i>,
        "<a href="#uploadtime" title="Uploadtime">Uploadtime</a>" : <i>String</i>,
        "<a href="#uploadtype" title="Uploadtype">Uploadtype</a>" : <i>String</i>,
        "<a href="#uploaduser" title="Uploaduser">Uploaduser</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::LogdiskSetting
Properties:
    <a href="#diskfull" title="Diskfull">Diskfull</a>: <i>String</i>
    <a href="#dlparchivequota" title="DlpArchiveQuota">DlpArchiveQuota</a>: <i>Double</i>
    <a href="#fullfinalwarningthreshold" title="FullFinalWarningThreshold">FullFinalWarningThreshold</a>: <i>Double</i>
    <a href="#fullfirstwarningthreshold" title="FullFirstWarningThreshold">FullFirstWarningThreshold</a>: <i>Double</i>
    <a href="#fullsecondwarningthreshold" title="FullSecondWarningThreshold">FullSecondWarningThreshold</a>: <i>Double</i>
    <a href="#interface" title="Interface">Interface</a>: <i>String</i>
    <a href="#interfaceselectmethod" title="InterfaceSelectMethod">InterfaceSelectMethod</a>: <i>String</i>
    <a href="#ipsarchive" title="IpsArchive">IpsArchive</a>: <i>String</i>
    <a href="#logquota" title="LogQuota">LogQuota</a>: <i>Double</i>
    <a href="#maxlogfilesize" title="MaxLogFileSize">MaxLogFileSize</a>: <i>Double</i>
    <a href="#maxpolicypacketcapturesize" title="MaxPolicyPacketCaptureSize">MaxPolicyPacketCaptureSize</a>: <i>Double</i>
    <a href="#maximumlogage" title="MaximumLogAge">MaximumLogAge</a>: <i>Double</i>
    <a href="#reportquota" title="ReportQuota">ReportQuota</a>: <i>Double</i>
    <a href="#rollday" title="RollDay">RollDay</a>: <i>String</i>
    <a href="#rollschedule" title="RollSchedule">RollSchedule</a>: <i>String</i>
    <a href="#rolltime" title="RollTime">RollTime</a>: <i>String</i>
    <a href="#sourceip" title="SourceIp">SourceIp</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#upload" title="Upload">Upload</a>: <i>String</i>
    <a href="#uploaddeletefiles" title="UploadDeleteFiles">UploadDeleteFiles</a>: <i>String</i>
    <a href="#uploaddestination" title="UploadDestination">UploadDestination</a>: <i>String</i>
    <a href="#uploadsslconn" title="UploadSslConn">UploadSslConn</a>: <i>String</i>
    <a href="#uploaddir" title="Uploaddir">Uploaddir</a>: <i>String</i>
    <a href="#uploadip" title="Uploadip">Uploadip</a>: <i>String</i>
    <a href="#uploadpass" title="Uploadpass">Uploadpass</a>: <i>String</i>
    <a href="#uploadport" title="Uploadport">Uploadport</a>: <i>Double</i>
    <a href="#uploadsched" title="Uploadsched">Uploadsched</a>: <i>String</i>
    <a href="#uploadtime" title="Uploadtime">Uploadtime</a>: <i>String</i>
    <a href="#uploadtype" title="Uploadtype">Uploadtype</a>: <i>String</i>
    <a href="#uploaduser" title="Uploaduser">Uploaduser</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### Diskfull

Action to take when disk is full. The system can overwrite the oldest log messages or stop logging when the disk is full (default = overwrite). Valid values: `overwrite`, `nolog`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DlpArchiveQuota

DLP archive quota (MB).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FullFinalWarningThreshold

Log full final warning threshold as a percent (3 - 100, default = 95).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FullFirstWarningThreshold

Log full first warning threshold as a percent (1 - 98, default = 75).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FullSecondWarningThreshold

Log full second warning threshold as a percent (2 - 99, default = 90).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

Specify outgoing interface to reach server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceSelectMethod

Specify how to select outgoing interface to reach server. Valid values: `auto`, `sdwan`, `specify`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsArchive

Enable/disable IPS packet archiving to the local disk. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogQuota

Disk log quota (MB).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxLogFileSize

Maximum log file size before rolling (1 - 100 Mbytes).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPolicyPacketCaptureSize

Maximum size of policy sniffer in MB (0 means unlimited).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumLogAge

Delete log files older than (days).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReportQuota

Report quota (MB).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RollDay

Day of week on which to roll log file. Valid values: `sunday`, `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RollSchedule

Frequency to check log file for rolling. Valid values: `daily`, `weekly`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RollTime

Time of day to roll the log file (hh:mm).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

Source IP address to use for uploading disk log files.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable local disk logging. Valid values: `enable`, `disable`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Upload

Enable/disable uploading log files when they are rolled. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UploadDeleteFiles

Delete log files after uploading (default = enable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UploadDestination

The type of server to upload log files to. Only FTP is currently supported. Valid values: `ftp-server`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UploadSslConn

Enable/disable encrypted FTPS communication to upload log files. Valid values: `default`, `high`, `low`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uploaddir

The remote directory on the FTP server to upload log files to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uploadip

IP address of the FTP server to upload log files to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uploadpass

Password required to log into the FTP server to upload disk log files.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uploadport

TCP port to use for communicating with the FTP server (default = 21).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uploadsched

Set the schedule for uploading log files to the FTP server (default = disable = upload when rolling). Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uploadtime

Time of day at which log files are uploaded if uploadsched is enabled (hh:mm or hh).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uploadtype

Types of log files to upload. Separate multiple entries with a space.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uploaduser

Username required to log into the FTP server to upload disk log files.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

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

