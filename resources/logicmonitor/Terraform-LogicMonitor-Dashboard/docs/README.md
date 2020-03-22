# Terraform::LogicMonitor::Dashboard

Provides a LogicMonitor dashboard resource. This can be used to create and manage LogicMonitor dashboards
Currently only creating a dashboard based on an existing JSON template is supported

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::LogicMonitor::Dashboard",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#groupid" title="GroupId">GroupId</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#public" title="Public">Public</a>" : <i>Boolean</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#widgettokens" title="WidgetTokens">WidgetTokens</a>" : <i>[ <a href="widgettokens.md">WidgetTokens</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::LogicMonitor::Dashboard
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#groupid" title="GroupId">GroupId</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#public" title="Public">Public</a>: <i>Boolean</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#widgettokens" title="WidgetTokens">WidgetTokens</a>: <i>
      - <a href="widgettokens.md">WidgetTokens</a></i>
</pre>

## Properties

#### Description

Description of dashboard.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupId

The id of the parent group for this dashboard.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of dashboard.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Public

Defines if it is a public or private dashboard.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

Defines if an existing exported JSON template is used to create dashboard.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WidgetTokens

Dashboard tokens allow users to apply a single dashboard template to different device or website groups simply by changing the tokens’ values.

_Required_: No

_Type_: List of <a href="widgettokens.md">WidgetTokens</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

