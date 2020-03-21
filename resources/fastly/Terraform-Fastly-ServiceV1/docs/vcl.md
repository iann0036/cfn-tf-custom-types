# Terraform::Fastly::ServiceV1 Vcl

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#content" title="Content">Content</a>" : <i>String</i>,
    "<a href="#main" title="Main">Main</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#content" title="Content">Content</a>: <i>String</i>
<a href="#main" title="Main">Main</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### Content

The custom VCL code to upload.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Main

If `true`, use this block as the main configuration. If
`false`, use this block as an includable library. Only a single VCL block can be
marked as the main block. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name for this configuration block.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

