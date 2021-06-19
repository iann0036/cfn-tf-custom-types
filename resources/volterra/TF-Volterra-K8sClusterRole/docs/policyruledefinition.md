# TF::Volterra::K8sClusterRole PolicyRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#nonresourceurllist" title="NonResourceUrlList">NonResourceUrlList</a>" : <i>[ <a href="nonresourceurllistdefinition.md">NonResourceUrlListDefinition</a>, ... ]</i>,
    "<a href="#resourcelist" title="ResourceList">ResourceList</a>" : <i>[ <a href="resourcelistdefinition.md">ResourceListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#nonresourceurllist" title="NonResourceUrlList">NonResourceUrlList</a>: <i>
      - <a href="nonresourceurllistdefinition.md">NonResourceUrlListDefinition</a></i>
<a href="#resourcelist" title="ResourceList">ResourceList</a>: <i>
      - <a href="resourcelistdefinition.md">ResourceListDefinition</a></i>
</pre>

## Properties

#### NonResourceUrlList

_Required_: No

_Type_: List of <a href="nonresourceurllistdefinition.md">NonResourceUrlListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceList

_Required_: No

_Type_: List of <a href="resourcelistdefinition.md">ResourceListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

