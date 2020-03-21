# Terraform::Google::ComputeRouter Bgp

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#advertisemode" title="AdvertiseMode">AdvertiseMode</a>" : <i>String</i>,
    "<a href="#advertisedgroups" title="AdvertisedGroups">AdvertisedGroups</a>" : <i>[ String, ... ]</i>,
    "<a href="#asn" title="Asn">Asn</a>" : <i>Double</i>,
    "<a href="#advertisedipranges" title="AdvertisedIpRanges">AdvertisedIpRanges</a>" : <i>[ &lt;a href=&#34;bgp-advertisedipranges.md&#34;&gt;AdvertisedIpRanges&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#advertisemode" title="AdvertiseMode">AdvertiseMode</a>: <i>String</i>
<a href="#advertisedgroups" title="AdvertisedGroups">AdvertisedGroups</a>: <i>
      - String</i>
<a href="#asn" title="Asn">Asn</a>: <i>Double</i>
<a href="#advertisedipranges" title="AdvertisedIpRanges">AdvertisedIpRanges</a>: <i>
      - &lt;a href=&#34;bgp-advertisedipranges.md&#34;&gt;AdvertisedIpRanges&lt;/a&gt;</i>
</pre>

## Properties

#### AdvertiseMode

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertisedGroups

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Asn

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvertisedIpRanges

_Required_: No
_Type_: List of &lt;a href=&#34;bgp-advertisedipranges.md&#34;&gt;AdvertisedIpRanges&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

