# Terraform::AWS::DlmLifecyclePolicy PolicyDetails Schedule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#copytags" title="CopyTags">CopyTags</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#tagstoadd" title="TagsToAdd">TagsToAdd</a>" : <i>[ &lt;a href=&#34;policydetails-schedule-tagstoadd.md&#34;&gt;TagsToAdd&lt;/a&gt;, ... ]</i>,
    "<a href="#createrule" title="CreateRule">CreateRule</a>" : <i>[ &lt;a href=&#34;policydetails-schedule-createrule.md&#34;&gt;CreateRule&lt;/a&gt;, ... ]</i>,
    "<a href="#retainrule" title="RetainRule">RetainRule</a>" : <i>[ &lt;a href=&#34;policydetails-schedule-retainrule.md&#34;&gt;RetainRule&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#copytags" title="CopyTags">CopyTags</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#tagstoadd" title="TagsToAdd">TagsToAdd</a>: <i>
      - &lt;a href=&#34;policydetails-schedule-tagstoadd.md&#34;&gt;TagsToAdd&lt;/a&gt;</i>
<a href="#createrule" title="CreateRule">CreateRule</a>: <i>
      - &lt;a href=&#34;policydetails-schedule-createrule.md&#34;&gt;CreateRule&lt;/a&gt;</i>
<a href="#retainrule" title="RetainRule">RetainRule</a>: <i>
      - &lt;a href=&#34;policydetails-schedule-retainrule.md&#34;&gt;RetainRule&lt;/a&gt;</i>
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
_Type_: List of &lt;a href=&#34;policydetails-schedule-tagstoadd.md&#34;&gt;TagsToAdd&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateRule

_Required_: No
_Type_: List of &lt;a href=&#34;policydetails-schedule-createrule.md&#34;&gt;CreateRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetainRule

_Required_: No
_Type_: List of &lt;a href=&#34;policydetails-schedule-retainrule.md&#34;&gt;RetainRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

