# TF::FortiOS::SystemGeoipoverride IpRangeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#endip" title="EndIp">EndIp</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#startip" title="StartIp">StartIp</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#endip" title="EndIp">EndIp</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#startip" title="StartIp">StartIp</a>: <i>String</i>
</pre>

## Properties

#### EndIp

Final IP address, inclusive, of the address range (format: xxx.xxx.xxx.xxx).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

ID number for individual entry in the IP-Range table.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartIp

Starting IP address, inclusive, of the address range (format: xxx.xxx.xxx.xxx).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

