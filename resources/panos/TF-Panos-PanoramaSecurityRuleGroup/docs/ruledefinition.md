# TF::Panos::PanoramaSecurityRuleGroup RuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#applications" title="Applications">Applications</a>" : <i>[ String, ... ]</i>,
    "<a href="#categories" title="Categories">Categories</a>" : <i>[ String, ... ]</i>,
    "<a href="#datafiltering" title="DataFiltering">DataFiltering</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#destinationaddresses" title="DestinationAddresses">DestinationAddresses</a>" : <i>[ String, ... ]</i>,
    "<a href="#destinationzones" title="DestinationZones">DestinationZones</a>" : <i>[ String, ... ]</i>,
    "<a href="#disableserverresponseinspection" title="DisableServerResponseInspection">DisableServerResponseInspection</a>" : <i>Boolean</i>,
    "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
    "<a href="#fileblocking" title="FileBlocking">FileBlocking</a>" : <i>String</i>,
    "<a href="#group" title="Group">Group</a>" : <i>String</i>,
    "<a href="#hipprofiles" title="HipProfiles">HipProfiles</a>" : <i>[ String, ... ]</i>,
    "<a href="#icmpunreachable" title="IcmpUnreachable">IcmpUnreachable</a>" : <i>Boolean</i>,
    "<a href="#logend" title="LogEnd">LogEnd</a>" : <i>Boolean</i>,
    "<a href="#logsetting" title="LogSetting">LogSetting</a>" : <i>String</i>,
    "<a href="#logstart" title="LogStart">LogStart</a>" : <i>Boolean</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#negatedestination" title="NegateDestination">NegateDestination</a>" : <i>Boolean</i>,
    "<a href="#negatesource" title="NegateSource">NegateSource</a>" : <i>Boolean</i>,
    "<a href="#negatetarget" title="NegateTarget">NegateTarget</a>" : <i>Boolean</i>,
    "<a href="#schedule" title="Schedule">Schedule</a>" : <i>String</i>,
    "<a href="#services" title="Services">Services</a>" : <i>[ String, ... ]</i>,
    "<a href="#sourceaddresses" title="SourceAddresses">SourceAddresses</a>" : <i>[ String, ... ]</i>,
    "<a href="#sourceusers" title="SourceUsers">SourceUsers</a>" : <i>[ String, ... ]</i>,
    "<a href="#sourcezones" title="SourceZones">SourceZones</a>" : <i>[ String, ... ]</i>,
    "<a href="#spyware" title="Spyware">Spyware</a>" : <i>String</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#urlfiltering" title="UrlFiltering">UrlFiltering</a>" : <i>String</i>,
    "<a href="#virus" title="Virus">Virus</a>" : <i>String</i>,
    "<a href="#vulnerability" title="Vulnerability">Vulnerability</a>" : <i>String</i>,
    "<a href="#wildfireanalysis" title="WildfireAnalysis">WildfireAnalysis</a>" : <i>String</i>,
    "<a href="#target" title="Target">Target</a>" : <i>[ <a href="targetdefinition.md">TargetDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#applications" title="Applications">Applications</a>: <i>
      - String</i>
<a href="#categories" title="Categories">Categories</a>: <i>
      - String</i>
<a href="#datafiltering" title="DataFiltering">DataFiltering</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#destinationaddresses" title="DestinationAddresses">DestinationAddresses</a>: <i>
      - String</i>
<a href="#destinationzones" title="DestinationZones">DestinationZones</a>: <i>
      - String</i>
<a href="#disableserverresponseinspection" title="DisableServerResponseInspection">DisableServerResponseInspection</a>: <i>Boolean</i>
<a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
<a href="#fileblocking" title="FileBlocking">FileBlocking</a>: <i>String</i>
<a href="#group" title="Group">Group</a>: <i>String</i>
<a href="#hipprofiles" title="HipProfiles">HipProfiles</a>: <i>
      - String</i>
<a href="#icmpunreachable" title="IcmpUnreachable">IcmpUnreachable</a>: <i>Boolean</i>
<a href="#logend" title="LogEnd">LogEnd</a>: <i>Boolean</i>
<a href="#logsetting" title="LogSetting">LogSetting</a>: <i>String</i>
<a href="#logstart" title="LogStart">LogStart</a>: <i>Boolean</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#negatedestination" title="NegateDestination">NegateDestination</a>: <i>Boolean</i>
<a href="#negatesource" title="NegateSource">NegateSource</a>: <i>Boolean</i>
<a href="#negatetarget" title="NegateTarget">NegateTarget</a>: <i>Boolean</i>
<a href="#schedule" title="Schedule">Schedule</a>: <i>String</i>
<a href="#services" title="Services">Services</a>: <i>
      - String</i>
<a href="#sourceaddresses" title="SourceAddresses">SourceAddresses</a>: <i>
      - String</i>
<a href="#sourceusers" title="SourceUsers">SourceUsers</a>: <i>
      - String</i>
<a href="#sourcezones" title="SourceZones">SourceZones</a>: <i>
      - String</i>
<a href="#spyware" title="Spyware">Spyware</a>: <i>String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#urlfiltering" title="UrlFiltering">UrlFiltering</a>: <i>String</i>
<a href="#virus" title="Virus">Virus</a>: <i>String</i>
<a href="#vulnerability" title="Vulnerability">Vulnerability</a>: <i>String</i>
<a href="#wildfireanalysis" title="WildfireAnalysis">WildfireAnalysis</a>: <i>String</i>
<a href="#target" title="Target">Target</a>: <i>
      - <a href="targetdefinition.md">TargetDefinition</a></i>
</pre>

## Properties

#### Action

Action for the matched traffic.  This can be `allow`
(default), `deny`, `drop`, `reset-client`, `reset-server`, or `reset-both`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Applications

List of applications.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Categories

List of categories.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataFiltering

Profile Setting: `Profiles` - The Data
Filtering setting.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationAddresses

List of destination addresses.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationZones

List of destination zones.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableServerResponseInspection

Set to `true` to disable
server response inspection.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

Set to `true` to disable this rule.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileBlocking

Profile Setting: `Profiles` - The file blocking
setting.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

Profile Setting: `Group` - The group profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HipProfiles

List of HIP profiles.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpUnreachable

Set to `true` to enable ICMP unreachable.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogEnd

Log the end of the traffic flow (default: `true`).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogSetting

Log forwarding profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogStart

Log the start of the traffic flow.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The security rule name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NegateDestination

If the destination should be negated.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NegateSource

If the source should be negated.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NegateTarget

Instead of applying the rule for the
given serial numbers, apply it to everything except them.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

The security rule schedule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Services

List of services.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddresses

List of source addresses.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceUsers

List of source users.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceZones

List of source zones.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Spyware

Profile Setting: `Profiles` - The anti-spyware
setting.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

List of tags for this security rule.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Rule type.  This can be `universal` (default),
`interzone`, or `intrazone`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlFiltering

Profile Setting: `Profiles` - The URL filtering
setting.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Virus

Profile Setting: `Profiles` - The antivirus setting.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vulnerability

Profile Setting: `Profiles` - The Vulnerability
Protection setting.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WildfireAnalysis

Profile Setting: `Profiles` - The WildFire
Analysis setting.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

_Required_: No

_Type_: List of <a href="targetdefinition.md">TargetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

