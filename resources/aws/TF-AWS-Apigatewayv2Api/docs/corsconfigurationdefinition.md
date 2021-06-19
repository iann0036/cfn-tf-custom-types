# TF::AWS::Apigatewayv2Api CorsConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowcredentials" title="AllowCredentials">AllowCredentials</a>" : <i>Boolean</i>,
    "<a href="#allowheaders" title="AllowHeaders">AllowHeaders</a>" : <i>[ String, ... ]</i>,
    "<a href="#allowmethods" title="AllowMethods">AllowMethods</a>" : <i>[ String, ... ]</i>,
    "<a href="#alloworigins" title="AllowOrigins">AllowOrigins</a>" : <i>[ String, ... ]</i>,
    "<a href="#exposeheaders" title="ExposeHeaders">ExposeHeaders</a>" : <i>[ String, ... ]</i>,
    "<a href="#maxage" title="MaxAge">MaxAge</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#allowcredentials" title="AllowCredentials">AllowCredentials</a>: <i>Boolean</i>
<a href="#allowheaders" title="AllowHeaders">AllowHeaders</a>: <i>
      - String</i>
<a href="#allowmethods" title="AllowMethods">AllowMethods</a>: <i>
      - String</i>
<a href="#alloworigins" title="AllowOrigins">AllowOrigins</a>: <i>
      - String</i>
<a href="#exposeheaders" title="ExposeHeaders">ExposeHeaders</a>: <i>
      - String</i>
<a href="#maxage" title="MaxAge">MaxAge</a>: <i>Double</i>
</pre>

## Properties

#### AllowCredentials

Whether credentials are included in the CORS request.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowHeaders

The set of allowed HTTP headers.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowMethods

The set of allowed HTTP methods.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowOrigins

The set of allowed origins.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExposeHeaders

The set of exposed HTTP headers.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxAge

The number of seconds that the browser should cache preflight request results.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

