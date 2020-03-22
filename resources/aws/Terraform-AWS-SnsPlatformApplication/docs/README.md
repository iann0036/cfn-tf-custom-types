# Terraform::AWS::SnsPlatformApplication

CloudFormation equivalent of aws_sns_platform_application

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

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventEndpointCreatedTopicArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventEndpointDeletedTopicArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventEndpointUpdatedTopicArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailureFeedbackRoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Platform

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlatformCredential

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlatformPrincipal

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuccessFeedbackRoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuccessFeedbackSampleRate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

