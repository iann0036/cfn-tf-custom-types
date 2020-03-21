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
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#taskdefinition" title="TaskDefinition">TaskDefinition</a>" : <i>String</i>,
        "<a href="#capacityproviderstrategy" title="CapacityProviderStrategy">CapacityProviderStrategy</a>" : <i>[ &lt;a href=&#34;capacityproviderstrategy.md&#34;&gt;CapacityProviderStrategy&lt;/a&gt;, ... ]</i>,
        "<a href="#deploymentcontroller" title="DeploymentController">DeploymentController</a>" : <i>[ &lt;a href=&#34;deploymentcontroller.md&#34;&gt;DeploymentController&lt;/a&gt;, ... ]</i>,
        "<a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>" : <i>[ &lt;a href=&#34;loadbalancer.md&#34;&gt;LoadBalancer&lt;/a&gt;, ... ]</i>,
        "<a href="#networkconfiguration" title="NetworkConfiguration">NetworkConfiguration</a>" : <i>[ &lt;a href=&#34;networkconfiguration.md&#34;&gt;NetworkConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#orderedplacementstrategy" title="OrderedPlacementStrategy">OrderedPlacementStrategy</a>" : <i>[ &lt;a href=&#34;orderedplacementstrategy.md&#34;&gt;OrderedPlacementStrategy&lt;/a&gt;, ... ]</i>,
        "<a href="#placementconstraints" title="PlacementConstraints">PlacementConstraints</a>" : <i>[ &lt;a href=&#34;placementconstraints.md&#34;&gt;PlacementConstraints&lt;/a&gt;, ... ]</i>,
        "<a href="#placementstrategy" title="PlacementStrategy">PlacementStrategy</a>" : <i>[ &lt;a href=&#34;placementstrategy.md&#34;&gt;PlacementStrategy&lt;/a&gt;, ... ]</i>,
        "<a href="#serviceregistries" title="ServiceRegistries">ServiceRegistries</a>" : <i>[ &lt;a href=&#34;serviceregistries.md&#34;&gt;ServiceRegistries&lt;/a&gt;, ... ]</i>
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
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#taskdefinition" title="TaskDefinition">TaskDefinition</a>: <i>String</i>
    <a href="#capacityproviderstrategy" title="CapacityProviderStrategy">CapacityProviderStrategy</a>: <i>
      - &lt;a href=&#34;capacityproviderstrategy.md&#34;&gt;CapacityProviderStrategy&lt;/a&gt;</i>
    <a href="#deploymentcontroller" title="DeploymentController">DeploymentController</a>: <i>
      - &lt;a href=&#34;deploymentcontroller.md&#34;&gt;DeploymentController&lt;/a&gt;</i>
    <a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>: <i>
      - &lt;a href=&#34;loadbalancer.md&#34;&gt;LoadBalancer&lt;/a&gt;</i>
    <a href="#networkconfiguration" title="NetworkConfiguration">NetworkConfiguration</a>: <i>
      - &lt;a href=&#34;networkconfiguration.md&#34;&gt;NetworkConfiguration&lt;/a&gt;</i>
    <a href="#orderedplacementstrategy" title="OrderedPlacementStrategy">OrderedPlacementStrategy</a>: <i>
      - &lt;a href=&#34;orderedplacementstrategy.md&#34;&gt;OrderedPlacementStrategy&lt;/a&gt;</i>
    <a href="#placementconstraints" title="PlacementConstraints">PlacementConstraints</a>: <i>
      - &lt;a href=&#34;placementconstraints.md&#34;&gt;PlacementConstraints&lt;/a&gt;</i>
    <a href="#placementstrategy" title="PlacementStrategy">PlacementStrategy</a>: <i>
      - &lt;a href=&#34;placementstrategy.md&#34;&gt;PlacementStrategy&lt;/a&gt;</i>
    <a href="#serviceregistries" title="ServiceRegistries">ServiceRegistries</a>: <i>
      - &lt;a href=&#34;serviceregistries.md&#34;&gt;ServiceRegistries&lt;/a&gt;</i>
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

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaskDefinition

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapacityProviderStrategy

_Required_: No

_Type_: List of &lt;a href=&#34;capacityproviderstrategy.md&#34;&gt;CapacityProviderStrategy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentController

_Required_: No

_Type_: List of &lt;a href=&#34;deploymentcontroller.md&#34;&gt;DeploymentController&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancer

_Required_: No

_Type_: List of &lt;a href=&#34;loadbalancer.md&#34;&gt;LoadBalancer&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;networkconfiguration.md&#34;&gt;NetworkConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrderedPlacementStrategy

_Required_: No

_Type_: List of &lt;a href=&#34;orderedplacementstrategy.md&#34;&gt;OrderedPlacementStrategy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlacementConstraints

_Required_: No

_Type_: List of &lt;a href=&#34;placementconstraints.md&#34;&gt;PlacementConstraints&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlacementStrategy

_Required_: No

_Type_: List of &lt;a href=&#34;placementstrategy.md&#34;&gt;PlacementStrategy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRegistries

_Required_: No

_Type_: List of &lt;a href=&#34;serviceregistries.md&#34;&gt;ServiceRegistries&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

