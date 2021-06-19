# TF::Nutanix::NetworkSecurityRule AdRuleOutboundAllowListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#expirationtime" title="ExpirationTime">ExpirationTime</a>" : <i>String</i>,
    "<a href="#filterkindlist" title="FilterKindList">FilterKindList</a>" : <i>[ String, ... ]</i>,
    "<a href="#filtertype" title="FilterType">FilterType</a>" : <i>String</i>,
    "<a href="#ipsubnet" title="IpSubnet">IpSubnet</a>" : <i>String</i>,
    "<a href="#ipsubnetprefixlength" title="IpSubnetPrefixLength">IpSubnetPrefixLength</a>" : <i>String</i>,
    "<a href="#networkfunctionchainreference" title="NetworkFunctionChainReference">NetworkFunctionChainReference</a>" : <i>[ <a href="networkfunctionchainreferencedefinition.md">NetworkFunctionChainReferenceDefinition</a>, ... ]</i>,
    "<a href="#peerspecificationtype" title="PeerSpecificationType">PeerSpecificationType</a>" : <i>String</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#filterparams" title="FilterParams">FilterParams</a>" : <i>[ <a href="filterparamsdefinition.md">FilterParamsDefinition</a>, ... ]</i>,
    "<a href="#icmptypecodelist" title="IcmpTypeCodeList">IcmpTypeCodeList</a>" : <i>[ <a href="icmptypecodelistdefinition.md">IcmpTypeCodeListDefinition</a>, ... ]</i>,
    "<a href="#tcpportrangelist" title="TcpPortRangeList">TcpPortRangeList</a>" : <i>[ <a href="tcpportrangelistdefinition.md">TcpPortRangeListDefinition</a>, ... ]</i>,
    "<a href="#udpportrangelist" title="UdpPortRangeList">UdpPortRangeList</a>" : <i>[ <a href="udpportrangelistdefinition.md">UdpPortRangeListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#expirationtime" title="ExpirationTime">ExpirationTime</a>: <i>String</i>
<a href="#filterkindlist" title="FilterKindList">FilterKindList</a>: <i>
      - String</i>
<a href="#filtertype" title="FilterType">FilterType</a>: <i>String</i>
<a href="#ipsubnet" title="IpSubnet">IpSubnet</a>: <i>String</i>
<a href="#ipsubnetprefixlength" title="IpSubnetPrefixLength">IpSubnetPrefixLength</a>: <i>String</i>
<a href="#networkfunctionchainreference" title="NetworkFunctionChainReference">NetworkFunctionChainReference</a>: <i>
      - <a href="networkfunctionchainreferencedefinition.md">NetworkFunctionChainReferenceDefinition</a></i>
<a href="#peerspecificationtype" title="PeerSpecificationType">PeerSpecificationType</a>: <i>String</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#filterparams" title="FilterParams">FilterParams</a>: <i>
      - <a href="filterparamsdefinition.md">FilterParamsDefinition</a></i>
<a href="#icmptypecodelist" title="IcmpTypeCodeList">IcmpTypeCodeList</a>: <i>
      - <a href="icmptypecodelistdefinition.md">IcmpTypeCodeListDefinition</a></i>
<a href="#tcpportrangelist" title="TcpPortRangeList">TcpPortRangeList</a>: <i>
      - <a href="tcpportrangelistdefinition.md">TcpPortRangeListDefinition</a></i>
<a href="#udpportrangelist" title="UdpPortRangeList">UdpPortRangeList</a>: <i>
      - <a href="udpportrangelistdefinition.md">UdpPortRangeListDefinition</a></i>
</pre>

## Properties

#### ExpirationTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterKindList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpSubnet

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpSubnetPrefixLength

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkFunctionChainReference

_Required_: No

_Type_: List of <a href="networkfunctionchainreferencedefinition.md">NetworkFunctionChainReferenceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeerSpecificationType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterParams

_Required_: No

_Type_: List of <a href="filterparamsdefinition.md">FilterParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IcmpTypeCodeList

_Required_: No

_Type_: List of <a href="icmptypecodelistdefinition.md">IcmpTypeCodeListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpPortRangeList

_Required_: No

_Type_: List of <a href="tcpportrangelistdefinition.md">TcpPortRangeListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UdpPortRangeList

_Required_: No

_Type_: List of <a href="udpportrangelistdefinition.md">UdpPortRangeListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

