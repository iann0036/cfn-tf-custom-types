# TF::AzureRM::ApplicationGateway UrlDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#querystring" title="QueryString">QueryString</a>" : <i>String</i>,
    "<a href="#reroute" title="Reroute">Reroute</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#querystring" title="QueryString">QueryString</a>: <i>String</i>
<a href="#reroute" title="Reroute">Reroute</a>: <i>Boolean</i>
</pre>

## Properties

#### Path

The URL path to rewrite.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryString

The query string to rewrite.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reroute

Whether the URL path map should be reevaluated after this rewrite has been applied. [More info on rewrite configutation](https://docs.microsoft.com/en-us/azure/application-gateway/rewrite-http-headers-url#rewrite-configuration).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

