# TF::Cloudflare::RateLimit ResponseDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#headers" title="Headers">Headers</a>" : <i>[ [ <a href="headersdefinition.md">HeadersDefinition</a>, ... ], ... ]</i>,
    "<a href="#origintraffic" title="OriginTraffic">OriginTraffic</a>" : <i>Boolean</i>,
    "<a href="#statuses" title="Statuses">Statuses</a>" : <i>[ Double, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#headers" title="Headers">Headers</a>: <i>
      - 
      - <a href="headersdefinition.md">HeadersDefinition</a></i>
<a href="#origintraffic" title="OriginTraffic">OriginTraffic</a>: <i>Boolean</i>
<a href="#statuses" title="Statuses">Statuses</a>: <i>
      - Double</i>
</pre>

## Properties

#### Headers

_Required_: No

_Type_: List of List of <a href="headersdefinition.md">HeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginTraffic

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Statuses

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

