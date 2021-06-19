# TF::Volterra::HttpLoadbalancer DirectResponseRouteDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#httpmethod" title="HttpMethod">HttpMethod</a>" : <i>[ <a href="httpmethoddefinition.md">HttpMethodDefinition</a>, ... ]</i>,
    "<a href="#path" title="Path">Path</a>" : <i>[ <a href="pathdefinition.md">PathDefinition</a>, ... ]</i>,
    "<a href="#routedirectresponse" title="RouteDirectResponse">RouteDirectResponse</a>" : <i>[ <a href="routedirectresponsedefinition.md">RouteDirectResponseDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#httpmethod" title="HttpMethod">HttpMethod</a>: <i>
      - <a href="httpmethoddefinition.md">HttpMethodDefinition</a></i>
<a href="#path" title="Path">Path</a>: <i>
      - <a href="pathdefinition.md">PathDefinition</a></i>
<a href="#routedirectresponse" title="RouteDirectResponse">RouteDirectResponse</a>: <i>
      - <a href="routedirectresponsedefinition.md">RouteDirectResponseDefinition</a></i>
</pre>

## Properties

#### HttpMethod

_Required_: No

_Type_: List of <a href="httpmethoddefinition.md">HttpMethodDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No

_Type_: List of <a href="pathdefinition.md">PathDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteDirectResponse

_Required_: No

_Type_: List of <a href="routedirectresponsedefinition.md">RouteDirectResponseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

