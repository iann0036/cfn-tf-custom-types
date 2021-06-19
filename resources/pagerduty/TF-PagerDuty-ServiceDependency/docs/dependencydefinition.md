# TF::PagerDuty::ServiceDependency DependencyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#dependentservice" title="DependentService">DependentService</a>" : <i>[ <a href="dependentservicedefinition.md">DependentServiceDefinition</a>, ... ]</i>,
    "<a href="#supportingservice" title="SupportingService">SupportingService</a>" : <i>[ <a href="supportingservicedefinition.md">SupportingServiceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#dependentservice" title="DependentService">DependentService</a>: <i>
      - <a href="dependentservicedefinition.md">DependentServiceDefinition</a></i>
<a href="#supportingservice" title="SupportingService">SupportingService</a>: <i>
      - <a href="supportingservicedefinition.md">SupportingServiceDefinition</a></i>
</pre>

## Properties

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DependentService

_Required_: No

_Type_: List of <a href="dependentservicedefinition.md">DependentServiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupportingService

_Required_: No

_Type_: List of <a href="supportingservicedefinition.md">SupportingServiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

