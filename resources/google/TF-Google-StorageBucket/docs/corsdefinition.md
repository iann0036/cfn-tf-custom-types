# TF::Google::StorageBucket CorsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maxageseconds" title="MaxAgeSeconds">MaxAgeSeconds</a>" : <i>Double</i>,
    "<a href="#method" title="Method">Method</a>" : <i>[ String, ... ]</i>,
    "<a href="#origin" title="Origin">Origin</a>" : <i>[ String, ... ]</i>,
    "<a href="#responseheader" title="ResponseHeader">ResponseHeader</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#maxageseconds" title="MaxAgeSeconds">MaxAgeSeconds</a>: <i>Double</i>
<a href="#method" title="Method">Method</a>: <i>
      - String</i>
<a href="#origin" title="Origin">Origin</a>: <i>
      - String</i>
<a href="#responseheader" title="ResponseHeader">ResponseHeader</a>: <i>
      - String</i>
</pre>

## Properties

#### MaxAgeSeconds

The value, in seconds, to return in the [Access-Control-Max-Age header](https://www.w3.org/TR/cors/#access-control-max-age-response-header) used in preflight responses.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

The list of HTTP methods on which to include CORS response headers, (GET, OPTIONS, POST, etc) Note: "*" is permitted in the list of methods, and means "any method".

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Origin

The list of [Origins](https://tools.ietf.org/html/rfc6454) eligible to receive CORS response headers. Note: "*" is permitted in the list of origins, and means "any Origin".

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseHeader

The list of HTTP headers other than the [simple response headers](https://www.w3.org/TR/cors/#simple-response-header) to give permission for the user-agent to share across domains.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

