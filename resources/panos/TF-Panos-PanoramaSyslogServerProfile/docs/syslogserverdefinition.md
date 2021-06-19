# TF::Panos::PanoramaSyslogServerProfile SyslogServerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#facility" title="Facility">Facility</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#server" title="Server">Server</a>" : <i>String</i>,
    "<a href="#syslogformat" title="SyslogFormat">SyslogFormat</a>" : <i>String</i>,
    "<a href="#transport" title="Transport">Transport</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#facility" title="Facility">Facility</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#server" title="Server">Server</a>: <i>String</i>
<a href="#syslogformat" title="SyslogFormat">SyslogFormat</a>: <i>String</i>
<a href="#transport" title="Transport">Transport</a>: <i>String</i>
</pre>

## Properties

#### Facility

The syslog facility.  Valid values are `LOG_USER`
(default), `LOG_LOCAL0`, `LOG_LOCAL1`, `LOG_LOCAL2`, `LOG_LOCAL3`,
`LOG_LOCAL4`, `LOG_LOCAL5`, `LOG_LOCAL6`, or `LOG_LOCAL7`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Server name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

The port number (default: 514).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

The hostname.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyslogFormat

The syslog format.  Valid values are `BSD`
(default) or `IETF`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Transport

The transport.  Valid values are `UDP` (default),
`TCP`, or `SSL`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

