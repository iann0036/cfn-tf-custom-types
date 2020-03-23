# Terraform::AWS::LambdaLayerVersion

Provides a Lambda Layer Version resource. Lambda Layers allow you to reuse shared bits of code across multiple lambda functions.

For information about Lambda Layers and how to use them, see [AWS Lambda Layers][1]

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::LambdaLayerVersion",
    "Properties" : {
        "<a href="#compatibleruntimes" title="CompatibleRuntimes">CompatibleRuntimes</a>" : <i>[ String, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#filename" title="Filename">Filename</a>" : <i>String</i>,
        "<a href="#layername" title="LayerName">LayerName</a>" : <i>String</i>,
        "<a href="#licenseinfo" title="LicenseInfo">LicenseInfo</a>" : <i>String</i>,
        "<a href="#s3bucket" title="S3Bucket">S3Bucket</a>" : <i>String</i>,
        "<a href="#s3key" title="S3Key">S3Key</a>" : <i>String</i>,
        "<a href="#s3objectversion" title="S3ObjectVersion">S3ObjectVersion</a>" : <i>String</i>,
        "<a href="#sourcecodehash" title="SourceCodeHash">SourceCodeHash</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::LambdaLayerVersion
Properties:
    <a href="#compatibleruntimes" title="CompatibleRuntimes">CompatibleRuntimes</a>: <i>
      - String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#filename" title="Filename">Filename</a>: <i>String</i>
    <a href="#layername" title="LayerName">LayerName</a>: <i>String</i>
    <a href="#licenseinfo" title="LicenseInfo">LicenseInfo</a>: <i>String</i>
    <a href="#s3bucket" title="S3Bucket">S3Bucket</a>: <i>String</i>
    <a href="#s3key" title="S3Key">S3Key</a>: <i>String</i>
    <a href="#s3objectversion" title="S3ObjectVersion">S3ObjectVersion</a>: <i>String</i>
    <a href="#sourcecodehash" title="SourceCodeHash">SourceCodeHash</a>: <i>String</i>
</pre>

## Properties

#### CompatibleRuntimes

A list of [Runtimes][2] this layer is compatible with. Up to 5 runtimes can be specified.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of what your Lambda Layer does.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filename

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LayerName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseInfo

License info for your Lambda Layer. See [License Info][3].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Bucket

The S3 bucket location containing the function's deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Key

The S3 key of an object containing the function's deployment package. Conflicts with `filename`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3ObjectVersion

The object version containing the function's deployment package. Conflicts with `filename`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceCodeHash

Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `${filebase64sha256("file.zip")}` (Terraform 0.11.12 or later) or `${base64sha256(file("file.zip"))}` (Terraform 0.11.11 and earlier), where "file.zip" is the local filename of the lambda layer source archive.

_Required_: No

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

#### Arn

Returns the <code>Arn</code> value.

#### CreatedDate

Returns the <code>CreatedDate</code> value.

#### Id

Returns the <code>Id</code> value.

#### LayerArn

Returns the <code>LayerArn</code> value.

#### SourceCodeSize

Returns the <code>SourceCodeSize</code> value.

#### Version

Returns the <code>Version</code> value.

