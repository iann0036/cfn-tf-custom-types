# TF::OCI::MeteringComputationQuery QueryDefinitionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#version" title="Version">Version</a>" : <i>Double</i>,
    "<a href="#costanalysisui" title="CostAnalysisUi">CostAnalysisUi</a>" : <i>[ <a href="costanalysisuidefinition.md">CostAnalysisUiDefinition</a>, ... ]</i>,
    "<a href="#reportquery" title="ReportQuery">ReportQuery</a>" : <i>[ <a href="reportquerydefinition.md">ReportQueryDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#version" title="Version">Version</a>: <i>Double</i>
<a href="#costanalysisui" title="CostAnalysisUi">CostAnalysisUi</a>: <i>
      - <a href="costanalysisuidefinition.md">CostAnalysisUiDefinition</a></i>
<a href="#reportquery" title="ReportQuery">ReportQuery</a>: <i>
      - <a href="reportquerydefinition.md">ReportQueryDefinition</a></i>
</pre>

## Properties

#### DisplayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CostAnalysisUi

_Required_: No

_Type_: List of <a href="costanalysisuidefinition.md">CostAnalysisUiDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReportQuery

_Required_: No

_Type_: List of <a href="reportquerydefinition.md">ReportQueryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

