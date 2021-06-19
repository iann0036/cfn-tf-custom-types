# TF::Spotinst::ElastigroupAws IntegrationCodedeployDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cleanuponfailure" title="CleanupOnFailure">CleanupOnFailure</a>" : <i>Boolean</i>,
    "<a href="#terminateinstanceonfailure" title="TerminateInstanceOnFailure">TerminateInstanceOnFailure</a>" : <i>Boolean</i>,
    "<a href="#deploymentgroups" title="DeploymentGroups">DeploymentGroups</a>" : <i>[ <a href="deploymentgroupsdefinition.md">DeploymentGroupsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cleanuponfailure" title="CleanupOnFailure">CleanupOnFailure</a>: <i>Boolean</i>
<a href="#terminateinstanceonfailure" title="TerminateInstanceOnFailure">TerminateInstanceOnFailure</a>: <i>Boolean</i>
<a href="#deploymentgroups" title="DeploymentGroups">DeploymentGroups</a>: <i>
      - <a href="deploymentgroupsdefinition.md">DeploymentGroupsDefinition</a></i>
</pre>

## Properties

#### CleanupOnFailure

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminateInstanceOnFailure

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentGroups

_Required_: No

_Type_: List of <a href="deploymentgroupsdefinition.md">DeploymentGroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

