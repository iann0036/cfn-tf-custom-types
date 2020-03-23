# Terraform::AWS::Codepipeline

Provides a CodePipeline.

~> **NOTE on `aws_codepipeline`:** - the `GITHUB_TOKEN` environment variable must be set if the GitHub provider is specified.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::Codepipeline",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#artifactstore" title="ArtifactStore">ArtifactStore</a>" : <i>[ <a href="artifactstore.md">ArtifactStore</a>, ... ]</i>,
        "<a href="#stage" title="Stage">Stage</a>" : <i>[ <a href="stage.md">Stage</a>, ... ]</i>,
        "<a href="#encryptionkey" title="EncryptionKey">EncryptionKey</a>" : <i>[ <a href="encryptionkey.md">EncryptionKey</a>, ... ]</i>,
        "<a href="#action" title="Action">Action</a>" : <i>[ <a href="action.md">Action</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::Codepipeline
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#artifactstore" title="ArtifactStore">ArtifactStore</a>: <i>
      - <a href="artifactstore.md">ArtifactStore</a></i>
    <a href="#stage" title="Stage">Stage</a>: <i>
      - <a href="stage.md">Stage</a></i>
    <a href="#encryptionkey" title="EncryptionKey">EncryptionKey</a>: <i>
      - <a href="encryptionkey.md">EncryptionKey</a></i>
    <a href="#action" title="Action">Action</a>: <i>
      - <a href="action.md">Action</a></i>
</pre>

## Properties

#### Name

The name of the pipeline.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

A service role Amazon Resource Name (ARN) that grants AWS CodePipeline permission to make calls to AWS services on your behalf.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArtifactStore

_Required_: No

_Type_: List of <a href="artifactstore.md">ArtifactStore</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stage

_Required_: No

_Type_: List of <a href="stage.md">Stage</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionKey

_Required_: No

_Type_: List of <a href="encryptionkey.md">EncryptionKey</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No

_Type_: List of <a href="action.md">Action</a>

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

