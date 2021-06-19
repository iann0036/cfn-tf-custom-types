# TF::Logzio::AlertV2

CloudFormation equivalent of logzio_alert_v2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Logzio::AlertV2",
    "Properties" : {
        "<a href="#alertnotificationendpoints" title="AlertNotificationEndpoints">AlertNotificationEndpoints</a>" : <i>[ Double, ... ]</i>,
        "<a href="#correlationoperator" title="CorrelationOperator">CorrelationOperator</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
        "<a href="#joins" title="Joins">Joins</a>" : <i>[ [ <a href="joinsdefinition.md">JoinsDefinition</a>, ... ], ... ]</i>,
        "<a href="#notificationemails" title="NotificationEmails">NotificationEmails</a>" : <i>[ String, ... ]</i>,
        "<a href="#outputtype" title="OutputType">OutputType</a>" : <i>String</i>,
        "<a href="#searchtimeframeminutes" title="SearchTimeframeMinutes">SearchTimeframeMinutes</a>" : <i>Double</i>,
        "<a href="#suppressnotificationsminutes" title="SuppressNotificationsMinutes">SuppressNotificationsMinutes</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
        "<a href="#subcomponents" title="SubComponents">SubComponents</a>" : <i>[ <a href="subcomponentsdefinition.md">SubComponentsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Logzio::AlertV2
Properties:
    <a href="#alertnotificationendpoints" title="AlertNotificationEndpoints">AlertNotificationEndpoints</a>: <i>
      - Double</i>
    <a href="#correlationoperator" title="CorrelationOperator">CorrelationOperator</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
    <a href="#joins" title="Joins">Joins</a>: <i>
      - 
      - <a href="joinsdefinition.md">JoinsDefinition</a></i>
    <a href="#notificationemails" title="NotificationEmails">NotificationEmails</a>: <i>
      - String</i>
    <a href="#outputtype" title="OutputType">OutputType</a>: <i>String</i>
    <a href="#searchtimeframeminutes" title="SearchTimeframeMinutes">SearchTimeframeMinutes</a>: <i>Double</i>
    <a href="#suppressnotificationsminutes" title="SuppressNotificationsMinutes">SuppressNotificationsMinutes</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
    <a href="#subcomponents" title="SubComponents">SubComponents</a>: <i>
      - <a href="subcomponentsdefinition.md">SubComponentsDefinition</a></i>
</pre>

## Properties

#### AlertNotificationEndpoints

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorrelationOperator

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Joins

_Required_: No

_Type_: List of List of <a href="joinsdefinition.md">JoinsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationEmails

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SearchTimeframeMinutes

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuppressNotificationsMinutes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubComponents

_Required_: No

_Type_: List of <a href="subcomponentsdefinition.md">SubComponentsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### CreatedBy

Returns the <code>CreatedBy</code> value.

#### Id

Returns the <code>Id</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.

#### UpdatedBy

Returns the <code>UpdatedBy</code> value.

