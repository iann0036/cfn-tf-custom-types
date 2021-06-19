# TF::AWS::LambdaFunction

Provides a Lambda Function resource. Lambda allows you to trigger execution of code in response to events in AWS, enabling serverless backend solutions. The Lambda Function itself includes source code and runtime configuration.

For information about Lambda and how to use it, see [What is AWS Lambda?][1]

For a detailed example of setting up Lambda and API Gateway, see [Serverless Applications with AWS Lambda and API Gateway.][11]

~> **NOTE:** Due to [AWS Lambda improved VPC networking changes that began deploying in September 2019](https://aws.amazon.com/blogs/compute/announcing-improved-vpc-networking-for-aws-lambda-functions/), EC2 subnets and security groups associated with Lambda Functions can take up to 45 minutes to successfully delete. Terraform AWS Provider version 2.31.0 and later automatically handles this increased timeout, however prior versions require setting the customizable deletion timeouts of those Terraform resources to 45 minutes (`delete = "45m"`). AWS and HashiCorp are working toge...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::LambdaFunction",
    "Properties" : {
        "<a href="#codesigningconfigarn" title="CodeSigningConfigArn">CodeSigningConfigArn</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#filename" title="Filename">Filename</a>" : <i>String</i>,
        "<a href="#functionname" title="FunctionName">FunctionName</a>" : <i>String</i>,
        "<a href="#handler" title="Handler">Handler</a>" : <i>String</i>,
        "<a href="#imageuri" title="ImageUri">ImageUri</a>" : <i>String</i>,
        "<a href="#kmskeyarn" title="KmsKeyArn">KmsKeyArn</a>" : <i>String</i>,
        "<a href="#layers" title="Layers">Layers</a>" : <i>[ String, ... ]</i>,
        "<a href="#memorysize" title="MemorySize">MemorySize</a>" : <i>Double</i>,
        "<a href="#packagetype" title="PackageType">PackageType</a>" : <i>String</i>,
        "<a href="#publish" title="Publish">Publish</a>" : <i>Boolean</i>,
        "<a href="#reservedconcurrentexecutions" title="ReservedConcurrentExecutions">ReservedConcurrentExecutions</a>" : <i>Double</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#runtime" title="Runtime">Runtime</a>" : <i>String</i>,
        "<a href="#s3bucket" title="S3Bucket">S3Bucket</a>" : <i>String</i>,
        "<a href="#s3key" title="S3Key">S3Key</a>" : <i>String</i>,
        "<a href="#s3objectversion" title="S3ObjectVersion">S3ObjectVersion</a>" : <i>String</i>,
        "<a href="#sourcecodehash" title="SourceCodeHash">SourceCodeHash</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#deadletterconfig" title="DeadLetterConfig">DeadLetterConfig</a>" : <i>[ <a href="deadletterconfigdefinition.md">DeadLetterConfigDefinition</a>, ... ]</i>,
        "<a href="#environment" title="Environment">Environment</a>" : <i>[ <a href="environmentdefinition.md">EnvironmentDefinition</a>, ... ]</i>,
        "<a href="#filesystemconfig" title="FileSystemConfig">FileSystemConfig</a>" : <i>[ <a href="filesystemconfigdefinition.md">FileSystemConfigDefinition</a>, ... ]</i>,
        "<a href="#imageconfig" title="ImageConfig">ImageConfig</a>" : <i>[ <a href="imageconfigdefinition.md">ImageConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#tracingconfig" title="TracingConfig">TracingConfig</a>" : <i>[ <a href="tracingconfigdefinition.md">TracingConfigDefinition</a>, ... ]</i>,
        "<a href="#vpcconfig" title="VpcConfig">VpcConfig</a>" : <i>[ <a href="vpcconfigdefinition.md">VpcConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::LambdaFunction
Properties:
    <a href="#codesigningconfigarn" title="CodeSigningConfigArn">CodeSigningConfigArn</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#filename" title="Filename">Filename</a>: <i>String</i>
    <a href="#functionname" title="FunctionName">FunctionName</a>: <i>String</i>
    <a href="#handler" title="Handler">Handler</a>: <i>String</i>
    <a href="#imageuri" title="ImageUri">ImageUri</a>: <i>String</i>
    <a href="#kmskeyarn" title="KmsKeyArn">KmsKeyArn</a>: <i>String</i>
    <a href="#layers" title="Layers">Layers</a>: <i>
      - String</i>
    <a href="#memorysize" title="MemorySize">MemorySize</a>: <i>Double</i>
    <a href="#packagetype" title="PackageType">PackageType</a>: <i>String</i>
    <a href="#publish" title="Publish">Publish</a>: <i>Boolean</i>
    <a href="#reservedconcurrentexecutions" title="ReservedConcurrentExecutions">ReservedConcurrentExecutions</a>: <i>Double</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#runtime" title="Runtime">Runtime</a>: <i>String</i>
    <a href="#s3bucket" title="S3Bucket">S3Bucket</a>: <i>String</i>
    <a href="#s3key" title="S3Key">S3Key</a>: <i>String</i>
    <a href="#s3objectversion" title="S3ObjectVersion">S3ObjectVersion</a>: <i>String</i>
    <a href="#sourcecodehash" title="SourceCodeHash">SourceCodeHash</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#deadletterconfig" title="DeadLetterConfig">DeadLetterConfig</a>: <i>
      - <a href="deadletterconfigdefinition.md">DeadLetterConfigDefinition</a></i>
    <a href="#environment" title="Environment">Environment</a>: <i>
      - <a href="environmentdefinition.md">EnvironmentDefinition</a></i>
    <a href="#filesystemconfig" title="FileSystemConfig">FileSystemConfig</a>: <i>
      - <a href="filesystemconfigdefinition.md">FileSystemConfigDefinition</a></i>
    <a href="#imageconfig" title="ImageConfig">ImageConfig</a>: <i>
      - <a href="imageconfigdefinition.md">ImageConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#tracingconfig" title="TracingConfig">TracingConfig</a>: <i>
      - <a href="tracingconfigdefinition.md">TracingConfigDefinition</a></i>
    <a href="#vpcconfig" title="VpcConfig">VpcConfig</a>: <i>
      - <a href="vpcconfigdefinition.md">VpcConfigDefinition</a></i>
</pre>

## Properties

#### CodeSigningConfigArn

To enable code signing for this function, specify the ARN of a code-signing configuration. A code-signing configuration includes a set of signing profiles, which define the trusted publishers for this function.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of what your Lambda Function does.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filename

Path to the function's deployment package within the local filesystem. Conflicts with `image_uri`, `s3_bucket`, `s3_key`, and `s3_object_version`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FunctionName

Unique name for your Lambda Function.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Handler

Function [entrypoint][3] in your code.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageUri

ECR image URI containing the function's deployment package. Conflicts with `filename`, `s3_bucket`, `s3_key`, and `s3_object_version`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyArn

Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key that is used to encrypt environment variables. If this configuration is not provided when environment variables are in use, AWS Lambda uses a default service key. If this configuration is provided when environment variables are not in use, the AWS Lambda API does not save this configuration and Terraform will show a perpetual difference of adding the key. To fix the perpetual difference, remove this configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Layers

List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10].

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemorySize

Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5].

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PackageType

