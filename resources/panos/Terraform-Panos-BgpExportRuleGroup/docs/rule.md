# Terraform::Panos::BgpExportRuleGroup Rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#aspathlimit" title="AsPathLimit">AsPathLimit</a>" : <i>Double</i>,
    "<a href="#aspathtype" title="AsPathType">AsPathType</a>" : <i>String</i>,
    "<a href="#aspathvalue" title="AsPathValue">AsPathValue</a>" : <i>String</i>,
    "<a href="#communitytype" title="CommunityType">CommunityType</a>" : <i>String</i>,
    "<a href="#communityvalue" title="CommunityValue">CommunityValue</a>" : <i>String</i>,
    "<a href="#enable" title="Enable">Enable</a>" : <i>Boolean</i>,
    "<a href="#extendedcommunitytype" title="ExtendedCommunityType">ExtendedCommunityType</a>" : <i>String</i>,
    "<a href="#extendedcommunityvalue" title="ExtendedCommunityValue">ExtendedCommunityValue</a>" : <i>String</i>,
    "<a href="#localpreference" title="LocalPreference">LocalPreference</a>" : <i>String</i>,
    "<a href="#matchaspathregex" title="MatchAsPathRegex">MatchAsPathRegex</a>" : <i>String</i>,
    "<a href="#matchcommunityregex" title="MatchCommunityRegex">MatchCommunityRegex</a>" : <i>String</i>,
    "<a href="#matchextendedcommunityregex" title="MatchExtendedCommunityRegex">MatchExtendedCommunityRegex</a>" : <i>String</i>,
    "<a href="#matchfrompeers" title="MatchFromPeers">MatchFromPeers</a>" : <i>[ String, ... ]</i>,
    "<a href="#matchmed" title="MatchMed">MatchMed</a>" : <i>String</i>,
    "<a href="#matchnexthops" title="MatchNextHops">MatchNextHops</a>" : <i>[ String, ... ]</i>,
    "<a href="#matchroutetable" title="MatchRouteTable">MatchRouteTable</a>" : <i>String</i>,
    "<a href="#med" title="Med">Med</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#nexthop" title="NextHop">NextHop</a>" : <i>String</i>,
    "<a href="#origin" title="Origin">Origin</a>" : <i>String</i>,
    "<a href="#usedby" title="UsedBy">UsedBy</a>" : <i>[ String, ... ]</i>,
    "<a href="#matchaddressprefix" title="MatchAddressPrefix">MatchAddressPrefix</a>" : <i>[ &lt;a href=&#34;rule-matchaddressprefix.md&#34;&gt;MatchAddressPrefix&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#aspathlimit" title="AsPathLimit">AsPathLimit</a>: <i>Double</i>
<a href="#aspathtype" title="AsPathType">AsPathType</a>: <i>String</i>
<a href="#aspathvalue" title="AsPathValue">AsPathValue</a>: <i>String</i>
<a href="#communitytype" title="CommunityType">CommunityType</a>: <i>String</i>
<a href="#communityvalue" title="CommunityValue">CommunityValue</a>: <i>String</i>
<a href="#enable" title="Enable">Enable</a>: <i>Boolean</i>
<a href="#extendedcommunitytype" title="ExtendedCommunityType">ExtendedCommunityType</a>: <i>String</i>
<a href="#extendedcommunityvalue" title="ExtendedCommunityValue">ExtendedCommunityValue</a>: <i>String</i>
<a href="#localpreference" title="LocalPreference">LocalPreference</a>: <i>String</i>
<a href="#matchaspathregex" title="MatchAsPathRegex">MatchAsPathRegex</a>: <i>String</i>
<a href="#matchcommunityregex" title="MatchCommunityRegex">MatchCommunityRegex</a>: <i>String</i>
<a href="#matchextendedcommunityregex" title="MatchExtendedCommunityRegex">MatchExtendedCommunityRegex</a>: <i>String</i>
<a href="#matchfrompeers" title="MatchFromPeers">MatchFromPeers</a>: <i>
      - String</i>
<a href="#matchmed" title="MatchMed">MatchMed</a>: <i>String</i>
<a href="#matchnexthops" title="MatchNextHops">MatchNextHops</a>: <i>
      - String</i>
<a href="#matchroutetable" title="MatchRouteTable">MatchRouteTable</a>: <i>String</i>
<a href="#med" title="Med">Med</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#nexthop" title="NextHop">NextHop</a>: <i>String</i>
<a href="#origin" title="Origin">Origin</a>: <i>String</i>
<a href="#usedby" title="UsedBy">UsedBy</a>: <i>
      - String</i>
<a href="#matchaddressprefix" title="MatchAddressPrefix">MatchAddressPrefix</a>: <i>
      - &lt;a href=&#34;rule-matchaddressprefix.md&#34;&gt;MatchAddressPrefix&lt;/a&gt;</i>
</pre>

## Properties

#### Action

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsPathLimit

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsPathType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsPathValue

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommunityType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommunityValue

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enable

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedCommunityType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedCommunityValue

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalPreference

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchAsPathRegex

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchCommunityRegex

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchExtendedCommunityRegex

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchFromPeers

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchMed

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchNextHops

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchRouteTable

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Med

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHop

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Origin

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsedBy

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchAddressPrefix

_Required_: No
_Type_: List of &lt;a href=&#34;rule-matchaddressprefix.md&#34;&gt;MatchAddressPrefix&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

