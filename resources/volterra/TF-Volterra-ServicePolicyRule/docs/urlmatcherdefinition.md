# TF::Volterra::ServicePolicyRule UrlMatcherDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#invertmatcher" title="InvertMatcher">InvertMatcher</a>" : <i>Boolean</i>,
    "<a href="#urlitems" title="UrlItems">UrlItems</a>" : <i>[ <a href="urlitemsdefinition.md">UrlItemsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#invertmatcher" title="InvertMatcher">InvertMatcher</a>: <i>Boolean</i>
<a href="#urlitems" title="UrlItems">UrlItems</a>: <i>
      - <a href="urlitemsdefinition.md">UrlItemsDefinition</a></i>
</pre>

## Properties

#### InvertMatcher

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlItems

_Required_: No

_Type_: List of <a href="urlitemsdefinition.md">UrlItemsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

