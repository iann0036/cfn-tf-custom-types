# TF::Dynatrace::Dashboard TileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#assignedentities" title="AssignedEntities">AssignedEntities</a>" : <i>[ String, ... ]</i>,
    "<a href="#chartvisible" title="ChartVisible">ChartVisible</a>" : <i>Boolean</i>,
    "<a href="#configured" title="Configured">Configured</a>" : <i>Boolean</i>,
    "<a href="#customname" title="CustomName">CustomName</a>" : <i>String</i>,
    "<a href="#excludemaintenancewindows" title="ExcludeMaintenanceWindows">ExcludeMaintenanceWindows</a>" : <i>Boolean</i>,
    "<a href="#limit" title="Limit">Limit</a>" : <i>Double</i>,
    "<a href="#markdown" title="Markdown">Markdown</a>" : <i>String</i>,
    "<a href="#metric" title="Metric">Metric</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#query" title="Query">Query</a>" : <i>String</i>,
    "<a href="#tiletype" title="TileType">TileType</a>" : <i>String</i>,
    "<a href="#timeframeshift" title="TimeFrameShift">TimeFrameShift</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>,
    "<a href="#visualization" title="Visualization">Visualization</a>" : <i>String</i>,
    "<a href="#bounds" title="Bounds">Bounds</a>" : <i>[ <a href="boundsdefinition.md">BoundsDefinition</a>, ... ]</i>,
    "<a href="#filter" title="Filter">Filter</a>" : <i>[ <a href="filterdefinition.md">FilterDefinition</a>, ... ]</i>,
    "<a href="#filterconfig" title="FilterConfig">FilterConfig</a>" : <i>[ <a href="filterconfigdefinition.md">FilterConfigDefinition</a>, ... ]</i>,
    "<a href="#visualizationconfig" title="VisualizationConfig">VisualizationConfig</a>" : <i>[ <a href="visualizationconfigdefinition.md">VisualizationConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#assignedentities" title="AssignedEntities">AssignedEntities</a>: <i>
      - String</i>
<a href="#chartvisible" title="ChartVisible">ChartVisible</a>: <i>Boolean</i>
<a href="#configured" title="Configured">Configured</a>: <i>Boolean</i>
<a href="#customname" title="CustomName">CustomName</a>: <i>String</i>
<a href="#excludemaintenancewindows" title="ExcludeMaintenanceWindows">ExcludeMaintenanceWindows</a>: <i>Boolean</i>
<a href="#limit" title="Limit">Limit</a>: <i>Double</i>
<a href="#markdown" title="Markdown">Markdown</a>: <i>String</i>
<a href="#metric" title="Metric">Metric</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#query" title="Query">Query</a>: <i>String</i>
<a href="#tiletype" title="TileType">TileType</a>: <i>String</i>
<a href="#timeframeshift" title="TimeFrameShift">TimeFrameShift</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
<a href="#visualization" title="Visualization">Visualization</a>: <i>String</i>
<a href="#bounds" title="Bounds">Bounds</a>: <i>
      - <a href="boundsdefinition.md">BoundsDefinition</a></i>
<a href="#filter" title="Filter">Filter</a>: <i>
      - <a href="filterdefinition.md">FilterDefinition</a></i>
<a href="#filterconfig" title="FilterConfig">FilterConfig</a>: <i>
      - <a href="filterconfigdefinition.md">FilterConfigDefinition</a></i>
<a href="#visualizationconfig" title="VisualizationConfig">VisualizationConfig</a>: <i>
      - <a href="visualizationconfigdefinition.md">VisualizationConfigDefinition</a></i>
</pre>

## Properties

#### AssignedEntities

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChartVisible

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Configured

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeMaintenanceWindows

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Limit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Markdown

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TileType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeFrameShift

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Visualization

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bounds

_Required_: No

_Type_: List of <a href="boundsdefinition.md">BoundsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: List of <a href="filterdefinition.md">FilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterConfig

_Required_: No

_Type_: List of <a href="filterconfigdefinition.md">FilterConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VisualizationConfig

_Required_: No

_Type_: List of <a href="visualizationconfigdefinition.md">VisualizationConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

