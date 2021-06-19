# TF::AWS::LexIntent FollowUpPromptDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#prompt" title="Prompt">Prompt</a>" : <i>[ <a href="promptdefinition.md">PromptDefinition</a>, ... ]</i>,
    "<a href="#rejectionstatement" title="RejectionStatement">RejectionStatement</a>" : <i>[ <a href="rejectionstatementdefinition.md">RejectionStatementDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#prompt" title="Prompt">Prompt</a>: <i>
      - <a href="promptdefinition.md">PromptDefinition</a></i>
<a href="#rejectionstatement" title="RejectionStatement">RejectionStatement</a>: <i>
      - <a href="rejectionstatementdefinition.md">RejectionStatementDefinition</a></i>
</pre>

## Properties

#### Prompt

_Required_: No

_Type_: List of <a href="promptdefinition.md">PromptDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RejectionStatement

_Required_: No

_Type_: List of <a href="rejectionstatementdefinition.md">RejectionStatementDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

