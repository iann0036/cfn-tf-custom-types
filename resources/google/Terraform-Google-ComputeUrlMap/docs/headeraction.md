# Terraform::Google::ComputeUrlMap HeaderAction

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#requestheaderstoremove" title="RequestHeadersToRemove">RequestHeadersToRemove</a>" : <i>[ String, ... ]</i>,
    "<a href="#responseheaderstoremove" title="ResponseHeadersToRemove">ResponseHeadersToRemove</a>" : <i>[ String, ... ]</i>,
    "<a href="#requestheaderstoadd" title="RequestHeadersToAdd">RequestHeadersToAdd</a>" : <i>[ &lt;a href=&#34;headeraction-requestheaderstoadd.md&#34;&gt;RequestHeadersToAdd&lt;/a&gt;, ... ]</i>,
    "<a href="#responseheaderstoadd" title="ResponseHeadersToAdd">ResponseHeadersToAdd</a>" : <i>[ &lt;a href=&#34;headeraction-responseheaderstoadd.md&#34;&gt;ResponseHeadersToAdd&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#requestheaderstoremove" title="RequestHeadersToRemove">RequestHeadersToRemove</a>: <i>
      - String</i>
<a href="#responseheaderstoremove" title="ResponseHeadersToRemove">ResponseHeadersToRemove</a>: <i>
      - String</i>
<a href="#requestheaderstoadd" title="RequestHeadersToAdd">RequestHeadersToAdd</a>: <i>
      - &lt;a href=&#34;headeraction-requestheaderstoadd.md&#34;&gt;RequestHeadersToAdd&lt;/a&gt;</i>
<a href="#responseheaderstoadd" title="ResponseHeadersToAdd">ResponseHeadersToAdd</a>: <i>
      - &lt;a href=&#34;headeraction-responseheaderstoadd.md&#34;&gt;ResponseHeadersToAdd&lt;/a&gt;</i>
</pre>

## Properties

#### RequestHeadersToRemove

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseHeadersToRemove

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeadersToAdd

_Required_: No
_Type_: List of &lt;a href=&#34;headeraction-requestheaderstoadd.md&#34;&gt;RequestHeadersToAdd&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseHeadersToAdd

_Required_: No
_Type_: List of &lt;a href=&#34;headeraction-responseheaderstoadd.md&#34;&gt;ResponseHeadersToAdd&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

