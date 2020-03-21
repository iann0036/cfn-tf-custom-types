# Terraform::AWS::DlmLifecyclePolicy PolicyDetails

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#resourcetypes" title="ResourceTypes">ResourceTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#targettags" title="TargetTags">TargetTags</a>" : <i>[ &lt;a href=&#34;policydetails-targettags.md&#34;&gt;TargetTags&lt;/a&gt;, ... ]</i>,
    "<a href="#schedule" title="Schedule">Schedule</a>" : <i>[ &lt;a href=&#34;policydetails-schedule.md&#34;&gt;Schedule&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#resourcetypes" title="ResourceTypes">ResourceTypes</a>: <i>
      - String</i>
<a href="#targettags" title="TargetTags">TargetTags</a>: <i>
      - &lt;a href=&#34;policydetails-targettags.md&#34;&gt;TargetTags&lt;/a&gt;</i>
<a href="#schedule" title="Schedule">Schedule</a>: <i>
      - &lt;a href=&#34;policydetails-schedule.md&#34;&gt;Schedule&lt;/a&gt;</i>
</pre>

## Properties

#### ResourceTypes

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetTags

_Required_: Yes
_Type_: List of &lt;a href=&#34;policydetails-targettags.md&#34;&gt;TargetTags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No
_Type_: List of &lt;a href=&#34;policydetails-schedule.md&#34;&gt;Schedule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

