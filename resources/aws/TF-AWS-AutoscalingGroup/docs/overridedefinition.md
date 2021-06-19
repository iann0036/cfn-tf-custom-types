# TF::AWS::AutoscalingGroup OverrideDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
    "<a href="#weightedcapacity" title="WeightedCapacity">WeightedCapacity</a>" : <i>String</i>,
    "<a href="#launchtemplatespecification" title="LaunchTemplateSpecification">LaunchTemplateSpecification</a>" : <i>[ <a href="launchtemplatespecificationdefinition.md">LaunchTemplateSpecificationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
<a href="#weightedcapacity" title="WeightedCapacity">WeightedCapacity</a>: <i>String</i>
<a href="#launchtemplatespecification" title="LaunchTemplateSpecification">LaunchTemplateSpecification</a>: <i>
      - <a href="launchtemplatespecificationdefinition.md">LaunchTemplateSpecificationDefinition</a></i>
</pre>

## Properties

#### InstanceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeightedCapacity

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchTemplateSpecification

_Required_: No

_Type_: List of <a href="launchtemplatespecificationdefinition.md">LaunchTemplateSpecificationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

