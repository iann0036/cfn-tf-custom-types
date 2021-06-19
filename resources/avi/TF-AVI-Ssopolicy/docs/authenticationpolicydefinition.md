# TF::AVI::Ssopolicy AuthenticationPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultauthprofileref" title="DefaultAuthProfileRef">DefaultAuthProfileRef</a>" : <i>String</i>,
    "<a href="#authnrules" title="AuthnRules">AuthnRules</a>" : <i>[ <a href="authnrulesdefinition.md">AuthnRulesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultauthprofileref" title="DefaultAuthProfileRef">DefaultAuthProfileRef</a>: <i>String</i>
<a href="#authnrules" title="AuthnRules">AuthnRules</a>: <i>
      - <a href="authnrulesdefinition.md">AuthnRulesDefinition</a></i>
</pre>

## Properties

#### DefaultAuthProfileRef

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthnRules

_Required_: No

_Type_: List of <a href="authnrulesdefinition.md">AuthnRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

