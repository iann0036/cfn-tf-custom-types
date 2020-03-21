# Terraform::Nomad::Job TaskGroups

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#count" title="Count">Count</a>" : <i>Double</i>,
    "<a href="#meta" title="Meta">Meta</a>" : <i>[ &lt;a href=&#34;taskgroups-meta.md&#34;&gt;Meta&lt;/a&gt;, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#task" title="Task">Task</a>" : <i>[ &lt;a href=&#34;taskgroups-task.md&#34;&gt;Task&lt;/a&gt;, ... ]</i>,
    "<a href="#volumes" title="Volumes">Volumes</a>" : <i>[ &lt;a href=&#34;taskgroups-volumes.md&#34;&gt;Volumes&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#count" title="Count">Count</a>: <i>Double</i>
<a href="#meta" title="Meta">Meta</a>: <i>
      - &lt;a href=&#34;taskgroups-meta.md&#34;&gt;Meta&lt;/a&gt;</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#task" title="Task">Task</a>: <i>
      - &lt;a href=&#34;taskgroups-task.md&#34;&gt;Task&lt;/a&gt;</i>
<a href="#volumes" title="Volumes">Volumes</a>: <i>
      - &lt;a href=&#34;taskgroups-volumes.md&#34;&gt;Volumes&lt;/a&gt;</i>
</pre>

## Properties

#### Count

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Meta

_Required_: No
_Type_: List of &lt;a href=&#34;taskgroups-meta.md&#34;&gt;Meta&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Task

_Required_: No
_Type_: List of &lt;a href=&#34;taskgroups-task.md&#34;&gt;Task&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volumes

_Required_: No
_Type_: List of &lt;a href=&#34;taskgroups-volumes.md&#34;&gt;Volumes&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

