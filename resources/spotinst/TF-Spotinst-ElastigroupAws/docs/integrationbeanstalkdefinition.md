# TF::Spotinst::ElastigroupAws IntegrationBeanstalkDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#environmentid" title="EnvironmentId">EnvironmentId</a>" : <i>String</i>,
    "<a href="#deploymentpreferences" title="DeploymentPreferences">DeploymentPreferences</a>" : <i>[ <a href="deploymentpreferencesdefinition.md">DeploymentPreferencesDefinition</a>, ... ]</i>,
    "<a href="#managedactions" title="ManagedActions">ManagedActions</a>" : <i>[ <a href="managedactionsdefinition.md">ManagedActionsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#environmentid" title="EnvironmentId">EnvironmentId</a>: <i>String</i>
<a href="#deploymentpreferences" title="DeploymentPreferences">DeploymentPreferences</a>: <i>
      - <a href="deploymentpreferencesdefinition.md">DeploymentPreferencesDefinition</a></i>
<a href="#managedactions" title="ManagedActions">ManagedActions</a>: <i>
      - <a href="managedactionsdefinition.md">ManagedActionsDefinition</a></i>
</pre>

## Properties

#### EnvironmentId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentPreferences

_Required_: No

_Type_: List of <a href="deploymentpreferencesdefinition.md">DeploymentPreferencesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedActions

_Required_: No

_Type_: List of <a href="managedactionsdefinition.md">ManagedActionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

