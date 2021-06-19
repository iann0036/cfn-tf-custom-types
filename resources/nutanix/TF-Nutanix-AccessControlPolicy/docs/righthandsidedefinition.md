# TF::Nutanix::AccessControlPolicy RightHandSideDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#collection" title="Collection">Collection</a>" : <i>String</i>,
    "<a href="#uuidlist" title="UuidList">UuidList</a>" : <i>[ String, ... ]</i>,
    "<a href="#categories" title="Categories">Categories</a>" : <i>[ <a href="categoriesdefinition.md">CategoriesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#collection" title="Collection">Collection</a>: <i>String</i>
<a href="#uuidlist" title="UuidList">UuidList</a>: <i>
      - String</i>
<a href="#categories" title="Categories">Categories</a>: <i>
      - <a href="categoriesdefinition.md">CategoriesDefinition</a></i>
</pre>

## Properties

#### Collection

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UuidList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Categories

_Required_: No

_Type_: List of <a href="categoriesdefinition.md">CategoriesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

