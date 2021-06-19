# TF::Google::DataLossPreventionJobTrigger CloudStorageOptionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#byteslimitperfile" title="BytesLimitPerFile">BytesLimitPerFile</a>" : <i>Double</i>,
    "<a href="#byteslimitperfilepercent" title="BytesLimitPerFilePercent">BytesLimitPerFilePercent</a>" : <i>Double</i>,
    "<a href="#filetypes" title="FileTypes">FileTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#fileslimitpercent" title="FilesLimitPercent">FilesLimitPercent</a>" : <i>Double</i>,
    "<a href="#samplemethod" title="SampleMethod">SampleMethod</a>" : <i>String</i>,
    "<a href="#fileset" title="FileSet">FileSet</a>" : <i>[ <a href="filesetdefinition.md">FileSetDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#byteslimitperfile" title="BytesLimitPerFile">BytesLimitPerFile</a>: <i>Double</i>
<a href="#byteslimitperfilepercent" title="BytesLimitPerFilePercent">BytesLimitPerFilePercent</a>: <i>Double</i>
<a href="#filetypes" title="FileTypes">FileTypes</a>: <i>
      - String</i>
<a href="#fileslimitpercent" title="FilesLimitPercent">FilesLimitPercent</a>: <i>Double</i>
<a href="#samplemethod" title="SampleMethod">SampleMethod</a>: <i>String</i>
<a href="#fileset" title="FileSet">FileSet</a>: <i>
      - <a href="filesetdefinition.md">FileSetDefinition</a></i>
</pre>

## Properties

#### BytesLimitPerFile

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BytesLimitPerFilePercent

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileTypes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilesLimitPercent

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SampleMethod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileSet

_Required_: No

_Type_: List of <a href="filesetdefinition.md">FileSetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

