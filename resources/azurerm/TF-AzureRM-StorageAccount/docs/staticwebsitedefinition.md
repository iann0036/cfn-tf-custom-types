# TF::AzureRM::StorageAccount StaticWebsiteDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#error404document" title="Error404Document">Error404Document</a>" : <i>String</i>,
    "<a href="#indexdocument" title="IndexDocument">IndexDocument</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#error404document" title="Error404Document">Error404Document</a>: <i>String</i>
<a href="#indexdocument" title="IndexDocument">IndexDocument</a>: <i>String</i>
</pre>

## Properties

#### Error404Document

The absolute path to a custom webpage that should be used when a request is made which does not correspond to an existing file.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndexDocument

The webpage that Azure Storage serves for requests to the root of a website or any subfolder. For example, index.html. The value is case-sensitive.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

