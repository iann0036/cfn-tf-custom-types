# Terraform::AWS::SnsSmsPreferences

Provides a way to set SNS SMS preferences.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::SnsSmsPreferences",
    "Properties" : {
        "<a href="#defaultsenderid" title="DefaultSenderId">DefaultSenderId</a>" : <i>String</i>,
        "<a href="#defaultsmstype" title="DefaultSmsType">DefaultSmsType</a>" : <i>String</i>,
        "<a href="#deliverystatusiamrolearn" title="DeliveryStatusIamRoleArn">DeliveryStatusIamRoleArn</a>" : <i>String</i>,
        "<a href="#deliverystatussuccesssamplingrate" title="DeliveryStatusSuccessSamplingRate">DeliveryStatusSuccessSamplingRate</a>" : <i>String</i>,
        "<a href="#monthlyspendlimit" title="MonthlySpendLimit">MonthlySpendLimit</a>" : <i>String</i>,
        "<a href="#usagereports3bucket" title="UsageReportS3Bucket">UsageReportS3Bucket</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::SnsSmsPreferences
Properties:
    <a href="#defaultsenderid" title="DefaultSenderId">DefaultSenderId</a>: <i>String</i>
    <a href="#defaultsmstype" title="DefaultSmsType">DefaultSmsType</a>: <i>String</i>
    <a href="#deliverystatusiamrolearn" title="DeliveryStatusIamRoleArn">DeliveryStatusIamRoleArn</a>: <i>String</i>
    <a href="#deliverystatussuccesssamplingrate" title="DeliveryStatusSuccessSamplingRate">DeliveryStatusSuccessSamplingRate</a>: <i>String</i>
    <a href="#monthlyspendlimit" title="MonthlySpendLimit">MonthlySpendLimit</a>: <i>String</i>
    <a href="#usagereports3bucket" title="UsageReportS3Bucket">UsageReportS3Bucket</a>: <i>String</i>
</pre>

## Properties

#### DefaultSenderId

A string, such as your business brand, that is displayed as the sender on the receiving device.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultSmsType

The type of SMS message that you will send by default. Possible values are: Promotional, Transactional.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeliveryStatusIamRoleArn

The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeliveryStatusSuccessSamplingRate

The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value must be between 0 and 100.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MonthlySpendLimit

The maximum amount in USD that you are willing to spend each month to send SMS messages.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsageReportS3Bucket

The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS.

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

#### Id

Returns the <code>Id</code> value.

