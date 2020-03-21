# Terraform::AWS::SsmMaintenanceWindowTask TaskInvocationParameters RunCommandParameters

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
    "<a href="#documenthash" title="DocumentHash">DocumentHash</a>" : <i>String</i>,
    "<a href="#documenthashtype" title="DocumentHashType">DocumentHashType</a>" : <i>String</i>,
    "<a href="#outputs3bucket" title="OutputS3Bucket">OutputS3Bucket</a>" : <i>String</i>,
    "<a href="#outputs3keyprefix" title="OutputS3KeyPrefix">OutputS3KeyPrefix</a>" : <i>String</i>,
    "<a href="#servicerolearn" title="ServiceRoleArn">ServiceRoleArn</a>" : <i>String</i>,
    "<a href="#timeoutseconds" title="TimeoutSeconds">TimeoutSeconds</a>" : <i>Double</i>,
    "<a href="#notificationconfig" title="NotificationConfig">NotificationConfig</a>" : <i>[ &lt;a href=&#34;taskinvocationparameters-runcommandparameters-notificationconfig.md&#34;&gt;NotificationConfig&lt;/a&gt;, ... ]</i>,
    "<a href="#parameter" title="Parameter">Parameter</a>" : <i>[ &lt;a href=&#34;taskinvocationparameters-runcommandparameters-parameter.md&#34;&gt;Parameter&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#comment" title="Comment">Comment</a>: <i>String</i>
<a href="#documenthash" title="DocumentHash">DocumentHash</a>: <i>String</i>
<a href="#documenthashtype" title="DocumentHashType">DocumentHashType</a>: <i>String</i>
<a href="#outputs3bucket" title="OutputS3Bucket">OutputS3Bucket</a>: <i>String</i>
<a href="#outputs3keyprefix" title="OutputS3KeyPrefix">OutputS3KeyPrefix</a>: <i>String</i>
<a href="#servicerolearn" title="ServiceRoleArn">ServiceRoleArn</a>: <i>String</i>
<a href="#timeoutseconds" title="TimeoutSeconds">TimeoutSeconds</a>: <i>Double</i>
<a href="#notificationconfig" title="NotificationConfig">NotificationConfig</a>: <i>
      - &lt;a href=&#34;taskinvocationparameters-runcommandparameters-notificationconfig.md&#34;&gt;NotificationConfig&lt;/a&gt;</i>
<a href="#parameter" title="Parameter">Parameter</a>: <i>
      - &lt;a href=&#34;taskinvocationparameters-runcommandparameters-parameter.md&#34;&gt;Parameter&lt;/a&gt;</i>
</pre>

## Properties

#### Comment

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DocumentHash

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DocumentHashType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputS3Bucket

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputS3KeyPrefix

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRoleArn

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutSeconds

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationConfig

_Required_: No
_Type_: List of &lt;a href=&#34;taskinvocationparameters-runcommandparameters-notificationconfig.md&#34;&gt;NotificationConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameter

_Required_: No
_Type_: List of &lt;a href=&#34;taskinvocationparameters-runcommandparameters-parameter.md&#34;&gt;Parameter&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

