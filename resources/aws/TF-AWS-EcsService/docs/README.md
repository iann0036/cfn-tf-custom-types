# TF::AWS::EcsService

-> **Note:** To prevent a race condition during service deletion, make sure to set `depends_on` to the related `aws_iam_role_policy`; otherwise, the policy may be destroyed too soon and the ECS service will then get stuck in the `DRAINING` state.

Provides an ECS service - effectively a task that is expected to run until an error occurs or a user terminates it (typically a webserver or a database).

See [ECS Services section in AWS developer guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::EcsService",
    "Properties" : {
        "<a href="#cluster" title="Cluster">Cluster</a>" : <i>String</i>,
        "<a href="#deploymentmaximumpercent" title="DeploymentMaximumPercent">DeploymentMaximumPercent</a>" : <i>Double</i>,
        "<a href="#deploymentminimumhealthypercent" title="DeploymentMinimumHealthyPercent">DeploymentMinimumHealthyPercent</a>" : <i>Double</i>,
        "<a href="#desiredcount" title="DesiredCount">DesiredCount</a>" : <i>Double</i>,
        "<a href="#enableecsmanagedtags" title="EnableEcsManagedTags">EnableEcsManagedTags</a>" : <i>Boolean</i>,
        "<a href="#enableexecutecommand" title="EnableExecuteCommand">EnableExecuteCommand</a>" : <i>Boolean</i>,
        "<a href="#forcenewdeployment" title="ForceNewDeployment">ForceNewDeployment</a>" : <i>Boolean</i>,
        "<a href="#healthcheckgraceperiodseconds" title="HealthCheckGracePeriodSeconds">HealthCheckGracePeriodSeconds</a>" : <i>Double</i>,
        "<a href="#iamrole" title="IamRole">IamRole</a>" : <i>String</i>,
        "<a href="#launchtype" title="LaunchType">LaunchType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#platformversion" title="PlatformVersion">PlatformVersion</a>" : <i>String</i>,
        "<a href="#propagatetags" title="PropagateTags">PropagateTags</a>" : <i>String</i>,
        "<a href="#schedulingstrategy" title="SchedulingStrategy">SchedulingStrategy</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#taskdefinition" title="TaskDefinition">TaskDefinition</a>" : <i>String</i>,
        "<a href="#waitforsteadystate" title="WaitForSteadyState">WaitForSteadyState</a>" : <i>Boolean</i>,
        "<a href="#capacityproviderstrategy" title="CapacityProviderStrategy">CapacityProviderStrategy</a>" : <i>[ <a href="capacityproviderstrategydefinition.md">CapacityProviderStrategyDefinition</a>, ... ]</i>,
        "<a href="#deploymentcircuitbreaker" title="DeploymentCircuitBreaker">DeploymentCircuitBreaker</a>" : <i>[ <a href="deploymentcircuitbreakerdefinition.md">DeploymentCircuitBreakerDefinition</a>, ... ]</i>,
        "<a href="#deploymentcontroller" title="DeploymentController">DeploymentController</a>" : <i>[ <a href="deploymentcontrollerdefinition.md">DeploymentControllerDefinition</a>, ... ]</i>,
        "<a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>" : <i>[ <a href="loadbalancerdefinition.md">LoadBalancerDefinition</a>, ... ]</i>,
        "<a href="#networkconfiguration" title="NetworkConfiguration">NetworkConfiguration</a>" : <i>[ <a href="networkconfigurationdefinition.md">NetworkConfigurationDefinition</a>, ... ]</i>,
        "<a href="#orderedplacementstrategy" title="OrderedPlacementStrategy">OrderedPlacementStrategy</a>" : <i>[ <a href="orderedplacementstrategydefinition.md">OrderedPlacementStrategyDefinition</a>, ... ]</i>,
        "<a href="#placementconstraints" title="PlacementConstraints">PlacementConstraints</a>" : <i>[ <a href="placementconstraintsdefinition.md">PlacementConstraintsDefinition</a>, ... ]</i>,
        "<a href="#serviceregistries" title="ServiceRegistries">ServiceRegistries</a>" : <i>[ <a href="serviceregistriesdefinition.md">ServiceRegistriesDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::EcsService
Properties:
    <a href="#cluster" title="Cluster">Cluster</a>: <i>String</i>
    <a href="#deploymentmaximumpercent" title="DeploymentMaximumPercent">DeploymentMaximumPercent</a>: <i>Double</i>
    <a href="#deploymentminimumhealthypercent" title="DeploymentMinimumHealthyPercent">DeploymentMinimumHealthyPercent</a>: <i>Double</i>
    <a href="#desiredcount" title="DesiredCount">DesiredCount</a>: <i>Double</i>
    <a href="#enableecsmanagedtags" title="EnableEcsManagedTags">EnableEcsManagedTags</a>: <i>Boolean</i>
    <a href="#enableexecutecommand" title="EnableExecuteCommand">EnableExecuteCommand</a>: <i>Boolean</i>
    <a href="#forcenewdeployment" title="ForceNewDeployment">ForceNewDeployment</a>: <i>Boolean</i>
    <a href="#healthcheckgraceperiodseconds" title="HealthCheckGracePeriodSeconds">HealthCheckGracePeriodSeconds</a>: <i>Double</i>
    <a href="#iamrole" title="IamRole">IamRole</a>: <i>String</i>
    <a href="#launchtype" title="LaunchType">LaunchType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#platformversion" title="PlatformVersion">PlatformVersion</a>: <i>String</i>
    <a href="#propagatetags" title="PropagateTags">PropagateTags</a>: <i>String</i>
    <a href="#schedulingstrategy" title="SchedulingStrategy">SchedulingStrategy</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#taskdefinition" title="TaskDefinition">TaskDefinition</a>: <i>String</i>
    <a href="#waitforsteadystate" title="WaitForSteadyState">WaitForSteadyState</a>: <i>Boolean</i>
    <a href="#capacityproviderstrategy" title="CapacityProviderStrategy">CapacityProviderStrategy</a>: <i>
      - <a href="capacityproviderstrategydefinition.md">CapacityProviderStrategyDefinition</a></i>
    <a href="#deploymentcircuitbreaker" title="DeploymentCircuitBreaker">DeploymentCircuitBreaker</a>: <i>
      - <a href="deploymentcircuitbreakerdefinition.md">DeploymentCircuitBreakerDefinition</a></i>
    <a href="#deploymentcontroller" title="DeploymentController">DeploymentController</a>: <i>
      - <a href="deploymentcontrollerdefinition.md">DeploymentControllerDefinition</a></i>
    <a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>: <i>
      - <a href="loadbalancerdefinition.md">LoadBalancerDefinition</a></i>
    <a href="#networkconfiguration" title="NetworkConfiguration">NetworkConfiguration</a>: <i>
      - <a href="networkconfigurationdefinition.md">NetworkConfigurationDefinition</a></i>
    <a href="#orderedplacementstrategy" title="OrderedPlacementStrategy">OrderedPlacementStrategy</a>: <i>
      - <a href="orderedplacementstrategydefinition.md">OrderedPlacementStrategyDefinition</a></i>
    <a href="#placementconstraints" title="PlacementConstraints">PlacementConstraints</a>: <i>
      - <a href="placementconstraintsdefinition.md">PlacementConstraintsDefinition</a></i>
    <a href="#serviceregistries" title="ServiceRegistries">ServiceRegistries</a>: <i>
      - <a href="serviceregistriesdefinition.md">ServiceRegistriesDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Cluster

ARN of an ECS cluster.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentMaximumPercent

Upper limit (as a percentage of the service's desiredCount) of the number of running tasks that can be running in a service during a deployment. Not valid when using the `DAEMON` scheduling strategy.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentMinimumHealthyPercent

Lower limit (as a percentage of the service's desiredCount) of the number of running tasks that must remain running and healthy in a service during a deployment.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredCount

Number of instances of the task definition to place and keep running. Defaults to 0. Do not specify if using the `DAEMON` scheduling strategy.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableEcsManagedTags

Specifies whether to enable Amazon ECS managed tags for the tasks within the service.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableExecuteCommand

Specifies whether to enable Amazon ECS Exec for the tasks within the service.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceNewDeployment

Enable to force a new task deployment of the service. This can be used to update tasks to use a newer Docker image with same image/tag combination (e.g. `myimage:latest`), roll Fargate tasks onto a newer platform version, or immediately deploy `ordered_placement_strategy` and `placement_constraints` updates.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckGracePeriodSeconds

Seconds to ignore failing load balancer health checks on newly instantiated tasks to prevent premature shutdown, up to 2147483647. Only valid for services configured to use load balancers.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamRole

ARN of the IAM role that allows Amazon ECS to make calls to your load balancer on your behalf. This parameter is required if you are using a load balancer with your service, but only if your task definition does not use the `awsvpc` network mode. If using `awsvpc` network mode, do not specify this role. If your account has already created the Amazon ECS service-linked role, that role is used by default for your service unless you specify a role here.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchType

Launch type on which to run your service. The valid values are `EC2`, `FARGATE`, and `EXTERNAL`. Defaults to `EC2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the service (up to 255 letters, numbers, hyphens, and underscores).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlatformVersion

Platform version on which to run your service. Only applicable for `launch_type` set to `FARGATE`. Defaults to `LATEST`. More information about Fargate platform versions can be found in the [AWS ECS User Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PropagateTags

Specifies whether to propagate the tags from the task definition or the service to the tasks. The valid values are `SERVICE` and `TASK_DEFINITION`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchedulingStrategy

Scheduling strategy to use for the service. The valid values are `REPLICA` and `DAEMON`. Defaults to `REPLICA`. Note that [*Tasks using the Fargate launch type or the `CODE_DEPLOY` or `EXTERNAL` deployment controller types don't support the `DAEMON` scheduling strategy*](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskDefinition

Family and revision (`family:revision`) or full ARN of the task definition that you want to run in your service. Required unless using the `EXTERNAL` deployment controller. If a revision is not specified, the latest `ACTIVE` revision is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForSteadyState

If `true`, Terraform will wait for the service to reach a steady state (like [`aws ecs wait services-stable`](https://docs.aws.amazon.com/cli/latest/reference/ecs/wait/services-stable.html)) before continuing. Default `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapacityProviderStrategy

_Required_: No

_Type_: List of <a href="capacityproviderstrategydefinition.md">CapacityProviderStrategyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentCircuitBreaker

_Required_: No

_Type_: List of <a href="deploymentcircuitbreakerdefinition.md">DeploymentCircuitBreakerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentController

_Required_: No

_Type_: List of <a href="deploymentcontrollerdefinition.md">DeploymentControllerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancer

_Required_: No

_Type_: List of <a href="loadbalancerdefinition.md">LoadBalancerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkConfiguration

_Required_: No

_Type_: List of <a href="networkconfigurationdefinition.md">NetworkConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrderedPlacementStrategy

_Required_: No

_Type_: List of <a href="orderedplacementstrategydefinition.md">OrderedPlacementStrategyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlacementConstraints

_Required_: No

_Type_: List of <a href="placementconstraintsdefinition.md">PlacementConstraintsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRegistries

_Required_: No

_Type_: List of <a href="serviceregistriesdefinition.md">ServiceRegistriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

