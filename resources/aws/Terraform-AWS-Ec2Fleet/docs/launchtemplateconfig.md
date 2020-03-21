# Terraform::AWS::Ec2Fleet LaunchTemplateConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#launchtemplatespecification" title="LaunchTemplateSpecification">LaunchTemplateSpecification</a>" : <i>[ <a href="launchtemplateconfig-launchtemplatespecification.md">LaunchTemplateSpecification</a>, ... ]</i>,
    "<a href="#override" title="Override">Override</a>" : <i>[ <a href="launchtemplateconfig-override.md">Override</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#launchtemplatespecification" title="LaunchTemplateSpecification">LaunchTemplateSpecification</a>: <i>
      - <a href="launchtemplateconfig-launchtemplatespecification.md">LaunchTemplateSpecification</a></i>
<a href="#override" title="Override">Override</a>: <i>
      - <a href="launchtemplateconfig-override.md">Override</a></i>
</pre>

## Properties

#### LaunchTemplateSpecification

_Required_: No

_Type_: List of <a href="launchtemplateconfig-launchtemplatespecification.md">LaunchTemplateSpecification</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Override

_Required_: No

_Type_: List of <a href="launchtemplateconfig-override.md">Override</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

