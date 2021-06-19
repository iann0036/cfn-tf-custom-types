# TF::FortiOS::SystemAccprofile UtmgrpPermissionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#antivirus" title="Antivirus">Antivirus</a>" : <i>String</i>,
    "<a href="#applicationcontrol" title="ApplicationControl">ApplicationControl</a>" : <i>String</i>,
    "<a href="#datalossprevention" title="DataLossPrevention">DataLossPrevention</a>" : <i>String</i>,
    "<a href="#dnsfilter" title="Dnsfilter">Dnsfilter</a>" : <i>String</i>,
    "<a href="#emailfilter" title="Emailfilter">Emailfilter</a>" : <i>String</i>,
    "<a href="#endpointcontrol" title="EndpointControl">EndpointControl</a>" : <i>String</i>,
    "<a href="#filefilter" title="FileFilter">FileFilter</a>" : <i>String</i>,
    "<a href="#icap" title="Icap">Icap</a>" : <i>String</i>,
    "<a href="#ips" title="Ips">Ips</a>" : <i>String</i>,
    "<a href="#spamfilter" title="Spamfilter">Spamfilter</a>" : <i>String</i>,
    "<a href="#voip" title="Voip">Voip</a>" : <i>String</i>,
    "<a href="#waf" title="Waf">Waf</a>" : <i>String</i>,
    "<a href="#webfilter" title="Webfilter">Webfilter</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#antivirus" title="Antivirus">Antivirus</a>: <i>String</i>
<a href="#applicationcontrol" title="ApplicationControl">ApplicationControl</a>: <i>String</i>
<a href="#datalossprevention" title="DataLossPrevention">DataLossPrevention</a>: <i>String</i>
<a href="#dnsfilter" title="Dnsfilter">Dnsfilter</a>: <i>String</i>
<a href="#emailfilter" title="Emailfilter">Emailfilter</a>: <i>String</i>
<a href="#endpointcontrol" title="EndpointControl">EndpointControl</a>: <i>String</i>
<a href="#filefilter" title="FileFilter">FileFilter</a>: <i>String</i>
<a href="#icap" title="Icap">Icap</a>: <i>String</i>
<a href="#ips" title="Ips">Ips</a>: <i>String</i>
<a href="#spamfilter" title="Spamfilter">Spamfilter</a>: <i>String</i>
<a href="#voip" title="Voip">Voip</a>: <i>String</i>
<a href="#waf" title="Waf">Waf</a>: <i>String</i>
<a href="#webfilter" title="Webfilter">Webfilter</a>: <i>String</i>
</pre>

## Properties

#### Antivirus

Antivirus profiles and settings. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationControl

Application Control profiles and settings. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataLossPrevention

DLP profiles and settings. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dnsfilter

DNS Filter profiles and settings. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Emailfilter

AntiSpam filter and settings. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointControl

FortiClient Profiles. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileFilter

File-filter profiles and settings. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Icap

ICAP profiles and settings. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ips

IPS profiles and settings. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Spamfilter

AntiSpam filter and settings. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Voip

VoIP profiles and settings. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Waf

Web Application Firewall profiles and settings. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Webfilter

Web Filter profiles and settings. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

