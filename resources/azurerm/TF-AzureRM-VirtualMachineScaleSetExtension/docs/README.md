# TF::AzureRM::VirtualMachineScaleSetExtension

Manages an Extension for a Virtual Machine Scale Set.

~> **NOTE:** This resource is not intended to be used with the `azurerm_virtual_machine_scale_set` resource - instead it's intended for this to be used with the `azurerm_linux_virtual_machine_scale_set` and `azurerm_windows_virtual_machine_scale_set` resources.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::VirtualMachineScaleSetExtension",
    "Properties" : {
        "<a href="#autoupgrademinorversion" title="AutoUpgradeMinorVersion">AutoUpgradeMinorVersion</a>" : <i>Boolean</i>,
        "<a href="#forceupdatetag" title="ForceUpdateTag">ForceUpdateTag</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#protectedsettings" title="ProtectedSettings">ProtectedSettings</a>" : <i>String</i>,
        "<a href="#provisionafterextensions" title="ProvisionAfterExtensions">ProvisionAfterExtensions</a>" : <i>[ String, ... ]</i>,
        "<a href="#publisher" title="Publisher">Publisher</a>" : <i>String</i>,
        "<a href="#settings" title="Settings">Settings</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#typehandlerversion" title="TypeHandlerVersion">TypeHandlerVersion</a>" : <i>String</i>,
        "<a href="#virtualmachinescalesetid" title="VirtualMachineScaleSetId">VirtualMachineScaleSetId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::VirtualMachineScaleSetExtension
Properties:
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
    <a href="#virtualmachinescalesetid" title="VirtualMachineScaleSetId">VirtualMachineScaleSetId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
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

The name for the Virtual Machine Scale Set Extension. Changing this forces a new resource to be created.

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

Specifies the Publisher of the Extension. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Settings

A JSON String which specifies Settings for the Extension.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Specifies the Type of the Extension. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TypeHandlerVersion

Specifies the version of the extension to use, available versions can be found using the Azure CLI.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualMachineScaleSetId

The ID of the Virtual Machine Scale Set. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

