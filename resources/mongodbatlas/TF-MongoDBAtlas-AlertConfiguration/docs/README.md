# TF::MongoDBAtlas::AlertConfiguration

`mongodbatlas_alert_configuration` provides an Alert Configuration resource to define the conditions that trigger an alert and the methods of notification within a MongoDB Atlas project.

-> **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MongoDBAtlas::AlertConfiguration",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#eventtype" title="EventType">EventType</a>" : <i>String</i>,
        "<a href="#metricthreshold" title="MetricThreshold">MetricThreshold</a>" : <i>[ <a href="metricthresholddefinition.md">MetricThresholdDefinition</a>, ... ]</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#threshold" title="Threshold">Threshold</a>" : <i>[ <a href="thresholddefinition.md">ThresholdDefinition</a>, ... ]</i>,
        "<a href="#matcher" title="Matcher">Matcher</a>" : <i>[ <a href="matcherdefinition.md">MatcherDefinition</a>, ... ]</i>,
        "<a href="#notification" title="Notification">Notification</a>" : <i>[ <a href="notificationdefinition.md">NotificationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MongoDBAtlas::AlertConfiguration
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#eventtype" title="EventType">EventType</a>: <i>String</i>
    <a href="#metricthreshold" title="MetricThreshold">MetricThreshold</a>: <i>
      - <a href="metricthresholddefinition.md">MetricThresholdDefinition</a></i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#threshold" title="Threshold">Threshold</a>: <i>
      - <a href="thresholddefinition.md">ThresholdDefinition</a></i>
    <a href="#matcher" title="Matcher">Matcher</a>: <i>
      - <a href="matcherdefinition.md">MatcherDefinition</a></i>
    <a href="#notification" title="Notification">Notification</a>: <i>
      - <a href="notificationdefinition.md">NotificationDefinition</a></i>
</pre>

## Properties

#### Enabled

It is not required, but If the attribute is omitted, by default will be false, and the configuration would be disabled. You must set true to enable the configuration.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventType

The type of event that will trigger an alert.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricThreshold

_Required_: No

_Type_: List of <a href="metricthresholddefinition.md">MetricThresholdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The ID of the project where the alert configuration will create.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Threshold

_Required_: No

_Type_: List of <a href="thresholddefinition.md">ThresholdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Matcher

_Required_: No

_Type_: List of <a href="matcherdefinition.md">MatcherDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notification

_Required_: No

_Type_: List of <a href="notificationdefinition.md">NotificationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AlertConfigurationId

Returns the <code>AlertConfigurationId</code> value.

#### Created

Returns the <code>Created</code> value.

#### Id

Returns the <code>Id</code> value.

#### Updated

Returns the <code>Updated</code> value.

