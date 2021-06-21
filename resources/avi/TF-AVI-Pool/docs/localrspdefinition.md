# TF::AVI::Pool LocalRspDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#statuscode" title="StatusCode">StatusCode</a>" : <i>String</i>,
    "<a href="#file" title="File">File</a>" : <i>[ <a href="filedefinition.md">FileDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#statuscode" title="StatusCode">StatusCode</a>: <i>String</i>
<a href="#file" title="File">File</a>: <i>
      - <a href="filedefinition.md">FileDefinition</a></i>
</pre>

## Properties

#### StatusCode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### File

_Required_: No

_Type_: List of <a href="filedefinition.md">FileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
