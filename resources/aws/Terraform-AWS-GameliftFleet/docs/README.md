# Terraform::AWS::GameliftFleet

CloudFormation equivalent of aws_gamelift_fleet

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::GameliftFleet",
    "Properties" : {
        "<a href="#buildid" title="BuildId">BuildId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#ec2instancetype" title="Ec2InstanceType">Ec2InstanceType</a>" : <i>String</i>,
        "<a href="#fleettype" title="FleetType">FleetType</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#instancerolearn" title="InstanceRoleArn">InstanceRoleArn</a>" : <i>String</i>,
        "<a href="#metricgroups" title="MetricGroups">MetricGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#newgamesessionprotectionpolicy" title="NewGameSessionProtectionPolicy">NewGameSessionProtectionPolicy</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#ec2inboundpermission" title="Ec2InboundPermission">Ec2InboundPermission</a>" : <i>[ <a href="ec2inboundpermission.md">Ec2InboundPermission</a>, ... ]</i>,
        "<a href="#resourcecreationlimitpolicy" title="ResourceCreationLimitPolicy">ResourceCreationLimitPolicy</a>" : <i>[ <a href="resourcecreationlimitpolicy.md">ResourceCreationLimitPolicy</a>, ... ]</i>,
        "<a href="#runtimeconfiguration" title="RuntimeConfiguration">RuntimeConfiguration</a>" : <i>[ <a href="runtimeconfiguration.md">RuntimeConfiguration</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#serverprocess" title="ServerProcess">ServerProcess</a>" : <i>[ <a href="serverprocess.md">ServerProcess</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::GameliftFleet
Properties:
    <a href="#buildid" title="BuildId">BuildId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#ec2instancetype" title="Ec2InstanceType">Ec2InstanceType</a>: <i>String</i>
    <a href="#fleettype" title="FleetType">FleetType</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#instancerolearn" title="InstanceRoleArn">InstanceRoleArn</a>: <i>String</i>
    <a href="#metricgroups" title="MetricGroups">MetricGroups</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#newgamesessionprotectionpolicy" title="NewGameSessionProtectionPolicy">NewGameSessionProtectionPolicy</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#ec2inboundpermission" title="Ec2InboundPermission">Ec2InboundPermission</a>: <i>
      - <a href="ec2inboundpermission.md">Ec2InboundPermission</a></i>
    <a href="#resourcecreationlimitpolicy" title="ResourceCreationLimitPolicy">ResourceCreationLimitPolicy</a>: <i>
      - <a href="resourcecreationlimitpolicy.md">ResourceCreationLimitPolicy</a></i>
    <a href="#runtimeconfiguration" title="RuntimeConfiguration">RuntimeConfiguration</a>: <i>
      - <a href="runtimeconfiguration.md">RuntimeConfiguration</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#serverprocess" title="ServerProcess">ServerProcess</a>: <i>
      - <a href="serverprocess.md">ServerProcess</a></i>
</pre>

## Properties

#### BuildId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ec2InstanceType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FleetType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceRoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NewGameSessionProtectionPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ec2InboundPermission

_Required_: No

_Type_: List of <a href="ec2inboundpermission.md">Ec2InboundPermission</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceCreationLimitPolicy

_Required_: No

_Type_: List of <a href="resourcecreationlimitpolicy.md">ResourceCreationLimitPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuntimeConfiguration

_Required_: No

_Type_: List of <a href="runtimeconfiguration.md">RuntimeConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerProcess

_Required_: No

_Type_: List of <a href="serverprocess.md">ServerProcess</a>

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

#### LogPaths

Returns the <code>LogPaths</code> value.

#### OperatingSystem

Returns the <code>OperatingSystem</code> value.

