# TF::FortiOS::SpamfilterProfile

Configure AntiSpam profiles. Applies to FortiOS Version `<= 6.2.0`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SpamfilterProfile",
    "Properties" : {
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#external" title="External">External</a>" : <i>String</i>,
        "<a href="#flowbased" title="FlowBased">FlowBased</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#options" title="Options">Options</a>" : <i>String</i>,
        "<a href="#replacemsggroup" title="ReplacemsgGroup">ReplacemsgGroup</a>" : <i>String</i>,
        "<a href="#spambwltable" title="SpamBwlTable">SpamBwlTable</a>" : <i>Double</i>,
        "<a href="#spambwordtable" title="SpamBwordTable">SpamBwordTable</a>" : <i>Double</i>,
        "<a href="#spambwordthreshold" title="SpamBwordThreshold">SpamBwordThreshold</a>" : <i>Double</i>,
        "<a href="#spamfiltering" title="SpamFiltering">SpamFiltering</a>" : <i>String</i>,
        "<a href="#spamiptrusttable" title="SpamIptrustTable">SpamIptrustTable</a>" : <i>Double</i>,
        "<a href="#spamlog" title="SpamLog">SpamLog</a>" : <i>String</i>,
        "<a href="#spamlogfortiguardresponse" title="SpamLogFortiguardResponse">SpamLogFortiguardResponse</a>" : <i>String</i>,
        "<a href="#spammheadertable" title="SpamMheaderTable">SpamMheaderTable</a>" : <i>Double</i>,
        "<a href="#spamrbltable" title="SpamRblTable">SpamRblTable</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#gmail" title="Gmail">Gmail</a>" : <i>[ <a href="gmaildefinition.md">GmailDefinition</a>, ... ]</i>,
        "<a href="#imap" title="Imap">Imap</a>" : <i>[ <a href="imapdefinition.md">ImapDefinition</a>, ... ]</i>,
        "<a href="#mapi" title="Mapi">Mapi</a>" : <i>[ <a href="mapidefinition.md">MapiDefinition</a>, ... ]</i>,
        "<a href="#msnhotmail" title="MsnHotmail">MsnHotmail</a>" : <i>[ <a href="msnhotmaildefinition.md">MsnHotmailDefinition</a>, ... ]</i>,
        "<a href="#pop3" title="Pop3">Pop3</a>" : <i>[ <a href="pop3definition.md">Pop3Definition</a>, ... ]</i>,
        "<a href="#smtp" title="Smtp">Smtp</a>" : <i>[ <a href="smtpdefinition.md">SmtpDefinition</a>, ... ]</i>,
        "<a href="#yahoomail" title="YahooMail">YahooMail</a>" : <i>[ <a href="yahoomaildefinition.md">YahooMailDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SpamfilterProfile
Properties:
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#external" title="External">External</a>: <i>String</i>
    <a href="#flowbased" title="FlowBased">FlowBased</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#options" title="Options">Options</a>: <i>String</i>
    <a href="#replacemsggroup" title="ReplacemsgGroup">ReplacemsgGroup</a>: <i>String</i>
    <a href="#spambwltable" title="SpamBwlTable">SpamBwlTable</a>: <i>Double</i>
    <a href="#spambwordtable" title="SpamBwordTable">SpamBwordTable</a>: <i>Double</i>
    <a href="#spambwordthreshold" title="SpamBwordThreshold">SpamBwordThreshold</a>: <i>Double</i>
    <a href="#spamfiltering" title="SpamFiltering">SpamFiltering</a>: <i>String</i>
    <a href="#spamiptrusttable" title="SpamIptrustTable">SpamIptrustTable</a>: <i>Double</i>
    <a href="#spamlog" title="SpamLog">SpamLog</a>: <i>String</i>
    <a href="#spamlogfortiguardresponse" title="SpamLogFortiguardResponse">SpamLogFortiguardResponse</a>: <i>String</i>
    <a href="#spammheadertable" title="SpamMheaderTable">SpamMheaderTable</a>: <i>Double</i>
    <a href="#spamrbltable" title="SpamRblTable">SpamRblTable</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#gmail" title="Gmail">Gmail</a>: <i>
      - <a href="gmaildefinition.md">GmailDefinition</a></i>
    <a href="#imap" title="Imap">Imap</a>: <i>
      - <a href="imapdefinition.md">ImapDefinition</a></i>
    <a href="#mapi" title="Mapi">Mapi</a>: <i>
      - <a href="mapidefinition.md">MapiDefinition</a></i>
    <a href="#msnhotmail" title="MsnHotmail">MsnHotmail</a>: <i>
      - <a href="msnhotmaildefinition.md">MsnHotmailDefinition</a></i>
    <a href="#pop3" title="Pop3">Pop3</a>: <i>
      - <a href="pop3definition.md">Pop3Definition</a></i>
    <a href="#smtp" title="Smtp">Smtp</a>: <i>
      - <a href="smtpdefinition.md">SmtpDefinition</a></i>
    <a href="#yahoomail" title="YahooMail">YahooMail</a>: <i>
      - <a href="yahoomaildefinition.md">YahooMailDefinition</a></i>
</pre>

## Properties

#### Comment

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### External

Enable/disable external Email inspection. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlowBased

Enable/disable flow-based spam filtering. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Profile name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

Options. Valid values: `bannedword`, `spambwl`, `spamfsip`, `spamfssubmit`, `spamfschksum`, `spamfsurl`, `spamhelodns`, `spamraddrdns`, `spamrbl`, `spamhdrcheck`, `spamfsphish`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplacemsgGroup

Replacement message group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpamBwlTable

Anti-spam black/white list table ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpamBwordTable

Anti-spam banned word table ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpamBwordThreshold

Spam banned word threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpamFiltering

Enable/disable spam filtering. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpamIptrustTable

Anti-spam IP trust table ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpamLog

Enable/disable spam logging for email filtering. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpamLogFortiguardResponse

Enable/disable logging FortiGuard spam response. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpamMheaderTable

Anti-spam MIME header table ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpamRblTable

Anti-spam DNSBL table ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gmail

_Required_: No

_Type_: List of <a href="gmaildefinition.md">GmailDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Imap

_Required_: No

_Type_: List of <a href="imapdefinition.md">ImapDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mapi

_Required_: No

_Type_: List of <a href="mapidefinition.md">MapiDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MsnHotmail

_Required_: No

_Type_: List of <a href="msnhotmaildefinition.md">MsnHotmailDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pop3

_Required_: No

_Type_: List of <a href="pop3definition.md">Pop3Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Smtp

_Required_: No

_Type_: List of <a href="smtpdefinition.md">SmtpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### YahooMail

_Required_: No

_Type_: List of <a href="yahoomaildefinition.md">YahooMailDefinition</a>

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

