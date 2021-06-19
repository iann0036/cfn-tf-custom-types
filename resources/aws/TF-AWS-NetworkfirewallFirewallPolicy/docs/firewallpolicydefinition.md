# TF::AWS::NetworkfirewallFirewallPolicy FirewallPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#statelessdefaultactions" title="StatelessDefaultActions">StatelessDefaultActions</a>" : <i>[ String, ... ]</i>,
    "<a href="#statelessfragmentdefaultactions" title="StatelessFragmentDefaultActions">StatelessFragmentDefaultActions</a>" : <i>[ String, ... ]</i>,
    "<a href="#statefulrulegroupreference" title="StatefulRuleGroupReference">StatefulRuleGroupReference</a>" : <i>[ <a href="statefulrulegroupreferencedefinition.md">StatefulRuleGroupReferenceDefinition</a>, ... ]</i>,
    "<a href="#statelesscustomaction" title="StatelessCustomAction">StatelessCustomAction</a>" : <i>[ <a href="statelesscustomactiondefinition.md">StatelessCustomActionDefinition</a>, ... ]</i>,
    "<a href="#statelessrulegroupreference" title="StatelessRuleGroupReference">StatelessRuleGroupReference</a>" : <i>[ <a href="statelessrulegroupreferencedefinition.md">StatelessRuleGroupReferenceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#statelessdefaultactions" title="StatelessDefaultActions">StatelessDefaultActions</a>: <i>
      - String</i>
<a href="#statelessfragmentdefaultactions" title="StatelessFragmentDefaultActions">StatelessFragmentDefaultActions</a>: <i>
      - String</i>
<a href="#statefulrulegroupreference" title="StatefulRuleGroupReference">StatefulRuleGroupReference</a>: <i>
      - <a href="statefulrulegroupreferencedefinition.md">StatefulRuleGroupReferenceDefinition</a></i>
<a href="#statelesscustomaction" title="StatelessCustomAction">StatelessCustomAction</a>: <i>
      - <a href="statelesscustomactiondefinition.md">StatelessCustomActionDefinition</a></i>
<a href="#statelessrulegroupreference" title="StatelessRuleGroupReference">StatelessRuleGroupReference</a>: <i>
      - <a href="statelessrulegroupreferencedefinition.md">StatelessRuleGroupReferenceDefinition</a></i>
</pre>

## Properties

#### StatelessDefaultActions

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatelessFragmentDefaultActions

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatefulRuleGroupReference

_Required_: No

_Type_: List of <a href="statefulrulegroupreferencedefinition.md">StatefulRuleGroupReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatelessCustomAction

_Required_: No

_Type_: List of <a href="statelesscustomactiondefinition.md">StatelessCustomActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatelessRuleGroupReference

_Required_: No

_Type_: List of <a href="statelessrulegroupreferencedefinition.md">StatelessRuleGroupReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

