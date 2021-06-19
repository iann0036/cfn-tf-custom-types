# TF::AWS::GuarddutyPublishingDestination

Provides a resource to manage a GuardDuty PublishingDestination. Requires an existing GuardDuty Detector.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::GuarddutyPublishingDestination",
    "Properties" : {
        "<a href="#destinationarn" title="DestinationArn">DestinationArn</a>" : <i>String</i>,
        "<a href="#destinationtype" title="DestinationType">DestinationType</a>" : <i>String</i>,
        "<a href="#detectorid" title="DetectorId">DetectorId</a>" : <i>String</i>,
        "<a href="#kmskeyarn" title="KmsKeyArn">KmsKeyArn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::GuarddutyPublishingDestination
Properties:
    <a href="#destinationarn" title="DestinationArn">DestinationArn</a>: <i>String</i>
    <a href="#destinationtype" title="DestinationType">DestinationType</a>: <i>String</i>
    <a href="#detectorid" title="DetectorId">DetectorId</a>: <i>String</i>
    <a href="#kmskeyarn" title="KmsKeyArn">KmsKeyArn</a>: <i>String</i>
</pre>

## Properties

#### DestinationArn

The bucket arn and prefix under which the findings get exported. Bucket-ARN is required, the prefix is optional and will be `AWSLogs/[Account-ID]/GuardDuty/[Region]/` if not provided.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationType

Currently there is only "S3" available as destination type which is also the default value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DetectorId

The detector ID of the GuardDuty.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyArn

The ARN of the KMS key used to encrypt GuardDuty findings. GuardDuty enforces this to be encrypted.

_Required_: Yes

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

