# Terraform::AzureRM::Frontdoor RoutingRule RedirectConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#customfragment" title="CustomFragment">CustomFragment</a>" : <i>String</i>,
    "<a href="#customhost" title="CustomHost">CustomHost</a>" : <i>String</i>,
    "<a href="#custompath" title="CustomPath">CustomPath</a>" : <i>String</i>,
    "<a href="#customquerystring" title="CustomQueryString">CustomQueryString</a>" : <i>String</i>,
    "<a href="#redirectprotocol" title="RedirectProtocol">RedirectProtocol</a>" : <i>String</i>,
    "<a href="#redirecttype" title="RedirectType">RedirectType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#customfragment" title="CustomFragment">CustomFragment</a>: <i>String</i>
<a href="#customhost" title="CustomHost">CustomHost</a>: <i>String</i>
<a href="#custompath" title="CustomPath">CustomPath</a>: <i>String</i>
<a href="#customquerystring" title="CustomQueryString">CustomQueryString</a>: <i>String</i>
<a href="#redirectprotocol" title="RedirectProtocol">RedirectProtocol</a>: <i>String</i>
<a href="#redirecttype" title="RedirectType">RedirectType</a>: <i>String</i>
</pre>

## Properties

#### CustomFragment

The destination fragment in the portion of URL after '#'. Set this to add a fragment to the redirect URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomHost

Set this to change the URL for the redirection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomPath

The path to retain as per the incoming request, or update in the URL for the redirection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomQueryString

Replace any existing query string from the incoming request URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectProtocol

Protocol to use when redirecting. Valid options are `HttpOnly`, `HttpsOnly`, or `MatchRequest`. Defaults to `MatchRequest`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectType

Status code for the redirect. Valida options are `Moved`, `Found`, `TemporaryRedirect`, `PermanentRedirect`. Defaults to `Found`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

