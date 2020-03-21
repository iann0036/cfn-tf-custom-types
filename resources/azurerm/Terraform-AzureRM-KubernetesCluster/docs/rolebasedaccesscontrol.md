# Terraform::AzureRM::KubernetesCluster RoleBasedAccessControl

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#azureactivedirectory" title="AzureActiveDirectory">AzureActiveDirectory</a>" : <i>[ <a href="rolebasedaccesscontrol-azureactivedirectory.md">AzureActiveDirectory</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#azureactivedirectory" title="AzureActiveDirectory">AzureActiveDirectory</a>: <i>
      - <a href="rolebasedaccesscontrol-azureactivedirectory.md">AzureActiveDirectory</a></i>
</pre>

## Properties

#### Enabled

Is Role Based Access Control Enabled? Changing this forces a new resource to be created.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureActiveDirectory

_Required_: No

_Type_: List of <a href="rolebasedaccesscontrol-azureactivedirectory.md">AzureActiveDirectory</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

