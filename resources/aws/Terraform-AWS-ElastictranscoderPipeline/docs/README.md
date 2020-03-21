# Terraform::AWS::ElastictranscoderPipeline

CloudFormation equivalent of aws_elastictranscoder_pipeline

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ElastictranscoderPipeline",
    "Properties" : {
        "<a href="#awskmskeyarn" title="AwsKmsKeyArn">AwsKmsKeyArn</a>" : <i>String</i>,
        "<a href="#inputbucket" title="InputBucket">InputBucket</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#outputbucket" title="OutputBucket">OutputBucket</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#contentconfig" title="ContentConfig">ContentConfig</a>" : <i>[ <a href="contentconfig.md">ContentConfig</a>, ... ]</i>,
        "<a href="#contentconfigpermissions" title="ContentConfigPermissions">ContentConfigPermissions</a>" : <i>[ <a href="contentconfigpermissions.md">ContentConfigPermissions</a>, ... ]</i>,
        "<a href="#notifications" title="Notifications">Notifications</a>" : <i>[ <a href="notifications.md">Notifications</a>, ... ]</i>,
        "<a href="#thumbnailconfig" title="ThumbnailConfig">ThumbnailConfig</a>" : <i>[ <a href="thumbnailconfig.md">ThumbnailConfig</a>, ... ]</i>,
        "<a href="#thumbnailconfigpermissions" title="ThumbnailConfigPermissions">ThumbnailConfigPermissions</a>" : <i>[ <a href="thumbnailconfigpermissions.md">ThumbnailConfigPermissions</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ElastictranscoderPipeline
Properties:
    <a href="#awskmskeyarn" title="AwsKmsKeyArn">AwsKmsKeyArn</a>: <i>String</i>
    <a href="#inputbucket" title="InputBucket">InputBucket</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#outputbucket" title="OutputBucket">OutputBucket</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#contentconfig" title="ContentConfig">ContentConfig</a>: <i>
      - <a href="contentconfig.md">ContentConfig</a></i>
    <a href="#contentconfigpermissions" title="ContentConfigPermissions">ContentConfigPermissions</a>: <i>
      - <a href="contentconfigpermissions.md">ContentConfigPermissions</a></i>
    <a href="#notifications" title="Notifications">Notifications</a>: <i>
      - <a href="notifications.md">Notifications</a></i>
    <a href="#thumbnailconfig" title="ThumbnailConfig">ThumbnailConfig</a>: <i>
      - <a href="thumbnailconfig.md">ThumbnailConfig</a></i>
    <a href="#thumbnailconfigpermissions" title="ThumbnailConfigPermissions">ThumbnailConfigPermissions</a>: <i>
      - <a href="thumbnailconfigpermissions.md">ThumbnailConfigPermissions</a></i>
</pre>

## Properties

#### AwsKmsKeyArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputBucket

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputBucket

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentConfig

_Required_: No

_Type_: List of <a href="contentconfig.md">ContentConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentConfigPermissions

_Required_: No

_Type_: List of <a href="contentconfigpermissions.md">ContentConfigPermissions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notifications

_Required_: No

_Type_: List of <a href="notifications.md">Notifications</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThumbnailConfig

_Required_: No

_Type_: List of <a href="thumbnailconfig.md">ThumbnailConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThumbnailConfigPermissions

_Required_: No

_Type_: List of <a href="thumbnailconfigpermissions.md">ThumbnailConfigPermissions</a>

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

