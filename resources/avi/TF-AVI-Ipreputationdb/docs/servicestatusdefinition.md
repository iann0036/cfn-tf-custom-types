# TF::AVI::Ipreputationdb ServiceStatusDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#error" title="Error">Error</a>" : <i>String</i>,
    "<a href="#lastsuccessfulupdatecheck" title="LastSuccessfulUpdateCheck">LastSuccessfulUpdateCheck</a>" : <i>[ <a href="lastsuccessfulupdatecheckdefinition.md">LastSuccessfulUpdateCheckDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#error" title="Error">Error</a>: <i>String</i>
<a href="#lastsuccessfulupdatecheck" title="LastSuccessfulUpdateCheck">LastSuccessfulUpdateCheck</a>: <i>
      - <a href="lastsuccessfulupdatecheckdefinition.md">LastSuccessfulUpdateCheckDefinition</a></i>
</pre>

## Properties

#### Error

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastSuccessfulUpdateCheck

_Required_: No

_Type_: List of <a href="lastsuccessfulupdatecheckdefinition.md">LastSuccessfulUpdateCheckDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

