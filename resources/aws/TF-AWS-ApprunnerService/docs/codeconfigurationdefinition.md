# TF::AWS::ApprunnerService CodeConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#configurationsource" title="ConfigurationSource">ConfigurationSource</a>" : <i>String</i>,
    "<a href="#codeconfigurationvalues" title="CodeConfigurationValues">CodeConfigurationValues</a>" : <i>[ <a href="codeconfigurationvaluesdefinition.md">CodeConfigurationValuesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#configurationsource" title="ConfigurationSource">ConfigurationSource</a>: <i>String</i>
<a href="#codeconfigurationvalues" title="CodeConfigurationValues">CodeConfigurationValues</a>: <i>
      - <a href="codeconfigurationvaluesdefinition.md">CodeConfigurationValuesDefinition</a></i>
</pre>

## Properties

#### ConfigurationSource

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CodeConfigurationValues

_Required_: No

_Type_: List of <a href="codeconfigurationvaluesdefinition.md">CodeConfigurationValuesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

