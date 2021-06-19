# TF::FortiOS::Logsyslogd3Overridefilter FreeStyleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#category" title="Category">Category</a>" : <i>String</i>,
    "<a href="#filter" title="Filter">Filter</a>" : <i>String</i>,
    "<a href="#filtertype" title="FilterType">FilterType</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#category" title="Category">Category</a>: <i>String</i>
<a href="#filter" title="Filter">Filter</a>: <i>String</i>
<a href="#filtertype" title="FilterType">FilterType</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
</pre>

## Properties

#### Category

Log category. Valid values: `traffic`, `event`, `virus`, `webfilter`, `attack`, `spam`, `anomaly`, `voip`, `dlp`, `app-ctrl`, `waf`, `gtp`, `dns`, `ssh`, `ssl`, `file-filter`, `icap`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

Free style filter string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterType

Include/exclude logs that match the filter. Valid values: `include`, `exclude`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Entry ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

