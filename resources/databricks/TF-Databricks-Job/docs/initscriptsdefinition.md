# TF::Databricks::Job InitScriptsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dbfs" title="Dbfs">Dbfs</a>" : <i>[ <a href="dbfsdefinition.md">DbfsDefinition</a>, ... ]</i>,
    "<a href="#file" title="File">File</a>" : <i>[ <a href="filedefinition.md">FileDefinition</a>, ... ]</i>,
    "<a href="#s3" title="S3">S3</a>" : <i>[ <a href="s3definition.md">S3Definition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dbfs" title="Dbfs">Dbfs</a>: <i>
      - <a href="dbfsdefinition.md">DbfsDefinition</a></i>
<a href="#file" title="File">File</a>: <i>
      - <a href="filedefinition.md">FileDefinition</a></i>
<a href="#s3" title="S3">S3</a>: <i>
      - <a href="s3definition.md">S3Definition</a></i>
</pre>

## Properties

#### Dbfs

_Required_: No

_Type_: List of <a href="dbfsdefinition.md">DbfsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### File

_Required_: No

_Type_: List of <a href="filedefinition.md">FileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3

_Required_: No

_Type_: List of <a href="s3definition.md">S3Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

