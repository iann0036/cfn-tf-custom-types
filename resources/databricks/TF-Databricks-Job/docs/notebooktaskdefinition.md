# TF::Databricks::Job NotebookTaskDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#baseparameters" title="BaseParameters">BaseParameters</a>" : <i>[ <a href="baseparametersdefinition.md">BaseParametersDefinition</a>, ... ]</i>,
    "<a href="#notebookpath" title="NotebookPath">NotebookPath</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#baseparameters" title="BaseParameters">BaseParameters</a>: <i>
      - <a href="baseparametersdefinition.md">BaseParametersDefinition</a></i>
<a href="#notebookpath" title="NotebookPath">NotebookPath</a>: <i>String</i>
</pre>

## Properties

#### BaseParameters

_Required_: No

_Type_: List of <a href="baseparametersdefinition.md">BaseParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotebookPath

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

