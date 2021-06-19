# TF::Google::StorageBucket WebsiteDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#mainpagesuffix" title="MainPageSuffix">MainPageSuffix</a>" : <i>String</i>,
    "<a href="#notfoundpage" title="NotFoundPage">NotFoundPage</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#mainpagesuffix" title="MainPageSuffix">MainPageSuffix</a>: <i>String</i>
<a href="#notfoundpage" title="NotFoundPage">NotFoundPage</a>: <i>String</i>
</pre>

## Properties

#### MainPageSuffix

Behaves as the bucket's directory index where
missing objects are treated as potential directories.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotFoundPage

The custom object to return when a requested
resource is not found.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

