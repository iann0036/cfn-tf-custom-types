# TF::AWS::LambdaEventSourceMapping DestinationConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#onfailure" title="OnFailure">OnFailure</a>" : <i>[ <a href="onfailuredefinition.md">OnFailureDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#onfailure" title="OnFailure">OnFailure</a>: <i>
      - <a href="onfailuredefinition.md">OnFailureDefinition</a></i>
</pre>

## Properties

#### OnFailure

_Required_: No

_Type_: List of <a href="onfailuredefinition.md">OnFailureDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
