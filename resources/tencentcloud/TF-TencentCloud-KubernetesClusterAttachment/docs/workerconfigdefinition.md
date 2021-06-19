# TF::TencentCloud::KubernetesClusterAttachment WorkerConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#desiredpodnum" title="DesiredPodNum">DesiredPodNum</a>" : <i>Double</i>,
    "<a href="#dockergraphpath" title="DockerGraphPath">DockerGraphPath</a>" : <i>String</i>,
    "<a href="#extraargs" title="ExtraArgs">ExtraArgs</a>" : <i>[ String, ... ]</i>,
    "<a href="#isschedule" title="IsSchedule">IsSchedule</a>" : <i>Boolean</i>,
    "<a href="#mounttarget" title="MountTarget">MountTarget</a>" : <i>String</i>,
    "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
    "<a href="#datadisk" title="DataDisk">DataDisk</a>" : <i>[ <a href="datadiskdefinition.md">DataDiskDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#desiredpodnum" title="DesiredPodNum">DesiredPodNum</a>: <i>Double</i>
<a href="#dockergraphpath" title="DockerGraphPath">DockerGraphPath</a>: <i>String</i>
<a href="#extraargs" title="ExtraArgs">ExtraArgs</a>: <i>
      - String</i>
<a href="#isschedule" title="IsSchedule">IsSchedule</a>: <i>Boolean</i>
<a href="#mounttarget" title="MountTarget">MountTarget</a>: <i>String</i>
<a href="#userdata" title="UserData">UserData</a>: <i>String</i>
<a href="#datadisk" title="DataDisk">DataDisk</a>: <i>
      - <a href="datadiskdefinition.md">DataDiskDefinition</a></i>
</pre>

## Properties

#### DesiredPodNum

Indicate to set desired pod number in node. valid when the cluster is podCIDR.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerGraphPath

Docker graph path. Default is `/var/lib/docker`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraArgs

Custom parameter information related to the node. This is a white-list parameter.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsSchedule

Indicate to schedule the adding node or not. Default is true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MountTarget

Mount target. Default is not mounting.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

Base64-encoded User Data text, the length limit is 16KB.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataDisk

_Required_: No

_Type_: List of <a href="datadiskdefinition.md">DataDiskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

