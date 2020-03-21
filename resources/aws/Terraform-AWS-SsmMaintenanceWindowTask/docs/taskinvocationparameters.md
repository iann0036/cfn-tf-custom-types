# Terraform::AWS::SsmMaintenanceWindowTask TaskInvocationParameters

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#automationparameters" title="AutomationParameters">AutomationParameters</a>" : <i>[ <a href="taskinvocationparameters-automationparameters.md">AutomationParameters</a>, ... ]</i>,
    "<a href="#lambdaparameters" title="LambdaParameters">LambdaParameters</a>" : <i>[ <a href="taskinvocationparameters-lambdaparameters.md">LambdaParameters</a>, ... ]</i>,
    "<a href="#runcommandparameters" title="RunCommandParameters">RunCommandParameters</a>" : <i>[ <a href="taskinvocationparameters-runcommandparameters.md">RunCommandParameters</a>, ... ]</i>,
    "<a href="#stepfunctionsparameters" title="StepFunctionsParameters">StepFunctionsParameters</a>" : <i>[ <a href="taskinvocationparameters-stepfunctionsparameters.md">StepFunctionsParameters</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#automationparameters" title="AutomationParameters">AutomationParameters</a>: <i>
      - <a href="taskinvocationparameters-automationparameters.md">AutomationParameters</a></i>
<a href="#lambdaparameters" title="LambdaParameters">LambdaParameters</a>: <i>
      - <a href="taskinvocationparameters-lambdaparameters.md">LambdaParameters</a></i>
<a href="#runcommandparameters" title="RunCommandParameters">RunCommandParameters</a>: <i>
      - <a href="taskinvocationparameters-runcommandparameters.md">RunCommandParameters</a></i>
<a href="#stepfunctionsparameters" title="StepFunctionsParameters">StepFunctionsParameters</a>: <i>
      - <a href="taskinvocationparameters-stepfunctionsparameters.md">StepFunctionsParameters</a></i>
</pre>

## Properties

#### AutomationParameters

_Required_: No

_Type_: List of <a href="taskinvocationparameters-automationparameters.md">AutomationParameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaParameters

_Required_: No

_Type_: List of <a href="taskinvocationparameters-lambdaparameters.md">LambdaParameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunCommandParameters

_Required_: No

_Type_: List of <a href="taskinvocationparameters-runcommandparameters.md">RunCommandParameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StepFunctionsParameters

_Required_: No

_Type_: List of <a href="taskinvocationparameters-stepfunctionsparameters.md">StepFunctionsParameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

