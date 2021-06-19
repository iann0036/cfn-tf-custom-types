# TF::FortiOS::AlertemailSetting

Configure alert email settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::AlertemailSetting",
    "Properties" : {
        "<a href="#adminloginlogs" title="AdminLoginLogs">AdminLoginLogs</a>" : <i>String</i>,
        "<a href="#alertinterval" title="AlertInterval">AlertInterval</a>" : <i>Double</i>,
        "<a href="#amcinterfacebypassmode" title="AmcInterfaceBypassMode">AmcInterfaceBypassMode</a>" : <i>String</i>,
        "<a href="#antiviruslogs" title="AntivirusLogs">AntivirusLogs</a>" : <i>String</i>,
        "<a href="#configurationchangeslogs" title="ConfigurationChangesLogs">ConfigurationChangesLogs</a>" : <i>String</i>,
        "<a href="#criticalinterval" title="CriticalInterval">CriticalInterval</a>" : <i>Double</i>,
        "<a href="#debuginterval" title="DebugInterval">DebugInterval</a>" : <i>Double</i>,
        "<a href="#emailinterval" title="EmailInterval">EmailInterval</a>" : <i>Double</i>,
        "<a href="#emergencyinterval" title="EmergencyInterval">EmergencyInterval</a>" : <i>Double</i>,
        "<a href="#errorinterval" title="ErrorInterval">ErrorInterval</a>" : <i>Double</i>,
        "<a href="#fdslicenseexpiringdays" title="FdsLicenseExpiringDays">FdsLicenseExpiringDays</a>" : <i>Double</i>,
        "<a href="#fdslicenseexpiringwarning" title="FdsLicenseExpiringWarning">FdsLicenseExpiringWarning</a>" : <i>String</i>,
        "<a href="#fdsupdatelogs" title="FdsUpdateLogs">FdsUpdateLogs</a>" : <i>String</i>,
        "<a href="#filtermode" title="FilterMode">FilterMode</a>" : <i>String</i>,
        "<a href="#fipsccerrors" title="FipsCcErrors">FipsCcErrors</a>" : <i>String</i>,
        "<a href="#firewallauthenticationfailurelogs" title="FirewallAuthenticationFailureLogs">FirewallAuthenticationFailureLogs</a>" : <i>String</i>,
        "<a href="#fortiguardlogquotawarning" title="FortiguardLogQuotaWarning">FortiguardLogQuotaWarning</a>" : <i>String</i>,
        "<a href="#fssodisconnectlogs" title="FssoDisconnectLogs">FssoDisconnectLogs</a>" : <i>String</i>,
        "<a href="#halogs" title="HaLogs">HaLogs</a>" : <i>String</i>,
        "<a href="#informationinterval" title="InformationInterval">InformationInterval</a>" : <i>Double</i>,
        "<a href="#ipslogs" title="IpsLogs">IpsLogs</a>" : <i>String</i>,
        "<a href="#ipsecerrorslogs" title="IpsecErrorsLogs">IpsecErrorsLogs</a>" : <i>String</i>,
        "<a href="#localdiskusage" title="LocalDiskUsage">LocalDiskUsage</a>" : <i>Double</i>,
        "<a href="#logdiskusagewarning" title="LogDiskUsageWarning">LogDiskUsageWarning</a>" : <i>String</i>,
        "<a href="#mailto1" title="Mailto1">Mailto1</a>" : <i>String</i>,
        "<a href="#mailto2" title="Mailto2">Mailto2</a>" : <i>String</i>,
        "<a href="#mailto3" title="Mailto3">Mailto3</a>" : <i>String</i>,
        "<a href="#notificationinterval" title="NotificationInterval">NotificationInterval</a>" : <i>Double</i>,
        "<a href="#ppperrorslogs" title="PppErrorsLogs">PppErrorsLogs</a>" : <i>String</i>,
        "<a href="#severity" title="Severity">Severity</a>" : <i>String</i>,
        "<a href="#sshlogs" title="SshLogs">SshLogs</a>" : <i>String</i>,
        "<a href="#sslvpnauthenticationerrorslogs" title="SslvpnAuthenticationErrorsLogs">SslvpnAuthenticationErrorsLogs</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#violationtrafficlogs" title="ViolationTrafficLogs">ViolationTrafficLogs</a>" : <i>String</i>,
        "<a href="#warninginterval" title="WarningInterval">WarningInterval</a>" : <i>Double</i>,
        "<a href="#webfilterlogs" title="WebfilterLogs">WebfilterLogs</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::AlertemailSetting
Properties:
    <a href="#adminloginlogs" title="AdminLoginLogs">AdminLoginLogs</a>: <i>String</i>
    <a href="#alertinterval" title="AlertInterval">AlertInterval</a>: <i>Double</i>
    <a href="#amcinterfacebypassmode" title="AmcInterfaceBypassMode">AmcInterfaceBypassMode</a>: <i>String</i>
    <a href="#antiviruslogs" title="AntivirusLogs">AntivirusLogs</a>: <i>String</i>
    <a href="#configurationchangeslogs" title="ConfigurationChangesLogs">ConfigurationChangesLogs</a>: <i>String</i>
    <a href="#criticalinterval" title="CriticalInterval">CriticalInterval</a>: <i>Double</i>
    <a href="#debuginterval" title="DebugInterval">DebugInterval</a>: <i>Double</i>
    <a href="#emailinterval" title="EmailInterval">EmailInterval</a>: <i>Double</i>
    <a href="#emergencyinterval" title="EmergencyInterval">EmergencyInterval</a>: <i>Double</i>
    <a href="#errorinterval" title="ErrorInterval">ErrorInterval</a>: <i>Double</i>
    <a href="#fdslicenseexpiringdays" title="FdsLicenseExpiringDays">FdsLicenseExpiringDays</a>: <i>Double</i>
    <a href="#fdslicenseexpiringwarning" title="FdsLicenseExpiringWarning">FdsLicenseExpiringWarning</a>: <i>String</i>
    <a href="#fdsupdatelogs" title="FdsUpdateLogs">FdsUpdateLogs</a>: <i>String</i>
    <a href="#filtermode" title="FilterMode">FilterMode</a>: <i>String</i>
    <a href="#fipsccerrors" title="FipsCcErrors">FipsCcErrors</a>: <i>String</i>
    <a href="#firewallauthenticationfailurelogs" title="FirewallAuthenticationFailureLogs">FirewallAuthenticationFailureLogs</a>: <i>String</i>
    <a href="#fortiguardlogquotawarning" title="FortiguardLogQuotaWarning">FortiguardLogQuotaWarning</a>: <i>String</i>
    <a href="#fssodisconnectlogs" title="FssoDisconnectLogs">FssoDisconnectLogs</a>: <i>String</i>
    <a href="#halogs" title="HaLogs">HaLogs</a>: <i>String</i>
    <a href="#informationinterval" title="InformationInterval">InformationInterval</a>: <i>Double</i>
    <a href="#ipslogs" title="IpsLogs">IpsLogs</a>: <i>String</i>
    <a href="#ipsecerrorslogs" title="IpsecErrorsLogs">IpsecErrorsLogs</a>: <i>String</i>
    <a href="#localdiskusage" title="LocalDiskUsage">LocalDiskUsage</a>: <i>Double</i>
    <a href="#logdiskusagewarning" title="LogDiskUsageWarning">LogDiskUsageWarning</a>: <i>String</i>
    <a href="#mailto1" title="Mailto1">Mailto1</a>: <i>String</i>
    <a href="#mailto2" title="Mailto2">Mailto2</a>: <i>String</i>
    <a href="#mailto3" title="Mailto3">Mailto3</a>: <i>String</i>
    <a href="#notificationinterval" title="NotificationInterval">NotificationInterval</a>: <i>Double</i>
    <a href="#ppperrorslogs" title="PppErrorsLogs">PppErrorsLogs</a>: <i>String</i>
    <a href="#severity" title="Severity">Severity</a>: <i>String</i>
    <a href="#sshlogs" title="SshLogs">SshLogs</a>: <i>String</i>
    <a href="#sslvpnauthenticationerrorslogs" title="SslvpnAuthenticationErrorsLogs">SslvpnAuthenticationErrorsLogs</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#violationtrafficlogs" title="ViolationTrafficLogs">ViolationTrafficLogs</a>: <i>String</i>
    <a href="#warninginterval" title="WarningInterval">WarningInterval</a>: <i>Double</i>
    <a href="#webfilterlogs" title="WebfilterLogs">WebfilterLogs</a>: <i>String</i>
</pre>

## Properties

#### AdminLoginLogs

Enable/disable administrator login/logout logs in alert email. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertInterval

Alert alert interval in minutes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AmcInterfaceBypassMode

Enable/disable Fortinet Advanced Mezzanine Card (AMC) interface bypass mode logs in alert email. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AntivirusLogs

Enable/disable antivirus logs in alert email. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigurationChangesLogs

Enable/disable configuration change logs in alert email. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CriticalInterval

Critical alert interval in minutes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DebugInterval

Debug alert interval in minutes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailInterval

Interval between sending alert emails (1 - 99999 min, default = 5).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmergencyInterval

Emergency alert interval in minutes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ErrorInterval

Error alert interval in minutes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FdsLicenseExpiringDays

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FdsLicenseExpiringWarning

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FdsUpdateLogs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterMode

How to filter log messages that are sent to alert emails. Valid values: `category`, `threshold`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FipsCcErrors

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallAuthenticationFailureLogs

Enable/disable firewall authentication failure logs in alert email. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FortiguardLogQuotaWarning

Enable/disable FortiCloud log quota warnings in alert email. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FssoDisconnectLogs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaLogs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InformationInterval

Information alert interval in minutes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsLogs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecErrorsLogs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalDiskUsage

Disk usage percentage at which to send alert email (1 - 99 percent, default = 75).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogDiskUsageWarning

Enable/disable disk usage warnings in alert email. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mailto1

Email address to send alert email to (usually a system administrator) (max. 64 characters).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mailto2

Optional second email address to send alert email to (max. 64 characters).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mailto3

Optional third email address to send alert email to (max. 64 characters).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationInterval

Notification alert interval in minutes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PppErrorsLogs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Severity

Lowest severity level to log. Valid values: `emergency`, `alert`, `critical`, `error`, `warning`, `notification`, `information`, `debug`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshLogs

Enable/disable SSH logs in alert email. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslvpnAuthenticationErrorsLogs

Enable/disable SSL-VPN authentication error logs in alert email. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

Name that appears in the From: field of alert emails (max. 36 characters).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViolationTrafficLogs

Enable/disable violation traffic logs in alert email. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WarningInterval

Warning alert interval in minutes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebfilterLogs

Enable/disable web filter logs in alert email. Valid values: `enable`, `disable`.

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

