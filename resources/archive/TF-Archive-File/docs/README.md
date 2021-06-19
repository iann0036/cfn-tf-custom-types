# TF::Archive::File

CloudFormation equivalent of archive_file

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Archive::File",
    "Properties" : {
        "<a href="#excludes" title="Excludes">Excludes</a>" : <i>[ String, ... ]</i>,
        "<a href="#outputfilemode" title="OutputFileMode">OutputFileMode</a>" : <i>String</i>,
        "<a href="#outputpath" title="OutputPath">OutputPath</a>" : <i>String</i>,
        "<a href="#sourcecontent" title="SourceContent">SourceContent</a>" : <i>String</i>,
        "<a href="#sourcecontentfilename" title="SourceContentFilename">SourceContentFilename</a>" : <i>String</i>,
        "<a href="#sourcedir" title="SourceDir">SourceDir</a>" : <i>String</i>,
        "<a href="#sourcefile" title="SourceFile">SourceFile</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>[ <a href="sourcedefinition.md">SourceDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Archive::File
Properties:
    <a href="#excludes" title="Excludes">Excludes</a>: <i>
      - String</i>
    <a href="#outputfilemode" title="OutputFileMode">OutputFileMode</a>: <i>String</i>
    <a href="#outputpath" title="OutputPath">OutputPath</a>: <i>String</i>
    <a href="#sourcecontent" title="SourceContent">SourceContent</a>: <i>String</i>
    <a href="#sourcecontentfilename" title="SourceContentFilename">SourceContentFilename</a>: <i>String</i>
    <a href="#sourcedir" title="SourceDir">SourceDir</a>: <i>String</i>
    <a href="#sourcefile" title="SourceFile">SourceFile</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>
      - <a href="sourcedefinition.md">SourceDefinition</a></i>
</pre>

## Properties

#### Excludes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputFileMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputPath

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceContent

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceContentFilename

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDir

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceFile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: List of <a href="sourcedefinition.md">SourceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### OutputBase64sha256

Returns the <code>OutputBase64sha256</code> value.

#### OutputMd5

Returns the <code>OutputMd5</code> value.

#### OutputSha

Returns the <code>OutputSha</code> value.

#### OutputSize

Returns the <code>OutputSize</code> value.

