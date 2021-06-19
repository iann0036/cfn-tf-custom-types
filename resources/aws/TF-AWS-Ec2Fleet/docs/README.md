# TF::AWS::Ec2Fleet

Provides a resource to manage EC2 Fleets.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Ec2Fleet",
    "Properties" : {
        "<a href="#excesscapacityterminationpolicy" title="ExcessCapacityTerminationPolicy">ExcessCapacityTerminationPolicy</a>" : <i>String</i>,
        "<a href="#replaceunhealthyinstances" title="ReplaceUnhealthyInstances">ReplaceUnhealthyInstances</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#terminateinstances" title="TerminateInstances">TerminateInstances</a>" : <i>Boolean</i>,
        "<a href="#terminateinstanceswithexpiration" title="TerminateInstancesWithExpiration">TerminateInstancesWithExpiration</a>" : <i>Boolean</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#launchtemplateconfig" title="LaunchTemplateConfig">LaunchTemplateConfig</a>" : <i>[ <a href="launchtemplateconfigdefinition.md">LaunchTemplateConfigDefinition</a>, ... ]</i>,
        "<a href="#ondemandoptions" title="OnDemandOptions">OnDemandOptions</a>" : <i>[ <a href="ondemandoptionsdefinition.md">OnDemandOptionsDefinition</a>, ... ]</i>,
        "<a href="#spotoptions" title="SpotOptions">SpotOptions</a>" : <i>[ <a href="spotoptionsdefinition.md">SpotOptionsDefinition</a>, ... ]</i>,
        "<a href="#targetcapacityspecification" title="TargetCapacitySpecification">TargetCapacitySpecification</a>" : <i>[ <a href="targetcapacityspecificationdefinition.md">TargetCapacitySpecificationDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Ec2Fleet
Properties:
    <a href="#excesscapacityterminationpolicy" title="ExcessCapacityTerminationPolicy">ExcessCapacityTerminationPolicy</a>: <i>String</i>
    <a href="#replaceunhealthyinstances" title="ReplaceUnhealthyInstances">ReplaceUnhealthyInstances</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#terminateinstances" title="TerminateInstances">TerminateInstances</a>: <i>Boolean</i>
    <a href="#terminateinstanceswithexpiration" title="TerminateInstancesWithExpiration">TerminateInstancesWithExpiration</a>: <i>Boolean</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#launchtemplateconfig" title="LaunchTemplateConfig">LaunchTemplateConfig</a>: <i>
      - <a href="launchtemplateconfigdefinition.md">LaunchTemplateConfigDefinition</a></i>
    <a href="#ondemandoptions" title="OnDemandOptions">OnDemandOptions</a>: <i>
      - <a href="ondemandoptionsdefinition.md">OnDemandOptionsDefinition</a></i>
    <a href="#spotoptions" title="SpotOptions">SpotOptions</a>: <i>
      - <a href="spotoptionsdefinition.md">SpotOptionsDefinition</a></i>
    <a href="#targetcapacityspecification" title="TargetCapacitySpecification">TargetCapacitySpecification</a>: <i>
      - <a href="targetcapacityspecificationdefinition.md">TargetCapacitySpecificationDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ExcessCapacityTerminationPolicy

Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. Defaults to `termination`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplaceUnhealthyInstances

Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Map of Fleet tags. To tag instances at launch, specify the tags in the Launch Template. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminateInstances

Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminateInstancesWithExpiration

Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchTemplateConfig

_Required_: No

_Type_: List of <a href="launchtemplateconfigdefinition.md">LaunchTemplateConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnDemandOptions

_Required_: No

_Type_: List of <a href="ondemandoptionsdefinition.md">OnDemandOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotOptions

_Required_: No

_Type_: List of <a href="spotoptionsdefinition.md">SpotOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetCapacitySpecification

_Required_: No

_Type_: List of <a href="targetcapacityspecificationdefinition.md">TargetCapacitySpecificationDefinition</a>

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

