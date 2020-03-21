# Terraform::Spotinst::ElastigroupAws IntegrationBeanstalk

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#environmentid" title="EnvironmentId">EnvironmentId</a>" : <i>String</i>,
    "<a href="#deploymentpreferences" title="DeploymentPreferences">DeploymentPreferences</a>" : <i>[ <a href="integrationbeanstalk-deploymentpreferences.md">DeploymentPreferences</a>, ... ]</i>,
    "<a href="#managedactions" title="ManagedActions">ManagedActions</a>" : <i>[ <a href="integrationbeanstalk-managedactions.md">ManagedActions</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#environmentid" title="EnvironmentId">EnvironmentId</a>: <i>String</i>
<a href="#deploymentpreferences" title="DeploymentPreferences">DeploymentPreferences</a>: <i>
      - <a href="integrationbeanstalk-deploymentpreferences.md">DeploymentPreferences</a></i>
<a href="#managedactions" title="ManagedActions">ManagedActions</a>: <i>
      - <a href="integrationbeanstalk-managedactions.md">ManagedActions</a></i>
</pre>

## Properties

#### EnvironmentId

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentPreferences

_Required_: No
_Type_: List of <a href="integrationbeanstalk-deploymentpreferences.md">DeploymentPreferences</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedActions

_Required_: No
_Type_: List of <a href="integrationbeanstalk-managedactions.md">ManagedActions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

