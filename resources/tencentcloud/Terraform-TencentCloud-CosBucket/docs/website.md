# Terraform::TencentCloud::CosBucket Website

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#errordocument" title="ErrorDocument">ErrorDocument</a>" : <i>String</i>,
    "<a href="#indexdocument" title="IndexDocument">IndexDocument</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#errordocument" title="ErrorDocument">ErrorDocument</a>: <i>String</i>
<a href="#indexdocument" title="IndexDocument">IndexDocument</a>: <i>String</i>
</pre>

## Properties

#### ErrorDocument

An absolute path to the document to return in case of a 4XX error.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndexDocument

COS returns this index document when requests are made to the root domain or any of the subfolders.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

