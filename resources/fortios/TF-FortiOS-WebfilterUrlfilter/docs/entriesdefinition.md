# TF::FortiOS::WebfilterUrlfilter EntriesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#antiphishaction" title="AntiphishAction">AntiphishAction</a>" : <i>String</i>,
    "<a href="#dnsaddressfamily" title="DnsAddressFamily">DnsAddressFamily</a>" : <i>String</i>,
    "<a href="#exempt" title="Exempt">Exempt</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#referrerhost" title="ReferrerHost">ReferrerHost</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#url" title="Url">Url</a>" : <i>String</i>,
    "<a href="#webproxyprofile" title="WebProxyProfile">WebProxyProfile</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#antiphishaction" title="AntiphishAction">AntiphishAction</a>: <i>String</i>
<a href="#dnsaddressfamily" title="DnsAddressFamily">DnsAddressFamily</a>: <i>String</i>
<a href="#exempt" title="Exempt">Exempt</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#referrerhost" title="ReferrerHost">ReferrerHost</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#url" title="Url">Url</a>: <i>String</i>
<a href="#webproxyprofile" title="WebProxyProfile">WebProxyProfile</a>: <i>String</i>
</pre>

## Properties

#### Action

Action to take for URL filter matches. Valid values: `exempt`, `block`, `allow`, `monitor`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AntiphishAction

Action to take for AntiPhishing matches. Valid values: `block`, `log`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsAddressFamily

Resolve IPv4 address, IPv6 address, or both from DNS server. Valid values: `ipv4`, `ipv6`, `both`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exempt

If action is set to exempt, select the security profile operations that exempt URLs skip. Separate multiple options with a space.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Id.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReferrerHost

Referrer host name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable this URL filter. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Filter type (simple, regex, or wildcard). Valid values: `simple`, `regex`, `wildcard`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

URL to be filtered.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebProxyProfile

Web proxy profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

