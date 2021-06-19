# TF::AVI::Applicationprofile DosRlProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dosprofile" title="DosProfile">DosProfile</a>" : <i>[ <a href="dosprofiledefinition.md">DosProfileDefinition</a>, ... ]</i>,
    "<a href="#rlprofile" title="RlProfile">RlProfile</a>" : <i>[ <a href="rlprofiledefinition.md">RlProfileDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dosprofile" title="DosProfile">DosProfile</a>: <i>
      - <a href="dosprofiledefinition.md">DosProfileDefinition</a></i>
<a href="#rlprofile" title="RlProfile">RlProfile</a>: <i>
      - <a href="rlprofiledefinition.md">RlProfileDefinition</a></i>
</pre>

## Properties

#### DosProfile

_Required_: No

_Type_: List of <a href="dosprofiledefinition.md">DosProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RlProfile

_Required_: No

_Type_: List of <a href="rlprofiledefinition.md">RlProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

