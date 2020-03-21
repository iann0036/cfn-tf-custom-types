# Terraform::AWS::DlmLifecyclePolicy Schedule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#copytags" title="CopyTags">CopyTags</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#tagstoadd" title="TagsToAdd">TagsToAdd</a>" : <i>[ <a href="schedule-tagstoadd.md">TagsToAdd</a>, ... ]</i>,
    "<a href="#createrule" title="CreateRule">CreateRule</a>" : <i>[ <a href="schedule-createrule.md">CreateRule</a>, ... ]</i>,
    "<a href="#retainrule" title="RetainRule">RetainRule</a>" : <i>[ <a href="schedule-retainrule.md">RetainRule</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#copytags" title="CopyTags">CopyTags</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#tagstoadd" title="TagsToAdd">TagsToAdd</a>: <i>
      - <a href="schedule-tagstoadd.md">TagsToAdd</a></i>
<a href="#createrule" title="CreateRule">CreateRule</a>: <i>
      - <a href="schedule-createrule.md">CreateRule</a></i>
<a href="#retainrule" title="RetainRule">RetainRule</a>: <i>
      - <a href="schedule-retainrule.md">RetainRule</a></i>
</pre>

## Properties

#### CopyTags

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsToAdd

_Required_: No

_Type_: List of <a href="schedule-tagstoadd.md">TagsToAdd</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateRule

_Required_: No

_Type_: List of <a href="schedule-createrule.md">CreateRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetainRule

_Required_: No

_Type_: List of <a href="schedule-retainrule.md">RetainRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

