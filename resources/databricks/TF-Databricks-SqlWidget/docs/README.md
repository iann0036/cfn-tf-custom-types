# TF::Databricks::SqlWidget

CloudFormation equivalent of databricks_sql_widget

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Databricks::SqlWidget",
    "Properties" : {
        "<a href="#dashboardid" title="DashboardId">DashboardId</a>" : <i>String</i>,
        "<a href="#text" title="Text">Text</a>" : <i>String</i>,
        "<a href="#visualizationid" title="VisualizationId">VisualizationId</a>" : <i>String</i>,
        "<a href="#widgetid" title="WidgetId">WidgetId</a>" : <i>String</i>,
        "<a href="#parameter" title="Parameter">Parameter</a>" : <i>[ <a href="parameterdefinition.md">ParameterDefinition</a>, ... ]</i>,
        "<a href="#position" title="Position">Position</a>" : <i>[ <a href="positiondefinition.md">PositionDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Databricks::SqlWidget
Properties:
    <a href="#dashboardid" title="DashboardId">DashboardId</a>: <i>String</i>
    <a href="#text" title="Text">Text</a>: <i>String</i>
    <a href="#visualizationid" title="VisualizationId">VisualizationId</a>: <i>String</i>
    <a href="#widgetid" title="WidgetId">WidgetId</a>: <i>String</i>
    <a href="#parameter" title="Parameter">Parameter</a>: <i>
      - <a href="parameterdefinition.md">ParameterDefinition</a></i>
    <a href="#position" title="Position">Position</a>: <i>
      - <a href="positiondefinition.md">PositionDefinition</a></i>
</pre>

## Properties

#### DashboardId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Text

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VisualizationId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WidgetId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameter

_Required_: No

_Type_: List of <a href="parameterdefinition.md">ParameterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Position

_Required_: No

_Type_: List of <a href="positiondefinition.md">PositionDefinition</a>

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

