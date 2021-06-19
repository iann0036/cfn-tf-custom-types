# TF::AWS::SsmMaintenanceWindowTask RunCommandParametersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
    "<a href="#documenthash" title="DocumentHash">DocumentHash</a>" : <i>String</i>,
    "<a href="#documenthashtype" title="DocumentHashType">DocumentHashType</a>" : <i>String</i>,
    "<a href="#documentversion" title="DocumentVersion">DocumentVersion</a>" : <i>String</i>,
    "<a href="#outputs3bucket" title="OutputS3Bucket">OutputS3Bucket</a>" : <i>String</i>,
    "<a href="#outputs3keyprefix" title="OutputS3KeyPrefix">OutputS3KeyPrefix</a>" : <i>String</i>,
    "<a href="#servicerolearn" title="ServiceRoleArn">ServiceRoleArn</a>" : <i>String</i>,
    "<a href="#timeoutseconds" title="TimeoutSeconds">TimeoutSeconds</a>" : <i>Double</i>,
    "<a href="#cloudwatchconfig" title="CloudwatchConfig">CloudwatchConfig</a>" : <i>[ <a href="cloudwatchconfigdefinition.md">CloudwatchConfigDefinition</a>, ... ]</i>,
    "<a href="#notificationconfig" title="NotificationConfig">NotificationConfig</a>" : <i>[ <a href="notificationconfigdefinition.md">NotificationConfigDefinition</a>, ... ]</i>,
    "<a href="#parameter" title="Parameter">Parameter</a>" : <i>[ <a href="parameterdefinition.md">ParameterDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#comment" title="Comment">Comment</a>: <i>String</i>
<a href="#documenthash" title="DocumentHash">DocumentHash</a>: <i>String</i>
<a href="#documenthashtype" title="DocumentHashType">DocumentHashType</a>: <i>String</i>
<a href="#documentversion" title="DocumentVersion">DocumentVersion</a>: <i>String</i>
<a href="#outputs3bucket" title="OutputS3Bucket">OutputS3Bucket</a>: <i>String</i>
<a href="#outputs3keyprefix" title="OutputS3KeyPrefix">OutputS3KeyPrefix</a>: <i>String</i>
<a href="#servicerolearn" title="ServiceRoleArn">ServiceRoleArn</a>: <i>String</i>
<a href="#timeoutseconds" title="TimeoutSeconds">TimeoutSeconds</a>: <i>Double</i>
<a href="#cloudwatchconfig" title="CloudwatchConfig">CloudwatchConfig</a>: <i>
      - <a href="cloudwatchconfigdefinition.md">CloudwatchConfigDefinition</a></i>
<a href="#notificationconfig" title="NotificationConfig">NotificationConfig</a>: <i>
      - <a href="notificationconfigdefinition.md">NotificationConfigDefinition</a></i>
<a href="#parameter" title="Parameter">Parameter</a>: <i>
      - <a href="parameterdefinition.md">ParameterDefinition</a></i>
</pre>

## Properties

#### Comment

Information about the command(s) to execute.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DocumentHash

The SHA-256 or SHA-1 hash created by the system when the document was created. SHA-1 hashes have been deprecated.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DocumentHashType

SHA-256 or SHA-1. SHA-1 hashes have been deprecated. Valid values: `Sha256` and `Sha1`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DocumentVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputS3Bucket

The name of the Amazon S3 bucket.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputS3KeyPrefix

The Amazon S3 bucket subfolder.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRoleArn

The IAM service role to assume during task execution.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutSeconds

If this time is reached and the command has not already started executing, it doesn't run.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchConfig

_Required_: No

_Type_: List of <a href="cloudwatchconfigdefinition.md">CloudwatchConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationConfig

_Required_: No

_Type_: List of <a href="notificationconfigdefinition.md">NotificationConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameter

_Required_: No

_Type_: List of <a href="parameterdefinition.md">ParameterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

