# TF::AzureRM::WindowsVirtualMachineScaleSet ExtensionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoupgrademinorversion" title="AutoUpgradeMinorVersion">AutoUpgradeMinorVersion</a>" : <i>Boolean</i>,
    "<a href="#forceupdatetag" title="ForceUpdateTag">ForceUpdateTag</a>" : <i>String</i>,
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
<a href="#forceupdatetag" title="ForceUpdateTag">ForceUpdateTag</a>: <i>String</i>
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

Should the latest version of the Extension be used at Deployment Time, if one is available? This won't auto-update the extension on existing installation. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceUpdateTag

A value which, when different to the previous value can be used to force-run the Extension even if the Extension Configuration hasn't changed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name for the Virtual Machine Scale Set Extension.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtectedSettings

A JSON String which specifies Sensitive Settings (such as Passwords) for the Extension.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProvisionAfterExtensions

An ordered list of Extension names which this should be provisioned after.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Publisher

Specifies the Publisher of the Extension.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Settings

A JSON String which specifies Settings for the Extension.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Specifies the Type of the Extension.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TypeHandlerVersion

Specifies the version of the extension to use, available versions can be found using the Azure CLI.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