Lambda deployment package type. Valid values are `Zip` and `Image`. Defaults to `Zip`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Publish

Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReservedConcurrentExecutions

Amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency][9].

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

Amazon Resource Name (ARN) of the function's execution role. The role provides the function's identity and access to AWS services and resources.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Runtime

Identifier of the function's runtime. See [Runtimes][6] for valid values.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Bucket

S3 bucket location containing the function's deployment package. Conflicts with `filename` and `image_uri`. This bucket must reside in the same AWS region where you are creating the Lambda function.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Key

S3 key of an object containing the function's deployment package. Conflicts with `filename` and `image_uri`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3ObjectVersion

Object version containing the function's deployment package. Conflicts with `filename` and `image_uri`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceCodeHash

Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `filebase64sha256("file.zip")` (Terraform 0.11.12 and later) or `base64sha256(file("file.zip"))` (Terraform 0.11.11 and earlier), where "file.zip" is the local filename of the lambda function source archive.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Map of tags to assign to the object. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

Amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5].

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeadLetterConfig

_Required_: No

_Type_: List of <a href="deadletterconfigdefinition.md">DeadLetterConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Environment

_Required_: No

_Type_: List of <a href="environmentdefinition.md">EnvironmentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileSystemConfig

_Required_: No

_Type_: List of <a href="filesystemconfigdefinition.md">FileSystemConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageConfig

_Required_: No

_Type_: List of <a href="imageconfigdefinition.md">ImageConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TracingConfig

_Required_: No

_Type_: List of <a href="tracingconfigdefinition.md">TracingConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcConfig

_Required_: No

_Type_: List of <a href="vpcconfigdefinition.md">VpcConfigDefinition</a>

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

#### InvokeArn

Returns the <code>InvokeArn</code> value.

#### LastModified

Returns the <code>LastModified</code> value.

#### QualifiedArn

Returns the <code>QualifiedArn</code> value.

#### SigningJobArn

Returns the <code>SigningJobArn</code> value.

#### SigningProfileVersionArn

Returns the <code>SigningProfileVersionArn</code> value.

#### SourceCodeSize

Returns the <code>SourceCodeSize</code> value.

#### Version

Returns the <code>Version</code> value.

