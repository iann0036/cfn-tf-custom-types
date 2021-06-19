# TF::SumoLogic::Dashboard SumoSearchPanelDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#keepvisualsettingsconsistentwithparent" title="KeepVisualSettingsConsistentWithParent">KeepVisualSettingsConsistentWithParent</a>" : <i>Boolean</i>,
    "<a href="#key" title="Key">Key</a>" : <i>String</i>,
    "<a href="#title" title="Title">Title</a>" : <i>String</i>,
    "<a href="#visualsettings" title="VisualSettings">VisualSettings</a>" : <i>String</i>,
    "<a href="#coloringrule" title="ColoringRule">ColoringRule</a>" : <i>[ <a href="coloringruledefinition.md">ColoringRuleDefinition</a>, ... ]</i>,
    "<a href="#linkeddashboard" title="LinkedDashboard">LinkedDashboard</a>" : <i>[ <a href="linkeddashboarddefinition.md">LinkedDashboardDefinition</a>, ... ]</i>,
    "<a href="#query" title="Query">Query</a>" : <i>[ <a href="querydefinition.md">QueryDefinition</a>, ... ]</i>,
    "<a href="#timerange" title="TimeRange">TimeRange</a>" : <i>[ <a href="timerangedefinition.md">TimeRangeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#keepvisualsettingsconsistentwithparent" title="KeepVisualSettingsConsistentWithParent">KeepVisualSettingsConsistentWithParent</a>: <i>Boolean</i>
<a href="#key" title="Key">Key</a>: <i>String</i>
<a href="#title" title="Title">Title</a>: <i>String</i>
<a href="#visualsettings" title="VisualSettings">VisualSettings</a>: <i>String</i>
<a href="#coloringrule" title="ColoringRule">ColoringRule</a>: <i>
      - <a href="coloringruledefinition.md">ColoringRuleDefinition</a></i>
<a href="#linkeddashboard" title="LinkedDashboard">LinkedDashboard</a>: <i>
      - <a href="linkeddashboarddefinition.md">LinkedDashboardDefinition</a></i>
<a href="#query" title="Query">Query</a>: <i>
      - <a href="querydefinition.md">QueryDefinition</a></i>
<a href="#timerange" title="TimeRange">TimeRange</a>: <i>
      - <a href="timerangedefinition.md">TimeRangeDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepVisualSettingsConsistentWithParent

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VisualSettings

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ColoringRule

_Required_: No

_Type_: List of <a href="coloringruledefinition.md">ColoringRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinkedDashboard

_Required_: No

_Type_: List of <a href="linkeddashboarddefinition.md">LinkedDashboardDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

_Required_: No

_Type_: List of <a href="querydefinition.md">QueryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeRange

_Required_: No

_Type_: List of <a href="timerangedefinition.md">TimeRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

