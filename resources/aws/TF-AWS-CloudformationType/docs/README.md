# TF::AWS::CloudformationType

Manages a version of a CloudFormation Type.

~> **NOTE:** The destroy operation of this resource marks the version as deprecated. If this was the only `LIVE` version, the type is marked as deprecated. It is recommended to enable the [resource `lifecycle` configuration block `create_before_destroy` argument](https://www.terraform.io/docs/configuration/resources.html#create_before_destroy) in this resource configuration to properly order redeployments in Terraform.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::CloudformationType",
    "Properties" : {
        "<a href="#executionrolearn" title="ExecutionRoleArn">ExecutionRoleArn</a>" : <i>String</i>,
        "<a href="#schemahandlerpackage" title="SchemaHandlerPackage">SchemaHandlerPackage</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#typename" title="TypeName">TypeName</a>" : <i>String</i>,
        "<a href="#loggingconfig" title="LoggingConfig">LoggingConfig</a>" : <i>[ <a href="loggingconfigdefinition.md">LoggingConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::CloudformationType
Properties:
    <a href="#executionrolearn" title="ExecutionRoleArn">ExecutionRoleArn</a>: <i>String</i>
    <a href="#schemahandlerpackage" title="SchemaHandlerPackage">SchemaHandlerPackage</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#typename" title="TypeName">TypeName</a>: <i>String</i>
    <a href="#loggingconfig" title="LoggingConfig">LoggingConfig</a>: <i>
      - <a href="loggingconfigdefinition.md">LoggingConfigDefinition</a></i>
</pre>

## Properties

#### ExecutionRoleArn

Amazon Resource Name (ARN) of the IAM Role for CloudFormation to assume when invoking the extension. If your extension calls AWS APIs in any of its handlers, you must create an IAM execution role that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. When CloudFormation needs to invoke the extension handler, CloudFormation assumes this execution role to create a temporary session token, which it then passes to the extension handler, thereby supplying your extension with the appropriate credentials.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SchemaHandlerPackage

URL to the S3 bucket containing the extension project package that contains the necessary files for the extension you want to register. Must begin with `s3://` or `https://`. For example, `s3://example-bucket/example-object`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

CloudFormation Registry Type. For example, `RESOURCE` or `MODULE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TypeName

CloudFormation Type name. For example, `ExampleCompany::ExampleService::ExampleResource`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingConfig

_Required_: No

_Type_: List of <a href="loggingconfigdefinition.md">LoggingConfigDefinition</a>

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

#### DefaultVersionId

Returns the <code>DefaultVersionId</code> value.

#### DeprecatedStatus

Returns the <code>DeprecatedStatus</code> value.

#### Description

Returns the <code>Description</code> value.

#### DocumentationUrl

Returns the <code>DocumentationUrl</code> value.

#### Id

Returns the <code>Id</code> value.

#### IsDefaultVersion

Returns the <code>IsDefaultVersion</code> value.

#### ProvisioningType

Returns the <code>ProvisioningType</code> value.

#### Schema

Returns the <code>Schema</code> value.

#### SourceUrl

Returns the <code>SourceUrl</code> value.

#### TypeArn

Returns the <code>TypeArn</code> value.

#### VersionId

Returns the <code>VersionId</code> value.

#### Visibility

Returns the <code>Visibility</code> value.

