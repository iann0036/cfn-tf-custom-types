# Terraform::AzureStack::VirtualMachineScaleSet AdditionalUnattendConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#component" title="Component">Component</a>" : <i>String</i>,
    "<a href="#content" title="Content">Content</a>" : <i>String</i>,
    "<a href="#pass" title="Pass">Pass</a>" : <i>String</i>,
    "<a href="#settingname" title="SettingName">SettingName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#component" title="Component">Component</a>: <i>String</i>
<a href="#content" title="Content">Content</a>: <i>String</i>
<a href="#pass" title="Pass">Pass</a>: <i>String</i>
<a href="#settingname" title="SettingName">SettingName</a>: <i>String</i>
</pre>

## Properties

#### Component

Specifies the name of the component to configure with the added content. The only allowable value is `Microsoft-Windows-Shell-Setup`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Content

Specifies the base-64 encoded XML formatted content that is added to the unattend.xml file for the specified path and component.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pass

Specifies the name of the pass that the content applies to. The only allowable value is `oobeSystem`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SettingName

Specifies the name of the setting to which the content applies. Possible values are: `FirstLogonCommands` and `AutoLogon`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

