# TF::AWS::SsmMaintenanceWindowTask TaskInvocationParametersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#automationparameters" title="AutomationParameters">AutomationParameters</a>" : <i>[ <a href="automationparametersdefinition.md">AutomationParametersDefinition</a>, ... ]</i>,
    "<a href="#lambdaparameters" title="LambdaParameters">LambdaParameters</a>" : <i>[ <a href="lambdaparametersdefinition.md">LambdaParametersDefinition</a>, ... ]</i>,
    "<a href="#runcommandparameters" title="RunCommandParameters">RunCommandParameters</a>" : <i>[ <a href="runcommandparametersdefinition.md">RunCommandParametersDefinition</a>, ... ]</i>,
    "<a href="#stepfunctionsparameters" title="StepFunctionsParameters">StepFunctionsParameters</a>" : <i>[ <a href="stepfunctionsparametersdefinition.md">StepFunctionsParametersDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#automationparameters" title="AutomationParameters">AutomationParameters</a>: <i>
      - <a href="automationparametersdefinition.md">AutomationParametersDefinition</a></i>
<a href="#lambdaparameters" title="LambdaParameters">LambdaParameters</a>: <i>
      - <a href="lambdaparametersdefinition.md">LambdaParametersDefinition</a></i>
<a href="#runcommandparameters" title="RunCommandParameters">RunCommandParameters</a>: <i>
      - <a href="runcommandparametersdefinition.md">RunCommandParametersDefinition</a></i>
<a href="#stepfunctionsparameters" title="StepFunctionsParameters">StepFunctionsParameters</a>: <i>
      - <a href="stepfunctionsparametersdefinition.md">StepFunctionsParametersDefinition</a></i>
</pre>

## Properties

#### AutomationParameters

_Required_: No

_Type_: List of <a href="automationparametersdefinition.md">AutomationParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaParameters

_Required_: No

_Type_: List of <a href="lambdaparametersdefinition.md">LambdaParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunCommandParameters

_Required_: No

_Type_: List of <a href="runcommandparametersdefinition.md">RunCommandParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StepFunctionsParameters

_Required_: No

_Type_: List of <a href="stepfunctionsparametersdefinition.md">StepFunctionsParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

