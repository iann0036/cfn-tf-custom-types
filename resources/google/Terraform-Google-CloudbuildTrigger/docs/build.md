# Terraform::Google::CloudbuildTrigger Build

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#images" title="Images">Images</a>" : <i>[ String, ... ]</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>String</i>,
    "<a href="#step" title="Step">Step</a>" : <i>[ &lt;a href=&#34;build-step.md&#34;&gt;Step&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#images" title="Images">Images</a>: <i>
      - String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>String</i>
<a href="#step" title="Step">Step</a>: <i>
      - &lt;a href=&#34;build-step.md&#34;&gt;Step&lt;/a&gt;</i>
</pre>

## Properties

#### Images

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Step

_Required_: No
_Type_: List of &lt;a href=&#34;build-step.md&#34;&gt;Step&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

