# TF::AzureStack::VirtualMachineScaleSet NetworkProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#networksecuritygroupid" title="NetworkSecurityGroupId">NetworkSecurityGroupId</a>" : <i>String</i>,
    "<a href="#primary" title="Primary">Primary</a>" : <i>Boolean</i>,
    "<a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>" : <i>[ <a href="ipconfigurationdefinition.md">IpConfigurationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#networksecuritygroupid" title="NetworkSecurityGroupId">NetworkSecurityGroupId</a>: <i>String</i>
<a href="#primary" title="Primary">Primary</a>: <i>Boolean</i>
<a href="#ipconfiguration" title="IpConfiguration">IpConfiguration</a>: <i>
      - <a href="ipconfigurationdefinition.md">IpConfigurationDefinition</a></i>
</pre>

## Properties

#### Name

The name of the public ip address configuration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkSecurityGroupId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Primary

Indicates whether network interfaces created from the network interface configuration will be the primary NIC of the VM.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpConfiguration

_Required_: No

_Type_: List of <a href="ipconfigurationdefinition.md">IpConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

