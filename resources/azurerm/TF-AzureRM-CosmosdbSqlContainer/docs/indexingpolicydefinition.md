# TF::AzureRM::CosmosdbSqlContainer IndexingPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#indexingmode" title="IndexingMode">IndexingMode</a>" : <i>String</i>,
    "<a href="#compositeindex" title="CompositeIndex">CompositeIndex</a>" : <i>[ <a href="compositeindexdefinition.md">CompositeIndexDefinition</a>, ... ]</i>,
    "<a href="#excludedpath" title="ExcludedPath">ExcludedPath</a>" : <i>[ <a href="excludedpathdefinition.md">ExcludedPathDefinition</a>, ... ]</i>,
    "<a href="#includedpath" title="IncludedPath">IncludedPath</a>" : <i>[ <a href="includedpathdefinition.md">IncludedPathDefinition</a>, ... ]</i>,
    "<a href="#spatialindex" title="SpatialIndex">SpatialIndex</a>" : <i>[ <a href="spatialindexdefinition.md">SpatialIndexDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#indexingmode" title="IndexingMode">IndexingMode</a>: <i>String</i>
<a href="#compositeindex" title="CompositeIndex">CompositeIndex</a>: <i>
      - <a href="compositeindexdefinition.md">CompositeIndexDefinition</a></i>
<a href="#excludedpath" title="ExcludedPath">ExcludedPath</a>: <i>
      - <a href="excludedpathdefinition.md">ExcludedPathDefinition</a></i>
<a href="#includedpath" title="IncludedPath">IncludedPath</a>: <i>
      - <a href="includedpathdefinition.md">IncludedPathDefinition</a></i>
<a href="#spatialindex" title="SpatialIndex">SpatialIndex</a>: <i>
      - <a href="spatialindexdefinition.md">SpatialIndexDefinition</a></i>
</pre>

## Properties

#### IndexingMode

Indicates the indexing mode. Possible values include: `Consistent` and `None`. Defaults to `Consistent`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompositeIndex

_Required_: No

_Type_: List of <a href="compositeindexdefinition.md">CompositeIndexDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludedPath

_Required_: No

_Type_: List of <a href="excludedpathdefinition.md">ExcludedPathDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludedPath

_Required_: No

_Type_: List of <a href="includedpathdefinition.md">IncludedPathDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpatialIndex

_Required_: No

_Type_: List of <a href="spatialindexdefinition.md">SpatialIndexDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

