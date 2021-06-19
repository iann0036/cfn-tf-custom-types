# TF::AWS::ApprunnerService CodeConfigurationValuesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#buildcommand" title="BuildCommand">BuildCommand</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>String</i>,
    "<a href="#runtime" title="Runtime">Runtime</a>" : <i>String</i>,
    "<a href="#runtimeenvironmentvariables" title="RuntimeEnvironmentVariables">RuntimeEnvironmentVariables</a>" : <i>[ <a href="runtimeenvironmentvariablesdefinition2.md">RuntimeEnvironmentVariablesDefinition2</a>, ... ]</i>,
    "<a href="#startcommand" title="StartCommand">StartCommand</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#buildcommand" title="BuildCommand">BuildCommand</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>String</i>
<a href="#runtime" title="Runtime">Runtime</a>: <i>String</i>
<a href="#runtimeenvironmentvariables" title="RuntimeEnvironmentVariables">RuntimeEnvironmentVariables</a>: <i>
      - <a href="runtimeenvironmentvariablesdefinition2.md">RuntimeEnvironmentVariablesDefinition2</a></i>
<a href="#startcommand" title="StartCommand">StartCommand</a>: <i>String</i>
</pre>

## Properties

#### BuildCommand

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Runtime

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuntimeEnvironmentVariables

_Required_: No

_Type_: List of <a href="runtimeenvironmentvariablesdefinition2.md">RuntimeEnvironmentVariablesDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartCommand

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

