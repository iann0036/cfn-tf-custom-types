# Terraform::AWS::EcsService

CloudFormation equivalent of aws_ecs_service

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
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
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
    <a href="#id" title="Id">Id</a>: <i>String</i>
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

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentMaximumPercent

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentMinimumHealthyPercent

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableEcsManagedTags

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckGracePeriodSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamRole

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlatformVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PropagateTags

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchedulingStrategy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskDefinition

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

