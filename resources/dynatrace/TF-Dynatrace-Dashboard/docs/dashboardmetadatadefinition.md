# TF::Dynatrace::Dashboard DashboardMetadataDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#owner" title="Owner">Owner</a>" : <i>String</i>,
    "<a href="#shared" title="Shared">Shared</a>" : <i>Boolean</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>,
    "<a href="#validfilterkeys" title="ValidFilterKeys">ValidFilterKeys</a>" : <i>[ String, ... ]</i>,
    "<a href="#dynamicfilters" title="DynamicFilters">DynamicFilters</a>" : <i>[ <a href="dynamicfiltersdefinition.md">DynamicFiltersDefinition</a>, ... ]</i>,
    "<a href="#filter" title="Filter">Filter</a>" : <i>[ <a href="filterdefinition.md">FilterDefinition</a>, ... ]</i>,
    "<a href="#sharingdetails" title="SharingDetails">SharingDetails</a>" : <i>[ <a href="sharingdetailsdefinition.md">SharingDetailsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#owner" title="Owner">Owner</a>: <i>String</i>
<a href="#shared" title="Shared">Shared</a>: <i>Boolean</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
<a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
<a href="#validfilterkeys" title="ValidFilterKeys">ValidFilterKeys</a>: <i>
      - String</i>
<a href="#dynamicfilters" title="DynamicFilters">DynamicFilters</a>: <i>
      - <a href="dynamicfiltersdefinition.md">DynamicFiltersDefinition</a></i>
<a href="#filter" title="Filter">Filter</a>: <i>
      - <a href="filterdefinition.md">FilterDefinition</a></i>
<a href="#sharingdetails" title="SharingDetails">SharingDetails</a>: <i>
      - <a href="sharingdetailsdefinition.md">SharingDetailsDefinition</a></i>
</pre>

## Properties

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owner

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shared

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidFilterKeys

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicFilters

_Required_: No

_Type_: List of <a href="dynamicfiltersdefinition.md">DynamicFiltersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: List of <a href="filterdefinition.md">FilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharingDetails

_Required_: No

_Type_: List of <a href="sharingdetailsdefinition.md">SharingDetailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

