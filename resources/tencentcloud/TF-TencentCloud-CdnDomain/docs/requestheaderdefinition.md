# TF::TencentCloud::CdnDomain RequestHeaderDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#switch" title="Switch">Switch</a>" : <i>String</i>,
    "<a href="#headerrules" title="HeaderRules">HeaderRules</a>" : <i>[ <a href="headerrulesdefinition.md">HeaderRulesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#switch" title="Switch">Switch</a>: <i>String</i>
<a href="#headerrules" title="HeaderRules">HeaderRules</a>: <i>
      - <a href="headerrulesdefinition.md">HeaderRulesDefinition</a></i>
</pre>

## Properties

#### Switch

Custom request header configuration switch. Valid values are `on` and `off`. and default value is `off`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderRules

_Required_: No

_Type_: List of <a href="headerrulesdefinition.md">HeaderRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

