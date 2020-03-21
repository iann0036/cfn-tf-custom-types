# Terraform::AzureRM::FrontdoorFirewallPolicy ManagedRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>,
    "<a href="#exclusion" title="Exclusion">Exclusion</a>" : <i>[ &lt;a href=&#34;managedrule-exclusion.md&#34;&gt;Exclusion&lt;/a&gt;, ... ]</i>,
    "<a href="#override" title="Override">Override</a>" : <i>[ &lt;a href=&#34;managedrule-override.md&#34;&gt;Override&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
<a href="#exclusion" title="Exclusion">Exclusion</a>: <i>
      - &lt;a href=&#34;managedrule-exclusion.md&#34;&gt;Exclusion&lt;/a&gt;</i>
<a href="#override" title="Override">Override</a>: <i>
      - &lt;a href=&#34;managedrule-override.md&#34;&gt;Override&lt;/a&gt;</i>
</pre>

## Properties

#### Type

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exclusion

_Required_: No
_Type_: List of &lt;a href=&#34;managedrule-exclusion.md&#34;&gt;Exclusion&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Override

_Required_: No
_Type_: List of &lt;a href=&#34;managedrule-override.md&#34;&gt;Override&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

