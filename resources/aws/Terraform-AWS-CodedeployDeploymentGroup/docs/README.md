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
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#servicerolearn" title="ServiceRoleArn">ServiceRoleArn</a>" : <i>String</i>,
        "<a href="#alarmconfiguration" title="AlarmConfiguration">AlarmConfiguration</a>" : <i>[ &lt;a href=&#34;alarmconfiguration.md&#34;&gt;AlarmConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#autorollbackconfiguration" title="AutoRollbackConfiguration">AutoRollbackConfiguration</a>" : <i>[ &lt;a href=&#34;autorollbackconfiguration.md&#34;&gt;AutoRollbackConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#bluegreendeploymentconfig" title="BlueGreenDeploymentConfig">BlueGreenDeploymentConfig</a>" : <i>[ &lt;a href=&#34;bluegreendeploymentconfig.md&#34;&gt;BlueGreenDeploymentConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#deploymentstyle" title="DeploymentStyle">DeploymentStyle</a>" : <i>[ &lt;a href=&#34;deploymentstyle.md&#34;&gt;DeploymentStyle&lt;/a&gt;, ... ]</i>,
        "<a href="#ec2tagfilter" title="Ec2TagFilter">Ec2TagFilter</a>" : <i>[ &lt;a href=&#34;ec2tagfilter.md&#34;&gt;Ec2TagFilter&lt;/a&gt;, ... ]</i>,
        "<a href="#ec2tagset" title="Ec2TagSet">Ec2TagSet</a>" : <i>[ &lt;a href=&#34;ec2tagset.md&#34;&gt;Ec2TagSet&lt;/a&gt;, ... ]</i>,
        "<a href="#ecsservice" title="EcsService">EcsService</a>" : <i>[ &lt;a href=&#34;ecsservice.md&#34;&gt;EcsService&lt;/a&gt;, ... ]</i>,
        "<a href="#loadbalancerinfo" title="LoadBalancerInfo">LoadBalancerInfo</a>" : <i>[ &lt;a href=&#34;loadbalancerinfo.md&#34;&gt;LoadBalancerInfo&lt;/a&gt;, ... ]</i>,
        "<a href="#onpremisesinstancetagfilter" title="OnPremisesInstanceTagFilter">OnPremisesInstanceTagFilter</a>" : <i>[ &lt;a href=&#34;onpremisesinstancetagfilter.md&#34;&gt;OnPremisesInstanceTagFilter&lt;/a&gt;, ... ]</i>,
        "<a href="#triggerconfiguration" title="TriggerConfiguration">TriggerConfiguration</a>" : <i>[ &lt;a href=&#34;triggerconfiguration.md&#34;&gt;TriggerConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#deploymentreadyoption" title="DeploymentReadyOption">DeploymentReadyOption</a>" : <i>[ &lt;a href=&#34;deploymentreadyoption.md&#34;&gt;DeploymentReadyOption&lt;/a&gt;, ... ]</i>,
        "<a href="#greenfleetprovisioningoption" title="GreenFleetProvisioningOption">GreenFleetProvisioningOption</a>" : <i>[ &lt;a href=&#34;greenfleetprovisioningoption.md&#34;&gt;GreenFleetProvisioningOption&lt;/a&gt;, ... ]</i>,
        "<a href="#terminateblueinstancesondeploymentsuccess" title="TerminateBlueInstancesOnDeploymentSuccess">TerminateBlueInstancesOnDeploymentSuccess</a>" : <i>[ &lt;a href=&#34;terminateblueinstancesondeploymentsuccess.md&#34;&gt;TerminateBlueInstancesOnDeploymentSuccess&lt;/a&gt;, ... ]</i>,
        "<a href="#elbinfo" title="ElbInfo">ElbInfo</a>" : <i>[ &lt;a href=&#34;elbinfo.md&#34;&gt;ElbInfo&lt;/a&gt;, ... ]</i>,
        "<a href="#targetgroupinfo" title="TargetGroupInfo">TargetGroupInfo</a>" : <i>[ &lt;a href=&#34;targetgroupinfo.md&#34;&gt;TargetGroupInfo&lt;/a&gt;, ... ]</i>,
        "<a href="#targetgrouppairinfo" title="TargetGroupPairInfo">TargetGroupPairInfo</a>" : <i>[ &lt;a href=&#34;targetgrouppairinfo.md&#34;&gt;TargetGroupPairInfo&lt;/a&gt;, ... ]</i>,
        "<a href="#prodtrafficroute" title="ProdTrafficRoute">ProdTrafficRoute</a>" : <i>[ &lt;a href=&#34;prodtrafficroute.md&#34;&gt;ProdTrafficRoute&lt;/a&gt;, ... ]</i>,
        "<a href="#targetgroup" title="TargetGroup">TargetGroup</a>" : <i>[ &lt;a href=&#34;targetgroup.md&#34;&gt;TargetGroup&lt;/a&gt;, ... ]</i>,
        "<a href="#testtrafficroute" title="TestTrafficRoute">TestTrafficRoute</a>" : <i>[ &lt;a href=&#34;testtrafficroute.md&#34;&gt;TestTrafficRoute&lt;/a&gt;, ... ]</i>
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
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#servicerolearn" title="ServiceRoleArn">ServiceRoleArn</a>: <i>String</i>
    <a href="#alarmconfiguration" title="AlarmConfiguration">AlarmConfiguration</a>: <i>
      - &lt;a href=&#34;alarmconfiguration.md&#34;&gt;AlarmConfiguration&lt;/a&gt;</i>
    <a href="#autorollbackconfiguration" title="AutoRollbackConfiguration">AutoRollbackConfiguration</a>: <i>
      - &lt;a href=&#34;autorollbackconfiguration.md&#34;&gt;AutoRollbackConfiguration&lt;/a&gt;</i>
    <a href="#bluegreendeploymentconfig" title="BlueGreenDeploymentConfig">BlueGreenDeploymentConfig</a>: <i>
      - &lt;a href=&#34;bluegreendeploymentconfig.md&#34;&gt;BlueGreenDeploymentConfig&lt;/a&gt;</i>
    <a href="#deploymentstyle" title="DeploymentStyle">DeploymentStyle</a>: <i>
      - &lt;a href=&#34;deploymentstyle.md&#34;&gt;DeploymentStyle&lt;/a&gt;</i>
    <a href="#ec2tagfilter" title="Ec2TagFilter">Ec2TagFilter</a>: <i>
      - &lt;a href=&#34;ec2tagfilter.md&#34;&gt;Ec2TagFilter&lt;/a&gt;</i>
    <a href="#ec2tagset" title="Ec2TagSet">Ec2TagSet</a>: <i>
      - &lt;a href=&#34;ec2tagset.md&#34;&gt;Ec2TagSet&lt;/a&gt;</i>
    <a href="#ecsservice" title="EcsService">EcsService</a>: <i>
      - &lt;a href=&#34;ecsservice.md&#34;&gt;EcsService&lt;/a&gt;</i>
    <a href="#loadbalancerinfo" title="LoadBalancerInfo">LoadBalancerInfo</a>: <i>
      - &lt;a href=&#34;loadbalancerinfo.md&#34;&gt;LoadBalancerInfo&lt;/a&gt;</i>
    <a href="#onpremisesinstancetagfilter" title="OnPremisesInstanceTagFilter">OnPremisesInstanceTagFilter</a>: <i>
      - &lt;a href=&#34;onpremisesinstancetagfilter.md&#34;&gt;OnPremisesInstanceTagFilter&lt;/a&gt;</i>
    <a href="#triggerconfiguration" title="TriggerConfiguration">TriggerConfiguration</a>: <i>
      - &lt;a href=&#34;triggerconfiguration.md&#34;&gt;TriggerConfiguration&lt;/a&gt;</i>
    <a href="#deploymentreadyoption" title="DeploymentReadyOption">DeploymentReadyOption</a>: <i>
      - &lt;a href=&#34;deploymentreadyoption.md&#34;&gt;DeploymentReadyOption&lt;/a&gt;</i>
    <a href="#greenfleetprovisioningoption" title="GreenFleetProvisioningOption">GreenFleetProvisioningOption</a>: <i>
      - &lt;a href=&#34;greenfleetprovisioningoption.md&#34;&gt;GreenFleetProvisioningOption&lt;/a&gt;</i>
    <a href="#terminateblueinstancesondeploymentsuccess" title="TerminateBlueInstancesOnDeploymentSuccess">TerminateBlueInstancesOnDeploymentSuccess</a>: <i>
      - &lt;a href=&#34;terminateblueinstancesondeploymentsuccess.md&#34;&gt;TerminateBlueInstancesOnDeploymentSuccess&lt;/a&gt;</i>
    <a href="#elbinfo" title="ElbInfo">ElbInfo</a>: <i>
      - &lt;a href=&#34;elbinfo.md&#34;&gt;ElbInfo&lt;/a&gt;</i>
    <a href="#targetgroupinfo" title="TargetGroupInfo">TargetGroupInfo</a>: <i>
      - &lt;a href=&#34;targetgroupinfo.md&#34;&gt;TargetGroupInfo&lt;/a&gt;</i>
    <a href="#targetgrouppairinfo" title="TargetGroupPairInfo">TargetGroupPairInfo</a>: <i>
      - &lt;a href=&#34;targetgrouppairinfo.md&#34;&gt;TargetGroupPairInfo&lt;/a&gt;</i>
    <a href="#prodtrafficroute" title="ProdTrafficRoute">ProdTrafficRoute</a>: <i>
      - &lt;a href=&#34;prodtrafficroute.md&#34;&gt;ProdTrafficRoute&lt;/a&gt;</i>
    <a href="#targetgroup" title="TargetGroup">TargetGroup</a>: <i>
      - &lt;a href=&#34;targetgroup.md&#34;&gt;TargetGroup&lt;/a&gt;</i>
    <a href="#testtrafficroute" title="TestTrafficRoute">TestTrafficRoute</a>: <i>
      - &lt;a href=&#34;testtrafficroute.md&#34;&gt;TestTrafficRoute&lt;/a&gt;</i>
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

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRoleArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlarmConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;alarmconfiguration.md&#34;&gt;AlarmConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoRollbackConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;autorollbackconfiguration.md&#34;&gt;AutoRollbackConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlueGreenDeploymentConfig

