# TF::Databricks::Pipeline LibraryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#jar" title="Jar">Jar</a>" : <i>String</i>,
    "<a href="#whl" title="Whl">Whl</a>" : <i>String</i>,
    "<a href="#maven" title="Maven">Maven</a>" : <i>[ <a href="mavendefinition.md">MavenDefinition</a>, ... ]</i>,
    "<a href="#notebook" title="Notebook">Notebook</a>" : <i>[ <a href="notebookdefinition.md">NotebookDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#jar" title="Jar">Jar</a>: <i>String</i>
<a href="#whl" title="Whl">Whl</a>: <i>String</i>
<a href="#maven" title="Maven">Maven</a>: <i>
      - <a href="mavendefinition.md">MavenDefinition</a></i>
<a href="#notebook" title="Notebook">Notebook</a>: <i>
      - <a href="notebookdefinition.md">NotebookDefinition</a></i>
</pre>

## Properties

#### Jar

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Whl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Maven

_Required_: No

_Type_: List of <a href="mavendefinition.md">MavenDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notebook

_Required_: No

_Type_: List of <a href="notebookdefinition.md">NotebookDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

