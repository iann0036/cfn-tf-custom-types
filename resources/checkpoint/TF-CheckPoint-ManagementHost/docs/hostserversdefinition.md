# TF::CheckPoint::ManagementHost HostServersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dnsserver" title="DnsServer">DnsServer</a>" : <i>Boolean</i>,
    "<a href="#mailserver" title="MailServer">MailServer</a>" : <i>Boolean</i>,
    "<a href="#webserver" title="WebServer">WebServer</a>" : <i>Boolean</i>,
    "<a href="#webserverconfig" title="WebServerConfig">WebServerConfig</a>" : <i>[ <a href="webserverconfigdefinition.md">WebServerConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dnsserver" title="DnsServer">DnsServer</a>: <i>Boolean</i>
<a href="#mailserver" title="MailServer">MailServer</a>: <i>Boolean</i>
<a href="#webserver" title="WebServer">WebServer</a>: <i>Boolean</i>
<a href="#webserverconfig" title="WebServerConfig">WebServerConfig</a>: <i>
      - <a href="webserverconfigdefinition.md">WebServerConfigDefinition</a></i>
</pre>

## Properties

#### DnsServer

Gets True if this server is a DNS Server.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MailServer

Gets True if this server is a Mail Server.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebServer

Gets True if this server is a Web Server.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebServerConfig

_Required_: No

_Type_: List of <a href="webserverconfigdefinition.md">WebServerConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

