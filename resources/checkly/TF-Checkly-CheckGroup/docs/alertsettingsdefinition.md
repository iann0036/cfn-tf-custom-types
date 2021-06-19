# TF::Checkly::CheckGroup AlertSettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#escalationtype" title="EscalationType">EscalationType</a>" : <i>String</i>,
    "<a href="#reminders" title="Reminders">Reminders</a>" : <i>[ <a href="remindersdefinition.md">RemindersDefinition</a>, ... ]</i>,
    "<a href="#runbasedescalation" title="RunBasedEscalation">RunBasedEscalation</a>" : <i>[ <a href="runbasedescalationdefinition.md">RunBasedEscalationDefinition</a>, ... ]</i>,
    "<a href="#sslcertificates" title="SslCertificates">SslCertificates</a>" : <i>[ <a href="sslcertificatesdefinition.md">SslCertificatesDefinition</a>, ... ]</i>,
    "<a href="#timebasedescalation" title="TimeBasedEscalation">TimeBasedEscalation</a>" : <i>[ <a href="timebasedescalationdefinition.md">TimeBasedEscalationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#escalationtype" title="EscalationType">EscalationType</a>: <i>String</i>
<a href="#reminders" title="Reminders">Reminders</a>: <i>
      - <a href="remindersdefinition.md">RemindersDefinition</a></i>
<a href="#runbasedescalation" title="RunBasedEscalation">RunBasedEscalation</a>: <i>
      - <a href="runbasedescalationdefinition.md">RunBasedEscalationDefinition</a></i>
<a href="#sslcertificates" title="SslCertificates">SslCertificates</a>: <i>
      - <a href="sslcertificatesdefinition.md">SslCertificatesDefinition</a></i>
<a href="#timebasedescalation" title="TimeBasedEscalation">TimeBasedEscalation</a>: <i>
      - <a href="timebasedescalationdefinition.md">TimeBasedEscalationDefinition</a></i>
</pre>

## Properties

#### EscalationType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reminders

_Required_: No

_Type_: List of <a href="remindersdefinition.md">RemindersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunBasedEscalation

_Required_: No

_Type_: List of <a href="runbasedescalationdefinition.md">RunBasedEscalationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCertificates

_Required_: No

_Type_: List of <a href="sslcertificatesdefinition.md">SslCertificatesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeBasedEscalation

_Required_: No

_Type_: List of <a href="timebasedescalationdefinition.md">TimeBasedEscalationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

