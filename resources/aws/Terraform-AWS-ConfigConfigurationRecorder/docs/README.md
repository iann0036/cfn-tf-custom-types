# Terraform::AWS::ConfigConfigurationRecorder

Provides an AWS Config Configuration Recorder. Please note that this resource **does not start** the created recorder automatically.

~> **Note:** _Starting_ the Configuration Recorder requires a [delivery channel](/docs/providers/aws/r/config_delivery_channel.html) (while delivery channel creation requires Configuration Recorder). This is why [`aws_config_configuration_recorder_status`](/docs/providers/aws/r/config_configuration_recorder_status.html) is a separate resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ConfigConfigurationRecorder",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
        "<a href="#recordinggroup" title="RecordingGroup">RecordingGroup</a>" : <i>[ <a href="recordinggroup.md">RecordingGroup</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ConfigConfigurationRecorder
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
    <a href="#recordinggroup" title="RecordingGroup">RecordingGroup</a>: <i>
      - <a href="recordinggroup.md">RecordingGroup</a></i>
</pre>

## Properties

#### Name

The name of the recorder. Defaults to `default`. Changing it recreates the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

Amazon Resource Name (ARN) of the IAM role.
used to make read or write requests to the delivery channel and to describe the AWS resources associated with the account.
See [AWS Docs](http://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html) for more details.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecordingGroup

_Required_: No

_Type_: List of <a href="recordinggroup.md">RecordingGroup</a>

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

