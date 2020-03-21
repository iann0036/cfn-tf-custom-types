# Terraform::NSXT::LbPool MemberGroup

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipversionfilter" title="IpVersionFilter">IpVersionFilter</a>" : <i>String</i>,
    "<a href="#limitiplistsize" title="LimitIpListSize">LimitIpListSize</a>" : <i>Boolean</i>,
    "<a href="#maxiplistsize" title="MaxIpListSize">MaxIpListSize</a>" : <i>Double</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#groupingobject" title="GroupingObject">GroupingObject</a>" : <i>[ &lt;a href=&#34;membergroup-groupingobject.md&#34;&gt;GroupingObject&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ipversionfilter" title="IpVersionFilter">IpVersionFilter</a>: <i>String</i>
<a href="#limitiplistsize" title="LimitIpListSize">LimitIpListSize</a>: <i>Boolean</i>
<a href="#maxiplistsize" title="MaxIpListSize">MaxIpListSize</a>: <i>Double</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#groupingobject" title="GroupingObject">GroupingObject</a>: <i>
      - &lt;a href=&#34;membergroup-groupingobject.md&#34;&gt;GroupingObject&lt;/a&gt;</i>
</pre>

## Properties

#### IpVersionFilter

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitIpListSize

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxIpListSize

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupingObject

_Required_: No
_Type_: List of &lt;a href=&#34;membergroup-groupingobject.md&#34;&gt;GroupingObject&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

