# TF::Volterra::Fleet UseChapDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#chaptargetusername" title="ChapTargetUsername">ChapTargetUsername</a>" : <i>String</i>,
    "<a href="#chapusername" title="ChapUsername">ChapUsername</a>" : <i>String</i>,
    "<a href="#chapinitiatorsecret" title="ChapInitiatorSecret">ChapInitiatorSecret</a>" : <i>[ <a href="chapinitiatorsecretdefinition.md">ChapInitiatorSecretDefinition</a>, ... ]</i>,
    "<a href="#chaptargetinitiatorsecret" title="ChapTargetInitiatorSecret">ChapTargetInitiatorSecret</a>" : <i>[ <a href="chaptargetinitiatorsecretdefinition.md">ChapTargetInitiatorSecretDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#chaptargetusername" title="ChapTargetUsername">ChapTargetUsername</a>: <i>String</i>
<a href="#chapusername" title="ChapUsername">ChapUsername</a>: <i>String</i>
<a href="#chapinitiatorsecret" title="ChapInitiatorSecret">ChapInitiatorSecret</a>: <i>
      - <a href="chapinitiatorsecretdefinition.md">ChapInitiatorSecretDefinition</a></i>
<a href="#chaptargetinitiatorsecret" title="ChapTargetInitiatorSecret">ChapTargetInitiatorSecret</a>: <i>
      - <a href="chaptargetinitiatorsecretdefinition.md">ChapTargetInitiatorSecretDefinition</a></i>
</pre>

## Properties

#### ChapTargetUsername

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChapUsername

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChapInitiatorSecret

_Required_: No

_Type_: List of <a href="chapinitiatorsecretdefinition.md">ChapInitiatorSecretDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChapTargetInitiatorSecret

_Required_: No

_Type_: List of <a href="chaptargetinitiatorsecretdefinition.md">ChapTargetInitiatorSecretDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

