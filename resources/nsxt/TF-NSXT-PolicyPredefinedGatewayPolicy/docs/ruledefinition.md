# TF::NSXT::PolicyPredefinedGatewayPolicy RuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#destinationgroups" title="DestinationGroups">DestinationGroups</a>" : <i>[ String, ... ]</i>,
    "<a href="#destinationsexcluded" title="DestinationsExcluded">DestinationsExcluded</a>" : <i>Boolean</i>,
    "<a href="#direction" title="Direction">Direction</a>" : <i>String</i>,
    "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#ipversion" title="IpVersion">IpVersion</a>" : <i>String</i>,
    "<a href="#loglabel" title="LogLabel">LogLabel</a>" : <i>String</i>,
    "<a href="#logged" title="Logged">Logged</a>" : <i>Boolean</i>,
    "<a href="#notes" title="Notes">Notes</a>" : <i>String</i>,
    "<a href="#nsxid" title="NsxId">NsxId</a>" : <i>String</i>,
    "<a href="#profiles" title="Profiles">Profiles</a>" : <i>[ String, ... ]</i>,
    "<a href="#scope" title="Scope">Scope</a>" : <i>[ String, ... ]</i>,
    "<a href="#sequencenumber" title="SequenceNumber">SequenceNumber</a>" : <i>Double</i>,
    "<a href="#services" title="Services">Services</a>" : <i>[ String, ... ]</i>,
    "<a href="#sourcegroups" title="SourceGroups">SourceGroups</a>" : <i>[ String, ... ]</i>,
    "<a href="#sourcesexcluded" title="SourcesExcluded">SourcesExcluded</a>" : <i>Boolean</i>,
    "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#destinationgroups" title="DestinationGroups">DestinationGroups</a>: <i>
      - String</i>
<a href="#destinationsexcluded" title="DestinationsExcluded">DestinationsExcluded</a>: <i>Boolean</i>
<a href="#direction" title="Direction">Direction</a>: <i>String</i>
<a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#ipversion" title="IpVersion">IpVersion</a>: <i>String</i>
<a href="#loglabel" title="LogLabel">LogLabel</a>: <i>String</i>
<a href="#logged" title="Logged">Logged</a>: <i>Boolean</i>
<a href="#notes" title="Notes">Notes</a>: <i>String</i>
<a href="#nsxid" title="NsxId">NsxId</a>: <i>String</i>
<a href="#profiles" title="Profiles">Profiles</a>: <i>
      - String</i>
<a href="#scope" title="Scope">Scope</a>: <i>
      - String</i>
<a href="#sequencenumber" title="SequenceNumber">SequenceNumber</a>: <i>Double</i>
<a href="#services" title="Services">Services</a>: <i>
      - String</i>
<a href="#sourcegroups" title="SourceGroups">SourceGroups</a>: <i>
      - String</i>
<a href="#sourcesexcluded" title="SourcesExcluded">SourcesExcluded</a>: <i>Boolean</i>
<a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### Action

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationsExcluded

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Direction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogLabel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logged

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Profiles

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SequenceNumber

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Services

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcesExcluded

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

