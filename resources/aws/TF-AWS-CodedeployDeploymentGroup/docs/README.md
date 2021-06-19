# TF::AWS::CodedeployDeploymentGroup

Provides a CodeDeploy Deployment Group for a CodeDeploy Application

~> **NOTE on blue/green deployments:** When using `green_fleet_provisioning_option` with the `COPY_AUTO_SCALING_GROUP` action, CodeDeploy will create a new ASG with a different name. This ASG is _not_ managed by terraform and will conflict with existing configuration and state. You may want to use a different approach to managing deployments that involve multiple ASG, such as `DISCOVER_EXISTING` with separate blue and green ASG.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::CodedeployDeploymentGroup",
    "Properties" : {
        "<a href="#appname" title="AppName">AppName</a>" : <i>String</i>,
        "<a href="#autoscalinggroups" title="AutoscalingGroups">AutoscalingGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#deploymentconfigname" title="DeploymentConfigName">DeploymentConfigName</a>" : <i>String</i>,
        "<a href="#deploymentgroupname" title="DeploymentGroupName">DeploymentGroupName</a>" : <i>String</i>,
        "<a href="#servicerolearn" title="ServiceRoleArn">ServiceRoleArn</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#alarmconfiguration" title="AlarmConfiguration">AlarmConfiguration</a>" : <i>[ <a href="alarmconfigurationdefinition.md">AlarmConfigurationDefinition</a>, ... ]</i>,
        "<a href="#autorollbackconfiguration" title="AutoRollbackConfiguration">AutoRollbackConfiguration</a>" : <i>[ <a href="autorollbackconfigurationdefinition.md">AutoRollbackConfigurationDefinition</a>, ... ]</i>,
        "<a href="#bluegreendeploymentconfig" title="BlueGreenDeploymentConfig">BlueGreenDeploymentConfig</a>" : <i>[ <a href="bluegreendeploymentconfigdefinition.md">BlueGreenDeploymentConfigDefinition</a>, ... ]</i>,
        "<a href="#deploymentstyle" title="DeploymentStyle">DeploymentStyle</a>" : <i>[ <a href="deploymentstyledefinition.md">DeploymentStyleDefinition</a>, ... ]</i>,
        "<a href="#ec2tagfilter" title="Ec2TagFilter">Ec2TagFilter</a>" : <i>[ <a href="ec2tagfilterdefinition.md">Ec2TagFilterDefinition</a>, ... ]</i>,
        "<a href="#ec2tagset" title="Ec2TagSet">Ec2TagSet</a>" : <i>[ <a href="ec2tagsetdefinition.md">Ec2TagSetDefinition</a>, ... ]</i>,
        "<a href="#ecsservice" title="EcsService">EcsService</a>" : <i>[ <a href="ecsservicedefinition.md">EcsServiceDefinition</a>, ... ]</i>,
        "<a href="#loadbalancerinfo" title="LoadBalancerInfo">LoadBalancerInfo</a>" : <i>[ <a href="loadbalancerinfodefinition.md">LoadBalancerInfoDefinition</a>, ... ]</i>,
        "<a href="#onpremisesinstancetagfilter" title="OnPremisesInstanceTagFilter">OnPremisesInstanceTagFilter</a>" : <i>[ <a href="onpremisesinstancetagfilterdefinition.md">OnPremisesInstanceTagFilterDefinition</a>, ... ]</i>,
        "<a href="#triggerconfiguration" title="TriggerConfiguration">TriggerConfiguration</a>" : <i>[ <a href="triggerconfigurationdefinition.md">TriggerConfigurationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::CodedeployDeploymentGroup
Properties:
    <a href="#appname" title="AppName">AppName</a>: <i>String</i>
    <a href="#autoscalinggroups" title="AutoscalingGroups">AutoscalingGroups</a>: <i>
      - String</i>
    <a href="#deploymentconfigname" title="DeploymentConfigName">DeploymentConfigName</a>: <i>String</i>
    <a href="#deploymentgroupname" title="DeploymentGroupName">DeploymentGroupName</a>: <i>String</i>
    <a href="#servicerolearn" title="ServiceRoleArn">ServiceRoleArn</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#alarmconfiguration" title="AlarmConfiguration">AlarmConfiguration</a>: <i>
      - <a href="alarmconfigurationdefinition.md">AlarmConfigurationDefinition</a></i>
    <a href="#autorollbackconfiguration" title="AutoRollbackConfiguration">AutoRollbackConfiguration</a>: <i>
      - <a href="autorollbackconfigurationdefinition.md">AutoRollbackConfigurationDefinition</a></i>
    <a href="#bluegreendeploymentconfig" title="BlueGreenDeploymentConfig">BlueGreenDeploymentConfig</a>: <i>
      - <a href="bluegreendeploymentconfigdefinition.md">BlueGreenDeploymentConfigDefinition</a></i>
    <a href="#deploymentstyle" title="DeploymentStyle">DeploymentStyle</a>: <i>
      - <a href="deploymentstyledefinition.md">DeploymentStyleDefinition</a></i>
    <a href="#ec2tagfilter" title="Ec2TagFilter">Ec2TagFilter</a>: <i>
      - <a href="ec2tagfilterdefinition.md">Ec2TagFilterDefinition</a></i>
    <a href="#ec2tagset" title="Ec2TagSet">Ec2TagSet</a>: <i>
      - <a href="ec2tagsetdefinition.md">Ec2TagSetDefinition</a></i>
    <a href="#ecsservice" title="EcsService">EcsService</a>: <i>
      - <a href="ecsservicedefinition.md">EcsServiceDefinition</a></i>
    <a href="#loadbalancerinfo" title="LoadBalancerInfo">LoadBalancerInfo</a>: <i>
      - <a href="loadbalancerinfodefinition.md">LoadBalancerInfoDefinition</a></i>
    <a href="#onpremisesinstancetagfilter" title="OnPremisesInstanceTagFilter">OnPremisesInstanceTagFilter</a>: <i>
      - <a href="onpremisesinstancetagfilterdefinition.md">OnPremisesInstanceTagFilterDefinition</a></i>
    <a href="#triggerconfiguration" title="TriggerConfiguration">TriggerConfiguration</a>: <i>
      - <a href="triggerconfigurationdefinition.md">TriggerConfigurationDefinition</a></i>
</pre>

## Properties

#### AppName

The name of the application.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscalingGroups

Autoscaling groups associated with the deployment group.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentConfigName

The name of the group's deployment config. The default is "CodeDeployDefault.OneAtATime".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentGroupName

The name of the deployment group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRoleArn

The service role ARN that allows deployments.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlarmConfiguration

_Required_: No

_Type_: List of <a href="alarmconfigurationdefinition.md">AlarmConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoRollbackConfiguration

_Required_: No

_Type_: List of <a href="autorollbackconfigurationdefinition.md">AutoRollbackConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlueGreenDeploymentConfig

_Required_: No

_Type_: List of <a href="bluegreendeploymentconfigdefinition.md">BlueGreenDeploymentConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentStyle

_Required_: No

_Type_: List of <a href="deploymentstyledefinition.md">DeploymentStyleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ec2TagFilter

_Required_: No

_Type_: List of <a href="ec2tagfilterdefinition.md">Ec2TagFilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ec2TagSet

_Required_: No

_Type_: List of <a href="ec2tagsetdefinition.md">Ec2TagSetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcsService

_Required_: No

_Type_: List of <a href="ecsservicedefinition.md">EcsServiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerInfo

_Required_: No

_Type_: List of <a href="loadbalancerinfodefinition.md">LoadBalancerInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnPremisesInstanceTagFilter

_Required_: No

_Type_: List of <a href="onpremisesinstancetagfilterdefinition.md">OnPremisesInstanceTagFilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerConfiguration

_Required_: No

_Type_: List of <a href="triggerconfigurationdefinition.md">TriggerConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### ComputePlatform

Returns the <code>ComputePlatform</code> value.

#### DeploymentGroupId

Returns the <code>DeploymentGroupId</code> value.

#### Id

Returns the <code>Id</code> value.

