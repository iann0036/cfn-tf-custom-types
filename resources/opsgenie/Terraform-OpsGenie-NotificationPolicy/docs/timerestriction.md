# Terraform::OpsGenie::NotificationPolicy TimeRestriction

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#restriction" title="Restriction">Restriction</a>" : <i>[ &lt;a href=&#34;timerestriction-restriction.md&#34;&gt;Restriction&lt;/a&gt;, ... ]</i>,
    "<a href="#restrictions" title="Restrictions">Restrictions</a>" : <i>[ &lt;a href=&#34;timerestriction-restrictions.md&#34;&gt;Restrictions&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#restriction" title="Restriction">Restriction</a>: <i>
      - &lt;a href=&#34;timerestriction-restriction.md&#34;&gt;Restriction&lt;/a&gt;</i>
<a href="#restrictions" title="Restrictions">Restrictions</a>: <i>
      - &lt;a href=&#34;timerestriction-restrictions.md&#34;&gt;Restrictions&lt;/a&gt;</i>
</pre>

## Properties

#### Type

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Restriction

_Required_: No
_Type_: List of &lt;a href=&#34;timerestriction-restriction.md&#34;&gt;Restriction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Restrictions

_Required_: No
_Type_: List of &lt;a href=&#34;timerestriction-restrictions.md&#34;&gt;Restrictions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

