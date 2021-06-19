# TF::CheckPoint::ManagementExport

This command resource allows you to execute Check Point Export.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementExport",
    "Properties" : {
        "<a href="#excludeclasses" title="ExcludeClasses">ExcludeClasses</a>" : <i>[ String, ... ]</i>,
        "<a href="#excludetopics" title="ExcludeTopics">ExcludeTopics</a>" : <i>[ String, ... ]</i>,
        "<a href="#exportfilesbyclass" title="ExportFilesByClass">ExportFilesByClass</a>" : <i>Boolean</i>,
        "<a href="#includeclasses" title="IncludeClasses">IncludeClasses</a>" : <i>[ String, ... ]</i>,
        "<a href="#includetopics" title="IncludeTopics">IncludeTopics</a>" : <i>[ String, ... ]</i>,
        "<a href="#querylimit" title="QueryLimit">QueryLimit</a>" : <i>Double</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementExport
Properties:
    <a href="#excludeclasses" title="ExcludeClasses">ExcludeClasses</a>: <i>
      - String</i>
    <a href="#excludetopics" title="ExcludeTopics">ExcludeTopics</a>: <i>
      - String</i>
    <a href="#exportfilesbyclass" title="ExportFilesByClass">ExportFilesByClass</a>: <i>Boolean</i>
    <a href="#includeclasses" title="IncludeClasses">IncludeClasses</a>: <i>
      - String</i>
    <a href="#includetopics" title="IncludeTopics">IncludeTopics</a>: <i>
      - String</i>
    <a href="#querylimit" title="QueryLimit">QueryLimit</a>: <i>Double</i>
</pre>

## Properties

#### ExcludeClasses

N/Aexclude_classes blocks are documented below.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeTopics

N/Aexclude_topics blocks are documented below.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExportFilesByClass

N/A.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeClasses

N/Ainclude_classes blocks are documented below.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeTopics

N/Ainclude_topics blocks are documented below.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryLimit

N/A.

_Required_: No

_Type_: Double

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

#### TaskId

Asynchronous task unique identifier.