_Required_: No

_Type_: List of &lt;a href=&#34;bluegreendeploymentconfig.md&#34;&gt;BlueGreenDeploymentConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentStyle

_Required_: No

_Type_: List of &lt;a href=&#34;deploymentstyle.md&#34;&gt;DeploymentStyle&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ec2TagFilter

_Required_: No

_Type_: List of &lt;a href=&#34;ec2tagfilter.md&#34;&gt;Ec2TagFilter&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ec2TagSet

_Required_: No

_Type_: List of &lt;a href=&#34;ec2tagset.md&#34;&gt;Ec2TagSet&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcsService

_Required_: No

_Type_: List of &lt;a href=&#34;ecsservice.md&#34;&gt;EcsService&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerInfo

_Required_: No

_Type_: List of &lt;a href=&#34;loadbalancerinfo.md&#34;&gt;LoadBalancerInfo&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnPremisesInstanceTagFilter

_Required_: No

_Type_: List of &lt;a href=&#34;onpremisesinstancetagfilter.md&#34;&gt;OnPremisesInstanceTagFilter&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;triggerconfiguration.md&#34;&gt;TriggerConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentReadyOption

_Required_: No

_Type_: List of &lt;a href=&#34;deploymentreadyoption.md&#34;&gt;DeploymentReadyOption&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GreenFleetProvisioningOption

