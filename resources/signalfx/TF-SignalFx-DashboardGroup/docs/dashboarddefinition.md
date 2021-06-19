# TF::SignalFx::DashboardGroup DashboardDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dashboardid" title="DashboardId">DashboardId</a>" : <i>String</i>,
    "<a href="#descriptionoverride" title="DescriptionOverride">DescriptionOverride</a>" : <i>String</i>,
    "<a href="#nameoverride" title="NameOverride">NameOverride</a>" : <i>String</i>,
    "<a href="#filteroverride" title="FilterOverride">FilterOverride</a>" : <i>[ <a href="filteroverridedefinition.md">FilterOverrideDefinition</a>, ... ]</i>,
    "<a href="#variableoverride" title="VariableOverride">VariableOverride</a>" : <i>[ <a href="variableoverridedefinition.md">VariableOverrideDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dashboardid" title="DashboardId">DashboardId</a>: <i>String</i>
<a href="#descriptionoverride" title="DescriptionOverride">DescriptionOverride</a>: <i>String</i>
<a href="#nameoverride" title="NameOverride">NameOverride</a>: <i>String</i>
<a href="#filteroverride" title="FilterOverride">FilterOverride</a>: <i>
      - <a href="filteroverridedefinition.md">FilterOverrideDefinition</a></i>
<a href="#variableoverride" title="VariableOverride">VariableOverride</a>: <i>
      - <a href="variableoverridedefinition.md">VariableOverrideDefinition</a></i>
</pre>

## Properties

#### DashboardId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DescriptionOverride

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameOverride

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterOverride

_Required_: No

_Type_: List of <a href="filteroverridedefinition.md">FilterOverrideDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VariableOverride

_Required_: No

_Type_: List of <a href="variableoverridedefinition.md">VariableOverrideDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

