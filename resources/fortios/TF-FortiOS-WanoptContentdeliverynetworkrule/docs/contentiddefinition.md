# TF::FortiOS::WanoptContentdeliverynetworkrule ContentIdDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enddirection" title="EndDirection">EndDirection</a>" : <i>String</i>,
    "<a href="#endskip" title="EndSkip">EndSkip</a>" : <i>Double</i>,
    "<a href="#endstr" title="EndStr">EndStr</a>" : <i>String</i>,
    "<a href="#rangestr" title="RangeStr">RangeStr</a>" : <i>String</i>,
    "<a href="#startdirection" title="StartDirection">StartDirection</a>" : <i>String</i>,
    "<a href="#startskip" title="StartSkip">StartSkip</a>" : <i>Double</i>,
    "<a href="#startstr" title="StartStr">StartStr</a>" : <i>String</i>,
    "<a href="#target" title="Target">Target</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#enddirection" title="EndDirection">EndDirection</a>: <i>String</i>
<a href="#endskip" title="EndSkip">EndSkip</a>: <i>Double</i>
<a href="#endstr" title="EndStr">EndStr</a>: <i>String</i>
<a href="#rangestr" title="RangeStr">RangeStr</a>: <i>String</i>
<a href="#startdirection" title="StartDirection">StartDirection</a>: <i>String</i>
<a href="#startskip" title="StartSkip">StartSkip</a>: <i>Double</i>
<a href="#startstr" title="StartStr">StartStr</a>: <i>String</i>
<a href="#target" title="Target">Target</a>: <i>String</i>
</pre>

## Properties

#### EndDirection

Search direction from end-str match. Valid values: `forward`, `backward`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndSkip

Number of characters in URL to skip after end-str has been matched.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndStr

String from which to end search.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RangeStr

Name of content ID within the start string and end string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartDirection

Search direction from start-str match. Valid values: `forward`, `backward`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartSkip

Number of characters in URL to skip after start-str has been matched.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartStr

String from which to start search.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

Option in HTTP header or URL parameter to match. Valid values: `path`, `parameter`, `referrer`, `youtube-map`, `youtube-id`, `youku-id`, `hls-manifest`, `dash-manifest`, `hls-fragment`, `dash-fragment`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

