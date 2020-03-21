# Terraform::AWS::LambdaFunction

CloudFormation equivalent of aws_lambda_function

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::LambdaFunction",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#filename" title="Filename">Filename</a>" : <i>String</i>,
        "<a href="#functionname" title="FunctionName">FunctionName</a>" : <i>String</i>,
        "<a href="#handler" title="Handler">Handler</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#kmskeyarn" title="KmsKeyArn">KmsKeyArn</a>" : <i>String</i>,
        "<a href="#layers" title="Layers">Layers</a>" : <i>[ String, ... ]</i>,
        "<a href="#memorysize" title="MemorySize">MemorySize</a>" : <i>Double</i>,
        "<a href="#publish" title="Publish">Publish</a>" : <i>Boolean</i>,
        "<a href="#reservedconcurrentexecutions" title="ReservedConcurrentExecutions">ReservedConcurrentExecutions</a>" : <i>Double</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#runtime" title="Runtime">Runtime</a>" : <i>String</i>,
        "<a href="#s3bucket" title="S3Bucket">S3Bucket</a>" : <i>String</i>,
        "<a href="#s3key" title="S3Key">S3Key</a>" : <i>String</i>,
        "<a href="#s3objectversion" title="S3ObjectVersion">S3ObjectVersion</a>" : <i>String</i>,
        "<a href="#sourcecodehash" title="SourceCodeHash">SourceCodeHash</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
        "<a href="#deadletterconfig" title="DeadLetterConfig">DeadLetterConfig</a>" : <i>[ &lt;a href=&#34;deadletterconfig.md&#34;&gt;DeadLetterConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#environment" title="Environment">Environment</a>" : <i>[ &lt;a href=&#34;environment.md&#34;&gt;Environment&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#tracingconfig" title="TracingConfig">TracingConfig</a>" : <i>[ &lt;a href=&#34;tracingconfig.md&#34;&gt;TracingConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#vpcconfig" title="VpcConfig">VpcConfig</a>" : <i>[ &lt;a href=&#34;vpcconfig.md&#34;&gt;VpcConfig&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::LambdaFunction
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#filename" title="Filename">Filename</a>: <i>String</i>
    <a href="#functionname" title="FunctionName">FunctionName</a>: <i>String</i>
    <a href="#handler" title="Handler">Handler</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#kmskeyarn" title="KmsKeyArn">KmsKeyArn</a>: <i>String</i>
    <a href="#layers" title="Layers">Layers</a>: <i>
      - String</i>
    <a href="#memorysize" title="MemorySize">MemorySize</a>: <i>Double</i>
    <a href="#publish" title="Publish">Publish</a>: <i>Boolean</i>
    <a href="#reservedconcurrentexecutions" title="ReservedConcurrentExecutions">ReservedConcurrentExecutions</a>: <i>Double</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#runtime" title="Runtime">Runtime</a>: <i>String</i>
    <a href="#s3bucket" title="S3Bucket">S3Bucket</a>: <i>String</i>
    <a href="#s3key" title="S3Key">S3Key</a>: <i>String</i>
    <a href="#s3objectversion" title="S3ObjectVersion">S3ObjectVersion</a>: <i>String</i>
    <a href="#sourcecodehash" title="SourceCodeHash">SourceCodeHash</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
    <a href="#deadletterconfig" title="DeadLetterConfig">DeadLetterConfig</a>: <i>
      - &lt;a href=&#34;deadletterconfig.md&#34;&gt;DeadLetterConfig&lt;/a&gt;</i>
    <a href="#environment" title="Environment">Environment</a>: <i>
      - &lt;a href=&#34;environment.md&#34;&gt;Environment&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#tracingconfig" title="TracingConfig">TracingConfig</a>: <i>
      - &lt;a href=&#34;tracingconfig.md&#34;&gt;TracingConfig&lt;/a&gt;</i>
    <a href="#vpcconfig" title="VpcConfig">VpcConfig</a>: <i>
      - &lt;a href=&#34;vpcconfig.md&#34;&gt;VpcConfig&lt;/a&gt;</i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filename

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FunctionName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Handler

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Layers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemorySize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Publish

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReservedConcurrentExecutions

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Runtime

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Bucket

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Key

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3ObjectVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceCodeHash

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeadLetterConfig

_Required_: No

_Type_: List of &lt;a href=&#34;deadletterconfig.md&#34;&gt;DeadLetterConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Environment

_Required_: No

_Type_: List of &lt;a href=&#34;environment.md&#34;&gt;Environment&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TracingConfig

_Required_: No

_Type_: List of &lt;a href=&#34;tracingconfig.md&#34;&gt;TracingConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcConfig

_Required_: No

_Type_: List of &lt;a href=&#34;vpcconfig.md&#34;&gt;VpcConfig&lt;/a&gt;

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

#### InvokeArn

Returns the &lt;code&gt;InvokeArn&lt;/code&gt; value.

#### LastModified

Returns the &lt;code&gt;LastModified&lt;/code&gt; value.

#### QualifiedArn

Returns the &lt;code&gt;QualifiedArn&lt;/code&gt; value.

#### SourceCodeSize

Returns the &lt;code&gt;SourceCodeSize&lt;/code&gt; value.

#### Version

Returns the &lt;code&gt;Version&lt;/code&gt; value.

