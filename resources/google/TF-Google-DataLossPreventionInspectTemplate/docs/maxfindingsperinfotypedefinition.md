# TF::Google::DataLossPreventionInspectTemplate MaxFindingsPerInfoTypeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maxfindings" title="MaxFindings">MaxFindings</a>" : <i>Double</i>,
    "<a href="#infotype" title="InfoType">InfoType</a>" : <i>[ <a href="infotypedefinition.md">InfoTypeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#maxfindings" title="MaxFindings">MaxFindings</a>: <i>Double</i>
<a href="#infotype" title="InfoType">InfoType</a>: <i>
      - <a href="infotypedefinition.md">InfoTypeDefinition</a></i>
</pre>

## Properties

#### MaxFindings

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InfoType

_Required_: No

_Type_: List of <a href="infotypedefinition.md">InfoTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

