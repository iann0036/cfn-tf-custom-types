# TF::AzureRM::ApplicationGateway RewriteRuleSetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#rewriterule" title="RewriteRule">RewriteRule</a>" : <i>[ <a href="rewriteruledefinition.md">RewriteRuleDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#rewriterule" title="RewriteRule">RewriteRule</a>: <i>
      - <a href="rewriteruledefinition.md">RewriteRuleDefinition</a></i>
</pre>

## Properties

#### Name

Unique name of the rewrite rule set block.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RewriteRule

_Required_: No

_Type_: List of <a href="rewriteruledefinition.md">RewriteRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

