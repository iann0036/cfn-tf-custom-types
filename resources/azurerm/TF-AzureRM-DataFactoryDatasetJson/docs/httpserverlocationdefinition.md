# TF::AzureRM::DataFactoryDatasetJson HttpServerLocationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#filename" title="Filename">Filename</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#relativeurl" title="RelativeUrl">RelativeUrl</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#filename" title="Filename">Filename</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#relativeurl" title="RelativeUrl">RelativeUrl</a>: <i>String</i>
</pre>

## Properties

#### Filename

The filename of the file on the web server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

The folder path to the file on the web server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelativeUrl

The base URL to the web server hosting the file.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

