# TF::FortiOS::DnsfilterProfile

Configure DNS domain filter profiles.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::DnsfilterProfile",
    "Properties" : {
        "<a href="#blockaction" title="BlockAction">BlockAction</a>" : <i>String</i>,
        "<a href="#blockbotnet" title="BlockBotnet">BlockBotnet</a>" : <i>String</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#logalldomain" title="LogAllDomain">LogAllDomain</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#redirectportal" title="RedirectPortal">RedirectPortal</a>" : <i>String</i>,
        "<a href="#redirectportal6" title="RedirectPortal6">RedirectPortal6</a>" : <i>String</i>,
        "<a href="#safesearch" title="SafeSearch">SafeSearch</a>" : <i>String</i>,
        "<a href="#sdnsdomainlog" title="SdnsDomainLog">SdnsDomainLog</a>" : <i>String</i>,
        "<a href="#sdnsftgderrlog" title="SdnsFtgdErrLog">SdnsFtgdErrLog</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#youtuberestrict" title="YoutubeRestrict">YoutubeRestrict</a>" : <i>String</i>,
        "<a href="#dnstranslation" title="DnsTranslation">DnsTranslation</a>" : <i>[ <a href="dnstranslationdefinition.md">DnsTranslationDefinition</a>, ... ]</i>,
        "<a href="#domainfilter" title="DomainFilter">DomainFilter</a>" : <i>[ <a href="domainfilterdefinition.md">DomainFilterDefinition</a>, ... ]</i>,
        "<a href="#externalipblocklist" title="ExternalIpBlocklist">ExternalIpBlocklist</a>" : <i>[ <a href="externalipblocklistdefinition.md">ExternalIpBlocklistDefinition</a>, ... ]</i>,
        "<a href="#ftgddns" title="FtgdDns">FtgdDns</a>" : <i>[ <a href="ftgddnsdefinition.md">FtgdDnsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::DnsfilterProfile
Properties:
    <a href="#blockaction" title="BlockAction">BlockAction</a>: <i>String</i>
    <a href="#blockbotnet" title="BlockBotnet">BlockBotnet</a>: <i>String</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#logalldomain" title="LogAllDomain">LogAllDomain</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#redirectportal" title="RedirectPortal">RedirectPortal</a>: <i>String</i>
    <a href="#redirectportal6" title="RedirectPortal6">RedirectPortal6</a>: <i>String</i>
    <a href="#safesearch" title="SafeSearch">SafeSearch</a>: <i>String</i>
    <a href="#sdnsdomainlog" title="SdnsDomainLog">SdnsDomainLog</a>: <i>String</i>
    <a href="#sdnsftgderrlog" title="SdnsFtgdErrLog">SdnsFtgdErrLog</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#youtuberestrict" title="YoutubeRestrict">YoutubeRestrict</a>: <i>String</i>
    <a href="#dnstranslation" title="DnsTranslation">DnsTranslation</a>: <i>
      - <a href="dnstranslationdefinition.md">DnsTranslationDefinition</a></i>
    <a href="#domainfilter" title="DomainFilter">DomainFilter</a>: <i>
      - <a href="domainfilterdefinition.md">DomainFilterDefinition</a></i>
    <a href="#externalipblocklist" title="ExternalIpBlocklist">ExternalIpBlocklist</a>: <i>
      - <a href="externalipblocklistdefinition.md">ExternalIpBlocklistDefinition</a></i>
    <a href="#ftgddns" title="FtgdDns">FtgdDns</a>: <i>
      - <a href="ftgddnsdefinition.md">FtgdDnsDefinition</a></i>
</pre>

## Properties

#### BlockAction

Action to take for blocked domains. Valid values: `block`, `redirect`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockBotnet

Enable/disable blocking botnet C&C DNS lookups. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogAllDomain

Enable/disable logging of all domains visited (detailed DNS logging). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Profile name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectPortal

IP address of the SDNS redirect portal.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectPortal6

IPv6 address of the SDNS redirect portal.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SafeSearch

Enable/disable Google, Bing, and YouTube safe search. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdnsDomainLog

Enable/disable domain filtering and botnet domain logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdnsFtgdErrLog

Enable/disable FortiGuard SDNS rating error logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### YoutubeRestrict

Set safe search for YouTube restriction level. Valid values: `strict`, `moderate`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsTranslation

_Required_: No

_Type_: List of <a href="dnstranslationdefinition.md">DnsTranslationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainFilter

_Required_: No

_Type_: List of <a href="domainfilterdefinition.md">DomainFilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalIpBlocklist

_Required_: No

_Type_: List of <a href="externalipblocklistdefinition.md">ExternalIpBlocklistDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FtgdDns

_Required_: No

_Type_: List of <a href="ftgddnsdefinition.md">FtgdDnsDefinition</a>

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

