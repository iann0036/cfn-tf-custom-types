# TF::Panos::LogForwardingProfile MatchListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#emailserverprofiles" title="EmailServerProfiles">EmailServerProfiles</a>" : <i>[ String, ... ]</i>,
    "<a href="#filter" title="Filter">Filter</a>" : <i>String</i>,
    "<a href="#httpserverprofiles" title="HttpServerProfiles">HttpServerProfiles</a>" : <i>[ String, ... ]</i>,
    "<a href="#logtype" title="LogType">LogType</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#sendtopanorama" title="SendToPanorama">SendToPanorama</a>" : <i>Boolean</i>,
    "<a href="#snmptrapserverprofiles" title="SnmptrapServerProfiles">SnmptrapServerProfiles</a>" : <i>[ String, ... ]</i>,
    "<a href="#syslogserverprofiles" title="SyslogServerProfiles">SyslogServerProfiles</a>" : <i>[ String, ... ]</i>,
    "<a href="#action" title="Action">Action</a>" : <i>[ <a href="actiondefinition.md">ActionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#emailserverprofiles" title="EmailServerProfiles">EmailServerProfiles</a>: <i>
      - String</i>
<a href="#filter" title="Filter">Filter</a>: <i>String</i>
<a href="#httpserverprofiles" title="HttpServerProfiles">HttpServerProfiles</a>: <i>
      - String</i>
<a href="#logtype" title="LogType">LogType</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#sendtopanorama" title="SendToPanorama">SendToPanorama</a>: <i>Boolean</i>
<a href="#snmptrapserverprofiles" title="SnmptrapServerProfiles">SnmptrapServerProfiles</a>: <i>
      - String</i>
<a href="#syslogserverprofiles" title="SyslogServerProfiles">SyslogServerProfiles</a>: <i>
      - String</i>
<a href="#action" title="Action">Action</a>: <i>
      - <a href="actiondefinition.md">ActionDefinition</a></i>
</pre>

## Properties

#### Description

The description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailServerProfiles

List of email server profiles.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

The filter (default: `All Logs`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpServerProfiles

List of http server profiles.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogType

The log type.  Valid values are `traffic` (default),
`threat`, `wildfire`, `url`, `data`, `gtp`, `tunnel`, `auth`, or `sctp`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendToPanorama

Set to `true` to send to Panorama.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnmptrapServerProfiles

List of SNMP server profiles.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyslogServerProfiles

List of syslog server profiles.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No

_Type_: List of <a href="actiondefinition.md">ActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

