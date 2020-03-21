# Terraform::OCI::DnsSteeringPolicy Rules

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultcount" title="DefaultCount">DefaultCount</a>" : <i>Double</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#ruletype" title="RuleType">RuleType</a>" : <i>String</i>,
    "<a href="#cases" title="Cases">Cases</a>" : <i>[ &lt;a href=&#34;rules-cases.md&#34;&gt;Cases&lt;/a&gt;, ... ]</i>,
    "<a href="#defaultanswerdata" title="DefaultAnswerData">DefaultAnswerData</a>" : <i>[ &lt;a href=&#34;rules-defaultanswerdata.md&#34;&gt;DefaultAnswerData&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultcount" title="DefaultCount">DefaultCount</a>: <i>Double</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#ruletype" title="RuleType">RuleType</a>: <i>String</i>
<a href="#cases" title="Cases">Cases</a>: <i>
      - &lt;a href=&#34;rules-cases.md&#34;&gt;Cases&lt;/a&gt;</i>
<a href="#defaultanswerdata" title="DefaultAnswerData">DefaultAnswerData</a>: <i>
      - &lt;a href=&#34;rules-defaultanswerdata.md&#34;&gt;DefaultAnswerData&lt;/a&gt;</i>
</pre>

## Properties

#### DefaultCount

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cases

_Required_: No
_Type_: List of &lt;a href=&#34;rules-cases.md&#34;&gt;Cases&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultAnswerData

_Required_: No
_Type_: List of &lt;a href=&#34;rules-defaultanswerdata.md&#34;&gt;DefaultAnswerData&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

