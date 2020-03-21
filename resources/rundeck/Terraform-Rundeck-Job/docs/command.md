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
    "<a href="#job" title="Job">Job</a>" : <i>[ &lt;a href=&#34;command-job.md&#34;&gt;Job&lt;/a&gt;, ... ]</i>,
    "<a href="#nodestepplugin" title="NodeStepPlugin">NodeStepPlugin</a>" : <i>[ &lt;a href=&#34;command-nodestepplugin.md&#34;&gt;NodeStepPlugin&lt;/a&gt;, ... ]</i>,
    "<a href="#stepplugin" title="StepPlugin">StepPlugin</a>" : <i>[ &lt;a href=&#34;command-stepplugin.md&#34;&gt;StepPlugin&lt;/a&gt;, ... ]</i>
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
      - &lt;a href=&#34;command-job.md&#34;&gt;Job&lt;/a&gt;</i>
<a href="#nodestepplugin" title="NodeStepPlugin">NodeStepPlugin</a>: <i>
      - &lt;a href=&#34;command-nodestepplugin.md&#34;&gt;NodeStepPlugin&lt;/a&gt;</i>
<a href="#stepplugin" title="StepPlugin">StepPlugin</a>: <i>
      - &lt;a href=&#34;command-stepplugin.md&#34;&gt;StepPlugin&lt;/a&gt;</i>
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
_Type_: List of &lt;a href=&#34;command-job.md&#34;&gt;Job&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeStepPlugin

_Required_: No
_Type_: List of &lt;a href=&#34;command-nodestepplugin.md&#34;&gt;NodeStepPlugin&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StepPlugin

_Required_: No
_Type_: List of &lt;a href=&#34;command-stepplugin.md&#34;&gt;StepPlugin&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

