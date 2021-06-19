# TF::AzureRM::StorageAccount CorsRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowedheaders" title="AllowedHeaders">AllowedHeaders</a>" : <i>[ String, ... ]</i>,
    "<a href="#allowedmethods" title="AllowedMethods">AllowedMethods</a>" : <i>[ String, ... ]</i>,
    "<a href="#allowedorigins" title="AllowedOrigins">AllowedOrigins</a>" : <i>[ String, ... ]</i>,
    "<a href="#exposedheaders" title="ExposedHeaders">ExposedHeaders</a>" : <i>[ String, ... ]</i>,
    "<a href="#maxageinseconds" title="MaxAgeInSeconds">MaxAgeInSeconds</a>" : <i>Double</i>
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
<a href="#exposedheaders" title="ExposedHeaders">ExposedHeaders</a>: <i>
      - String</i>
<a href="#maxageinseconds" title="MaxAgeInSeconds">MaxAgeInSeconds</a>: <i>Double</i>
</pre>

## Properties

#### AllowedHeaders

A list of headers that are allowed to be a part of the cross-origin request.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedMethods

A list of http headers that are allowed to be executed by the origin. Valid options are
`DELETE`, `GET`, `HEAD`, `MERGE`, `POST`, `OPTIONS`, `PUT` or `PATCH`.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedOrigins

A list of origin domains that will be allowed by CORS.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExposedHeaders

A list of response headers that are exposed to CORS clients.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxAgeInSeconds

The number of seconds the client should cache a preflight response.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

