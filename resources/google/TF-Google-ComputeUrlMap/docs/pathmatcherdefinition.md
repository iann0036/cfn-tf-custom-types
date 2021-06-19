# TF::Google::ComputeUrlMap PathMatcherDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultservice" title="DefaultService">DefaultService</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#defaultrouteaction" title="DefaultRouteAction">DefaultRouteAction</a>" : <i>[ <a href="defaultrouteactiondefinition.md">DefaultRouteActionDefinition</a>, ... ]</i>,
    "<a href="#defaulturlredirect" title="DefaultUrlRedirect">DefaultUrlRedirect</a>" : <i>[ <a href="defaulturlredirectdefinition.md">DefaultUrlRedirectDefinition</a>, ... ]</i>,
    "<a href="#headeraction" title="HeaderAction">HeaderAction</a>" : <i>[ <a href="headeractiondefinition.md">HeaderActionDefinition</a>, ... ]</i>,
    "<a href="#pathrule" title="PathRule">PathRule</a>" : <i>[ <a href="pathruledefinition.md">PathRuleDefinition</a>, ... ]</i>,
    "<a href="#routerules" title="RouteRules">RouteRules</a>" : <i>[ <a href="routerulesdefinition.md">RouteRulesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultservice" title="DefaultService">DefaultService</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#defaultrouteaction" title="DefaultRouteAction">DefaultRouteAction</a>: <i>
      - <a href="defaultrouteactiondefinition.md">DefaultRouteActionDefinition</a></i>
<a href="#defaulturlredirect" title="DefaultUrlRedirect">DefaultUrlRedirect</a>: <i>
      - <a href="defaulturlredirectdefinition.md">DefaultUrlRedirectDefinition</a></i>
<a href="#headeraction" title="HeaderAction">HeaderAction</a>: <i>
      - <a href="headeractiondefinition.md">HeaderActionDefinition</a></i>
<a href="#pathrule" title="PathRule">PathRule</a>: <i>
      - <a href="pathruledefinition.md">PathRuleDefinition</a></i>
<a href="#routerules" title="RouteRules">RouteRules</a>: <i>
      - <a href="routerulesdefinition.md">RouteRulesDefinition</a></i>
</pre>

## Properties

#### DefaultService

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRouteAction

_Required_: No

_Type_: List of <a href="defaultrouteactiondefinition.md">DefaultRouteActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultUrlRedirect

_Required_: No

_Type_: List of <a href="defaulturlredirectdefinition.md">DefaultUrlRedirectDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderAction

_Required_: No

_Type_: List of <a href="headeractiondefinition.md">HeaderActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathRule

_Required_: No

_Type_: List of <a href="pathruledefinition.md">PathRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteRules

_Required_: No

_Type_: List of <a href="routerulesdefinition.md">RouteRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

