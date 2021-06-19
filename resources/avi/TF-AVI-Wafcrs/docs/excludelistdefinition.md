# TF::AVI::Wafcrs ExcludeListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#matchelement" title="MatchElement">MatchElement</a>" : <i>String</i>,
    "<a href="#uripath" title="UriPath">UriPath</a>" : <i>String</i>,
    "<a href="#clientsubnet" title="ClientSubnet">ClientSubnet</a>" : <i>[ <a href="clientsubnetdefinition.md">ClientSubnetDefinition</a>, ... ]</i>,
    "<a href="#matchelementcriteria" title="MatchElementCriteria">MatchElementCriteria</a>" : <i>[ <a href="matchelementcriteriadefinition.md">MatchElementCriteriaDefinition</a>, ... ]</i>,
    "<a href="#urimatchcriteria" title="UriMatchCriteria">UriMatchCriteria</a>" : <i>[ <a href="urimatchcriteriadefinition.md">UriMatchCriteriaDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#matchelement" title="MatchElement">MatchElement</a>: <i>String</i>
<a href="#uripath" title="UriPath">UriPath</a>: <i>String</i>
<a href="#clientsubnet" title="ClientSubnet">ClientSubnet</a>: <i>
      - <a href="clientsubnetdefinition.md">ClientSubnetDefinition</a></i>
<a href="#matchelementcriteria" title="MatchElementCriteria">MatchElementCriteria</a>: <i>
      - <a href="matchelementcriteriadefinition.md">MatchElementCriteriaDefinition</a></i>
<a href="#urimatchcriteria" title="UriMatchCriteria">UriMatchCriteria</a>: <i>
      - <a href="urimatchcriteriadefinition.md">UriMatchCriteriaDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchElement

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UriPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientSubnet

_Required_: No

_Type_: List of <a href="clientsubnetdefinition.md">ClientSubnetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchElementCriteria

_Required_: No

_Type_: List of <a href="matchelementcriteriadefinition.md">MatchElementCriteriaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UriMatchCriteria

_Required_: No

_Type_: List of <a href="urimatchcriteriadefinition.md">UriMatchCriteriaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

