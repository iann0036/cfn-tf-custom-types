# TF::DigitalOcean::SpacesBucket CorsRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowedheaders" title="AllowedHeaders">AllowedHeaders</a>" : <i>[ String, ... ]</i>,
    "<a href="#allowedmethods" title="AllowedMethods">AllowedMethods</a>" : <i>[ String, ... ]</i>,
    "<a href="#allowedorigins" title="AllowedOrigins">AllowedOrigins</a>" : <i>[ String, ... ]</i>,
    "<a href="#maxageseconds" title="MaxAgeSeconds">MaxAgeSeconds</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#allowedheaders" title="AllowedHeaders">AllowedHeaders</a>: <i>
      - String</i>
<a href="#allowedmethods" title="AllowedMethods">AllowedMethods</a>: <i>
      - String</i>
<a href="#allowedorigins" title="AllowedOrigins">AllowedOrigins</a>: <i>
      - String</i>
<a href="#maxageseconds" title="MaxAgeSeconds">MaxAgeSeconds</a>: <i>Double</i>
</pre>

## Properties

#### AllowedHeaders

A list of headers that will be included in the CORS preflight request's `Access-Control-Request-Headers`. A header may contain one wildcard (e.g. `x-amz-*`).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedMethods

A list of HTTP methods (e.g. `GET`) which are allowed from the specified origin.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedOrigins

A list of hosts from which requests using the specified methods are allowed. A host may contain one wildcard (e.g. http://*.example.com).

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxAgeSeconds

The time in seconds that browser can cache the response for a preflight request.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

