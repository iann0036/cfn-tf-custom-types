# TF::AzureRM::CosmosdbGremlinGraph IndexPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#automatic" title="Automatic">Automatic</a>" : <i>Boolean</i>,
    "<a href="#excludedpaths" title="ExcludedPaths">ExcludedPaths</a>" : <i>[ String, ... ]</i>,
    "<a href="#includedpaths" title="IncludedPaths">IncludedPaths</a>" : <i>[ String, ... ]</i>,
    "<a href="#indexingmode" title="IndexingMode">IndexingMode</a>" : <i>String</i>,
    "<a href="#compositeindex" title="CompositeIndex">CompositeIndex</a>" : <i>[ <a href="compositeindexdefinition.md">CompositeIndexDefinition</a>, ... ]</i>,
    "<a href="#spatialindex" title="SpatialIndex">SpatialIndex</a>" : <i>[ <a href="spatialindexdefinition.md">SpatialIndexDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#automatic" title="Automatic">Automatic</a>: <i>Boolean</i>
<a href="#excludedpaths" title="ExcludedPaths">ExcludedPaths</a>: <i>
      - String</i>
<a href="#includedpaths" title="IncludedPaths">IncludedPaths</a>: <i>
      - String</i>
<a href="#indexingmode" title="IndexingMode">IndexingMode</a>: <i>String</i>
<a href="#compositeindex" title="CompositeIndex">CompositeIndex</a>: <i>
      - <a href="compositeindexdefinition.md">CompositeIndexDefinition</a></i>
<a href="#spatialindex" title="SpatialIndex">SpatialIndex</a>: <i>
      - <a href="spatialindexdefinition.md">SpatialIndexDefinition</a></i>
</pre>

## Properties

#### Automatic

Indicates if the indexing policy is automatic. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludedPaths

List of paths to exclude from indexing. Required if `indexing_mode` is `Consistent` or `Lazy`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludedPaths

List of paths to include in the indexing. Required if `indexing_mode` is `Consistent` or `Lazy`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndexingMode

Indicates the indexing mode. Possible values include: `Consistent`, `Lazy`, `None`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompositeIndex

_Required_: No

_Type_: List of <a href="compositeindexdefinition.md">CompositeIndexDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpatialIndex

_Required_: No

_Type_: List of <a href="spatialindexdefinition.md">SpatialIndexDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

