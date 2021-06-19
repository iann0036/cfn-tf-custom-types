# TF::AVI::Alertsyslogconfig SyslogServersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#anonauth" title="AnonAuth">AnonAuth</a>" : <i>Boolean</i>,
    "<a href="#format" title="Format">Format</a>" : <i>String</i>,
    "<a href="#pkiprofileref" title="PkiprofileRef">PkiprofileRef</a>" : <i>String</i>,
    "<a href="#sslkeyandcertificateref" title="SslKeyAndCertificateRef">SslKeyAndCertificateRef</a>" : <i>String</i>,
    "<a href="#syslogserver" title="SyslogServer">SyslogServer</a>" : <i>String</i>,
    "<a href="#syslogserverport" title="SyslogServerPort">SyslogServerPort</a>" : <i>Double</i>,
    "<a href="#tlsenable" title="TlsEnable">TlsEnable</a>" : <i>Boolean</i>,
    "<a href="#udp" title="Udp">Udp</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#anonauth" title="AnonAuth">AnonAuth</a>: <i>Boolean</i>
<a href="#format" title="Format">Format</a>: <i>String</i>
<a href="#pkiprofileref" title="PkiprofileRef">PkiprofileRef</a>: <i>String</i>
<a href="#sslkeyandcertificateref" title="SslKeyAndCertificateRef">SslKeyAndCertificateRef</a>: <i>String</i>
<a href="#syslogserver" title="SyslogServer">SyslogServer</a>: <i>String</i>
<a href="#syslogserverport" title="SyslogServerPort">SyslogServerPort</a>: <i>Double</i>
<a href="#tlsenable" title="TlsEnable">TlsEnable</a>: <i>Boolean</i>
<a href="#udp" title="Udp">Udp</a>: <i>Boolean</i>
</pre>

## Properties

#### AnonAuth

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PkiprofileRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslKeyAndCertificateRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyslogServer

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyslogServerPort

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsEnable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Udp

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

