# Terraform::AWS::ElastictranscoderPipeline Notifications

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#completed" title="Completed">Completed</a>" : <i>String</i>,
    "<a href="#error" title="Error">Error</a>" : <i>String</i>,
    "<a href="#progressing" title="Progressing">Progressing</a>" : <i>String</i>,
    "<a href="#warning" title="Warning">Warning</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#completed" title="Completed">Completed</a>: <i>String</i>
<a href="#error" title="Error">Error</a>: <i>String</i>
<a href="#progressing" title="Progressing">Progressing</a>: <i>String</i>
<a href="#warning" title="Warning">Warning</a>: <i>String</i>
</pre>

## Properties

#### Completed

The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing a job in this pipeline.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Error

The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition while processing a job in this pipeline.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Progressing

The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process a job in this pipeline.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Warning

The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition while processing a job in this pipeline.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

