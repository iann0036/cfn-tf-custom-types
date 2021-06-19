# TF::FortiOS::AntivirusProfile

Configure AntiVirus profiles.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::AntivirusProfile",
    "Properties" : {
        "<a href="#analyticsacceptfiletype" title="AnalyticsAcceptFiletype">AnalyticsAcceptFiletype</a>" : <i>Double</i>,
        "<a href="#analyticsblfiletype" title="AnalyticsBlFiletype">AnalyticsBlFiletype</a>" : <i>Double</i>,
        "<a href="#analyticsdb" title="AnalyticsDb">AnalyticsDb</a>" : <i>String</i>,
        "<a href="#analyticsignorefiletype" title="AnalyticsIgnoreFiletype">AnalyticsIgnoreFiletype</a>" : <i>Double</i>,
        "<a href="#analyticsmaxupload" title="AnalyticsMaxUpload">AnalyticsMaxUpload</a>" : <i>Double</i>,
        "<a href="#analyticswlfiletype" title="AnalyticsWlFiletype">AnalyticsWlFiletype</a>" : <i>Double</i>,
        "<a href="#avblocklog" title="AvBlockLog">AvBlockLog</a>" : <i>String</i>,
        "<a href="#avviruslog" title="AvVirusLog">AvVirusLog</a>" : <i>String</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#extendedlog" title="ExtendedLog">ExtendedLog</a>" : <i>String</i>,
        "<a href="#featureset" title="FeatureSet">FeatureSet</a>" : <i>String</i>,
        "<a href="#ftgdanalytics" title="FtgdAnalytics">FtgdAnalytics</a>" : <i>String</i>,
        "<a href="#inspectionmode" title="InspectionMode">InspectionMode</a>" : <i>String</i>,
        "<a href="#mobilemalwaredb" title="MobileMalwareDb">MobileMalwareDb</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#replacemsggroup" title="ReplacemsgGroup">ReplacemsgGroup</a>" : <i>String</i>,
        "<a href="#scanmode" title="ScanMode">ScanMode</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#cifs" title="Cifs">Cifs</a>" : <i>[ <a href="cifsdefinition.md">CifsDefinition</a>, ... ]</i>,
        "<a href="#contentdisarm" title="ContentDisarm">ContentDisarm</a>" : <i>[ <a href="contentdisarmdefinition.md">ContentDisarmDefinition</a>, ... ]</i>,
        "<a href="#ftp" title="Ftp">Ftp</a>" : <i>[ <a href="ftpdefinition.md">FtpDefinition</a>, ... ]</i>,
        "<a href="#http" title="Http">Http</a>" : <i>[ <a href="httpdefinition.md">HttpDefinition</a>, ... ]</i>,
        "<a href="#imap" title="Imap">Imap</a>" : <i>[ <a href="imapdefinition.md">ImapDefinition</a>, ... ]</i>,
        "<a href="#mapi" title="Mapi">Mapi</a>" : <i>[ <a href="mapidefinition.md">MapiDefinition</a>, ... ]</i>,
        "<a href="#nacquar" title="NacQuar">NacQuar</a>" : <i>[ <a href="nacquardefinition.md">NacQuarDefinition</a>, ... ]</i>,
        "<a href="#nntp" title="Nntp">Nntp</a>" : <i>[ <a href="nntpdefinition.md">NntpDefinition</a>, ... ]</i>,
        "<a href="#outbreakprevention" title="OutbreakPrevention">OutbreakPrevention</a>" : <i>[ <a href="outbreakpreventiondefinition.md">OutbreakPreventionDefinition</a>, ... ]</i>,
        "<a href="#pop3" title="Pop3">Pop3</a>" : <i>[ <a href="pop3definition.md">Pop3Definition</a>, ... ]</i>,
        "<a href="#smb" title="Smb">Smb</a>" : <i>[ <a href="smbdefinition.md">SmbDefinition</a>, ... ]</i>,
        "<a href="#smtp" title="Smtp">Smtp</a>" : <i>[ <a href="smtpdefinition.md">SmtpDefinition</a>, ... ]</i>,
        "<a href="#ssh" title="Ssh">Ssh</a>" : <i>[ <a href="sshdefinition.md">SshDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::AntivirusProfile
Properties:
    <a href="#analyticsacceptfiletype" title="AnalyticsAcceptFiletype">AnalyticsAcceptFiletype</a>: <i>Double</i>
    <a href="#analyticsblfiletype" title="AnalyticsBlFiletype">AnalyticsBlFiletype</a>: <i>Double</i>
    <a href="#analyticsdb" title="AnalyticsDb">AnalyticsDb</a>: <i>String</i>
    <a href="#analyticsignorefiletype" title="AnalyticsIgnoreFiletype">AnalyticsIgnoreFiletype</a>: <i>Double</i>
    <a href="#analyticsmaxupload" title="AnalyticsMaxUpload">AnalyticsMaxUpload</a>: <i>Double</i>
    <a href="#analyticswlfiletype" title="AnalyticsWlFiletype">AnalyticsWlFiletype</a>: <i>Double</i>
    <a href="#avblocklog" title="AvBlockLog">AvBlockLog</a>: <i>String</i>
    <a href="#avviruslog" title="AvVirusLog">AvVirusLog</a>: <i>String</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#extendedlog" title="ExtendedLog">ExtendedLog</a>: <i>String</i>
    <a href="#featureset" title="FeatureSet">FeatureSet</a>: <i>String</i>
    <a href="#ftgdanalytics" title="FtgdAnalytics">FtgdAnalytics</a>: <i>String</i>
    <a href="#inspectionmode" title="InspectionMode">InspectionMode</a>: <i>String</i>
    <a href="#mobilemalwaredb" title="MobileMalwareDb">MobileMalwareDb</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#replacemsggroup" title="ReplacemsgGroup">ReplacemsgGroup</a>: <i>String</i>
    <a href="#scanmode" title="ScanMode">ScanMode</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#cifs" title="Cifs">Cifs</a>: <i>
      - <a href="cifsdefinition.md">CifsDefinition</a></i>
    <a href="#contentdisarm" title="ContentDisarm">ContentDisarm</a>: <i>
      - <a href="contentdisarmdefinition.md">ContentDisarmDefinition</a></i>
    <a href="#ftp" title="Ftp">Ftp</a>: <i>
      - <a href="ftpdefinition.md">FtpDefinition</a></i>
    <a href="#http" title="Http">Http</a>: <i>
      - <a href="httpdefinition.md">HttpDefinition</a></i>
    <a href="#imap" title="Imap">Imap</a>: <i>
      - <a href="imapdefinition.md">ImapDefinition</a></i>
    <a href="#mapi" title="Mapi">Mapi</a>: <i>
      - <a href="mapidefinition.md">MapiDefinition</a></i>
    <a href="#nacquar" title="NacQuar">NacQuar</a>: <i>
      - <a href="nacquardefinition.md">NacQuarDefinition</a></i>
    <a href="#nntp" title="Nntp">Nntp</a>: <i>
      - <a href="nntpdefinition.md">NntpDefinition</a></i>
    <a href="#outbreakprevention" title="OutbreakPrevention">OutbreakPrevention</a>: <i>
      - <a href="outbreakpreventiondefinition.md">OutbreakPreventionDefinition</a></i>
    <a href="#pop3" title="Pop3">Pop3</a>: <i>
      - <a href="pop3definition.md">Pop3Definition</a></i>
    <a href="#smb" title="Smb">Smb</a>: <i>
      - <a href="smbdefinition.md">SmbDefinition</a></i>
    <a href="#smtp" title="Smtp">Smtp</a>: <i>
      - <a href="smtpdefinition.md">SmtpDefinition</a></i>
    <a href="#ssh" title="Ssh">Ssh</a>: <i>
      - <a href="sshdefinition.md">SshDefinition</a></i>
</pre>

## Properties

#### AnalyticsAcceptFiletype

Only submit files matching this DLP file-pattern to FortiSandbox.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnalyticsBlFiletype

Only submit files matching this DLP file-pattern to FortiSandbox.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnalyticsDb

Enable/disable using the FortiSandbox signature database to supplement the AV signature databases. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnalyticsIgnoreFiletype

Do not submit files matching this DLP file-pattern to FortiSandbox.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnalyticsMaxUpload

Maximum size of files that can be uploaded to FortiSandbox (1 - 395 MBytes, default = 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnalyticsWlFiletype

Do not submit files matching this DLP file-pattern to FortiSandbox.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvBlockLog

Enable/disable logging for AntiVirus file blocking. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvVirusLog

Enable/disable AntiVirus logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedLog

Enable/disable extended logging for antivirus. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FeatureSet

Flow/proxy feature set. Valid values: `flow`, `proxy`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FtgdAnalytics

Settings to control which files are uploaded to FortiSandbox. Valid values: `disable`, `suspicious`, `everything`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InspectionMode

Inspection mode. Valid values: `proxy`, `flow-based`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MobileMalwareDb

Enable/disable using the mobile malware signature database. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Profile name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplacemsgGroup

Replacement message group customized for this profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScanMode

Choose between full scan mode and quick scan mode.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cifs

_Required_: No

_Type_: List of <a href="cifsdefinition.md">CifsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentDisarm

_Required_: No

_Type_: List of <a href="contentdisarmdefinition.md">ContentDisarmDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ftp

_Required_: No

_Type_: List of <a href="ftpdefinition.md">FtpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http

_Required_: No

_Type_: List of <a href="httpdefinition.md">HttpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Imap

_Required_: No

_Type_: List of <a href="imapdefinition.md">ImapDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mapi

_Required_: No

_Type_: List of <a href="mapidefinition.md">MapiDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NacQuar

_Required_: No

_Type_: List of <a href="nacquardefinition.md">NacQuarDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nntp

_Required_: No

_Type_: List of <a href="nntpdefinition.md">NntpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutbreakPrevention

_Required_: No

_Type_: List of <a href="outbreakpreventiondefinition.md">OutbreakPreventionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pop3

_Required_: No

_Type_: List of <a href="pop3definition.md">Pop3Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Smb

_Required_: No

_Type_: List of <a href="smbdefinition.md">SmbDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Smtp

_Required_: No

_Type_: List of <a href="smtpdefinition.md">SmtpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ssh

_Required_: No

_Type_: List of <a href="sshdefinition.md">SshDefinition</a>

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

