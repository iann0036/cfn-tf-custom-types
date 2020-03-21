# Terraform::Google::ComputeRouter Bgp

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#advertisemode" title="AdvertiseMode">AdvertiseMode</a>" : <i>String</i>,
    "<a href="#advertisedgroups" title="AdvertisedGroups">AdvertisedGroups</a>" : <i>[ String, ... ]</i>,
    "<a href="#asn" title="Asn">Asn</a>" : <i>Double</i>,
    "<a href="#advertisedipranges" title="AdvertisedIpRanges">AdvertisedIpRanges</a>" : <i>[ <a href="bgp-advertisedipranges.md">AdvertisedIpRanges</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#advertisemode" title="AdvertiseMode">AdvertiseMode</a>: <i>String</i>
<a href="#advertisedgroups" title="AdvertisedGroups">AdvertisedGroups</a>: <i>
      - String</i>
<a href="#asn" title="Asn">Asn</a>: <i>Double</i>
<a href="#advertisedipranges" title="AdvertisedIpRanges">AdvertisedIpRanges</a>: <i>
      - <a href="bgp-advertisedipranges.md">AdvertisedIpRanges</a></i>
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
_Type_: List of <a href="bgp-advertisedipranges.md">AdvertisedIpRanges</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

