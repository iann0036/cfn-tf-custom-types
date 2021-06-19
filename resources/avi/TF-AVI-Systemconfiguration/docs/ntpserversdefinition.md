# TF::AVI::Systemconfiguration NtpServersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#keynumber" title="KeyNumber">KeyNumber</a>" : <i>Double</i>,
    "<a href="#server" title="Server">Server</a>" : <i>[ <a href="serverdefinition.md">ServerDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#keynumber" title="KeyNumber">KeyNumber</a>: <i>Double</i>
<a href="#server" title="Server">Server</a>: <i>
      - <a href="serverdefinition.md">ServerDefinition</a></i>
</pre>

## Properties

#### KeyNumber

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

_Required_: No

_Type_: List of <a href="serverdefinition.md">ServerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

