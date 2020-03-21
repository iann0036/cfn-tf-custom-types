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

_Required_: No

_Type_: List of <a href="inputtransformer-inputpaths.md">InputPaths</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputTemplate

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

