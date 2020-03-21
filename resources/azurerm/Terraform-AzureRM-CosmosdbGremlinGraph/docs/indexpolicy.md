# Terraform::AzureRM::CosmosdbGremlinGraph IndexPolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#automatic" title="Automatic">Automatic</a>" : <i>Boolean</i>,
    "<a href="#excludedpaths" title="ExcludedPaths">ExcludedPaths</a>" : <i>[ String, ... ]</i>,
    "<a href="#includedpaths" title="IncludedPaths">IncludedPaths</a>" : <i>[ String, ... ]</i>,
    "<a href="#indexingmode" title="IndexingMode">IndexingMode</a>" : <i>String</i>
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
</pre>

## Properties

#### Automatic

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludedPaths

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludedPaths

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndexingMode

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

