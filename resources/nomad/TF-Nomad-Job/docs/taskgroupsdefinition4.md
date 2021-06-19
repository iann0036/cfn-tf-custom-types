# TF::Nomad::Job TaskGroupsDefinition4

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#driver" title="Driver">Driver</a>" : <i>String</i>,
    "<a href="#meta" title="Meta">Meta</a>" : <i>[ <a href="taskgroupsdefinition.md">TaskGroupsDefinition</a>, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#volumemounts" title="VolumeMounts">VolumeMounts</a>" : <i>[ <a href="taskgroupsdefinition3.md">TaskGroupsDefinition3</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#driver" title="Driver">Driver</a>: <i>String</i>
<a href="#meta" title="Meta">Meta</a>: <i>
      - <a href="taskgroupsdefinition.md">TaskGroupsDefinition</a></i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#volumemounts" title="VolumeMounts">VolumeMounts</a>: <i>
      - <a href="taskgroupsdefinition3.md">TaskGroupsDefinition3</a></i>
</pre>

## Properties

#### Driver

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Meta

_Required_: No

_Type_: List of <a href="taskgroupsdefinition.md">TaskGroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeMounts

_Required_: No

_Type_: List of <a href="taskgroupsdefinition3.md">TaskGroupsDefinition3</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

