# TF::Wavefront::AlertTarget

CloudFormation equivalent of wavefront_alert_target

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Wavefront::AlertTarget",
    "Properties" : {
        "<a href="#contenttype" title="ContentType">ContentType</a>" : <i>String</i>,
        "<a href="#customheaders" title="CustomHeaders">CustomHeaders</a>" : <i>[ <a href="customheadersdefinition.md">CustomHeadersDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#emailsubject" title="EmailSubject">EmailSubject</a>" : <i>String</i>,
        "<a href="#ishtmlcontent" title="IsHtmlContent">IsHtmlContent</a>" : <i>Boolean</i>,
        "<a href="#method" title="Method">Method</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#recipient" title="Recipient">Recipient</a>" : <i>String</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#triggers" title="Triggers">Triggers</a>" : <i>[ String, ... ]</i>,
        "<a href="#route" title="Route">Route</a>" : <i>[ <a href="routedefinition.md">RouteDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Wavefront::AlertTarget
Properties:
    <a href="#contenttype" title="ContentType">ContentType</a>: <i>String</i>
    <a href="#customheaders" title="CustomHeaders">CustomHeaders</a>: <i>
      - <a href="customheadersdefinition.md">CustomHeadersDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#emailsubject" title="EmailSubject">EmailSubject</a>: <i>String</i>
    <a href="#ishtmlcontent" title="IsHtmlContent">IsHtmlContent</a>: <i>Boolean</i>
    <a href="#method" title="Method">Method</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#recipient" title="Recipient">Recipient</a>: <i>String</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#triggers" title="Triggers">Triggers</a>: <i>
      - String</i>
    <a href="#route" title="Route">Route</a>: <i>
      - <a href="routedefinition.md">RouteDefinition</a></i>
</pre>

## Properties

#### ContentType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomHeaders

_Required_: No

_Type_: List of <a href="customheadersdefinition.md">CustomHeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailSubject

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsHtmlContent

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recipient

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Triggers

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Route

_Required_: No

_Type_: List of <a href="routedefinition.md">RouteDefinition</a>

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

#### TargetId

Returns the <code>TargetId</code> value.

