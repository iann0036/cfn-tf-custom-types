# Terraform::AWS::SsmDocument

Provides an SSM Document resource

~> **NOTE on updating SSM documents:** Only documents with a schema version of 2.0
or greater can update their content once created, see [SSM Schema Features][1]. To update a document with an older
schema version you must recreate the resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::SsmDocument",
    "Properties" : {
        "<a href="#content" title="Content">Content</a>" : <i>String</i>,
        "<a href="#documentformat" title="DocumentFormat">DocumentFormat</a>" : <i>String</i>,
        "<a href="#documenttype" title="DocumentType">DocumentType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#permissions" title="Permissions">Permissions</a>" : <i>[ <a href="permissions.md">Permissions</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#targettype" title="TargetType">TargetType</a>" : <i>String</i>,
        "<a href="#attachmentssource" title="AttachmentsSource">AttachmentsSource</a>" : <i>[ <a href="attachmentssource.md">AttachmentsSource</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::SsmDocument
Properties:
    <a href="#content" title="Content">Content</a>: <i>String</i>
    <a href="#documentformat" title="DocumentFormat">DocumentFormat</a>: <i>String</i>
    <a href="#documenttype" title="DocumentType">DocumentType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#permissions" title="Permissions">Permissions</a>: <i>
      - <a href="permissions.md">Permissions</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#targettype" title="TargetType">TargetType</a>: <i>String</i>
    <a href="#attachmentssource" title="AttachmentsSource">AttachmentsSource</a>: <i>
      - <a href="attachmentssource.md">AttachmentsSource</a></i>
</pre>

## Properties

#### Content

The JSON or YAML content of the document.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DocumentFormat

The format of the document. Valid document types include: `JSON` and `YAML`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DocumentType

The type of the document. Valid document types include: `Automation`, `Command`, `Package`, `Policy`, and `Session`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the document.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permissions

Additional Permissions to attach to the document. See [Permissions](#permissions) below for details.

_Required_: No

_Type_: List of <a href="permissions.md">Permissions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the object.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetType

The target type which defines the kinds of resources the document can run on. For example, /AWS::EC2::Instance. For a list of valid resource types, see AWS Resource Types Reference (http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttachmentsSource

_Required_: No

_Type_: List of <a href="attachmentssource.md">AttachmentsSource</a>

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

#### DefaultVersion

Returns the <code>DefaultVersion</code> value.

#### Description

Returns the <code>Description</code> value.

#### Hash

Returns the <code>Hash</code> value.

#### HashType

Returns the <code>HashType</code> value.

#### Id

Returns the <code>Id</code> value.

#### LatestVersion

Returns the <code>LatestVersion</code> value.

#### Owner

Returns the <code>Owner</code> value.

#### Parameter

Returns the <code>Parameter</code> value.

#### PlatformTypes

Returns the <code>PlatformTypes</code> value.

#### SchemaVersion

Returns the <code>SchemaVersion</code> value.

#### Status

Returns the <code>Status</code> value.

