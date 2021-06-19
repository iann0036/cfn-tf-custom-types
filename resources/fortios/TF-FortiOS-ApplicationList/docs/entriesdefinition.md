# TF::FortiOS::ApplicationList EntriesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#behavior" title="Behavior">Behavior</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#log" title="Log">Log</a>" : <i>String</i>,
    "<a href="#logpacket" title="LogPacket">LogPacket</a>" : <i>String</i>,
    "<a href="#peripshaper" title="PerIpShaper">PerIpShaper</a>" : <i>String</i>,
    "<a href="#popularity" title="Popularity">Popularity</a>" : <i>String</i>,
    "<a href="#protocols" title="Protocols">Protocols</a>" : <i>String</i>,
    "<a href="#quarantine" title="Quarantine">Quarantine</a>" : <i>String</i>,
    "<a href="#quarantineexpiry" title="QuarantineExpiry">QuarantineExpiry</a>" : <i>String</i>,
    "<a href="#quarantinelog" title="QuarantineLog">QuarantineLog</a>" : <i>String</i>,
    "<a href="#ratecount" title="RateCount">RateCount</a>" : <i>Double</i>,
    "<a href="#rateduration" title="RateDuration">RateDuration</a>" : <i>Double</i>,
    "<a href="#ratemode" title="RateMode">RateMode</a>" : <i>String</i>,
    "<a href="#ratetrack" title="RateTrack">RateTrack</a>" : <i>String</i>,
    "<a href="#sessionttl" title="SessionTtl">SessionTtl</a>" : <i>Double</i>,
    "<a href="#shaper" title="Shaper">Shaper</a>" : <i>String</i>,
    "<a href="#shaperreverse" title="ShaperReverse">ShaperReverse</a>" : <i>String</i>,
    "<a href="#technology" title="Technology">Technology</a>" : <i>String</i>,
    "<a href="#vendor" title="Vendor">Vendor</a>" : <i>String</i>,
    "<a href="#application" title="Application">Application</a>" : <i>[ <a href="applicationdefinition.md">ApplicationDefinition</a>, ... ]</i>,
    "<a href="#category" title="Category">Category</a>" : <i>[ <a href="categorydefinition.md">CategoryDefinition</a>, ... ]</i>,
    "<a href="#exclusion" title="Exclusion">Exclusion</a>" : <i>[ <a href="exclusiondefinition.md">ExclusionDefinition</a>, ... ]</i>,
    "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="parametersdefinition.md">ParametersDefinition</a>, ... ]</i>,
    "<a href="#risk" title="Risk">Risk</a>" : <i>[ <a href="riskdefinition.md">RiskDefinition</a>, ... ]</i>,
    "<a href="#subcategory" title="SubCategory">SubCategory</a>" : <i>[ <a href="subcategorydefinition.md">SubCategoryDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#behavior" title="Behavior">Behavior</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#log" title="Log">Log</a>: <i>String</i>
<a href="#logpacket" title="LogPacket">LogPacket</a>: <i>String</i>
<a href="#peripshaper" title="PerIpShaper">PerIpShaper</a>: <i>String</i>
<a href="#popularity" title="Popularity">Popularity</a>: <i>String</i>
<a href="#protocols" title="Protocols">Protocols</a>: <i>String</i>
<a href="#quarantine" title="Quarantine">Quarantine</a>: <i>String</i>
<a href="#quarantineexpiry" title="QuarantineExpiry">QuarantineExpiry</a>: <i>String</i>
<a href="#quarantinelog" title="QuarantineLog">QuarantineLog</a>: <i>String</i>
<a href="#ratecount" title="RateCount">RateCount</a>: <i>Double</i>
<a href="#rateduration" title="RateDuration">RateDuration</a>: <i>Double</i>
<a href="#ratemode" title="RateMode">RateMode</a>: <i>String</i>
<a href="#ratetrack" title="RateTrack">RateTrack</a>: <i>String</i>
<a href="#sessionttl" title="SessionTtl">SessionTtl</a>: <i>Double</i>
<a href="#shaper" title="Shaper">Shaper</a>: <i>String</i>
<a href="#shaperreverse" title="ShaperReverse">ShaperReverse</a>: <i>String</i>
<a href="#technology" title="Technology">Technology</a>: <i>String</i>
<a href="#vendor" title="Vendor">Vendor</a>: <i>String</i>
<a href="#application" title="Application">Application</a>: <i>
      - <a href="applicationdefinition.md">ApplicationDefinition</a></i>
<a href="#category" title="Category">Category</a>: <i>
      - <a href="categorydefinition.md">CategoryDefinition</a></i>
<a href="#exclusion" title="Exclusion">Exclusion</a>: <i>
      - <a href="exclusiondefinition.md">ExclusionDefinition</a></i>
<a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="parametersdefinition.md">ParametersDefinition</a></i>
<a href="#risk" title="Risk">Risk</a>: <i>
      - <a href="riskdefinition.md">RiskDefinition</a></i>
<a href="#subcategory" title="SubCategory">SubCategory</a>: <i>
      - <a href="subcategorydefinition.md">SubCategoryDefinition</a></i>
</pre>

## Properties

#### Action

Pass or block traffic, or reset connection for traffic from this application. Valid values: `pass`, `block`, `reset`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Behavior

Application behavior filter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Entry ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Log

Enable/disable logging for this application list. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogPacket

Enable/disable packet logging. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PerIpShaper

Per-IP traffic shaper.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Popularity

Application popularity filter (1 - 5, from least to most popular). Valid values: `1`, `2`, `3`, `4`, `5`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocols

Application protocol filter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Quarantine

Quarantine method. Valid values: `none`, `attacker`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuarantineExpiry

Duration of quarantine. (Format ###d##h##m, minimum 1m, maximum 364d23h59m, default = 5m). Requires quarantine set to attacker.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuarantineLog

Enable/disable quarantine logging. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateCount

Count of the rate.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateDuration

Duration (sec) of the rate.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateMode

Rate limit mode. Valid values: `periodical`, `continuous`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateTrack

Track the packet protocol field. Valid values: `none`, `src-ip`, `dest-ip`, `dhcp-client-mac`, `dns-domain`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionTtl

Session TTL (0 = default).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shaper

Traffic shaper.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShaperReverse

Reverse traffic shaper.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Technology

Application technology filter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vendor

Application vendor filter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Application

_Required_: No

_Type_: List of <a href="applicationdefinition.md">ApplicationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Category

_Required_: No

_Type_: List of <a href="categorydefinition.md">CategoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exclusion

_Required_: No

_Type_: List of <a href="exclusiondefinition.md">ExclusionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

_Required_: No

_Type_: List of <a href="parametersdefinition.md">ParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Risk

_Required_: No

_Type_: List of <a href="riskdefinition.md">RiskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubCategory

_Required_: No

_Type_: List of <a href="subcategorydefinition.md">SubCategoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