_Required_: No

_Type_: List of &lt;a href=&#34;greenfleetprovisioningoption.md&#34;&gt;GreenFleetProvisioningOption&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminateBlueInstancesOnDeploymentSuccess

_Required_: No

_Type_: List of &lt;a href=&#34;terminateblueinstancesondeploymentsuccess.md&#34;&gt;TerminateBlueInstancesOnDeploymentSuccess&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElbInfo

_Required_: No

_Type_: List of &lt;a href=&#34;elbinfo.md&#34;&gt;ElbInfo&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroupInfo

_Required_: No

_Type_: List of &lt;a href=&#34;targetgroupinfo.md&#34;&gt;TargetGroupInfo&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroupPairInfo

_Required_: No

_Type_: List of &lt;a href=&#34;targetgrouppairinfo.md&#34;&gt;TargetGroupPairInfo&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProdTrafficRoute

_Required_: No

_Type_: List of &lt;a href=&#34;prodtrafficroute.md&#34;&gt;ProdTrafficRoute&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroup

_Required_: No

_Type_: List of &lt;a href=&#34;targetgroup.md&#34;&gt;TargetGroup&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TestTrafficRoute

_Required_: No

_Type_: List of &lt;a href=&#34;testtrafficroute.md&#34;&gt;TestTrafficRoute&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

