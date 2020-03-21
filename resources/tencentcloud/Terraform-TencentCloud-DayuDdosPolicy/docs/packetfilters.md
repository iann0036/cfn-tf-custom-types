# Terraform::TencentCloud::DayuDdosPolicy PacketFilters

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#dendport" title="DEndPort">DEndPort</a>" : <i>Double</i>,
    "<a href="#dstartport" title="DStartPort">DStartPort</a>" : <i>Double</i>,
    "<a href="#depth" title="Depth">Depth</a>" : <i>Double</i>,
    "<a href="#isinclude" title="IsInclude">IsInclude</a>" : <i>Boolean</i>,
    "<a href="#matchbegin" title="MatchBegin">MatchBegin</a>" : <i>String</i>,
    "<a href="#matchstr" title="MatchStr">MatchStr</a>" : <i>String</i>,
    "<a href="#matchtype" title="MatchType">MatchType</a>" : <i>String</i>,
    "<a href="#offset" title="Offset">Offset</a>" : <i>Double</i>,
    "<a href="#pktlengthmax" title="PktLengthMax">PktLengthMax</a>" : <i>Double</i>,
    "<a href="#pktlengthmin" title="PktLengthMin">PktLengthMin</a>" : <i>Double</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#sendport" title="SEndPort">SEndPort</a>" : <i>Double</i>,
    "<a href="#sstartport" title="SStartPort">SStartPort</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#dendport" title="DEndPort">DEndPort</a>: <i>Double</i>
<a href="#dstartport" title="DStartPort">DStartPort</a>: <i>Double</i>
<a href="#depth" title="Depth">Depth</a>: <i>Double</i>
<a href="#isinclude" title="IsInclude">IsInclude</a>: <i>Boolean</i>
<a href="#matchbegin" title="MatchBegin">MatchBegin</a>: <i>String</i>
<a href="#matchstr" title="MatchStr">MatchStr</a>: <i>String</i>
<a href="#matchtype" title="MatchType">MatchType</a>: <i>String</i>
<a href="#offset" title="Offset">Offset</a>: <i>Double</i>
<a href="#pktlengthmax" title="PktLengthMax">PktLengthMax</a>: <i>Double</i>
<a href="#pktlengthmin" title="PktLengthMin">PktLengthMin</a>: <i>Double</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#sendport" title="SEndPort">SEndPort</a>: <i>Double</i>
<a href="#sstartport" title="SStartPort">SStartPort</a>: <i>Double</i>
</pre>

## Properties

#### Action

Action of port to take, valid values area `drop`(drop the packet), `drop_black`(drop the packet and black the ip),`drop_rst`(drop the packet and disconnect),`drop_black_rst`(drop the packet, black the ip and disconnect),`transmit`(transmit the packet).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DEndPort

End port of the destination, valid value is range from 0 to 65535. It must be greater than `d_start_port`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DStartPort

Start port of the destination, valid value is range from 0 to 65535.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Depth

The depth of match, and valid value is range from 0 to 1500.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsInclude

Indicate whether to include the key word/regular expression or not.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchBegin

Indicate whether to check load or not, `begin_l5` means to match and `no_match` means not.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchStr

The key word or regular expression.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchType

Match type, valid values are `sunday` and `pcre`, `sunday` means key word match while `pcre` means regular match.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Offset

The offset of match, and valid value is range from 0 to 1500.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PktLengthMax

The max length of the packet, and valid value is range from 0 to 1500(Mbps). It must be greater than `pkt_length_min`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PktLengthMin

The minimum length of the packet, and valid value is range from 0 to 1500(Mbps).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Protocol, valid values are `tcp`, `udp`, `icmp`, `all`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SEndPort

End port of the source, valid value is range from 0 to 65535. It must be greater than `s_start_port`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SStartPort

Start port of the source, valid value is range from 0 to 65535.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

