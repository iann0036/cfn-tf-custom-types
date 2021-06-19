# TF::AWS::AppmeshVirtualGateway CertificateDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#file" title="File">File</a>" : <i>[ <a href="filedefinition.md">FileDefinition</a>, ... ]</i>,
    "<a href="#sds" title="Sds">Sds</a>" : <i>[ <a href="sdsdefinition.md">SdsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#file" title="File">File</a>: <i>
      - <a href="filedefinition.md">FileDefinition</a></i>
<a href="#sds" title="Sds">Sds</a>: <i>
      - <a href="sdsdefinition.md">SdsDefinition</a></i>
</pre>

## Properties

#### File

_Required_: No

_Type_: List of <a href="filedefinition.md">FileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sds

_Required_: No

_Type_: List of <a href="sdsdefinition.md">SdsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

