# Terraform::TencentCloud::CosBucket CorsRules

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowedheaders" title="AllowedHeaders">AllowedHeaders</a>" : <i>[ String, ... ]</i>,
    "<a href="#allowedmethods" title="AllowedMethods">AllowedMethods</a>" : <i>[ String, ... ]</i>,
    "<a href="#allowedorigins" title="AllowedOrigins">AllowedOrigins</a>" : <i>[ String, ... ]</i>,
    "<a href="#exposeheaders" title="ExposeHeaders">ExposeHeaders</a>" : <i>[ String, ... ]</i>,
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
<a href="#exposeheaders" title="ExposeHeaders">ExposeHeaders</a>: <i>
      - String</i>
<a href="#maxageseconds" title="MaxAgeSeconds">MaxAgeSeconds</a>: <i>Double</i>
</pre>

## Properties

#### AllowedHeaders

Specifies which headers are allowed.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedMethods

Specifies which methods are allowed. Can be GET, PUT, POST, DELETE or HEAD.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedOrigins

Specifies which origins are allowed.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExposeHeaders

Specifies expose header in the response.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxAgeSeconds

Specifies time in seconds that browser can cache the response for a preflight request.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

