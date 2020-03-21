# Terraform::AzureRM::WindowsVirtualMachineScaleSet AdditionalUnattendContent

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#content" title="Content">Content</a>" : <i>String</i>,
    "<a href="#setting" title="Setting">Setting</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#content" title="Content">Content</a>: <i>String</i>
<a href="#setting" title="Setting">Setting</a>: <i>String</i>
</pre>

## Properties

#### Content

The XML formatted content that is added to the unattend.xml file for the specified path and component. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Setting

The name of the setting to which the content applies. Possible values are `AutoLogon` and `FirstLogonCommands`. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

