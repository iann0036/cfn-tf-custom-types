# Terraform::AWS::CodedeployDeploymentGroup

CloudFormation equivalent of aws_codedeploy_deployment_group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::CodedeployDeploymentGroup",
    "Properties" : {
        "<a href="#appname" title="AppName">AppName</a>" : <i>String</i>,
        "<a href="#autoscalinggroups" title="AutoscalingGroups">AutoscalingGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#deploymentconfigname" title="DeploymentConfigName">DeploymentConfigName</a>" : <i>String</i>,
        "<a href="#deploymentgroupname" title="DeploymentGroupName">DeploymentGroupName</a>" : <i>String</i>,
        "<a href="#servicerolearn" title="ServiceRoleArn">ServiceRoleArn</a>" : <i>String</i>,
        "<a href="#alarmconfiguration" title="AlarmConfiguration">AlarmConfiguration</a>" : <i>[ <a href="alarmconfiguration.md">AlarmConfiguration</a>, ... ]</i>,
        "<a href="#autorollbackconfiguration" title="AutoRollbackConfiguration">AutoRollbackConfiguration</a>" : <i>[ <a href="autorollbackconfiguration.md">AutoRollbackConfiguration</a>, ... ]</i>,
        "<a href="#bluegreendeploymentconfig" title="BlueGreenDeploymentConfig">BlueGreenDeploymentConfig</a>" : <i>[ <a href="bluegreendeploymentconfig.md">BlueGreenDeploymentConfig</a>, ... ]</i>,
        "<a href="#deploymentstyle" title="DeploymentStyle">DeploymentStyle</a>" : <i>[ <a href="deploymentstyle.md">DeploymentStyle</a>, ... ]</i>,
        "<a href="#ec2tagfilter" title="Ec2TagFilter">Ec2TagFilter</a>" : <i>[ <a href="ec2tagfilter.md">Ec2TagFilter</a>, ... ]</i>,
        "<a href="#ec2tagset" title="Ec2TagSet">Ec2TagSet</a>" : <i>[ <a href="ec2tagset.md">Ec2TagSet</a>, ... ]</i>,
        "<a href="#ecsservice" title="EcsService">EcsService</a>" : <i>[ <a href="ecsservice.md">EcsService</a>, ... ]</i>,
        "<a href="#loadbalancerinfo" title="LoadBalancerInfo">LoadBalancerInfo</a>" : <i>[ <a href="loadbalancerinfo.md">LoadBalancerInfo</a>, ... ]</i>,
        "<a href="#onpremisesinstancetagfilter" title="OnPremisesInstanceTagFilter">OnPremisesInstanceTagFilter</a>" : <i>[ <a href="onpremisesinstancetagfilter.md">OnPremisesInstanceTagFilter</a>, ... ]</i>,
        "<a href="#triggerconfiguration" title="TriggerConfiguration">TriggerConfiguration</a>" : <i>[ <a href="triggerconfiguration.md">TriggerConfiguration</a>, ... ]</i>,
        "<a href="#deploymentreadyoption" title="DeploymentReadyOption">DeploymentReadyOption</a>" : <i>[ <a href="deploymentreadyoption.md">DeploymentReadyOption</a>, ... ]</i>,
        "<a href="#greenfleetprovisioningoption" title="GreenFleetProvisioningOption">GreenFleetProvisioningOption</a>" : <i>[ <a href="greenfleetprovisioningoption.md">GreenFleetProvisioningOption</a>, ... ]</i>,
        "<a href="#terminateblueinstancesondeploymentsuccess" title="TerminateBlueInstancesOnDeploymentSuccess">TerminateBlueInstancesOnDeploymentSuccess</a>" : <i>[ <a href="terminateblueinstancesondeploymentsuccess.md">TerminateBlueInstancesOnDeploymentSuccess</a>, ... ]</i>,
        "<a href="#elbinfo" title="ElbInfo">ElbInfo</a>" : <i>[ <a href="elbinfo.md">ElbInfo</a>, ... ]</i>,
        "<a href="#targetgroupinfo" title="TargetGroupInfo">TargetGroupInfo</a>" : <i>[ <a href="targetgroupinfo.md">TargetGroupInfo</a>, ... ]</i>,
        "<a href="#targetgrouppairinfo" title="TargetGroupPairInfo">TargetGroupPairInfo</a>" : <i>[ <a href="targetgrouppairinfo.md">TargetGroupPairInfo</a>, ... ]</i>,
        "<a href="#prodtrafficroute" title="ProdTrafficRoute">ProdTrafficRoute</a>" : <i>[ <a href="prodtrafficroute.md">ProdTrafficRoute</a>, ... ]</i>,
        "<a href="#targetgroup" title="TargetGroup">TargetGroup</a>" : <i>[ <a href="targetgroup.md">TargetGroup</a>, ... ]</i>,
        "<a href="#testtrafficroute" title="TestTrafficRoute">TestTrafficRoute</a>" : <i>[ <a href="testtrafficroute.md">TestTrafficRoute</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::CodedeployDeploymentGroup
Properties:
    <a href="#appname" title="AppName">AppName</a>: <i>String</i>
    <a href="#autoscalinggroups" title="AutoscalingGroups">AutoscalingGroups</a>: <i>
      - String</i>
    <a href="#deploymentconfigname" title="DeploymentConfigName">DeploymentConfigName</a>: <i>String</i>
    <a href="#deploymentgroupname" title="DeploymentGroupName">DeploymentGroupName</a>: <i>String</i>
    <a href="#servicerolearn" title="ServiceRoleArn">ServiceRoleArn</a>: <i>String</i>
    <a href="#alarmconfiguration" title="AlarmConfiguration">AlarmConfiguration</a>: <i>
      - <a href="alarmconfiguration.md">AlarmConfiguration</a></i>
    <a href="#autorollbackconfiguration" title="AutoRollbackConfiguration">AutoRollbackConfiguration</a>: <i>
      - <a href="autorollbackconfiguration.md">AutoRollbackConfiguration</a></i>
    <a href="#bluegreendeploymentconfig" title="BlueGreenDeploymentConfig">BlueGreenDeploymentConfig</a>: <i>
      - <a href="bluegreendeploymentconfig.md">BlueGreenDeploymentConfig</a></i>
    <a href="#deploymentstyle" title="DeploymentStyle">DeploymentStyle</a>: <i>
      - <a href="deploymentstyle.md">DeploymentStyle</a></i>
    <a href="#ec2tagfilter" title="Ec2TagFilter">Ec2TagFilter</a>: <i>
      - <a href="ec2tagfilter.md">Ec2TagFilter</a></i>
    <a href="#ec2tagset" title="Ec2TagSet">Ec2TagSet</a>: <i>
      - <a href="ec2tagset.md">Ec2TagSet</a></i>
    <a href="#ecsservice" title="EcsService">EcsService</a>: <i>
      - <a href="ecsservice.md">EcsService</a></i>
    <a href="#loadbalancerinfo" title="LoadBalancerInfo">LoadBalancerInfo</a>: <i>
      - <a href="loadbalancerinfo.md">LoadBalancerInfo</a></i>
    <a href="#onpremisesinstancetagfilter" title="OnPremisesInstanceTagFilter">OnPremisesInstanceTagFilter</a>: <i>
      - <a href="onpremisesinstancetagfilter.md">OnPremisesInstanceTagFilter</a></i>
    <a href="#triggerconfiguration" title="TriggerConfiguration">TriggerConfiguration</a>: <i>
      - <a href="triggerconfiguration.md">TriggerConfiguration</a></i>
    <a href="#deploymentreadyoption" title="DeploymentReadyOption">DeploymentReadyOption</a>: <i>
      - <a href="deploymentreadyoption.md">DeploymentReadyOption</a></i>
    <a href="#greenfleetprovisioningoption" title="GreenFleetProvisioningOption">GreenFleetProvisioningOption</a>: <i>
      - <a href="greenfleetprovisioningoption.md">GreenFleetProvisioningOption</a></i>
    <a href="#terminateblueinstancesondeploymentsuccess" title="TerminateBlueInstancesOnDeploymentSuccess">TerminateBlueInstancesOnDeploymentSuccess</a>: <i>
      - <a href="terminateblueinstancesondeploymentsuccess.md">TerminateBlueInstancesOnDeploymentSuccess</a></i>
    <a href="#elbinfo" title="ElbInfo">ElbInfo</a>: <i>
      - <a href="elbinfo.md">ElbInfo</a></i>
    <a href="#targetgroupinfo" title="TargetGroupInfo">TargetGroupInfo</a>: <i>
      - <a href="targetgroupinfo.md">TargetGroupInfo</a></i>
    <a href="#targetgrouppairinfo" title="TargetGroupPairInfo">TargetGroupPairInfo</a>: <i>
      - <a href="targetgrouppairinfo.md">TargetGroupPairInfo</a></i>
    <a href="#prodtrafficroute" title="ProdTrafficRoute">ProdTrafficRoute</a>: <i>
      - <a href="prodtrafficroute.md">ProdTrafficRoute</a></i>
    <a href="#targetgroup" title="TargetGroup">TargetGroup</a>: <i>
      - <a href="targetgroup.md">TargetGroup</a></i>
    <a href="#testtrafficroute" title="TestTrafficRoute">TestTrafficRoute</a>: <i>
      - <a href="testtrafficroute.md">TestTrafficRoute</a></i>
</pre>

## Properties

#### AppName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscalingGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentConfigName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRoleArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlarmConfiguration

_Required_: No

_Type_: List of <a href="alarmconfiguration.md">AlarmConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoRollbackConfiguration

_Required_: No

_Type_: List of <a href="autorollbackconfiguration.md">AutoRollbackConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlueGreenDeploymentConfig

_Required_: No

_Type_: List of <a href="bluegreendeploymentconfig.md">BlueGreenDeploymentConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentStyle

_Required_: No

_Type_: List of <a href="deploymentstyle.md">DeploymentStyle</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ec2TagFilter

_Required_: No

_Type_: List of <a href="ec2tagfilter.md">Ec2TagFilter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ec2TagSet

_Required_: No

_Type_: List of <a href="ec2tagset.md">Ec2TagSet</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcsService

_Required_: No

_Type_: List of <a href="ecsservice.md">EcsService</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerInfo

_Required_: No

_Type_: List of <a href="loadbalancerinfo.md">LoadBalancerInfo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnPremisesInstanceTagFilter

_Required_: No

_Type_: List of <a href="onpremisesinstancetagfilter.md">OnPremisesInstanceTagFilter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerConfiguration

_Required_: No

_Type_: List of <a href="triggerconfiguration.md">TriggerConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentReadyOption

_Required_: No

_Type_: List of <a href="deploymentreadyoption.md">DeploymentReadyOption</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GreenFleetProvisioningOption

_Required_: No

_Type_: List of <a href="greenfleetprovisioningoption.md">GreenFleetProvisioningOption</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminateBlueInstancesOnDeploymentSuccess

_Required_: No

_Type_: List of <a href="terminateblueinstancesondeploymentsuccess.md">TerminateBlueInstancesOnDeploymentSuccess</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElbInfo

_Required_: No

_Type_: List of <a href="elbinfo.md">ElbInfo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroupInfo

_Required_: No

_Type_: List of <a href="targetgroupinfo.md">TargetGroupInfo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroupPairInfo

_Required_: No

_Type_: List of <a href="targetgrouppairinfo.md">TargetGroupPairInfo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProdTrafficRoute

_Required_: No

_Type_: List of <a href="prodtrafficroute.md">ProdTrafficRoute</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroup

_Required_: No

_Type_: List of <a href="targetgroup.md">TargetGroup</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestTrafficRoute

_Required_: No

_Type_: List of <a href="testtrafficroute.md">TestTrafficRoute</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

