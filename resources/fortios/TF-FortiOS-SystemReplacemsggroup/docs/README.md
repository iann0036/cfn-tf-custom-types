# TF::FortiOS::SystemReplacemsggroup

Configure replacement message groups.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemReplacemsggroup",
    "Properties" : {
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#grouptype" title="GroupType">GroupType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#admin" title="Admin">Admin</a>" : <i>[ <a href="admindefinition.md">AdminDefinition</a>, ... ]</i>,
        "<a href="#alertmail" title="Alertmail">Alertmail</a>" : <i>[ <a href="alertmaildefinition.md">AlertmailDefinition</a>, ... ]</i>,
        "<a href="#auth" title="Auth">Auth</a>" : <i>[ <a href="authdefinition.md">AuthDefinition</a>, ... ]</i>,
        "<a href="#automation" title="Automation">Automation</a>" : <i>[ <a href="automationdefinition.md">AutomationDefinition</a>, ... ]</i>,
        "<a href="#custommessage" title="CustomMessage">CustomMessage</a>" : <i>[ <a href="custommessagedefinition.md">CustomMessageDefinition</a>, ... ]</i>,
        "<a href="#devicedetectionportal" title="DeviceDetectionPortal">DeviceDetectionPortal</a>" : <i>[ <a href="devicedetectionportaldefinition.md">DeviceDetectionPortalDefinition</a>, ... ]</i>,
        "<a href="#ec" title="Ec">Ec</a>" : <i>[ <a href="ecdefinition.md">EcDefinition</a>, ... ]</i>,
        "<a href="#fortiguardwf" title="FortiguardWf">FortiguardWf</a>" : <i>[ <a href="fortiguardwfdefinition.md">FortiguardWfDefinition</a>, ... ]</i>,
        "<a href="#ftp" title="Ftp">Ftp</a>" : <i>[ <a href="ftpdefinition.md">FtpDefinition</a>, ... ]</i>,
        "<a href="#http" title="Http">Http</a>" : <i>[ <a href="httpdefinition.md">HttpDefinition</a>, ... ]</i>,
        "<a href="#icap" title="Icap">Icap</a>" : <i>[ <a href="icapdefinition.md">IcapDefinition</a>, ... ]</i>,
        "<a href="#mail" title="Mail">Mail</a>" : <i>[ <a href="maildefinition.md">MailDefinition</a>, ... ]</i>,
        "<a href="#nacquar" title="NacQuar">NacQuar</a>" : <i>[ <a href="nacquardefinition.md">NacQuarDefinition</a>, ... ]</i>,
        "<a href="#nntp" title="Nntp">Nntp</a>" : <i>[ <a href="nntpdefinition.md">NntpDefinition</a>, ... ]</i>,
        "<a href="#spam" title="Spam">Spam</a>" : <i>[ <a href="spamdefinition.md">SpamDefinition</a>, ... ]</i>,
        "<a href="#sslvpn" title="Sslvpn">Sslvpn</a>" : <i>[ <a href="sslvpndefinition.md">SslvpnDefinition</a>, ... ]</i>,
        "<a href="#trafficquota" title="TrafficQuota">TrafficQuota</a>" : <i>[ <a href="trafficquotadefinition.md">TrafficQuotaDefinition</a>, ... ]</i>,
        "<a href="#utm" title="Utm">Utm</a>" : <i>[ <a href="utmdefinition.md">UtmDefinition</a>, ... ]</i>,
        "<a href="#webproxy" title="Webproxy">Webproxy</a>" : <i>[ <a href="webproxydefinition.md">WebproxyDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemReplacemsggroup
Properties:
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#grouptype" title="GroupType">GroupType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#admin" title="Admin">Admin</a>: <i>
      - <a href="admindefinition.md">AdminDefinition</a></i>
    <a href="#alertmail" title="Alertmail">Alertmail</a>: <i>
      - <a href="alertmaildefinition.md">AlertmailDefinition</a></i>
    <a href="#auth" title="Auth">Auth</a>: <i>
      - <a href="authdefinition.md">AuthDefinition</a></i>
    <a href="#automation" title="Automation">Automation</a>: <i>
      - <a href="automationdefinition.md">AutomationDefinition</a></i>
    <a href="#custommessage" title="CustomMessage">CustomMessage</a>: <i>
      - <a href="custommessagedefinition.md">CustomMessageDefinition</a></i>
    <a href="#devicedetectionportal" title="DeviceDetectionPortal">DeviceDetectionPortal</a>: <i>
      - <a href="devicedetectionportaldefinition.md">DeviceDetectionPortalDefinition</a></i>
    <a href="#ec" title="Ec">Ec</a>: <i>
      - <a href="ecdefinition.md">EcDefinition</a></i>
    <a href="#fortiguardwf" title="FortiguardWf">FortiguardWf</a>: <i>
      - <a href="fortiguardwfdefinition.md">FortiguardWfDefinition</a></i>
    <a href="#ftp" title="Ftp">Ftp</a>: <i>
      - <a href="ftpdefinition.md">FtpDefinition</a></i>
    <a href="#http" title="Http">Http</a>: <i>
      - <a href="httpdefinition.md">HttpDefinition</a></i>
    <a href="#icap" title="Icap">Icap</a>: <i>
      - <a href="icapdefinition.md">IcapDefinition</a></i>
    <a href="#mail" title="Mail">Mail</a>: <i>
      - <a href="maildefinition.md">MailDefinition</a></i>
    <a href="#nacquar" title="NacQuar">NacQuar</a>: <i>
      - <a href="nacquardefinition.md">NacQuarDefinition</a></i>
    <a href="#nntp" title="Nntp">Nntp</a>: <i>
      - <a href="nntpdefinition.md">NntpDefinition</a></i>
    <a href="#spam" title="Spam">Spam</a>: <i>
      - <a href="spamdefinition.md">SpamDefinition</a></i>
    <a href="#sslvpn" title="Sslvpn">Sslvpn</a>: <i>
      - <a href="sslvpndefinition.md">SslvpnDefinition</a></i>
    <a href="#trafficquota" title="TrafficQuota">TrafficQuota</a>: <i>
      - <a href="trafficquotadefinition.md">TrafficQuotaDefinition</a></i>
    <a href="#utm" title="Utm">Utm</a>: <i>
      - <a href="utmdefinition.md">UtmDefinition</a></i>
    <a href="#webproxy" title="Webproxy">Webproxy</a>: <i>
      - <a href="webproxydefinition.md">WebproxyDefinition</a></i>
</pre>

## Properties

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

#### GroupType

Group type.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Group name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Admin

_Required_: No

_Type_: List of <a href="admindefinition.md">AdminDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Alertmail

_Required_: No

_Type_: List of <a href="alertmaildefinition.md">AlertmailDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Auth

_Required_: No

_Type_: List of <a href="authdefinition.md">AuthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Automation

_Required_: No

_Type_: List of <a href="automationdefinition.md">AutomationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomMessage

_Required_: No

_Type_: List of <a href="custommessagedefinition.md">CustomMessageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceDetectionPortal

_Required_: No

_Type_: List of <a href="devicedetectionportaldefinition.md">DeviceDetectionPortalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ec

_Required_: No

_Type_: List of <a href="ecdefinition.md">EcDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortiguardWf

_Required_: No

_Type_: List of <a href="fortiguardwfdefinition.md">FortiguardWfDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ftp

_Required_: No

_Type_: List of <a href="ftpdefinition.md">FtpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http

_Required_: No

_Type_: List of <a href="httpdefinition.md">HttpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Icap

_Required_: No

_Type_: List of <a href="icapdefinition.md">IcapDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mail

_Required_: No

_Type_: List of <a href="maildefinition.md">MailDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NacQuar

_Required_: No

_Type_: List of <a href="nacquardefinition.md">NacQuarDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nntp

_Required_: No

_Type_: List of <a href="nntpdefinition.md">NntpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Spam

_Required_: No

_Type_: List of <a href="spamdefinition.md">SpamDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sslvpn

_Required_: No

_Type_: List of <a href="sslvpndefinition.md">SslvpnDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrafficQuota

_Required_: No

_Type_: List of <a href="trafficquotadefinition.md">TrafficQuotaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Utm

_Required_: No

_Type_: List of <a href="utmdefinition.md">UtmDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Webproxy

_Required_: No

_Type_: List of <a href="webproxydefinition.md">WebproxyDefinition</a>

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

