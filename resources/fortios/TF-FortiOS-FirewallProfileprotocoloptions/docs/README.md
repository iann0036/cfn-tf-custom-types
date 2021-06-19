# TF::FortiOS::FirewallProfileprotocoloptions

Configure protocol options.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FirewallProfileprotocoloptions",
    "Properties" : {
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#featureset" title="FeatureSet">FeatureSet</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#oversizelog" title="OversizeLog">OversizeLog</a>" : <i>String</i>,
        "<a href="#replacemsggroup" title="ReplacemsgGroup">ReplacemsgGroup</a>" : <i>String</i>,
        "<a href="#rpcoverhttp" title="RpcOverHttp">RpcOverHttp</a>" : <i>String</i>,
        "<a href="#switchingprotocolslog" title="SwitchingProtocolsLog">SwitchingProtocolsLog</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#cifs" title="Cifs">Cifs</a>" : <i>[ <a href="cifsdefinition.md">CifsDefinition</a>, ... ]</i>,
        "<a href="#dns" title="Dns">Dns</a>" : <i>[ <a href="dnsdefinition.md">DnsDefinition</a>, ... ]</i>,
        "<a href="#ftp" title="Ftp">Ftp</a>" : <i>[ <a href="ftpdefinition.md">FtpDefinition</a>, ... ]</i>,
        "<a href="#http" title="Http">Http</a>" : <i>[ <a href="httpdefinition.md">HttpDefinition</a>, ... ]</i>,
        "<a href="#imap" title="Imap">Imap</a>" : <i>[ <a href="imapdefinition.md">ImapDefinition</a>, ... ]</i>,
        "<a href="#mailsignature" title="MailSignature">MailSignature</a>" : <i>[ <a href="mailsignaturedefinition.md">MailSignatureDefinition</a>, ... ]</i>,
        "<a href="#mapi" title="Mapi">Mapi</a>" : <i>[ <a href="mapidefinition.md">MapiDefinition</a>, ... ]</i>,
        "<a href="#nntp" title="Nntp">Nntp</a>" : <i>[ <a href="nntpdefinition.md">NntpDefinition</a>, ... ]</i>,
        "<a href="#pop3" title="Pop3">Pop3</a>" : <i>[ <a href="pop3definition.md">Pop3Definition</a>, ... ]</i>,
        "<a href="#smtp" title="Smtp">Smtp</a>" : <i>[ <a href="smtpdefinition.md">SmtpDefinition</a>, ... ]</i>,
        "<a href="#ssh" title="Ssh">Ssh</a>" : <i>[ <a href="sshdefinition.md">SshDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FirewallProfileprotocoloptions
Properties:
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#featureset" title="FeatureSet">FeatureSet</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#oversizelog" title="OversizeLog">OversizeLog</a>: <i>String</i>
    <a href="#replacemsggroup" title="ReplacemsgGroup">ReplacemsgGroup</a>: <i>String</i>
    <a href="#rpcoverhttp" title="RpcOverHttp">RpcOverHttp</a>: <i>String</i>
    <a href="#switchingprotocolslog" title="SwitchingProtocolsLog">SwitchingProtocolsLog</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#cifs" title="Cifs">Cifs</a>: <i>
      - <a href="cifsdefinition.md">CifsDefinition</a></i>
    <a href="#dns" title="Dns">Dns</a>: <i>
      - <a href="dnsdefinition.md">DnsDefinition</a></i>
    <a href="#ftp" title="Ftp">Ftp</a>: <i>
      - <a href="ftpdefinition.md">FtpDefinition</a></i>
    <a href="#http" title="Http">Http</a>: <i>
      - <a href="httpdefinition.md">HttpDefinition</a></i>
    <a href="#imap" title="Imap">Imap</a>: <i>
      - <a href="imapdefinition.md">ImapDefinition</a></i>
    <a href="#mailsignature" title="MailSignature">MailSignature</a>: <i>
      - <a href="mailsignaturedefinition.md">MailSignatureDefinition</a></i>
    <a href="#mapi" title="Mapi">Mapi</a>: <i>
      - <a href="mapidefinition.md">MapiDefinition</a></i>
    <a href="#nntp" title="Nntp">Nntp</a>: <i>
      - <a href="nntpdefinition.md">NntpDefinition</a></i>
    <a href="#pop3" title="Pop3">Pop3</a>: <i>
      - <a href="pop3definition.md">Pop3Definition</a></i>
    <a href="#smtp" title="Smtp">Smtp</a>: <i>
      - <a href="smtpdefinition.md">SmtpDefinition</a></i>
    <a href="#ssh" title="Ssh">Ssh</a>: <i>
      - <a href="sshdefinition.md">SshDefinition</a></i>
</pre>

## Properties

#### Comment

Optional comments.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FeatureSet

Flow/proxy feature set. Valid values: `flow`, `proxy`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OversizeLog

Enable/disable logging for antivirus oversize file blocking. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplacemsgGroup

Name of the replacement message group to be used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RpcOverHttp

Enable/disable inspection of RPC over HTTP. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SwitchingProtocolsLog

Enable/disable logging for HTTP/HTTPS switching protocols. Valid values: `disable`, `enable`.

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

#### Dns

_Required_: No

_Type_: List of <a href="dnsdefinition.md">DnsDefinition</a>

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

#### MailSignature

_Required_: No

_Type_: List of <a href="mailsignaturedefinition.md">MailSignatureDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mapi

_Required_: No

_Type_: List of <a href="mapidefinition.md">MapiDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nntp

_Required_: No

_Type_: List of <a href="nntpdefinition.md">NntpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pop3

_Required_: No

_Type_: List of <a href="pop3definition.md">Pop3Definition</a>

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

