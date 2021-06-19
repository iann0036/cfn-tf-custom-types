# TF::AWS::SpotFleetRequest LaunchTemplateConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#launchtemplatespecification" title="LaunchTemplateSpecification">LaunchTemplateSpecification</a>" : <i>[ <a href="launchtemplatespecificationdefinition.md">LaunchTemplateSpecificationDefinition</a>, ... ]</i>,
    "<a href="#overrides" title="Overrides">Overrides</a>" : <i>[ <a href="overridesdefinition.md">OverridesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#launchtemplatespecification" title="LaunchTemplateSpecification">LaunchTemplateSpecification</a>: <i>
      - <a href="launchtemplatespecificationdefinition.md">LaunchTemplateSpecificationDefinition</a></i>
<a href="#overrides" title="Overrides">Overrides</a>: <i>
      - <a href="overridesdefinition.md">OverridesDefinition</a></i>
</pre>

## Properties

#### LaunchTemplateSpecification

_Required_: No

_Type_: List of <a href="launchtemplatespecificationdefinition.md">LaunchTemplateSpecificationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Overrides

_Required_: No

_Type_: List of <a href="overridesdefinition.md">OverridesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

