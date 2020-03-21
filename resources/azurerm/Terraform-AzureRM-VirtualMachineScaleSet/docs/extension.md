# Terraform::AzureRM::VirtualMachineScaleSet Extension

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoupgrademinorversion" title="AutoUpgradeMinorVersion">AutoUpgradeMinorVersion</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#protectedsettings" title="ProtectedSettings">ProtectedSettings</a>" : <i>String</i>,
    "<a href="#provisionafterextensions" title="ProvisionAfterExtensions">ProvisionAfterExtensions</a>" : <i>[ String, ... ]</i>,
    "<a href="#publisher" title="Publisher">Publisher</a>" : <i>String</i>,
    "<a href="#settings" title="Settings">Settings</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#typehandlerversion" title="TypeHandlerVersion">TypeHandlerVersion</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#autoupgrademinorversion" title="AutoUpgradeMinorVersion">AutoUpgradeMinorVersion</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#protectedsettings" title="ProtectedSettings">ProtectedSettings</a>: <i>String</i>
<a href="#provisionafterextensions" title="ProvisionAfterExtensions">ProvisionAfterExtensions</a>: <i>
      - String</i>
<a href="#publisher" title="Publisher">Publisher</a>: <i>String</i>
<a href="#settings" title="Settings">Settings</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#typehandlerversion" title="TypeHandlerVersion">TypeHandlerVersion</a>: <i>String</i>
</pre>

## Properties

#### AutoUpgradeMinorVersion

Specifies whether or not to use the latest minor version available.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the extension.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtectedSettings

The protected_settings passed to the extension, like settings, these are specified as a JSON object in a string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProvisionAfterExtensions

Specifies a dependency array of extensions required to be executed before, the array stores the name of each extension.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Publisher

The publisher of the extension, available publishers can be found by using the Azure CLI.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Settings

The settings passed to the extension, these are specified as a JSON object in a string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of extension, available types for a publisher can be found using the Azure CLI.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TypeHandlerVersion

Specifies the version of the extension to use, available versions can be found using the Azure CLI.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

