# TF::Google::ComputeRegionUrlMap RouteRulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#service" title="Service">Service</a>" : <i>String</i>,
    "<a href="#headeraction" title="HeaderAction">HeaderAction</a>" : <i>[ <a href="headeractiondefinition.md">HeaderActionDefinition</a>, ... ]</i>,
    "<a href="#matchrules" title="MatchRules">MatchRules</a>" : <i>[ <a href="matchrulesdefinition.md">MatchRulesDefinition</a>, ... ]</i>,
    "<a href="#routeaction" title="RouteAction">RouteAction</a>" : <i>[ <a href="routeactiondefinition.md">RouteActionDefinition</a>, ... ]</i>,
    "<a href="#urlredirect" title="UrlRedirect">UrlRedirect</a>" : <i>[ <a href="urlredirectdefinition.md">UrlRedirectDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#service" title="Service">Service</a>: <i>String</i>
<a href="#headeraction" title="HeaderAction">HeaderAction</a>: <i>
      - <a href="headeractiondefinition.md">HeaderActionDefinition</a></i>
<a href="#matchrules" title="MatchRules">MatchRules</a>: <i>
      - <a href="matchrulesdefinition.md">MatchRulesDefinition</a></i>
<a href="#routeaction" title="RouteAction">RouteAction</a>: <i>
      - <a href="routeactiondefinition.md">RouteActionDefinition</a></i>
<a href="#urlredirect" title="UrlRedirect">UrlRedirect</a>: <i>
      - <a href="urlredirectdefinition.md">UrlRedirectDefinition</a></i>
</pre>

## Properties

#### Priority

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderAction

_Required_: No

_Type_: List of <a href="headeractiondefinition.md">HeaderActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchRules

_Required_: No

_Type_: List of <a href="matchrulesdefinition.md">MatchRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteAction

_Required_: No

_Type_: List of <a href="routeactiondefinition.md">RouteActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlRedirect

_Required_: No

_Type_: List of <a href="urlredirectdefinition.md">UrlRedirectDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

