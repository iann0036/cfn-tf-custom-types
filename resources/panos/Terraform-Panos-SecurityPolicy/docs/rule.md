# Terraform::Panos::SecurityPolicy Rule

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
    "<a href="#wildfireanalysis" title="WildfireAnalysis">WildfireAnalysis</a>" : <i>String</i>
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
</pre>

## Properties

#### Action

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Applications

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Categories

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataFiltering

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationAddresses

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationZones

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableServerResponseInspection

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileBlocking

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HipProfiles

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpUnreachable

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogEnd

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogSetting

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogStart

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NegateDestination

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NegateSource

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Services

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddresses

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceUsers

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceZones

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Spyware

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlFiltering

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Virus

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vulnerability

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WildfireAnalysis

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

