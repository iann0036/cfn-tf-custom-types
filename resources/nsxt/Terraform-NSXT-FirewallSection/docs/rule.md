# Terraform::NSXT::FirewallSection Rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#destinationsexcluded" title="DestinationsExcluded">DestinationsExcluded</a>" : <i>Boolean</i>,
    "<a href="#direction" title="Direction">Direction</a>" : <i>String</i>,
    "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#ipprotocol" title="IpProtocol">IpProtocol</a>" : <i>String</i>,
    "<a href="#logged" title="Logged">Logged</a>" : <i>Boolean</i>,
    "<a href="#notes" title="Notes">Notes</a>" : <i>String</i>,
    "<a href="#ruletag" title="RuleTag">RuleTag</a>" : <i>String</i>,
    "<a href="#sourcesexcluded" title="SourcesExcluded">SourcesExcluded</a>" : <i>Boolean</i>,
    "<a href="#appliedto" title="AppliedTo">AppliedTo</a>" : <i>[ <a href="rule-appliedto.md">AppliedTo</a>, ... ]</i>,
    "<a href="#destination" title="Destination">Destination</a>" : <i>[ <a href="rule-destination.md">Destination</a>, ... ]</i>,
    "<a href="#service" title="Service">Service</a>" : <i>[ <a href="rule-service.md">Service</a>, ... ]</i>,
    "<a href="#source" title="Source">Source</a>" : <i>[ <a href="rule-source.md">Source</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#destinationsexcluded" title="DestinationsExcluded">DestinationsExcluded</a>: <i>Boolean</i>
<a href="#direction" title="Direction">Direction</a>: <i>String</i>
<a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#ipprotocol" title="IpProtocol">IpProtocol</a>: <i>String</i>
<a href="#logged" title="Logged">Logged</a>: <i>Boolean</i>
<a href="#notes" title="Notes">Notes</a>: <i>String</i>
<a href="#ruletag" title="RuleTag">RuleTag</a>: <i>String</i>
<a href="#sourcesexcluded" title="SourcesExcluded">SourcesExcluded</a>: <i>Boolean</i>
<a href="#appliedto" title="AppliedTo">AppliedTo</a>: <i>
      - <a href="rule-appliedto.md">AppliedTo</a></i>
<a href="#destination" title="Destination">Destination</a>: <i>
      - <a href="rule-destination.md">Destination</a></i>
<a href="#service" title="Service">Service</a>: <i>
      - <a href="rule-service.md">Service</a></i>
<a href="#source" title="Source">Source</a>: <i>
      - <a href="rule-source.md">Source</a></i>
</pre>

## Properties

#### Action

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No
_Type_: String

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

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpProtocol

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

#### RuleTag

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcesExcluded

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppliedTo

_Required_: No
_Type_: List of <a href="rule-appliedto.md">AppliedTo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No
_Type_: List of <a href="rule-destination.md">Destination</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No
_Type_: List of <a href="rule-service.md">Service</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No
_Type_: List of <a href="rule-source.md">Source</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

