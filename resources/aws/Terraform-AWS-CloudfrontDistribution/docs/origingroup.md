# Terraform::AWS::CloudfrontDistribution OriginGroup

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#originid" title="OriginId">OriginId</a>" : <i>String</i>,
    "<a href="#failovercriteria" title="FailoverCriteria">FailoverCriteria</a>" : <i>[ &lt;a href=&#34;origingroup-failovercriteria.md&#34;&gt;FailoverCriteria&lt;/a&gt;, ... ]</i>,
    "<a href="#member" title="Member">Member</a>" : <i>[ &lt;a href=&#34;origingroup-member.md&#34;&gt;Member&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#originid" title="OriginId">OriginId</a>: <i>String</i>
<a href="#failovercriteria" title="FailoverCriteria">FailoverCriteria</a>: <i>
      - &lt;a href=&#34;origingroup-failovercriteria.md&#34;&gt;FailoverCriteria&lt;/a&gt;</i>
<a href="#member" title="Member">Member</a>: <i>
      - &lt;a href=&#34;origingroup-member.md&#34;&gt;Member&lt;/a&gt;</i>
</pre>

## Properties

#### OriginId

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailoverCriteria

_Required_: No
_Type_: List of &lt;a href=&#34;origingroup-failovercriteria.md&#34;&gt;FailoverCriteria&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Member

_Required_: No
_Type_: List of &lt;a href=&#34;origingroup-member.md&#34;&gt;Member&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

