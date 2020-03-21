# Terraform::Google::ComputeSecurityPolicy Config

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#srcipranges" title="SrcIpRanges">SrcIpRanges</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#srcipranges" title="SrcIpRanges">SrcIpRanges</a>: <i>
      - String</i>
</pre>

## Properties

#### SrcIpRanges

Set of IP addresses or ranges (IPV4 or IPV6) in CIDR notation
to match against inbound traffic. There is a limit of 5 IP ranges per rule. A value of '\*' matches all IPs
(can be used to override the default behavior).

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

