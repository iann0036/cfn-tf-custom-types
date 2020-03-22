# Terraform::AWS::Ec2Fleet

CloudFormation equivalent of aws_ec2_fleet

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::Ec2Fleet",
    "Properties" : {
        "<a href="#excesscapacityterminationpolicy" title="ExcessCapacityTerminationPolicy">ExcessCapacityTerminationPolicy</a>" : <i>String</i>,
        "<a href="#replaceunhealthyinstances" title="ReplaceUnhealthyInstances">ReplaceUnhealthyInstances</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#terminateinstances" title="TerminateInstances">TerminateInstances</a>" : <i>Boolean</i>,
        "<a href="#terminateinstanceswithexpiration" title="TerminateInstancesWithExpiration">TerminateInstancesWithExpiration</a>" : <i>Boolean</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#launchtemplateconfig" title="LaunchTemplateConfig">LaunchTemplateConfig</a>" : <i>[ <a href="launchtemplateconfig.md">LaunchTemplateConfig</a>, ... ]</i>,
        "<a href="#ondemandoptions" title="OnDemandOptions">OnDemandOptions</a>" : <i>[ <a href="ondemandoptions.md">OnDemandOptions</a>, ... ]</i>,
        "<a href="#spotoptions" title="SpotOptions">SpotOptions</a>" : <i>[ <a href="spotoptions.md">SpotOptions</a>, ... ]</i>,
        "<a href="#targetcapacityspecification" title="TargetCapacitySpecification">TargetCapacitySpecification</a>" : <i>[ <a href="targetcapacityspecification.md">TargetCapacitySpecification</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#launchtemplatespecification" title="LaunchTemplateSpecification">LaunchTemplateSpecification</a>" : <i>[ <a href="launchtemplatespecification.md">LaunchTemplateSpecification</a>, ... ]</i>,
        "<a href="#override" title="Override">Override</a>" : <i>[ <a href="override.md">Override</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::Ec2Fleet
Properties:
    <a href="#excesscapacityterminationpolicy" title="ExcessCapacityTerminationPolicy">ExcessCapacityTerminationPolicy</a>: <i>String</i>
    <a href="#replaceunhealthyinstances" title="ReplaceUnhealthyInstances">ReplaceUnhealthyInstances</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#terminateinstances" title="TerminateInstances">TerminateInstances</a>: <i>Boolean</i>
    <a href="#terminateinstanceswithexpiration" title="TerminateInstancesWithExpiration">TerminateInstancesWithExpiration</a>: <i>Boolean</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#launchtemplateconfig" title="LaunchTemplateConfig">LaunchTemplateConfig</a>: <i>
      - <a href="launchtemplateconfig.md">LaunchTemplateConfig</a></i>
    <a href="#ondemandoptions" title="OnDemandOptions">OnDemandOptions</a>: <i>
      - <a href="ondemandoptions.md">OnDemandOptions</a></i>
    <a href="#spotoptions" title="SpotOptions">SpotOptions</a>: <i>
      - <a href="spotoptions.md">SpotOptions</a></i>
    <a href="#targetcapacityspecification" title="TargetCapacitySpecification">TargetCapacitySpecification</a>: <i>
      - <a href="targetcapacityspecification.md">TargetCapacitySpecification</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#launchtemplatespecification" title="LaunchTemplateSpecification">LaunchTemplateSpecification</a>: <i>
      - <a href="launchtemplatespecification.md">LaunchTemplateSpecification</a></i>
    <a href="#override" title="Override">Override</a>: <i>
      - <a href="override.md">Override</a></i>
</pre>

## Properties

#### ExcessCapacityTerminationPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplaceUnhealthyInstances

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminateInstances

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminateInstancesWithExpiration

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchTemplateConfig

_Required_: No

_Type_: List of <a href="launchtemplateconfig.md">LaunchTemplateConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnDemandOptions

_Required_: No

_Type_: List of <a href="ondemandoptions.md">OnDemandOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotOptions

_Required_: No

_Type_: List of <a href="spotoptions.md">SpotOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetCapacitySpecification

_Required_: No

_Type_: List of <a href="targetcapacityspecification.md">TargetCapacitySpecification</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchTemplateSpecification

_Required_: No

_Type_: List of <a href="launchtemplatespecification.md">LaunchTemplateSpecification</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Override

_Required_: No

_Type_: List of <a href="override.md">Override</a>

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

