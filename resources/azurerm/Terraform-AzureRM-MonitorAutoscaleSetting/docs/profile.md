# Terraform::AzureRM::MonitorAutoscaleSetting Profile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#capacity" title="Capacity">Capacity</a>" : <i>[ &lt;a href=&#34;profile-capacity.md&#34;&gt;Capacity&lt;/a&gt;, ... ]</i>,
    "<a href="#fixeddate" title="FixedDate">FixedDate</a>" : <i>[ &lt;a href=&#34;profile-fixeddate.md&#34;&gt;FixedDate&lt;/a&gt;, ... ]</i>,
    "<a href="#recurrence" title="Recurrence">Recurrence</a>" : <i>[ &lt;a href=&#34;profile-recurrence.md&#34;&gt;Recurrence&lt;/a&gt;, ... ]</i>,
    "<a href="#rule" title="Rule">Rule</a>" : <i>[ &lt;a href=&#34;profile-rule.md&#34;&gt;Rule&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#capacity" title="Capacity">Capacity</a>: <i>
      - &lt;a href=&#34;profile-capacity.md&#34;&gt;Capacity&lt;/a&gt;</i>
<a href="#fixeddate" title="FixedDate">FixedDate</a>: <i>
      - &lt;a href=&#34;profile-fixeddate.md&#34;&gt;FixedDate&lt;/a&gt;</i>
<a href="#recurrence" title="Recurrence">Recurrence</a>: <i>
      - &lt;a href=&#34;profile-recurrence.md&#34;&gt;Recurrence&lt;/a&gt;</i>
<a href="#rule" title="Rule">Rule</a>: <i>
      - &lt;a href=&#34;profile-rule.md&#34;&gt;Rule&lt;/a&gt;</i>
</pre>

## Properties

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capacity

_Required_: No
_Type_: List of &lt;a href=&#34;profile-capacity.md&#34;&gt;Capacity&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedDate

_Required_: No
_Type_: List of &lt;a href=&#34;profile-fixeddate.md&#34;&gt;FixedDate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recurrence

_Required_: No
_Type_: List of &lt;a href=&#34;profile-recurrence.md&#34;&gt;Recurrence&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No
_Type_: List of &lt;a href=&#34;profile-rule.md&#34;&gt;Rule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

