# TF::AWS::ElastictranscoderPipeline

Provides an Elastic Transcoder pipeline resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::ElastictranscoderPipeline",
    "Properties" : {
        "<a href="#awskmskeyarn" title="AwsKmsKeyArn">AwsKmsKeyArn</a>" : <i>String</i>,
        "<a href="#inputbucket" title="InputBucket">InputBucket</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#outputbucket" title="OutputBucket">OutputBucket</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#contentconfig" title="ContentConfig">ContentConfig</a>" : <i>[ <a href="contentconfigdefinition.md">ContentConfigDefinition</a>, ... ]</i>,
        "<a href="#contentconfigpermissions" title="ContentConfigPermissions">ContentConfigPermissions</a>" : <i>[ <a href="contentconfigpermissionsdefinition.md">ContentConfigPermissionsDefinition</a>, ... ]</i>,
        "<a href="#notifications" title="Notifications">Notifications</a>" : <i>[ <a href="notificationsdefinition.md">NotificationsDefinition</a>, ... ]</i>,
        "<a href="#thumbnailconfig" title="ThumbnailConfig">ThumbnailConfig</a>" : <i>[ <a href="thumbnailconfigdefinition.md">ThumbnailConfigDefinition</a>, ... ]</i>,
        "<a href="#thumbnailconfigpermissions" title="ThumbnailConfigPermissions">ThumbnailConfigPermissions</a>" : <i>[ <a href="thumbnailconfigpermissionsdefinition.md">ThumbnailConfigPermissionsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::ElastictranscoderPipeline
Properties:
    <a href="#awskmskeyarn" title="AwsKmsKeyArn">AwsKmsKeyArn</a>: <i>String</i>
    <a href="#inputbucket" title="InputBucket">InputBucket</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#outputbucket" title="OutputBucket">OutputBucket</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#contentconfig" title="ContentConfig">ContentConfig</a>: <i>
      - <a href="contentconfigdefinition.md">ContentConfigDefinition</a></i>
    <a href="#contentconfigpermissions" title="ContentConfigPermissions">ContentConfigPermissions</a>: <i>
      - <a href="contentconfigpermissionsdefinition.md">ContentConfigPermissionsDefinition</a></i>
    <a href="#notifications" title="Notifications">Notifications</a>: <i>
      - <a href="notificationsdefinition.md">NotificationsDefinition</a></i>
    <a href="#thumbnailconfig" title="ThumbnailConfig">ThumbnailConfig</a>: <i>
      - <a href="thumbnailconfigdefinition.md">ThumbnailConfigDefinition</a></i>
    <a href="#thumbnailconfigpermissions" title="ThumbnailConfigPermissions">ThumbnailConfigPermissions</a>: <i>
      - <a href="thumbnailconfigpermissionsdefinition.md">ThumbnailConfigPermissionsDefinition</a></i>
</pre>

## Properties

#### AwsKmsKeyArn

The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputBucket

The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the pipeline. Maximum 40 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputBucket

The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentConfig

_Required_: No

_Type_: List of <a href="contentconfigdefinition.md">ContentConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentConfigPermissions

_Required_: No

_Type_: List of <a href="contentconfigpermissionsdefinition.md">ContentConfigPermissionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notifications

_Required_: No

_Type_: List of <a href="notificationsdefinition.md">NotificationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThumbnailConfig

_Required_: No

_Type_: List of <a href="thumbnailconfigdefinition.md">ThumbnailConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThumbnailConfigPermissions

_Required_: No

_Type_: List of <a href="thumbnailconfigpermissionsdefinition.md">ThumbnailConfigPermissionsDefinition</a>

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

