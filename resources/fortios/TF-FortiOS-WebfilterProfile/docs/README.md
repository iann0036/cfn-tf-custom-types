# TF::FortiOS::WebfilterProfile

Configure Web filter profiles.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::WebfilterProfile",
    "Properties" : {
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#extendedlog" title="ExtendedLog">ExtendedLog</a>" : <i>String</i>,
        "<a href="#featureset" title="FeatureSet">FeatureSet</a>" : <i>String</i>,
        "<a href="#httpsreplacemsg" title="HttpsReplacemsg">HttpsReplacemsg</a>" : <i>String</i>,
        "<a href="#inspectionmode" title="InspectionMode">InspectionMode</a>" : <i>String</i>,
        "<a href="#logallurl" title="LogAllUrl">LogAllUrl</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#options" title="Options">Options</a>" : <i>String</i>,
        "<a href="#ovrdperm" title="OvrdPerm">OvrdPerm</a>" : <i>String</i>,
        "<a href="#postaction" title="PostAction">PostAction</a>" : <i>String</i>,
        "<a href="#replacemsggroup" title="ReplacemsgGroup">ReplacemsgGroup</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#webantiphishinglog" title="WebAntiphishingLog">WebAntiphishingLog</a>" : <i>String</i>,
        "<a href="#webcontentlog" title="WebContentLog">WebContentLog</a>" : <i>String</i>,
        "<a href="#webextendedallactionlog" title="WebExtendedAllActionLog">WebExtendedAllActionLog</a>" : <i>String</i>,
        "<a href="#webfilteractivexlog" title="WebFilterActivexLog">WebFilterActivexLog</a>" : <i>String</i>,
        "<a href="#webfilterappletlog" title="WebFilterAppletLog">WebFilterAppletLog</a>" : <i>String</i>,
        "<a href="#webfiltercommandblocklog" title="WebFilterCommandBlockLog">WebFilterCommandBlockLog</a>" : <i>String</i>,
        "<a href="#webfiltercookielog" title="WebFilterCookieLog">WebFilterCookieLog</a>" : <i>String</i>,
        "<a href="#webfiltercookieremovallog" title="WebFilterCookieRemovalLog">WebFilterCookieRemovalLog</a>" : <i>String</i>,
        "<a href="#webfilterjslog" title="WebFilterJsLog">WebFilterJsLog</a>" : <i>String</i>,
        "<a href="#webfilterjscriptlog" title="WebFilterJscriptLog">WebFilterJscriptLog</a>" : <i>String</i>,
        "<a href="#webfilterrefererlog" title="WebFilterRefererLog">WebFilterRefererLog</a>" : <i>String</i>,
        "<a href="#webfilterunknownlog" title="WebFilterUnknownLog">WebFilterUnknownLog</a>" : <i>String</i>,
        "<a href="#webfiltervbslog" title="WebFilterVbsLog">WebFilterVbsLog</a>" : <i>String</i>,
        "<a href="#webftgderrlog" title="WebFtgdErrLog">WebFtgdErrLog</a>" : <i>String</i>,
        "<a href="#webftgdquotausage" title="WebFtgdQuotaUsage">WebFtgdQuotaUsage</a>" : <i>String</i>,
        "<a href="#webinvaliddomainlog" title="WebInvalidDomainLog">WebInvalidDomainLog</a>" : <i>String</i>,
        "<a href="#weburllog" title="WebUrlLog">WebUrlLog</a>" : <i>String</i>,
        "<a href="#wisp" title="Wisp">Wisp</a>" : <i>String</i>,
        "<a href="#wispalgorithm" title="WispAlgorithm">WispAlgorithm</a>" : <i>String</i>,
        "<a href="#youtubechannelstatus" title="YoutubeChannelStatus">YoutubeChannelStatus</a>" : <i>String</i>,
        "<a href="#antiphish" title="Antiphish">Antiphish</a>" : <i>[ <a href="antiphishdefinition.md">AntiphishDefinition</a>, ... ]</i>,
        "<a href="#filefilter" title="FileFilter">FileFilter</a>" : <i>[ <a href="filefilterdefinition.md">FileFilterDefinition</a>, ... ]</i>,
        "<a href="#ftgdwf" title="FtgdWf">FtgdWf</a>" : <i>[ <a href="ftgdwfdefinition.md">FtgdWfDefinition</a>, ... ]</i>,
        "<a href="#override" title="Override">Override</a>" : <i>[ <a href="overridedefinition.md">OverrideDefinition</a>, ... ]</i>,
        "<a href="#web" title="Web">Web</a>" : <i>[ <a href="webdefinition.md">WebDefinition</a>, ... ]</i>,
        "<a href="#wispservers" title="WispServers">WispServers</a>" : <i>[ <a href="wispserversdefinition.md">WispServersDefinition</a>, ... ]</i>,
        "<a href="#youtubechannelfilter" title="YoutubeChannelFilter">YoutubeChannelFilter</a>" : <i>[ <a href="youtubechannelfilterdefinition.md">YoutubeChannelFilterDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::WebfilterProfile
Properties:
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#extendedlog" title="ExtendedLog">ExtendedLog</a>: <i>String</i>
    <a href="#featureset" title="FeatureSet">FeatureSet</a>: <i>String</i>
    <a href="#httpsreplacemsg" title="HttpsReplacemsg">HttpsReplacemsg</a>: <i>String</i>
    <a href="#inspectionmode" title="InspectionMode">InspectionMode</a>: <i>String</i>
    <a href="#logallurl" title="LogAllUrl">LogAllUrl</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#options" title="Options">Options</a>: <i>String</i>
    <a href="#ovrdperm" title="OvrdPerm">OvrdPerm</a>: <i>String</i>
    <a href="#postaction" title="PostAction">PostAction</a>: <i>String</i>
    <a href="#replacemsggroup" title="ReplacemsgGroup">ReplacemsgGroup</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#webantiphishinglog" title="WebAntiphishingLog">WebAntiphishingLog</a>: <i>String</i>
    <a href="#webcontentlog" title="WebContentLog">WebContentLog</a>: <i>String</i>
    <a href="#webextendedallactionlog" title="WebExtendedAllActionLog">WebExtendedAllActionLog</a>: <i>String</i>
    <a href="#webfilteractivexlog" title="WebFilterActivexLog">WebFilterActivexLog</a>: <i>String</i>
    <a href="#webfilterappletlog" title="WebFilterAppletLog">WebFilterAppletLog</a>: <i>String</i>
    <a href="#webfiltercommandblocklog" title="WebFilterCommandBlockLog">WebFilterCommandBlockLog</a>: <i>String</i>
    <a href="#webfiltercookielog" title="WebFilterCookieLog">WebFilterCookieLog</a>: <i>String</i>
    <a href="#webfiltercookieremovallog" title="WebFilterCookieRemovalLog">WebFilterCookieRemovalLog</a>: <i>String</i>
    <a href="#webfilterjslog" title="WebFilterJsLog">WebFilterJsLog</a>: <i>String</i>
    <a href="#webfilterjscriptlog" title="WebFilterJscriptLog">WebFilterJscriptLog</a>: <i>String</i>
    <a href="#webfilterrefererlog" title="WebFilterRefererLog">WebFilterRefererLog</a>: <i>String</i>
    <a href="#webfilterunknownlog" title="WebFilterUnknownLog">WebFilterUnknownLog</a>: <i>String</i>
    <a href="#webfiltervbslog" title="WebFilterVbsLog">WebFilterVbsLog</a>: <i>String</i>
    <a href="#webftgderrlog" title="WebFtgdErrLog">WebFtgdErrLog</a>: <i>String</i>
    <a href="#webftgdquotausage" title="WebFtgdQuotaUsage">WebFtgdQuotaUsage</a>: <i>String</i>
    <a href="#webinvaliddomainlog" title="WebInvalidDomainLog">WebInvalidDomainLog</a>: <i>String</i>
    <a href="#weburllog" title="WebUrlLog">WebUrlLog</a>: <i>String</i>
    <a href="#wisp" title="Wisp">Wisp</a>: <i>String</i>
    <a href="#wispalgorithm" title="WispAlgorithm">WispAlgorithm</a>: <i>String</i>
    <a href="#youtubechannelstatus" title="YoutubeChannelStatus">YoutubeChannelStatus</a>: <i>String</i>
    <a href="#antiphish" title="Antiphish">Antiphish</a>: <i>
      - <a href="antiphishdefinition.md">AntiphishDefinition</a></i>
    <a href="#filefilter" title="FileFilter">FileFilter</a>: <i>
      - <a href="filefilterdefinition.md">FileFilterDefinition</a></i>
    <a href="#ftgdwf" title="FtgdWf">FtgdWf</a>: <i>
      - <a href="ftgdwfdefinition.md">FtgdWfDefinition</a></i>
    <a href="#override" title="Override">Override</a>: <i>
      - <a href="overridedefinition.md">OverrideDefinition</a></i>
    <a href="#web" title="Web">Web</a>: <i>
      - <a href="webdefinition.md">WebDefinition</a></i>
    <a href="#wispservers" title="WispServers">WispServers</a>: <i>
      - <a href="wispserversdefinition.md">WispServersDefinition</a></i>
    <a href="#youtubechannelfilter" title="YoutubeChannelFilter">YoutubeChannelFilter</a>: <i>
      - <a href="youtubechannelfilterdefinition.md">YoutubeChannelFilterDefinition</a></i>
</pre>

## Properties

#### Comment

Optional comments.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedLog

Enable/disable extended logging for web filtering. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FeatureSet

Flow/proxy feature set. Valid values: `flow`, `proxy`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsReplacemsg

Enable replacement messages for HTTPS. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InspectionMode

Web filtering inspection mode. Valid values: `proxy`, `flow-based`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAllUrl

Enable/disable logging all URLs visited. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Profile name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

Options.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OvrdPerm

Permitted override types. Valid values: `bannedword-override`, `urlfilter-override`, `fortiguard-wf-override`, `contenttype-check-override`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostAction

Action taken for HTTP POST traffic. Valid values: `normal`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplacemsgGroup

Replacement message group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebAntiphishingLog

Enable/disable logging of AntiPhishing checks. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebContentLog

Enable/disable logging logging blocked web content. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebExtendedAllActionLog

Enable/disable extended any filter action logging for web filtering. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebFilterActivexLog

Enable/disable logging ActiveX. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebFilterAppletLog

Enable/disable logging Java applets. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebFilterCommandBlockLog

Enable/disable logging blocked commands. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebFilterCookieLog

Enable/disable logging cookie filtering. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebFilterCookieRemovalLog

Enable/disable logging blocked cookies. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebFilterJsLog

Enable/disable logging Java scripts. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebFilterJscriptLog

Enable/disable logging JScripts. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebFilterRefererLog

Enable/disable logging referrers. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebFilterUnknownLog

Enable/disable logging unknown scripts. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebFilterVbsLog

Enable/disable logging VBS scripts. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebFtgdErrLog

Enable/disable logging rating errors. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebFtgdQuotaUsage

Enable/disable logging daily quota usage. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebInvalidDomainLog

Enable/disable logging invalid domain names. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebUrlLog

Enable/disable logging URL filtering. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Wisp

Enable/disable web proxy WISP. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WispAlgorithm

WISP server selection algorithm. Valid values: `primary-secondary`, `round-robin`, `auto-learning`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### YoutubeChannelStatus

YouTube channel filter status.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Antiphish

_Required_: No

_Type_: List of <a href="antiphishdefinition.md">AntiphishDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileFilter

_Required_: No

_Type_: List of <a href="filefilterdefinition.md">FileFilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FtgdWf

_Required_: No

_Type_: List of <a href="ftgdwfdefinition.md">FtgdWfDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Override

_Required_: No

_Type_: List of <a href="overridedefinition.md">OverrideDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Web

_Required_: No

_Type_: List of <a href="webdefinition.md">WebDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WispServers

_Required_: No

_Type_: List of <a href="wispserversdefinition.md">WispServersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### YoutubeChannelFilter

_Required_: No

_Type_: List of <a href="youtubechannelfilterdefinition.md">YoutubeChannelFilterDefinition</a>

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

