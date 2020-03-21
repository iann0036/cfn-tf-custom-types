# Terraform::Docker::Container Devices

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#containerpath" title="ContainerPath">ContainerPath</a>" : <i>String</i>,
    "<a href="#hostpath" title="HostPath">HostPath</a>" : <i>String</i>,
    "<a href="#permissions" title="Permissions">Permissions</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#containerpath" title="ContainerPath">ContainerPath</a>: <i>String</i>
<a href="#hostpath" title="HostPath">HostPath</a>: <i>String</i>
<a href="#permissions" title="Permissions">Permissions</a>: <i>String</i>
</pre>

## Properties

#### ContainerPath

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostPath

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permissions

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

