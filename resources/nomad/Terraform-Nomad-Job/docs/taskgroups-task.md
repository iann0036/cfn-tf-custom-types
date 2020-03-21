# Terraform::Nomad::Job TaskGroups Task

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#driver" title="Driver">Driver</a>" : <i>String</i>,
    "<a href="#meta" title="Meta">Meta</a>" : <i>[ &lt;a href=&#34;taskgroups-task-meta.md&#34;&gt;Meta&lt;/a&gt;, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#volumemounts" title="VolumeMounts">VolumeMounts</a>" : <i>[ &lt;a href=&#34;taskgroups-task-volumemounts.md&#34;&gt;VolumeMounts&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#driver" title="Driver">Driver</a>: <i>String</i>
<a href="#meta" title="Meta">Meta</a>: <i>
      - &lt;a href=&#34;taskgroups-task-meta.md&#34;&gt;Meta&lt;/a&gt;</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#volumemounts" title="VolumeMounts">VolumeMounts</a>: <i>
      - &lt;a href=&#34;taskgroups-task-volumemounts.md&#34;&gt;VolumeMounts&lt;/a&gt;</i>
</pre>

## Properties

#### Driver

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Meta

_Required_: No
_Type_: List of &lt;a href=&#34;taskgroups-task-meta.md&#34;&gt;Meta&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeMounts

_Required_: No
_Type_: List of &lt;a href=&#34;taskgroups-task-volumemounts.md&#34;&gt;VolumeMounts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

