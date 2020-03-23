# Terraform::AWS::SnsPlatformApplication

Provides an SNS platform application resource

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::SnsPlatformApplication",
    "Properties" : {
        "<a href="#eventdeliveryfailuretopicarn" title="EventDeliveryFailureTopicArn">EventDeliveryFailureTopicArn</a>" : <i>String</i>,
        "<a href="#eventendpointcreatedtopicarn" title="EventEndpointCreatedTopicArn">EventEndpointCreatedTopicArn</a>" : <i>String</i>,
        "<a href="#eventendpointdeletedtopicarn" title="EventEndpointDeletedTopicArn">EventEndpointDeletedTopicArn</a>" : <i>String</i>,
        "<a href="#eventendpointupdatedtopicarn" title="EventEndpointUpdatedTopicArn">EventEndpointUpdatedTopicArn</a>" : <i>String</i>,
        "<a href="#failurefeedbackrolearn" title="FailureFeedbackRoleArn">FailureFeedbackRoleArn</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#platform" title="Platform">Platform</a>" : <i>String</i>,
        "<a href="#platformcredential" title="PlatformCredential">PlatformCredential</a>" : <i>String</i>,
        "<a href="#platformprincipal" title="PlatformPrincipal">PlatformPrincipal</a>" : <i>String</i>,
        "<a href="#successfeedbackrolearn" title="SuccessFeedbackRoleArn">SuccessFeedbackRoleArn</a>" : <i>String</i>,
        "<a href="#successfeedbacksamplerate" title="SuccessFeedbackSampleRate">SuccessFeedbackSampleRate</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::SnsPlatformApplication
Properties:
    <a href="#eventdeliveryfailuretopicarn" title="EventDeliveryFailureTopicArn">EventDeliveryFailureTopicArn</a>: <i>String</i>
    <a href="#eventendpointcreatedtopicarn" title="EventEndpointCreatedTopicArn">EventEndpointCreatedTopicArn</a>: <i>String</i>
    <a href="#eventendpointdeletedtopicarn" title="EventEndpointDeletedTopicArn">EventEndpointDeletedTopicArn</a>: <i>String</i>
    <a href="#eventendpointupdatedtopicarn" title="EventEndpointUpdatedTopicArn">EventEndpointUpdatedTopicArn</a>: <i>String</i>
    <a href="#failurefeedbackrolearn" title="FailureFeedbackRoleArn">FailureFeedbackRoleArn</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#platform" title="Platform">Platform</a>: <i>String</i>
    <a href="#platformcredential" title="PlatformCredential">PlatformCredential</a>: <i>String</i>
    <a href="#platformprincipal" title="PlatformPrincipal">PlatformPrincipal</a>: <i>String</i>
    <a href="#successfeedbackrolearn" title="SuccessFeedbackRoleArn">SuccessFeedbackRoleArn</a>: <i>String</i>
    <a href="#successfeedbacksamplerate" title="SuccessFeedbackSampleRate">SuccessFeedbackSampleRate</a>: <i>String</i>
</pre>

## Properties

#### EventDeliveryFailureTopicArn

SNS Topic triggered when a delivery to any of the platform endpoints associated with your platform application encounters a permanent failure.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventEndpointCreatedTopicArn

SNS Topic triggered when a new platform endpoint is added to your platform application.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventEndpointDeletedTopicArn

SNS Topic triggered when an existing platform endpoint is deleted from your platform application.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventEndpointUpdatedTopicArn

SNS Topic triggered when an existing platform endpoint is changed from your platform application.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailureFeedbackRoleArn

The IAM role permitted to receive failure feedback for this application.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The friendly name for the SNS platform application.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Platform

The platform that the app is registered with. See [Platform][1] for supported platforms.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlatformCredential

Application Platform credential. See [Credential][1] for type of credential required for platform. The value of this attribute when stored into the Terraform state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlatformPrincipal

Application Platform principal. See [Principal][2] for type of principal required for platform. The value of this attribute when stored into the Terraform state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuccessFeedbackRoleArn

The IAM role permitted to receive success feedback for this application.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuccessFeedbackSampleRate

The percentage of success to sample (0-100).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

