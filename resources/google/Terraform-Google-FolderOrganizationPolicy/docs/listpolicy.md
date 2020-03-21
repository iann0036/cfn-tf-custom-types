# Terraform::Google::FolderOrganizationPolicy ListPolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#inheritfromparent" title="InheritFromParent">InheritFromParent</a>" : <i>Boolean</i>,
    "<a href="#suggestedvalue" title="SuggestedValue">SuggestedValue</a>" : <i>String</i>,
    "<a href="#allow" title="Allow">Allow</a>" : <i>[ &lt;a href=&#34;listpolicy-allow.md&#34;&gt;Allow&lt;/a&gt;, ... ]</i>,
    "<a href="#deny" title="Deny">Deny</a>" : <i>[ &lt;a href=&#34;listpolicy-deny.md&#34;&gt;Deny&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#inheritfromparent" title="InheritFromParent">InheritFromParent</a>: <i>Boolean</i>
<a href="#suggestedvalue" title="SuggestedValue">SuggestedValue</a>: <i>String</i>
<a href="#allow" title="Allow">Allow</a>: <i>
      - &lt;a href=&#34;listpolicy-allow.md&#34;&gt;Allow&lt;/a&gt;</i>
<a href="#deny" title="Deny">Deny</a>: <i>
      - &lt;a href=&#34;listpolicy-deny.md&#34;&gt;Deny&lt;/a&gt;</i>
</pre>

## Properties

#### InheritFromParent

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuggestedValue

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Allow

_Required_: No
_Type_: List of &lt;a href=&#34;listpolicy-allow.md&#34;&gt;Allow&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Deny

_Required_: No
_Type_: List of &lt;a href=&#34;listpolicy-deny.md&#34;&gt;Deny&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

