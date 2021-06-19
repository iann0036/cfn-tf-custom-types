# TF::Google::CloudSchedulerJob AppEngineHttpTargetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#body" title="Body">Body</a>" : <i>String</i>,
    "<a href="#headers" title="Headers">Headers</a>" : <i>[ <a href="headersdefinition.md">HeadersDefinition</a>, ... ]</i>,
    "<a href="#httpmethod" title="HttpMethod">HttpMethod</a>" : <i>String</i>,
    "<a href="#relativeuri" title="RelativeUri">RelativeUri</a>" : <i>String</i>,
    "<a href="#appenginerouting" title="AppEngineRouting">AppEngineRouting</a>" : <i>[ <a href="appengineroutingdefinition.md">AppEngineRoutingDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#body" title="Body">Body</a>: <i>String</i>
<a href="#headers" title="Headers">Headers</a>: <i>
      - <a href="headersdefinition.md">HeadersDefinition</a></i>
<a href="#httpmethod" title="HttpMethod">HttpMethod</a>: <i>String</i>
<a href="#relativeuri" title="RelativeUri">RelativeUri</a>: <i>String</i>
<a href="#appenginerouting" title="AppEngineRouting">AppEngineRouting</a>: <i>
      - <a href="appengineroutingdefinition.md">AppEngineRoutingDefinition</a></i>
</pre>

## Properties

#### Body

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Headers

_Required_: No

_Type_: List of <a href="headersdefinition.md">HeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpMethod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelativeUri

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppEngineRouting

_Required_: No

_Type_: List of <a href="appengineroutingdefinition.md">AppEngineRoutingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

