# TF::AVI::Systemconfiguration NtpConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ntpauthenticationkeys" title="NtpAuthenticationKeys">NtpAuthenticationKeys</a>" : <i>[ <a href="ntpauthenticationkeysdefinition.md">NtpAuthenticationKeysDefinition</a>, ... ]</i>,
    "<a href="#ntpserverlist" title="NtpServerList">NtpServerList</a>" : <i>[ <a href="ntpserverlistdefinition.md">NtpServerListDefinition</a>, ... ]</i>,
    "<a href="#ntpservers" title="NtpServers">NtpServers</a>" : <i>[ <a href="ntpserversdefinition.md">NtpServersDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ntpauthenticationkeys" title="NtpAuthenticationKeys">NtpAuthenticationKeys</a>: <i>
      - <a href="ntpauthenticationkeysdefinition.md">NtpAuthenticationKeysDefinition</a></i>
<a href="#ntpserverlist" title="NtpServerList">NtpServerList</a>: <i>
      - <a href="ntpserverlistdefinition.md">NtpServerListDefinition</a></i>
<a href="#ntpservers" title="NtpServers">NtpServers</a>: <i>
      - <a href="ntpserversdefinition.md">NtpServersDefinition</a></i>
</pre>

## Properties

#### NtpAuthenticationKeys

_Required_: No

_Type_: List of <a href="ntpauthenticationkeysdefinition.md">NtpAuthenticationKeysDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpServerList

_Required_: No

_Type_: List of <a href="ntpserverlistdefinition.md">NtpServerListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NtpServers

_Required_: No

_Type_: List of <a href="ntpserversdefinition.md">NtpServersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

