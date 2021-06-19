# TF::GoogleBeta::GoogleDataprocWorkflowTemplate ValidationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#regex" title="Regex">Regex</a>" : <i>[ <a href="regexdefinition.md">RegexDefinition</a>, ... ]</i>,
    "<a href="#values" title="Values">Values</a>" : <i>[ <a href="valuesdefinition.md">ValuesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#regex" title="Regex">Regex</a>: <i>
      - <a href="regexdefinition.md">RegexDefinition</a></i>
<a href="#values" title="Values">Values</a>: <i>
      - <a href="valuesdefinition.md">ValuesDefinition</a></i>
</pre>

## Properties

#### Regex

_Required_: No

_Type_: List of <a href="regexdefinition.md">RegexDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Values

_Required_: No

_Type_: List of <a href="valuesdefinition.md">ValuesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

