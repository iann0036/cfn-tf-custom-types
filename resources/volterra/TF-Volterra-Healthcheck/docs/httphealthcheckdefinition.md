# TF::Volterra::Healthcheck HttpHealthCheckDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#headers" title="Headers">Headers</a>" : <i>[ <a href="headersdefinition.md">HeadersDefinition</a>, ... ]</i>,
    "<a href="#hostheader" title="HostHeader">HostHeader</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#requestheaderstoremove" title="RequestHeadersToRemove">RequestHeadersToRemove</a>" : <i>[ String, ... ]</i>,
    "<a href="#usehttp2" title="UseHttp2">UseHttp2</a>" : <i>Boolean</i>,
    "<a href="#useoriginservername" title="UseOriginServerName">UseOriginServerName</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#headers" title="Headers">Headers</a>: <i>
      - <a href="headersdefinition.md">HeadersDefinition</a></i>
<a href="#hostheader" title="HostHeader">HostHeader</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#requestheaderstoremove" title="RequestHeadersToRemove">RequestHeadersToRemove</a>: <i>
      - String</i>
<a href="#usehttp2" title="UseHttp2">UseHttp2</a>: <i>Boolean</i>
<a href="#useoriginservername" title="UseOriginServerName">UseOriginServerName</a>: <i>Boolean</i>
</pre>

## Properties

#### Headers

_Required_: No

_Type_: List of <a href="headersdefinition.md">HeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostHeader

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeadersToRemove

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseHttp2

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseOriginServerName

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

