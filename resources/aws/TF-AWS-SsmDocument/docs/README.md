# TF::AWS::SsmDocument

Provides an SSM Document resource

~> **NOTE on updating SSM documents:** Only documents with a schema version of 2.0
or greater can update their content once created, see [SSM Schema Features][1]. To update a document with an older
schema version you must recreate the resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::SsmDocument",
    "Properties" : {
        "<a href="#content" title="Content">Content</a>" : <i>String</i>,
        "<a href="#documentformat" title="DocumentFormat">DocumentFormat</a>" : <i>String</i>,
        "<a href="#documenttype" title="DocumentType">DocumentType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#permissions" title="Permissions">Permissions</a>" : <i>[ <a href="permissionsdefinition.md">PermissionsDefinition</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#targettype" title="TargetType">TargetType</a>" : <i>String</i>,
        "<a href="#versionname" title="VersionName">VersionName</a>" : <i>String</i>,
        "<a href="#attachmentssource" title="AttachmentsSource">AttachmentsSource</a>" : <i>[ <a href="attachmentssourcedefinition.md">AttachmentsSourceDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::SsmDocument
Properties:
    <a href="#content" title="Content">Content</a>: <i>String</i>
    <a href="#documentformat" title="DocumentFormat">DocumentFormat</a>: <i>String</i>
    <a href="#documenttype" title="DocumentType">DocumentType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#permissions" title="Permissions">Permissions</a>: <i>
      - <a href="permissionsdefinition.md">PermissionsDefinition</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#targettype" title="TargetType">TargetType</a>: <i>String</i>
    <a href="#versionname" title="VersionName">VersionName</a>: <i>String</i>
    <a href="#attachmentssource" title="AttachmentsSource">AttachmentsSource</a>: <i>
      - <a href="attachmentssourcedefinition.md">AttachmentsSourceDefinition</a></i>
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

_Type_: List of <a href="permissionsdefinition.md">PermissionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the object. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetType

The target type which defines the kinds of resources the document can run on. For example, /AWS::EC2::Instance. For a list of valid resource types, see AWS Resource Types Reference (http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionName

A field specifying the version of the artifact you are creating with the document. For example, "Release 12, Update 6". This value is unique across all versions of a document and cannot be changed for an existing document version.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttachmentsSource

_Required_: No

_Type_: List of <a href="attachmentssourcedefinition.md">AttachmentsSourceDefinition</a>

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

#### DocumentVersion

Returns the <code>DocumentVersion</code> value.

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

