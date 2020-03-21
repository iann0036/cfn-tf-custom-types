# Terraform::AWS::ConfigConfigRule Source

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#owner" title="Owner">Owner</a>" : <i>String</i>,
    "<a href="#sourceidentifier" title="SourceIdentifier">SourceIdentifier</a>" : <i>String</i>,
    "<a href="#sourcedetail" title="SourceDetail">SourceDetail</a>" : <i>[ &lt;a href=&#34;source-sourcedetail.md&#34;&gt;SourceDetail&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#owner" title="Owner">Owner</a>: <i>String</i>
<a href="#sourceidentifier" title="SourceIdentifier">SourceIdentifier</a>: <i>String</i>
<a href="#sourcedetail" title="SourceDetail">SourceDetail</a>: <i>
      - &lt;a href=&#34;source-sourcedetail.md&#34;&gt;SourceDetail&lt;/a&gt;</i>
</pre>

## Properties

#### Owner

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIdentifier

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDetail

_Required_: No
_Type_: List of &lt;a href=&#34;source-sourcedetail.md&#34;&gt;SourceDetail&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

