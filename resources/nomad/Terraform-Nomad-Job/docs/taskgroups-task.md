# Terraform::Nomad::Job TaskGroups Task

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#driver" title="Driver">Driver</a>" : <i>String</i>,
    "<a href="#meta" title="Meta">Meta</a>" : <i>[ <a href="taskgroups-task-meta.md">Meta</a>, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#volumemounts" title="VolumeMounts">VolumeMounts</a>" : <i>[ <a href="taskgroups-task-volumemounts.md">VolumeMounts</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#driver" title="Driver">Driver</a>: <i>String</i>
<a href="#meta" title="Meta">Meta</a>: <i>
      - <a href="taskgroups-task-meta.md">Meta</a></i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#volumemounts" title="VolumeMounts">VolumeMounts</a>: <i>
      - <a href="taskgroups-task-volumemounts.md">VolumeMounts</a></i>
</pre>

## Properties

#### Driver

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Meta

_Required_: No

_Type_: List of <a href="taskgroups-task-meta.md">Meta</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeMounts

_Required_: No

_Type_: List of <a href="taskgroups-task-volumemounts.md">VolumeMounts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

