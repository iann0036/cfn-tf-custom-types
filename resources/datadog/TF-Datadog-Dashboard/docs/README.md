# TF::Datadog::Dashboard

CloudFormation equivalent of datadog_dashboard

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Datadog::Dashboard",
    "Properties" : {
        "<a href="#dashboardlists" title="DashboardLists">DashboardLists</a>" : <i>[ Double, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#isreadonly" title="IsReadOnly">IsReadOnly</a>" : <i>Boolean</i>,
        "<a href="#layouttype" title="LayoutType">LayoutType</a>" : <i>String</i>,
        "<a href="#notifylist" title="NotifyList">NotifyList</a>" : <i>[ String, ... ]</i>,
        "<a href="#reflowtype" title="ReflowType">ReflowType</a>" : <i>String</i>,
        "<a href="#restrictedroles" title="RestrictedRoles">RestrictedRoles</a>" : <i>[ String, ... ]</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>,
        "<a href="#templatevariable" title="TemplateVariable">TemplateVariable</a>" : <i>[ <a href="templatevariabledefinition.md">TemplateVariableDefinition</a>, ... ]</i>,
        "<a href="#templatevariablepreset" title="TemplateVariablePreset">TemplateVariablePreset</a>" : <i>[ <a href="templatevariablepresetdefinition.md">TemplateVariablePresetDefinition</a>, ... ]</i>,
        "<a href="#widget" title="Widget">Widget</a>" : <i>[ <a href="widgetdefinition.md">WidgetDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Datadog::Dashboard
Properties:
    <a href="#dashboardlists" title="DashboardLists">DashboardLists</a>: <i>
      - Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#isreadonly" title="IsReadOnly">IsReadOnly</a>: <i>Boolean</i>
    <a href="#layouttype" title="LayoutType">LayoutType</a>: <i>String</i>
    <a href="#notifylist" title="NotifyList">NotifyList</a>: <i>
      - String</i>
    <a href="#reflowtype" title="ReflowType">ReflowType</a>: <i>String</i>
    <a href="#restrictedroles" title="RestrictedRoles">RestrictedRoles</a>: <i>
      - String</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
    <a href="#templatevariable" title="TemplateVariable">TemplateVariable</a>: <i>
      - <a href="templatevariabledefinition.md">TemplateVariableDefinition</a></i>
    <a href="#templatevariablepreset" title="TemplateVariablePreset">TemplateVariablePreset</a>: <i>
      - <a href="templatevariablepresetdefinition.md">TemplateVariablePresetDefinition</a></i>
    <a href="#widget" title="Widget">Widget</a>: <i>
      - <a href="widgetdefinition.md">WidgetDefinition</a></i>
</pre>

## Properties

#### DashboardLists

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsReadOnly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LayoutType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReflowType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestrictedRoles

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateVariable

_Required_: No

_Type_: List of <a href="templatevariabledefinition.md">TemplateVariableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateVariablePreset

_Required_: No

_Type_: List of <a href="templatevariablepresetdefinition.md">TemplateVariablePresetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Widget

_Required_: No

_Type_: List of <a href="widgetdefinition.md">WidgetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DashboardListsRemoved

Returns the <code>DashboardListsRemoved</code> value.

#### Id

Returns the <code>Id</code> value.

