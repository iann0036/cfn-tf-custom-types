# TF::AWS::Macie2ClassificationJob AndDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#simplescopeterm" title="SimpleScopeTerm">SimpleScopeTerm</a>" : <i>[ <a href="simplescopetermdefinition.md">SimpleScopeTermDefinition</a>, ... ]</i>,
    "<a href="#tagscopeterm" title="TagScopeTerm">TagScopeTerm</a>" : <i>[ <a href="tagscopetermdefinition.md">TagScopeTermDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#simplescopeterm" title="SimpleScopeTerm">SimpleScopeTerm</a>: <i>
      - <a href="simplescopetermdefinition.md">SimpleScopeTermDefinition</a></i>
<a href="#tagscopeterm" title="TagScopeTerm">TagScopeTerm</a>: <i>
      - <a href="tagscopetermdefinition.md">TagScopeTermDefinition</a></i>
</pre>

## Properties

#### SimpleScopeTerm

_Required_: No

_Type_: List of <a href="simplescopetermdefinition.md">SimpleScopeTermDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagScopeTerm

_Required_: No

_Type_: List of <a href="tagscopetermdefinition.md">TagScopeTermDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

