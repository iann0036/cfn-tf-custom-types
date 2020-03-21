# Terraform::AWS::CodedeployDeploymentGroup BlueGreenDeploymentConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#deploymentreadyoption" title="DeploymentReadyOption">DeploymentReadyOption</a>" : <i>[ &lt;a href=&#34;bluegreendeploymentconfig-deploymentreadyoption.md&#34;&gt;DeploymentReadyOption&lt;/a&gt;, ... ]</i>,
    "<a href="#greenfleetprovisioningoption" title="GreenFleetProvisioningOption">GreenFleetProvisioningOption</a>" : <i>[ &lt;a href=&#34;bluegreendeploymentconfig-greenfleetprovisioningoption.md&#34;&gt;GreenFleetProvisioningOption&lt;/a&gt;, ... ]</i>,
    "<a href="#terminateblueinstancesondeploymentsuccess" title="TerminateBlueInstancesOnDeploymentSuccess">TerminateBlueInstancesOnDeploymentSuccess</a>" : <i>[ &lt;a href=&#34;bluegreendeploymentconfig-terminateblueinstancesondeploymentsuccess.md&#34;&gt;TerminateBlueInstancesOnDeploymentSuccess&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#deploymentreadyoption" title="DeploymentReadyOption">DeploymentReadyOption</a>: <i>
      - &lt;a href=&#34;bluegreendeploymentconfig-deploymentreadyoption.md&#34;&gt;DeploymentReadyOption&lt;/a&gt;</i>
<a href="#greenfleetprovisioningoption" title="GreenFleetProvisioningOption">GreenFleetProvisioningOption</a>: <i>
      - &lt;a href=&#34;bluegreendeploymentconfig-greenfleetprovisioningoption.md&#34;&gt;GreenFleetProvisioningOption&lt;/a&gt;</i>
<a href="#terminateblueinstancesondeploymentsuccess" title="TerminateBlueInstancesOnDeploymentSuccess">TerminateBlueInstancesOnDeploymentSuccess</a>: <i>
      - &lt;a href=&#34;bluegreendeploymentconfig-terminateblueinstancesondeploymentsuccess.md&#34;&gt;TerminateBlueInstancesOnDeploymentSuccess&lt;/a&gt;</i>
</pre>

## Properties

#### DeploymentReadyOption

_Required_: No
_Type_: List of &lt;a href=&#34;bluegreendeploymentconfig-deploymentreadyoption.md&#34;&gt;DeploymentReadyOption&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GreenFleetProvisioningOption

_Required_: No
_Type_: List of &lt;a href=&#34;bluegreendeploymentconfig-greenfleetprovisioningoption.md&#34;&gt;GreenFleetProvisioningOption&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminateBlueInstancesOnDeploymentSuccess

_Required_: No
_Type_: List of &lt;a href=&#34;bluegreendeploymentconfig-terminateblueinstancesondeploymentsuccess.md&#34;&gt;TerminateBlueInstancesOnDeploymentSuccess&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

