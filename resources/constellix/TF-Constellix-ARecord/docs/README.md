# TF::Constellix::ARecord

Manages one or more A records within the specified domain.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Constellix::ARecord",
    "Properties" : {
        "<a href="#contactids" title="ContactIds">ContactIds</a>" : <i>[ Double, ... ]</i>,
        "<a href="#domainid" title="DomainId">DomainId</a>" : <i>String</i>,
        "<a href="#geolocation" title="GeoLocation">GeoLocation</a>" : <i>[ <a href="geolocationdefinition.md">GeoLocationDefinition</a>, ... ]</i>,
        "<a href="#gtdregion" title="GtdRegion">GtdRegion</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#noanswer" title="Noanswer">Noanswer</a>" : <i>Boolean</i>,
        "<a href="#note" title="Note">Note</a>" : <i>String</i>,
        "<a href="#pools" title="Pools">Pools</a>" : <i>[ Double, ... ]</i>,
        "<a href="#recordfailoverdisableflag" title="RecordFailoverDisableFlag">RecordFailoverDisableFlag</a>" : <i>String</i>,
        "<a href="#recordfailoverfailovertype" title="RecordFailoverFailoverType">RecordFailoverFailoverType</a>" : <i>String</i>,
        "<a href="#recordoption" title="RecordOption">RecordOption</a>" : <i>String</i>,
        "<a href="#sourcetype" title="SourceType">SourceType</a>" : <i>String</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#recordfailovervalues" title="RecordFailoverValues">RecordFailoverValues</a>" : <i>[ <a href="recordfailovervaluesdefinition.md">RecordFailoverValuesDefinition</a>, ... ]</i>,
        "<a href="#roundrobin" title="Roundrobin">Roundrobin</a>" : <i>[ <a href="roundrobindefinition.md">RoundrobinDefinition</a>, ... ]</i>,
        "<a href="#roundrobinfailover" title="RoundrobinFailover">RoundrobinFailover</a>" : <i>[ <a href="roundrobinfailoverdefinition.md">RoundrobinFailoverDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Constellix::ARecord
Properties:
    <a href="#contactids" title="ContactIds">ContactIds</a>: <i>
      - Double</i>
    <a href="#domainid" title="DomainId">DomainId</a>: <i>String</i>
    <a href="#geolocation" title="GeoLocation">GeoLocation</a>: <i>
      - <a href="geolocationdefinition.md">GeoLocationDefinition</a></i>
    <a href="#gtdregion" title="GtdRegion">GtdRegion</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#noanswer" title="Noanswer">Noanswer</a>: <i>Boolean</i>
    <a href="#note" title="Note">Note</a>: <i>String</i>
    <a href="#pools" title="Pools">Pools</a>: <i>
      - Double</i>
    <a href="#recordfailoverdisableflag" title="RecordFailoverDisableFlag">RecordFailoverDisableFlag</a>: <i>String</i>
    <a href="#recordfailoverfailovertype" title="RecordFailoverFailoverType">RecordFailoverFailoverType</a>: <i>String</i>
    <a href="#recordoption" title="RecordOption">RecordOption</a>: <i>String</i>
    <a href="#sourcetype" title="SourceType">SourceType</a>: <i>String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#recordfailovervalues" title="RecordFailoverValues">RecordFailoverValues</a>: <i>
      - <a href="recordfailovervaluesdefinition.md">RecordFailoverValuesDefinition</a></i>
    <a href="#roundrobin" title="Roundrobin">Roundrobin</a>: <i>
      - <a href="roundrobindefinition.md">RoundrobinDefinition</a></i>
    <a href="#roundrobinfailover" title="RoundrobinFailover">RoundrobinFailover</a>: <i>
      - <a href="roundrobinfailoverdefinition.md">RoundrobinFailoverDefinition</a></i>
</pre>

## Properties

#### ContactIds

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoLocation

_Required_: No

_Type_: List of <a href="geolocationdefinition.md">GeoLocationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GtdRegion

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Noanswer

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Note

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pools

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecordFailoverDisableFlag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecordFailoverFailoverType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecordOption

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecordFailoverValues

_Required_: No

_Type_: List of <a href="recordfailovervaluesdefinition.md">RecordFailoverValuesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Roundrobin

_Required_: No

_Type_: List of <a href="roundrobindefinition.md">RoundrobinDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoundrobinFailover

_Required_: No

_Type_: List of <a href="roundrobinfailoverdefinition.md">RoundrobinFailoverDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

