# Terraform::Docker::Service TaskSpec Placement

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#constraints" title="Constraints">Constraints</a>" : <i>[ String, ... ]</i>,
    "<a href="#prefs" title="Prefs">Prefs</a>" : <i>[ String, ... ]</i>,
    "<a href="#platforms" title="Platforms">Platforms</a>" : <i>[ &lt;a href=&#34;taskspec-placement-platforms.md&#34;&gt;Platforms&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#constraints" title="Constraints">Constraints</a>: <i>
      - String</i>
<a href="#prefs" title="Prefs">Prefs</a>: <i>
      - String</i>
<a href="#platforms" title="Platforms">Platforms</a>: <i>
      - &lt;a href=&#34;taskspec-placement-platforms.md&#34;&gt;Platforms&lt;/a&gt;</i>
</pre>

## Properties

#### Constraints

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefs

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Platforms

_Required_: No
_Type_: List of &lt;a href=&#34;taskspec-placement-platforms.md&#34;&gt;Platforms&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

