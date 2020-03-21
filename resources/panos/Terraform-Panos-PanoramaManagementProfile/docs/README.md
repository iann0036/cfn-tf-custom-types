# Terraform::Panos::PanoramaManagementProfile

This resource allows you to add/update/delete Panorama interface management profiles
for both templates and template stacks.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaManagementProfile",
    "Properties" : {
        "<a href="#http" title="Http">Http</a>" : <i>Boolean</i>,
        "<a href="#httpocsp" title="HttpOcsp">HttpOcsp</a>" : <i>Boolean</i>,
        "<a href="#https" title="Https">Https</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#permittedips" title="PermittedIps">PermittedIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#ping" title="Ping">Ping</a>" : <i>Boolean</i>,
        "<a href="#responsepages" title="ResponsePages">ResponsePages</a>" : <i>Boolean</i>,
        "<a href="#snmp" title="Snmp">Snmp</a>" : <i>Boolean</i>,
        "<a href="#ssh" title="Ssh">Ssh</a>" : <i>Boolean</i>,
        "<a href="#telnet" title="Telnet">Telnet</a>" : <i>Boolean</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#templatestack" title="TemplateStack">TemplateStack</a>" : <i>String</i>,
        "<a href="#useridservice" title="UseridService">UseridService</a>" : <i>Boolean</i>,
        "<a href="#useridsysloglistenerssl" title="UseridSyslogListenerSsl">UseridSyslogListenerSsl</a>" : <i>Boolean</i>,
        "<a href="#useridsysloglistenerudp" title="UseridSyslogListenerUdp">UseridSyslogListenerUdp</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::PanoramaManagementProfile
Properties:
    <a href="#http" title="Http">Http</a>: <i>Boolean</i>
    <a href="#httpocsp" title="HttpOcsp">HttpOcsp</a>: <i>Boolean</i>
    <a href="#https" title="Https">Https</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#permittedips" title="PermittedIps">PermittedIps</a>: <i>
      - String</i>
    <a href="#ping" title="Ping">Ping</a>: <i>Boolean</i>
    <a href="#responsepages" title="ResponsePages">ResponsePages</a>: <i>Boolean</i>
    <a href="#snmp" title="Snmp">Snmp</a>: <i>Boolean</i>
    <a href="#ssh" title="Ssh">Ssh</a>: <i>Boolean</i>
    <a href="#telnet" title="Telnet">Telnet</a>: <i>Boolean</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#templatestack" title="TemplateStack">TemplateStack</a>: <i>String</i>
    <a href="#useridservice" title="UseridService">UseridService</a>: <i>Boolean</i>
    <a href="#useridsysloglistenerssl" title="UseridSyslogListenerSsl">UseridSyslogListenerSsl</a>: <i>Boolean</i>
    <a href="#useridsysloglistenerudp" title="UseridSyslogListenerUdp">UseridSyslogListenerUdp</a>: <i>Boolean</i>
</pre>

## Properties

#### Http

Allow HTTP.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpOcsp

Allow HTTP OCSP.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Https

Allow HTTPS.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The management profile's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermittedIps

The list of permitted IP addresses or address
ranges for this management profile.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ping

Allow ping.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponsePages

Allow response pages.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Snmp

Allow SNMP.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ssh

Allow SSH.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Telnet

Allow telnet.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

The template name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateStack

The template stack name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseridService

Allow User ID service.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseridSyslogListenerSsl

Allow User ID syslog listener
for SSL.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseridSyslogListenerUdp

Allow User ID syslog listener
for UDP.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

