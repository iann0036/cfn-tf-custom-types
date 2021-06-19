# TF::GoogleBeta::GoogleDataprocWorkflowTemplate ClusterSelectorDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clusterlabels" title="ClusterLabels">ClusterLabels</a>" : <i>[ <a href="clusterlabelsdefinition.md">ClusterLabelsDefinition</a>, ... ]</i>,
    "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#clusterlabels" title="ClusterLabels">ClusterLabels</a>: <i>
      - <a href="clusterlabelsdefinition.md">ClusterLabelsDefinition</a></i>
<a href="#zone" title="Zone">Zone</a>: <i>String</i>
</pre>

## Properties

#### ClusterLabels

_Required_: Yes

_Type_: List of <a href="clusterlabelsdefinition.md">ClusterLabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

