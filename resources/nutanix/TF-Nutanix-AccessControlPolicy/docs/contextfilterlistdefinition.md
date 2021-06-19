# TF::Nutanix::AccessControlPolicy ContextFilterListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#entityfilterexpressionlist" title="EntityFilterExpressionList">EntityFilterExpressionList</a>" : <i>[ <a href="entityfilterexpressionlistdefinition.md">EntityFilterExpressionListDefinition</a>, ... ]</i>,
    "<a href="#scopefilterexpressionlist" title="ScopeFilterExpressionList">ScopeFilterExpressionList</a>" : <i>[ <a href="scopefilterexpressionlistdefinition.md">ScopeFilterExpressionListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#entityfilterexpressionlist" title="EntityFilterExpressionList">EntityFilterExpressionList</a>: <i>
      - <a href="entityfilterexpressionlistdefinition.md">EntityFilterExpressionListDefinition</a></i>
<a href="#scopefilterexpressionlist" title="ScopeFilterExpressionList">ScopeFilterExpressionList</a>: <i>
      - <a href="scopefilterexpressionlistdefinition.md">ScopeFilterExpressionListDefinition</a></i>
</pre>

## Properties

#### EntityFilterExpressionList

_Required_: No

_Type_: List of <a href="entityfilterexpressionlistdefinition.md">EntityFilterExpressionListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScopeFilterExpressionList

_Required_: No

_Type_: List of <a href="scopefilterexpressionlistdefinition.md">ScopeFilterExpressionListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

