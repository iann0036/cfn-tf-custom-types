# TF::Volterra::FastAcl ReAclDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allpublicvips" title="AllPublicVips">AllPublicVips</a>" : <i>Boolean</i>,
    "<a href="#defaulttenantvip" title="DefaultTenantVip">DefaultTenantVip</a>" : <i>Boolean</i>,
    "<a href="#fastaclrules" title="FastAclRules">FastAclRules</a>" : <i>[ <a href="fastaclrulesdefinition.md">FastAclRulesDefinition</a>, ... ]</i>,
    "<a href="#selectedtenantvip" title="SelectedTenantVip">SelectedTenantVip</a>" : <i>[ <a href="selectedtenantvipdefinition.md">SelectedTenantVipDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allpublicvips" title="AllPublicVips">AllPublicVips</a>: <i>Boolean</i>
<a href="#defaulttenantvip" title="DefaultTenantVip">DefaultTenantVip</a>: <i>Boolean</i>
<a href="#fastaclrules" title="FastAclRules">FastAclRules</a>: <i>
      - <a href="fastaclrulesdefinition.md">FastAclRulesDefinition</a></i>
<a href="#selectedtenantvip" title="SelectedTenantVip">SelectedTenantVip</a>: <i>
      - <a href="selectedtenantvipdefinition.md">SelectedTenantVipDefinition</a></i>
</pre>

## Properties

#### AllPublicVips

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultTenantVip

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FastAclRules

_Required_: No

_Type_: List of <a href="fastaclrulesdefinition.md">FastAclRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelectedTenantVip

_Required_: No

_Type_: List of <a href="selectedtenantvipdefinition.md">SelectedTenantVipDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

