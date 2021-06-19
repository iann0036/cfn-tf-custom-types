# TF::SumoLogic::CloudtrailSource PathDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bucketname" title="BucketName">BucketName</a>" : <i>String</i>,
    "<a href="#limittonamespaces" title="LimitToNamespaces">LimitToNamespaces</a>" : <i>[ String, ... ]</i>,
    "<a href="#limittoregions" title="LimitToRegions">LimitToRegions</a>" : <i>[ String, ... ]</i>,
    "<a href="#pathexpression" title="PathExpression">PathExpression</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#tagfilters" title="TagFilters">TagFilters</a>" : <i>[ <a href="tagfiltersdefinition.md">TagFiltersDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bucketname" title="BucketName">BucketName</a>: <i>String</i>
<a href="#limittonamespaces" title="LimitToNamespaces">LimitToNamespaces</a>: <i>
      - String</i>
<a href="#limittoregions" title="LimitToRegions">LimitToRegions</a>: <i>
      - String</i>
<a href="#pathexpression" title="PathExpression">PathExpression</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#tagfilters" title="TagFilters">TagFilters</a>: <i>
      - <a href="tagfiltersdefinition.md">TagFiltersDefinition</a></i>
</pre>

## Properties

#### BucketName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitToNamespaces

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitToRegions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathExpression

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagFilters

_Required_: No

_Type_: List of <a href="tagfiltersdefinition.md">TagFiltersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

