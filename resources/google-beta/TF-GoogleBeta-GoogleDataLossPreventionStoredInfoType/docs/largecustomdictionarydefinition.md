# TF::GoogleBeta::GoogleDataLossPreventionStoredInfoType LargeCustomDictionaryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bigqueryfield" title="BigQueryField">BigQueryField</a>" : <i>[ <a href="bigqueryfielddefinition.md">BigQueryFieldDefinition</a>, ... ]</i>,
    "<a href="#cloudstoragefileset" title="CloudStorageFileSet">CloudStorageFileSet</a>" : <i>[ <a href="cloudstoragefilesetdefinition.md">CloudStorageFileSetDefinition</a>, ... ]</i>,
    "<a href="#outputpath" title="OutputPath">OutputPath</a>" : <i>[ <a href="outputpathdefinition.md">OutputPathDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bigqueryfield" title="BigQueryField">BigQueryField</a>: <i>
      - <a href="bigqueryfielddefinition.md">BigQueryFieldDefinition</a></i>
<a href="#cloudstoragefileset" title="CloudStorageFileSet">CloudStorageFileSet</a>: <i>
      - <a href="cloudstoragefilesetdefinition.md">CloudStorageFileSetDefinition</a></i>
<a href="#outputpath" title="OutputPath">OutputPath</a>: <i>
      - <a href="outputpathdefinition.md">OutputPathDefinition</a></i>
</pre>

## Properties

#### BigQueryField

_Required_: No

_Type_: List of <a href="bigqueryfielddefinition.md">BigQueryFieldDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudStorageFileSet

_Required_: No

_Type_: List of <a href="cloudstoragefilesetdefinition.md">CloudStorageFileSetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputPath

_Required_: No

_Type_: List of <a href="outputpathdefinition.md">OutputPathDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

