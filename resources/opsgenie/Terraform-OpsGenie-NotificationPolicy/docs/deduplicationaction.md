# Terraform::OpsGenie::NotificationPolicy DeDuplicationAction

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#count" title="Count">Count</a>" : <i>Double</i>,
    "<a href="#deduplicationactiontype" title="DeDuplicationActionType">DeDuplicationActionType</a>" : <i>String</i>,
    "<a href="#duration" title="Duration">Duration</a>" : <i>[ &lt;a href=&#34;deduplicationaction-duration.md&#34;&gt;Duration&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#count" title="Count">Count</a>: <i>Double</i>
<a href="#deduplicationactiontype" title="DeDuplicationActionType">DeDuplicationActionType</a>: <i>String</i>
<a href="#duration" title="Duration">Duration</a>: <i>
      - &lt;a href=&#34;deduplicationaction-duration.md&#34;&gt;Duration&lt;/a&gt;</i>
</pre>

## Properties

#### Count

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeDuplicationActionType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Duration

_Required_: No
_Type_: List of &lt;a href=&#34;deduplicationaction-duration.md&#34;&gt;Duration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

