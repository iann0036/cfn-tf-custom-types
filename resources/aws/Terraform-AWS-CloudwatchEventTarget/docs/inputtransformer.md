# Terraform::AWS::CloudwatchEventTarget InputTransformer

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#inputpaths" title="InputPaths">InputPaths</a>" : <i>[ <a href="inputtransformer-inputpaths.md">InputPaths</a>, ... ]</i>,
    "<a href="#inputtemplate" title="InputTemplate">InputTemplate</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#inputpaths" title="InputPaths">InputPaths</a>: <i>
      - <a href="inputtransformer-inputpaths.md">InputPaths</a></i>
<a href="#inputtemplate" title="InputTemplate">InputTemplate</a>: <i>String</i>
</pre>

## Properties

#### InputPaths

Key value pairs specified in the form of JSONPath (for example, time = $.time).

_Required_: No

_Type_: List of <a href="inputtransformer-inputpaths.md">InputPaths</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputTemplate

Structure containing the template body.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

