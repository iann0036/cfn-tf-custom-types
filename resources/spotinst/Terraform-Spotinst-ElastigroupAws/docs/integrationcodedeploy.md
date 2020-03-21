# Terraform::Spotinst::ElastigroupAws IntegrationCodedeploy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cleanuponfailure" title="CleanupOnFailure">CleanupOnFailure</a>" : <i>Boolean</i>,
    "<a href="#terminateinstanceonfailure" title="TerminateInstanceOnFailure">TerminateInstanceOnFailure</a>" : <i>Boolean</i>,
    "<a href="#deploymentgroups" title="DeploymentGroups">DeploymentGroups</a>" : <i>[ &lt;a href=&#34;integrationcodedeploy-deploymentgroups.md&#34;&gt;DeploymentGroups&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cleanuponfailure" title="CleanupOnFailure">CleanupOnFailure</a>: <i>Boolean</i>
<a href="#terminateinstanceonfailure" title="TerminateInstanceOnFailure">TerminateInstanceOnFailure</a>: <i>Boolean</i>
<a href="#deploymentgroups" title="DeploymentGroups">DeploymentGroups</a>: <i>
      - &lt;a href=&#34;integrationcodedeploy-deploymentgroups.md&#34;&gt;DeploymentGroups&lt;/a&gt;</i>
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
_Type_: List of &lt;a href=&#34;integrationcodedeploy-deploymentgroups.md&#34;&gt;DeploymentGroups&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

