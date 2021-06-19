# TF::GoogleBeta::GoogleComputeUrlMap MetadataFiltersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#filtermatchcriteria" title="FilterMatchCriteria">FilterMatchCriteria</a>" : <i>String</i>,
    "<a href="#filterlabels" title="FilterLabels">FilterLabels</a>" : <i>[ <a href="filterlabelsdefinition.md">FilterLabelsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#filtermatchcriteria" title="FilterMatchCriteria">FilterMatchCriteria</a>: <i>String</i>
<a href="#filterlabels" title="FilterLabels">FilterLabels</a>: <i>
      - <a href="filterlabelsdefinition.md">FilterLabelsDefinition</a></i>
</pre>

## Properties

#### FilterMatchCriteria

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterLabels

_Required_: No

_Type_: List of <a href="filterlabelsdefinition.md">FilterLabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

