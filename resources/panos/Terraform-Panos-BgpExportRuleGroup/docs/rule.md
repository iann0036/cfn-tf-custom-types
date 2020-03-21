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
    "<a href="#matchaddressprefix" title="MatchAddressPrefix">MatchAddressPrefix</a>" : <i>[ <a href="rule-matchaddressprefix.md">MatchAddressPrefix</a>, ... ]</i>
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
      - <a href="rule-matchaddressprefix.md">MatchAddressPrefix</a></i>
</pre>

## Properties

#### Action

Rule action.  Valid values are `allow` (default) or
`deny`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsPathLimit

Add AS path limit attribute if it does
not exist.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsPathType

AS path update options.  Valid values are
`none`, `remove`, `prepend`, or `remove-and-prepend`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsPathValue

If `as_path_type` is `prepend` or `remove-and-prepend`,
the value to prepend.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommunityType

Community update options.  Valid values are
`none`, `remove-all`, `remove-regex`, `append`, or `overwrite`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommunityValue

If `community_type` is `remove-regex`,
`append`, or `overwrite`, the value associated with that setting.  For the
`append` and `overwrite` types specifically, valid values for `community_value`
are `no-export`, `no-advertise`, `local-as`, or `nopeer`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enable

Enable this export rule (default: `true`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedCommunityType

Extended community update options.  Valid
values are `none`, `remove-all`, `remove-regex`, `append`, or `overwrite`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedCommunityValue

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalPreference

New local preference value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchAsPathRegex

AS path to match.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchCommunityRegex

Community to match.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchExtendedCommunityRegex

Extended community to match.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchFromPeers

List of peers that advertised the route entry.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchMed

Match MED.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchNextHops

List of next hop attributes.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchRouteTable

Route table to match rule.  Valid
values are `unicast`, `multicast`, or `both`.  As of PAN-OS 8.1, there doesn't
seem to be a way to configure this in the GUI, it is always set to `unicast`.
Thus, if you're running this resource against PAN-OS 8.0+, the appropriate
thing to do is set this value to `unicast` as well to match the GUI functionality.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Med

New MED value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The security rule name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NextHop

Next hop address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Origin

New route origin.  Valid values are `igp`, `egp`, or
`incomplete`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsedBy

List of peer groups.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchAddressPrefix

_Required_: No

_Type_: List of <a href="rule-matchaddressprefix.md">MatchAddressPrefix</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

