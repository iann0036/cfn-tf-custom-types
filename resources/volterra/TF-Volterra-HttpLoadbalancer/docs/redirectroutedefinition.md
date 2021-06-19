# TF::Volterra::HttpLoadbalancer RedirectRouteDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#httpmethod" title="HttpMethod">HttpMethod</a>" : <i>[ <a href="httpmethoddefinition.md">HttpMethodDefinition</a>, ... ]</i>,
    "<a href="#path" title="Path">Path</a>" : <i>[ <a href="pathdefinition.md">PathDefinition</a>, ... ]</i>,
    "<a href="#routeredirect" title="RouteRedirect">RouteRedirect</a>" : <i>[ <a href="routeredirectdefinition.md">RouteRedirectDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#httpmethod" title="HttpMethod">HttpMethod</a>: <i>
      - <a href="httpmethoddefinition.md">HttpMethodDefinition</a></i>
<a href="#path" title="Path">Path</a>: <i>
      - <a href="pathdefinition.md">PathDefinition</a></i>
<a href="#routeredirect" title="RouteRedirect">RouteRedirect</a>: <i>
      - <a href="routeredirectdefinition.md">RouteRedirectDefinition</a></i>
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

#### RouteRedirect

_Required_: No

_Type_: List of <a href="routeredirectdefinition.md">RouteRedirectDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

