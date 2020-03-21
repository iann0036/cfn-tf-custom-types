# Terraform::Rundeck::Job Command

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#inlinescript" title="InlineScript">InlineScript</a>" : <i>String</i>,
    "<a href="#scriptfile" title="ScriptFile">ScriptFile</a>" : <i>String</i>,
    "<a href="#scriptfileargs" title="ScriptFileArgs">ScriptFileArgs</a>" : <i>String</i>,
    "<a href="#shellcommand" title="ShellCommand">ShellCommand</a>" : <i>String</i>,
    "<a href="#job" title="Job">Job</a>" : <i>[ <a href="command-job.md">Job</a>, ... ]</i>,
    "<a href="#nodestepplugin" title="NodeStepPlugin">NodeStepPlugin</a>" : <i>[ <a href="command-nodestepplugin.md">NodeStepPlugin</a>, ... ]</i>,
    "<a href="#stepplugin" title="StepPlugin">StepPlugin</a>" : <i>[ <a href="command-stepplugin.md">StepPlugin</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#inlinescript" title="InlineScript">InlineScript</a>: <i>String</i>
<a href="#scriptfile" title="ScriptFile">ScriptFile</a>: <i>String</i>
<a href="#scriptfileargs" title="ScriptFileArgs">ScriptFileArgs</a>: <i>String</i>
<a href="#shellcommand" title="ShellCommand">ShellCommand</a>: <i>String</i>
<a href="#job" title="Job">Job</a>: <i>
      - <a href="command-job.md">Job</a></i>
<a href="#nodestepplugin" title="NodeStepPlugin">NodeStepPlugin</a>: <i>
      - <a href="command-nodestepplugin.md">NodeStepPlugin</a></i>
<a href="#stepplugin" title="StepPlugin">StepPlugin</a>: <i>
      - <a href="command-stepplugin.md">StepPlugin</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InlineScript

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScriptFile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScriptFileArgs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShellCommand

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Job

_Required_: No

_Type_: List of <a href="command-job.md">Job</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeStepPlugin

_Required_: No

_Type_: List of <a href="command-nodestepplugin.md">NodeStepPlugin</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StepPlugin

_Required_: No

_Type_: List of <a href="command-stepplugin.md">StepPlugin</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

