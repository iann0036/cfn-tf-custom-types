# Terraform::AWS::EcsService

-> **Note:** To prevent a race condition during service deletion, make sure to set `depends_on` to the related `aws_iam_role_policy`; otherwise, the policy may be destroyed too soon and the ECS service will then get stuck in the `DRAINING` state.

Provides an ECS service - effectively a task that is expected to run until an error occurs or a user terminates it (typically a webserver or a database).

See [ECS Services section in AWS developer guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::EcsService",
    "Properties" : {
        "<a href="#cluster" title="Cluster">Cluster</a>" : <i>String</i>,
        "<a href="#deploymentmaximumpercent" title="DeploymentMaximumPercent">DeploymentMaximumPercent</a>" : <i>Double</i>,
        "<a href="#deploymentminimumhealthypercent" title="DeploymentMinimumHealthyPercent">DeploymentMinimumHealthyPercent</a>" : <i>Double</i>,
        "<a href="#desiredcount" title="DesiredCount">DesiredCount</a>" : <i>Double</i>,
        "<a href="#enableecsmanagedtags" title="EnableEcsManagedTags">EnableEcsManagedTags</a>" : <i>Boolean</i>,
        "<a href="#healthcheckgraceperiodseconds" title="HealthCheckGracePeriodSeconds">HealthCheckGracePeriodSeconds</a>" : <i>Double</i>,
        "<a href="#iamrole" title="IamRole">IamRole</a>" : <i>String</i>,
        "<a href="#launchtype" title="LaunchType">LaunchType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#platformversion" title="PlatformVersion">PlatformVersion</a>" : <i>String</i>,
        "<a href="#propagatetags" title="PropagateTags">PropagateTags</a>" : <i>String</i>,
        "<a href="#schedulingstrategy" title="SchedulingStrategy">SchedulingStrategy</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#taskdefinition" title="TaskDefinition">TaskDefinition</a>" : <i>String</i>,
        "<a href="#capacityproviderstrategy" title="CapacityProviderStrategy">CapacityProviderStrategy</a>" : <i>[ <a href="capacityproviderstrategy.md">CapacityProviderStrategy</a>, ... ]</i>,
        "<a href="#deploymentcontroller" title="DeploymentController">DeploymentController</a>" : <i>[ <a href="deploymentcontroller.md">DeploymentController</a>, ... ]</i>,
        "<a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>" : <i>[ <a href="loadbalancer.md">LoadBalancer</a>, ... ]</i>,
        "<a href="#networkconfiguration" title="NetworkConfiguration">NetworkConfiguration</a>" : <i>[ <a href="networkconfiguration.md">NetworkConfiguration</a>, ... ]</i>,
        "<a href="#orderedplacementstrategy" title="OrderedPlacementStrategy">OrderedPlacementStrategy</a>" : <i>[ <a href="orderedplacementstrategy.md">OrderedPlacementStrategy</a>, ... ]</i>,
        "<a href="#placementconstraints" title="PlacementConstraints">PlacementConstraints</a>" : <i>[ <a href="placementconstraints.md">PlacementConstraints</a>, ... ]</i>,
        "<a href="#placementstrategy" title="PlacementStrategy">PlacementStrategy</a>" : <i>[ <a href="placementstrategy.md">PlacementStrategy</a>, ... ]</i>,
        "<a href="#serviceregistries" title="ServiceRegistries">ServiceRegistries</a>" : <i>[ <a href="serviceregistries.md">ServiceRegistries</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::EcsService
Properties:
    <a href="#cluster" title="Cluster">Cluster</a>: <i>String</i>
    <a href="#deploymentmaximumpercent" title="DeploymentMaximumPercent">DeploymentMaximumPercent</a>: <i>Double</i>
    <a href="#deploymentminimumhealthypercent" title="DeploymentMinimumHealthyPercent">DeploymentMinimumHealthyPercent</a>: <i>Double</i>
    <a href="#desiredcount" title="DesiredCount">DesiredCount</a>: <i>Double</i>
    <a href="#enableecsmanagedtags" title="EnableEcsManagedTags">EnableEcsManagedTags</a>: <i>Boolean</i>
    <a href="#healthcheckgraceperiodseconds" title="HealthCheckGracePeriodSeconds">HealthCheckGracePeriodSeconds</a>: <i>Double</i>
    <a href="#iamrole" title="IamRole">IamRole</a>: <i>String</i>
    <a href="#launchtype" title="LaunchType">LaunchType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#platformversion" title="PlatformVersion">PlatformVersion</a>: <i>String</i>
    <a href="#propagatetags" title="PropagateTags">PropagateTags</a>: <i>String</i>
    <a href="#schedulingstrategy" title="SchedulingStrategy">SchedulingStrategy</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#taskdefinition" title="TaskDefinition">TaskDefinition</a>: <i>String</i>
    <a href="#capacityproviderstrategy" title="CapacityProviderStrategy">CapacityProviderStrategy</a>: <i>
      - <a href="capacityproviderstrategy.md">CapacityProviderStrategy</a></i>
    <a href="#deploymentcontroller" title="DeploymentController">DeploymentController</a>: <i>
      - <a href="deploymentcontroller.md">DeploymentController</a></i>
    <a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>: <i>
      - <a href="loadbalancer.md">LoadBalancer</a></i>
    <a href="#networkconfiguration" title="NetworkConfiguration">NetworkConfiguration</a>: <i>
      - <a href="networkconfiguration.md">NetworkConfiguration</a></i>
    <a href="#orderedplacementstrategy" title="OrderedPlacementStrategy">OrderedPlacementStrategy</a>: <i>
      - <a href="orderedplacementstrategy.md">OrderedPlacementStrategy</a></i>
    <a href="#placementconstraints" title="PlacementConstraints">PlacementConstraints</a>: <i>
      - <a href="placementconstraints.md">PlacementConstraints</a></i>
    <a href="#placementstrategy" title="PlacementStrategy">PlacementStrategy</a>: <i>
      - <a href="placementstrategy.md">PlacementStrategy</a></i>
    <a href="#serviceregistries" title="ServiceRegistries">ServiceRegistries</a>: <i>
      - <a href="serviceregistries.md">ServiceRegistries</a></i>
</pre>

## Properties

#### Cluster

ARN of an ECS cluster.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentMaximumPercent

The upper limit (as a percentage of the service's desiredCount) of the number of running tasks that can be running in a service during a deployment. Not valid when using the `DAEMON` scheduling strategy.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentMinimumHealthyPercent

The lower limit (as a percentage of the service's desiredCount) of the number of running tasks that must remain running and healthy in a service during a deployment.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredCount

The number of instances of the task definition to place and keep running. Defaults to 0. Do not specify if using the `DAEMON` scheduling strategy.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableEcsManagedTags

Specifies whether to enable Amazon ECS managed tags for the tasks within the service.

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

The launch type on which to run your service. The valid values are `EC2` and `FARGATE`. Defaults to `EC2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the service (up to 255 letters, numbers, hyphens, and underscores).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlatformVersion

The platform version on which to run your service. Only applicable for `launch_type` set to `FARGATE`. Defaults to `LATEST`. More information about Fargate platform versions can be found in the [AWS ECS User Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PropagateTags

Specifies whether to propagate the tags from the task definition or the service to the tasks. The valid values are `SERVICE` and `TASK_DEFINITION`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchedulingStrategy

The scheduling strategy to use for the service. The valid values are `REPLICA` and `DAEMON`. Defaults to `REPLICA`. Note that [*Fargate tasks do not support the `DAEMON` scheduling strategy*](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value mapping of resource tags.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskDefinition

The family and revision (`family:revision`) or full ARN of the task definition that you want to run in your service.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapacityProviderStrategy

_Required_: No

_Type_: List of <a href="capacityproviderstrategy.md">CapacityProviderStrategy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentController

_Required_: No

_Type_: List of <a href="deploymentcontroller.md">DeploymentController</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancer

_Required_: No

_Type_: List of <a href="loadbalancer.md">LoadBalancer</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkConfiguration

_Required_: No

_Type_: List of <a href="networkconfiguration.md">NetworkConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrderedPlacementStrategy

_Required_: No

_Type_: List of <a href="orderedplacementstrategy.md">OrderedPlacementStrategy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlacementConstraints

_Required_: No

_Type_: List of <a href="placementconstraints.md">PlacementConstraints</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlacementStrategy

_Required_: No

_Type_: List of <a href="placementstrategy.md">PlacementStrategy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRegistries

_Required_: No

_Type_: List of <a href="serviceregistries.md">ServiceRegistries</a>

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

