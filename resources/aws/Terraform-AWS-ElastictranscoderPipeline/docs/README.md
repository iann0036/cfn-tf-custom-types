# Terraform::AWS::ElastictranscoderPipeline

CloudFormation equivalent of aws_elastictranscoder_pipeline

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ElastictranscoderPipeline",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#awskmskeyarn" title="AwsKmsKeyArn">AwsKmsKeyArn</a>" : <i>String</i>,
        "<a href="#inputbucket" title="InputBucket">InputBucket</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#outputbucket" title="OutputBucket">OutputBucket</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#contentconfig" title="ContentConfig">ContentConfig</a>" : <i>[ &lt;a href=&#34;contentconfig.md&#34;&gt;ContentConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#contentconfigpermissions" title="ContentConfigPermissions">ContentConfigPermissions</a>" : <i>[ &lt;a href=&#34;contentconfigpermissions.md&#34;&gt;ContentConfigPermissions&lt;/a&gt;, ... ]</i>,
        "<a href="#notifications" title="Notifications">Notifications</a>" : <i>[ &lt;a href=&#34;notifications.md&#34;&gt;Notifications&lt;/a&gt;, ... ]</i>,
        "<a href="#thumbnailconfig" title="ThumbnailConfig">ThumbnailConfig</a>" : <i>[ &lt;a href=&#34;thumbnailconfig.md&#34;&gt;ThumbnailConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#thumbnailconfigpermissions" title="ThumbnailConfigPermissions">ThumbnailConfigPermissions</a>" : <i>[ &lt;a href=&#34;thumbnailconfigpermissions.md&#34;&gt;ThumbnailConfigPermissions&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ElastictranscoderPipeline
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
    <a href="#awskmskeyarn" title="AwsKmsKeyArn">AwsKmsKeyArn</a>: <i>String</i>
    <a href="#inputbucket" title="InputBucket">InputBucket</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#outputbucket" title="OutputBucket">OutputBucket</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#contentconfig" title="ContentConfig">ContentConfig</a>: <i>
      - &lt;a href=&#34;contentconfig.md&#34;&gt;ContentConfig&lt;/a&gt;</i>
    <a href="#contentconfigpermissions" title="ContentConfigPermissions">ContentConfigPermissions</a>: <i>
      - &lt;a href=&#34;contentconfigpermissions.md&#34;&gt;ContentConfigPermissions&lt;/a&gt;</i>
    <a href="#notifications" title="Notifications">Notifications</a>: <i>
      - &lt;a href=&#34;notifications.md&#34;&gt;Notifications&lt;/a&gt;</i>
    <a href="#thumbnailconfig" title="ThumbnailConfig">ThumbnailConfig</a>: <i>
      - &lt;a href=&#34;thumbnailconfig.md&#34;&gt;ThumbnailConfig&lt;/a&gt;</i>
    <a href="#thumbnailconfigpermissions" title="ThumbnailConfigPermissions">ThumbnailConfigPermissions</a>: <i>
      - &lt;a href=&#34;thumbnailconfigpermissions.md&#34;&gt;ThumbnailConfigPermissions&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

_Type_: List of &lt;a href=&#34;contentconfig.md&#34;&gt;ContentConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentConfigPermissions

_Required_: No

_Type_: List of &lt;a href=&#34;contentconfigpermissions.md&#34;&gt;ContentConfigPermissions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notifications

_Required_: No

_Type_: List of &lt;a href=&#34;notifications.md&#34;&gt;Notifications&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThumbnailConfig

_Required_: No

_Type_: List of &lt;a href=&#34;thumbnailconfig.md&#34;&gt;ThumbnailConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThumbnailConfigPermissions

_Required_: No

_Type_: List of &lt;a href=&#34;thumbnailconfigpermissions.md&#34;&gt;ThumbnailConfigPermissions&lt;/a&gt;

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

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

