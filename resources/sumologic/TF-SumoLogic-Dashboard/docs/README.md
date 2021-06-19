# TF::SumoLogic::Dashboard

Provides a [Sumologic Dashboard (New)][1].

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SumoLogic::Dashboard",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#folderid" title="FolderId">FolderId</a>" : <i>String</i>,
        "<a href="#refreshinterval" title="RefreshInterval">RefreshInterval</a>" : <i>Double</i>,
        "<a href="#theme" title="Theme">Theme</a>" : <i>String</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
        "<a href="#coloringrule" title="ColoringRule">ColoringRule</a>" : <i>[ <a href="coloringruledefinition.md">ColoringRuleDefinition</a>, ... ]</i>,
        "<a href="#layout" title="Layout">Layout</a>" : <i>[ <a href="layoutdefinition.md">LayoutDefinition</a>, ... ]</i>,
        "<a href="#panel" title="Panel">Panel</a>" : <i>[ <a href="paneldefinition.md">PanelDefinition</a>, ... ]</i>,
        "<a href="#timerange" title="TimeRange">TimeRange</a>" : <i>[ <a href="timerangedefinition.md">TimeRangeDefinition</a>, ... ]</i>,
        "<a href="#topologylabelmap" title="TopologyLabelMap">TopologyLabelMap</a>" : <i>[ <a href="topologylabelmapdefinition.md">TopologyLabelMapDefinition</a>, ... ]</i>,
        "<a href="#variable" title="Variable">Variable</a>" : <i>[ <a href="variabledefinition.md">VariableDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SumoLogic::Dashboard
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#folderid" title="FolderId">FolderId</a>: <i>String</i>
    <a href="#refreshinterval" title="RefreshInterval">RefreshInterval</a>: <i>Double</i>
    <a href="#theme" title="Theme">Theme</a>: <i>String</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
    <a href="#coloringrule" title="ColoringRule">ColoringRule</a>: <i>
      - <a href="coloringruledefinition.md">ColoringRuleDefinition</a></i>
    <a href="#layout" title="Layout">Layout</a>: <i>
      - <a href="layoutdefinition.md">LayoutDefinition</a></i>
    <a href="#panel" title="Panel">Panel</a>: <i>
      - <a href="paneldefinition.md">PanelDefinition</a></i>
    <a href="#timerange" title="TimeRange">TimeRange</a>: <i>
      - <a href="timerangedefinition.md">TimeRangeDefinition</a></i>
    <a href="#topologylabelmap" title="TopologyLabelMap">TopologyLabelMap</a>: <i>
      - <a href="topologylabelmapdefinition.md">TopologyLabelMapDefinition</a></i>
    <a href="#variable" title="Variable">Variable</a>: <i>
      - <a href="variabledefinition.md">VariableDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FolderId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RefreshInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Theme

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ColoringRule

_Required_: No

_Type_: List of <a href="coloringruledefinition.md">ColoringRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Layout

_Required_: No

_Type_: List of <a href="layoutdefinition.md">LayoutDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Panel

_Required_: No

_Type_: List of <a href="paneldefinition.md">PanelDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeRange

_Required_: No

_Type_: List of <a href="timerangedefinition.md">TimeRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopologyLabelMap

_Required_: No

_Type_: List of <a href="topologylabelmapdefinition.md">TopologyLabelMapDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Variable

_Required_: No

_Type_: List of <a href="variabledefinition.md">VariableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

