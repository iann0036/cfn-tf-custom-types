# TF::AWS::GameliftFleet

Provides a Gamelift Fleet resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::GameliftFleet",
    "Properties" : {
        "<a href="#buildid" title="BuildId">BuildId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#ec2instancetype" title="Ec2InstanceType">Ec2InstanceType</a>" : <i>String</i>,
        "<a href="#fleettype" title="FleetType">FleetType</a>" : <i>String</i>,
        "<a href="#instancerolearn" title="InstanceRoleArn">InstanceRoleArn</a>" : <i>String</i>,
        "<a href="#metricgroups" title="MetricGroups">MetricGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#newgamesessionprotectionpolicy" title="NewGameSessionProtectionPolicy">NewGameSessionProtectionPolicy</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#ec2inboundpermission" title="Ec2InboundPermission">Ec2InboundPermission</a>" : <i>[ <a href="ec2inboundpermissiondefinition.md">Ec2InboundPermissionDefinition</a>, ... ]</i>,
        "<a href="#resourcecreationlimitpolicy" title="ResourceCreationLimitPolicy">ResourceCreationLimitPolicy</a>" : <i>[ <a href="resourcecreationlimitpolicydefinition.md">ResourceCreationLimitPolicyDefinition</a>, ... ]</i>,
        "<a href="#runtimeconfiguration" title="RuntimeConfiguration">RuntimeConfiguration</a>" : <i>[ <a href="runtimeconfigurationdefinition.md">RuntimeConfigurationDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::GameliftFleet
Properties:
    <a href="#buildid" title="BuildId">BuildId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#ec2instancetype" title="Ec2InstanceType">Ec2InstanceType</a>: <i>String</i>
    <a href="#fleettype" title="FleetType">FleetType</a>: <i>String</i>
    <a href="#instancerolearn" title="InstanceRoleArn">InstanceRoleArn</a>: <i>String</i>
    <a href="#metricgroups" title="MetricGroups">MetricGroups</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#newgamesessionprotectionpolicy" title="NewGameSessionProtectionPolicy">NewGameSessionProtectionPolicy</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#ec2inboundpermission" title="Ec2InboundPermission">Ec2InboundPermission</a>: <i>
      - <a href="ec2inboundpermissiondefinition.md">Ec2InboundPermissionDefinition</a></i>
    <a href="#resourcecreationlimitpolicy" title="ResourceCreationLimitPolicy">ResourceCreationLimitPolicy</a>: <i>
      - <a href="resourcecreationlimitpolicydefinition.md">ResourceCreationLimitPolicyDefinition</a></i>
    <a href="#runtimeconfiguration" title="RuntimeConfiguration">RuntimeConfiguration</a>: <i>
      - <a href="runtimeconfigurationdefinition.md">RuntimeConfigurationDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### BuildId

ID of the Gamelift Build to be deployed on the fleet.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Human-readable description of the fleet.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ec2InstanceType

Name of an EC2 instance type. e.g. `t2.micro`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FleetType

Type of fleet. This value must be `ON_DEMAND` or `SPOT`. Defaults to `ON_DEMAND`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceRoleArn

ARN of an IAM role that instances in the fleet can assume.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricGroups

List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the fleet.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NewGameSessionProtectionPolicy

Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.

_Required_: No

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

#### Ec2InboundPermission

_Required_: No

_Type_: List of <a href="ec2inboundpermissiondefinition.md">Ec2InboundPermissionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceCreationLimitPolicy

_Required_: No

_Type_: List of <a href="resourcecreationlimitpolicydefinition.md">ResourceCreationLimitPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuntimeConfiguration

_Required_: No

_Type_: List of <a href="runtimeconfigurationdefinition.md">RuntimeConfigurationDefinition</a>

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

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

#### LogPaths

Returns the <code>LogPaths</code> value.

#### OperatingSystem

Returns the <code>OperatingSystem</code> value.

