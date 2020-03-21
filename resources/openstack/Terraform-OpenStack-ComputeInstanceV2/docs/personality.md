# Terraform::OpenStack::ComputeInstanceV2 Personality

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#content" title="Content">Content</a>" : <i>String</i>,
    "<a href="#file" title="File">File</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#content" title="Content">Content</a>: <i>String</i>
<a href="#file" title="File">File</a>: <i>String</i>
</pre>

## Properties

#### Content

The contents of the file. Limited to 255 bytes.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### File

The absolute path of the destination file.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

