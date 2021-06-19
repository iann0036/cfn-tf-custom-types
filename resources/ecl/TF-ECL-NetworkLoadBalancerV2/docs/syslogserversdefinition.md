# TF::ECL::NetworkLoadBalancerV2 SyslogServersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#acllogging" title="AclLogging">AclLogging</a>" : <i>String</i>,
    "<a href="#appflowlogging" title="AppflowLogging">AppflowLogging</a>" : <i>String</i>,
    "<a href="#dateformat" title="DateFormat">DateFormat</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
    "<a href="#logfacility" title="LogFacility">LogFacility</a>" : <i>String</i>,
    "<a href="#loglevel" title="LogLevel">LogLevel</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#portnumber" title="PortNumber">PortNumber</a>" : <i>Double</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#tcplogging" title="TcpLogging">TcpLogging</a>" : <i>String</i>,
    "<a href="#tenantid" title="TenantId">TenantId</a>" : <i>String</i>,
    "<a href="#timezone" title="TimeZone">TimeZone</a>" : <i>String</i>,
    "<a href="#transporttype" title="TransportType">TransportType</a>" : <i>String</i>,
    "<a href="#userconfigurablelogmessages" title="UserConfigurableLogMessages">UserConfigurableLogMessages</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#acllogging" title="AclLogging">AclLogging</a>: <i>String</i>
<a href="#appflowlogging" title="AppflowLogging">AppflowLogging</a>: <i>String</i>
<a href="#dateformat" title="DateFormat">DateFormat</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
<a href="#logfacility" title="LogFacility">LogFacility</a>: <i>String</i>
<a href="#loglevel" title="LogLevel">LogLevel</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#portnumber" title="PortNumber">PortNumber</a>: <i>Double</i>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#tcplogging" title="TcpLogging">TcpLogging</a>: <i>String</i>
<a href="#tenantid" title="TenantId">TenantId</a>: <i>String</i>
<a href="#timezone" title="TimeZone">TimeZone</a>: <i>String</i>
<a href="#transporttype" title="TransportType">TransportType</a>: <i>String</i>
<a href="#userconfigurablelogmessages" title="UserConfigurableLogMessages">UserConfigurableLogMessages</a>: <i>String</i>
</pre>

## Properties

#### AclLogging

Should syslog record acl info. Must be
one of "ENABLED" and "DISABLED".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppflowLogging

Should syslog record appflow info. Must be
one of "ENABLED" and "DISABLED".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DateFormat

Date format utilized by syslog. Must be
one of "DDMMYYYY", "MMDDYYYY" and "YYYYMMDD".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Load Balancer Syslog Server description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

IP address of syslog server. The syslog server
IP address must be in the network connected to the Load Balancer Interface
defined as the argument `interfaces`. Changing this creates a new syslog server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogFacility

Log facility for syslog. Must be
one of "LOCAL0", "LOCAL1", "LOCAL2", "LOCAL3", "LOCAL4", "LOCAL5",
"LOCAL6" and "LOCAL7".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogLevel

Valid elements for log_level are
"ALERT", "CRITICAL", "EMERGENCY", "INFORMATIONAL", "NOTICE",
"ALL", "DEBUG", "ERROR", "NONE", "WARNING". `log_level` value can be assigned
combining multiple elements as "ALERT|CRITICAL|EMERGENCY".
Caution: Can not combine "ALL" or "NONE" with the others.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Load Balancer Syslog Server.
Changing this creates a new syslog server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortNumber

The port number of syslog server.
This value is integer, no less than 1 and no more than 65535.
Changing this creates a new syslog server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

The priority of syslog server.
This value is integer, no less than 0 and no more than 255.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpLogging

Should syslog record tcp protocol info. Must be
one of "NONE" and "ALL".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantId

The owner of the syslog server. Required
if admin wants to create a syslog server for another tenant.
Changing this creates a new syslog server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeZone

Time zone utilized by syslog. Must be
one of "GMT_TIME" and "LOCAL_TIME".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransportType

Protocol for syslog transport. Must be
"UDP".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserConfigurableLogMessages

Can user configure log messages.
Must be one of "YES" and "NO".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

