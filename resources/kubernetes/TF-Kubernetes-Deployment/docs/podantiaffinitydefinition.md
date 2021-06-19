# TF::Kubernetes::Deployment PodAntiAffinityDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#preferredduringschedulingignoredduringexecution" title="PreferredDuringSchedulingIgnoredDuringExecution">PreferredDuringSchedulingIgnoredDuringExecution</a>" : <i>[ <a href="preferredduringschedulingignoredduringexecutiondefinition.md">PreferredDuringSchedulingIgnoredDuringExecutionDefinition</a>, ... ]</i>,
    "<a href="#requiredduringschedulingignoredduringexecution" title="RequiredDuringSchedulingIgnoredDuringExecution">RequiredDuringSchedulingIgnoredDuringExecution</a>" : <i>[ <a href="requiredduringschedulingignoredduringexecutiondefinition.md">RequiredDuringSchedulingIgnoredDuringExecutionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#preferredduringschedulingignoredduringexecution" title="PreferredDuringSchedulingIgnoredDuringExecution">PreferredDuringSchedulingIgnoredDuringExecution</a>: <i>
      - <a href="preferredduringschedulingignoredduringexecutiondefinition.md">PreferredDuringSchedulingIgnoredDuringExecutionDefinition</a></i>
<a href="#requiredduringschedulingignoredduringexecution" title="RequiredDuringSchedulingIgnoredDuringExecution">RequiredDuringSchedulingIgnoredDuringExecution</a>: <i>
      - <a href="requiredduringschedulingignoredduringexecutiondefinition.md">RequiredDuringSchedulingIgnoredDuringExecutionDefinition</a></i>
</pre>

## Properties

#### PreferredDuringSchedulingIgnoredDuringExecution

_Required_: No

_Type_: List of <a href="preferredduringschedulingignoredduringexecutiondefinition.md">PreferredDuringSchedulingIgnoredDuringExecutionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiredDuringSchedulingIgnoredDuringExecution

_Required_: No

_Type_: List of <a href="requiredduringschedulingignoredduringexecutiondefinition.md">RequiredDuringSchedulingIgnoredDuringExecutionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

