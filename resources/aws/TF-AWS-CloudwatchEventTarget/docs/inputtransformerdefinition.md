# TF::AWS::CloudwatchEventTarget InputTransformerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#inputpaths" title="InputPaths">InputPaths</a>" : <i>[ <a href="inputpathsdefinition.md">InputPathsDefinition</a>, ... ]</i>,
    "<a href="#inputtemplate" title="InputTemplate">InputTemplate</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#inputpaths" title="InputPaths">InputPaths</a>: <i>
      - <a href="inputpathsdefinition.md">InputPathsDefinition</a></i>
<a href="#inputtemplate" title="InputTemplate">InputTemplate</a>: <i>String</i>
</pre>

## Properties

#### InputPaths

Key value pairs specified in the form of JSONPath (for example, time = $.time)
* You can have as many as 100 key-value pairs.
* You must use JSON dot notation, not bracket notation.
* The keys can't start with "AWS".

_Required_: No

_Type_: List of <a href="inputpathsdefinition.md">InputPathsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputTemplate

Template to customize data sent to the target. Must be valid JSON. To send a string value, the string value must include double quotes. Values must be escaped for both JSON and Terraform, e.g. `"\"Your string goes here.\\nA new line.\""`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

