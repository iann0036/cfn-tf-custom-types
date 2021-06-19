# TF::AVI::Dnspolicy MatchDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clientipaddress" title="ClientIpAddress">ClientIpAddress</a>" : <i>[ <a href="clientipaddressdefinition.md">ClientIpAddressDefinition</a>, ... ]</i>,
    "<a href="#geolocation" title="GeoLocation">GeoLocation</a>" : <i>[ <a href="geolocationdefinition.md">GeoLocationDefinition</a>, ... ]</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>[ <a href="protocoldefinition.md">ProtocolDefinition</a>, ... ]</i>,
    "<a href="#queryname" title="QueryName">QueryName</a>" : <i>[ <a href="querynamedefinition.md">QueryNameDefinition</a>, ... ]</i>,
    "<a href="#querytype" title="QueryType">QueryType</a>" : <i>[ <a href="querytypedefinition.md">QueryTypeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#clientipaddress" title="ClientIpAddress">ClientIpAddress</a>: <i>
      - <a href="clientipaddressdefinition.md">ClientIpAddressDefinition</a></i>
<a href="#geolocation" title="GeoLocation">GeoLocation</a>: <i>
      - <a href="geolocationdefinition.md">GeoLocationDefinition</a></i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>
      - <a href="protocoldefinition.md">ProtocolDefinition</a></i>
<a href="#queryname" title="QueryName">QueryName</a>: <i>
      - <a href="querynamedefinition.md">QueryNameDefinition</a></i>
<a href="#querytype" title="QueryType">QueryType</a>: <i>
      - <a href="querytypedefinition.md">QueryTypeDefinition</a></i>
</pre>

## Properties

#### ClientIpAddress

_Required_: No

_Type_: List of <a href="clientipaddressdefinition.md">ClientIpAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoLocation

_Required_: No

_Type_: List of <a href="geolocationdefinition.md">GeoLocationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: List of <a href="protocoldefinition.md">ProtocolDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryName

_Required_: No

_Type_: List of <a href="querynamedefinition.md">QueryNameDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryType

_Required_: No

_Type_: List of <a href="querytypedefinition.md">QueryTypeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

