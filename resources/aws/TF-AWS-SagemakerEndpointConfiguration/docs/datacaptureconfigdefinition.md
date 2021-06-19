# TF::AWS::SagemakerEndpointConfiguration DataCaptureConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#destinations3uri" title="DestinationS3Uri">DestinationS3Uri</a>" : <i>String</i>,
    "<a href="#enablecapture" title="EnableCapture">EnableCapture</a>" : <i>Boolean</i>,
    "<a href="#initialsamplingpercentage" title="InitialSamplingPercentage">InitialSamplingPercentage</a>" : <i>Double</i>,
    "<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>" : <i>String</i>,
    "<a href="#capturecontenttypeheader" title="CaptureContentTypeHeader">CaptureContentTypeHeader</a>" : <i>[ <a href="capturecontenttypeheaderdefinition.md">CaptureContentTypeHeaderDefinition</a>, ... ]</i>,
    "<a href="#captureoptions" title="CaptureOptions">CaptureOptions</a>" : <i>[ <a href="captureoptionsdefinition.md">CaptureOptionsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#destinations3uri" title="DestinationS3Uri">DestinationS3Uri</a>: <i>String</i>
<a href="#enablecapture" title="EnableCapture">EnableCapture</a>: <i>Boolean</i>
<a href="#initialsamplingpercentage" title="InitialSamplingPercentage">InitialSamplingPercentage</a>: <i>Double</i>
<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>: <i>String</i>
<a href="#capturecontenttypeheader" title="CaptureContentTypeHeader">CaptureContentTypeHeader</a>: <i>
      - <a href="capturecontenttypeheaderdefinition.md">CaptureContentTypeHeaderDefinition</a></i>
<a href="#captureoptions" title="CaptureOptions">CaptureOptions</a>: <i>
      - <a href="captureoptionsdefinition.md">CaptureOptionsDefinition</a></i>
</pre>

## Properties

#### DestinationS3Uri

The URL for S3 location where the captured data is stored.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableCapture

Flag to enable data capture. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialSamplingPercentage

Portion of data to capture. Should be between 0 and 100.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyId

Amazon Resource Name (ARN) of a AWS Key Management Service key that Amazon SageMaker uses to encrypt the captured data on Amazon S3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptureContentTypeHeader

_Required_: No

_Type_: List of <a href="capturecontenttypeheaderdefinition.md">CaptureContentTypeHeaderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaptureOptions

_Required_: No

_Type_: List of <a href="captureoptionsdefinition.md">CaptureOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

