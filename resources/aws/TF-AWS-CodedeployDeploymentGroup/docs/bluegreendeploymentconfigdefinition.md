# TF::AWS::CodedeployDeploymentGroup BlueGreenDeploymentConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#deploymentreadyoption" title="DeploymentReadyOption">DeploymentReadyOption</a>" : <i>[ <a href="deploymentreadyoptiondefinition.md">DeploymentReadyOptionDefinition</a>, ... ]</i>,
    "<a href="#greenfleetprovisioningoption" title="GreenFleetProvisioningOption">GreenFleetProvisioningOption</a>" : <i>[ <a href="greenfleetprovisioningoptiondefinition.md">GreenFleetProvisioningOptionDefinition</a>, ... ]</i>,
    "<a href="#terminateblueinstancesondeploymentsuccess" title="TerminateBlueInstancesOnDeploymentSuccess">TerminateBlueInstancesOnDeploymentSuccess</a>" : <i>[ <a href="terminateblueinstancesondeploymentsuccessdefinition.md">TerminateBlueInstancesOnDeploymentSuccessDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#deploymentreadyoption" title="DeploymentReadyOption">DeploymentReadyOption</a>: <i>
      - <a href="deploymentreadyoptiondefinition.md">DeploymentReadyOptionDefinition</a></i>
<a href="#greenfleetprovisioningoption" title="GreenFleetProvisioningOption">GreenFleetProvisioningOption</a>: <i>
      - <a href="greenfleetprovisioningoptiondefinition.md">GreenFleetProvisioningOptionDefinition</a></i>
<a href="#terminateblueinstancesondeploymentsuccess" title="TerminateBlueInstancesOnDeploymentSuccess">TerminateBlueInstancesOnDeploymentSuccess</a>: <i>
      - <a href="terminateblueinstancesondeploymentsuccessdefinition.md">TerminateBlueInstancesOnDeploymentSuccessDefinition</a></i>
</pre>

## Properties

#### DeploymentReadyOption

_Required_: No

_Type_: List of <a href="deploymentreadyoptiondefinition.md">DeploymentReadyOptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GreenFleetProvisioningOption

_Required_: No

_Type_: List of <a href="greenfleetprovisioningoptiondefinition.md">GreenFleetProvisioningOptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminateBlueInstancesOnDeploymentSuccess

_Required_: No

_Type_: List of <a href="terminateblueinstancesondeploymentsuccessdefinition.md">TerminateBlueInstancesOnDeploymentSuccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

