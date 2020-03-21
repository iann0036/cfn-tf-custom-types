# Terraform::Nomad::Job TaskGroups

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#count" title="Count">Count</a>" : <i>Double</i>,
    "<a href="#meta" title="Meta">Meta</a>" : <i>[ <a href="taskgroups-meta.md">Meta</a>, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#task" title="Task">Task</a>" : <i>[ <a href="taskgroups-task.md">Task</a>, ... ]</i>,
    "<a href="#volumes" title="Volumes">Volumes</a>" : <i>[ <a href="taskgroups-volumes.md">Volumes</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#count" title="Count">Count</a>: <i>Double</i>
<a href="#meta" title="Meta">Meta</a>: <i>
      - <a href="taskgroups-meta.md">Meta</a></i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#task" title="Task">Task</a>: <i>
      - <a href="taskgroups-task.md">Task</a></i>
<a href="#volumes" title="Volumes">Volumes</a>: <i>
      - <a href="taskgroups-volumes.md">Volumes</a></i>
</pre>

## Properties

#### Count

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Meta

_Required_: No

_Type_: List of <a href="taskgroups-meta.md">Meta</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Task

_Required_: No

_Type_: List of <a href="taskgroups-task.md">Task</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volumes

_Required_: No

_Type_: List of <a href="taskgroups-volumes.md">Volumes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

