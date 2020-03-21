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
    "<a href="#appliedto" title="AppliedTo">AppliedTo</a>" : <i>[ &lt;a href=&#34;rule-appliedto.md&#34;&gt;AppliedTo&lt;/a&gt;, ... ]</i>,
    "<a href="#destination" title="Destination">Destination</a>" : <i>[ &lt;a href=&#34;rule-destination.md&#34;&gt;Destination&lt;/a&gt;, ... ]</i>,
    "<a href="#service" title="Service">Service</a>" : <i>[ &lt;a href=&#34;rule-service.md&#34;&gt;Service&lt;/a&gt;, ... ]</i>,
    "<a href="#source" title="Source">Source</a>" : <i>[ &lt;a href=&#34;rule-source.md&#34;&gt;Source&lt;/a&gt;, ... ]</i>
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
      - &lt;a href=&#34;rule-appliedto.md&#34;&gt;AppliedTo&lt;/a&gt;</i>
<a href="#destination" title="Destination">Destination</a>: <i>
      - &lt;a href=&#34;rule-destination.md&#34;&gt;Destination&lt;/a&gt;</i>
<a href="#service" title="Service">Service</a>: <i>
      - &lt;a href=&#34;rule-service.md&#34;&gt;Service&lt;/a&gt;</i>
<a href="#source" title="Source">Source</a>: <i>
      - &lt;a href=&#34;rule-source.md&#34;&gt;Source&lt;/a&gt;</i>
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
_Type_: List of &lt;a href=&#34;rule-appliedto.md&#34;&gt;AppliedTo&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No
_Type_: List of &lt;a href=&#34;rule-destination.md&#34;&gt;Destination&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No
_Type_: List of &lt;a href=&#34;rule-service.md&#34;&gt;Service&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No
_Type_: List of &lt;a href=&#34;rule-source.md&#34;&gt;Source&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

